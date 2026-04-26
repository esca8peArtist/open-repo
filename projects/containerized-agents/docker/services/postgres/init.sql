-- init.sql — PostgreSQL schema for Containerized AI Agents
-- Containerized AI Agents — v1.0
--
-- Executed automatically by the official postgres Docker image on first start
-- (any *.sql file placed in /docker-entrypoint-initdb.d/ is run as superuser).
--
-- Tables:
--   conversations    — per-channel dialogue sessions
--   messages         — individual turns within a conversation
--   agent_configs    — agent profile definitions (prompts stored encrypted)
--   audit_log        — immutable event log for compliance and debugging
--   users            — multi-user web access (admin dashboard)
--   documents        — knowledge-base document index (chunks stored in ChromaDB)

-- ---------------------------------------------------------------------------
-- Extensions
-- ---------------------------------------------------------------------------
CREATE EXTENSION IF NOT EXISTS "pgcrypto";      -- gen_random_uuid(), pgp_sym_encrypt
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";  -- query performance monitoring

-- ---------------------------------------------------------------------------
-- Conversations
-- ---------------------------------------------------------------------------
CREATE TABLE conversations (
    id            UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_profile VARCHAR(50)  NOT NULL,
    channel       VARCHAR(50)  NOT NULL,    -- web | voice | telegram | sms | whatsapp
    started_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    ended_at      TIMESTAMPTZ,
    metadata      JSONB        NOT NULL DEFAULT '{}'
);

COMMENT ON TABLE  conversations              IS 'One record per dialogue session across all channels';
COMMENT ON COLUMN conversations.agent_profile IS 'Agent profile name, e.g. personal_productivity, customer_support';
COMMENT ON COLUMN conversations.channel       IS 'Inbound channel: web | voice | telegram | sms | whatsapp';
COMMENT ON COLUMN conversations.metadata      IS 'Arbitrary JSON: user agent, locale, session flags, etc.';

-- ---------------------------------------------------------------------------
-- Messages
-- ---------------------------------------------------------------------------
CREATE TABLE messages (
    id              UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID         NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role            VARCHAR(20)  NOT NULL CHECK (role IN ('user', 'assistant', 'system', 'tool')),
    content         TEXT         NOT NULL,
    tokens_used     INTEGER      CHECK (tokens_used >= 0),
    model           VARCHAR(100),
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    metadata        JSONB        NOT NULL DEFAULT '{}'
);

COMMENT ON TABLE  messages              IS 'Individual LLM turns; role follows OpenAI convention';
COMMENT ON COLUMN messages.tokens_used  IS 'Total prompt+completion tokens for this turn (NULL if not tracked)';
COMMENT ON COLUMN messages.model        IS 'Model tag used for this turn, e.g. qwen2.5:7b-instruct';

CREATE INDEX idx_messages_conversation ON messages (conversation_id);
CREATE INDEX idx_messages_created      ON messages (created_at DESC);

-- ---------------------------------------------------------------------------
-- Agent Configurations
-- ---------------------------------------------------------------------------
CREATE TABLE agent_configs (
    id                       UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
    name                     VARCHAR(100) NOT NULL,
    profile                  VARCHAR(50)  NOT NULL,
    model                    VARCHAR(100) NOT NULL,
    -- System prompt is encrypted at rest with the hardware-derived key.
    -- Application layer decrypts on load; never stored in plaintext.
    system_prompt_encrypted  BYTEA,
    tools                    JSONB        NOT NULL DEFAULT '[]',
    channels                 JSONB        NOT NULL DEFAULT '[]',
    hardware_tier            INTEGER      NOT NULL DEFAULT 1 CHECK (hardware_tier BETWEEN 1 AND 4),
    active                   BOOLEAN      NOT NULL DEFAULT TRUE,
    created_at               TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_at               TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  agent_configs                       IS 'One row per configured agent instance on this machine';
COMMENT ON COLUMN agent_configs.system_prompt_encrypted IS 'AES-256 ciphertext; key derived from TPM hardware fingerprint';
COMMENT ON COLUMN agent_configs.tools                 IS 'JSON array of enabled tool names, e.g. ["rag","calendar","email"]';
COMMENT ON COLUMN agent_configs.channels              IS 'JSON array of active channels, e.g. ["web","telegram"]';

-- Keep updated_at current automatically
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_agent_configs_updated_at
    BEFORE UPDATE ON agent_configs
    FOR EACH ROW EXECUTE FUNCTION set_updated_at();

-- ---------------------------------------------------------------------------
-- Audit Log
-- ---------------------------------------------------------------------------
CREATE TABLE audit_log (
    id          BIGSERIAL    PRIMARY KEY,
    event_type  VARCHAR(100) NOT NULL,
    agent_id    UUID         REFERENCES agent_configs(id) ON DELETE SET NULL,
    details     JSONB        NOT NULL DEFAULT '{}',
    created_at  TIMESTAMPTZ  NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE  audit_log            IS 'Append-only event log; rows are never updated or deleted';
COMMENT ON COLUMN audit_log.event_type IS 'e.g. agent.started, model.pulled, config.changed, error.inference';

CREATE INDEX idx_audit_created ON audit_log (created_at DESC);
CREATE INDEX idx_audit_event   ON audit_log (event_type);
CREATE INDEX idx_audit_agent   ON audit_log (agent_id) WHERE agent_id IS NOT NULL;

-- Prevent updates and deletes on the audit log (immutability enforcement)
CREATE OR REPLACE FUNCTION audit_log_immutable()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
    RAISE EXCEPTION 'audit_log rows are immutable — UPDATE and DELETE are not permitted';
END;
$$;

CREATE TRIGGER trg_audit_log_no_update
    BEFORE UPDATE ON audit_log
    FOR EACH ROW EXECUTE FUNCTION audit_log_immutable();

CREATE TRIGGER trg_audit_log_no_delete
    BEFORE DELETE ON audit_log
    FOR EACH ROW EXECUTE FUNCTION audit_log_immutable();

-- ---------------------------------------------------------------------------
-- Users  (multi-user web access — admin dashboard)
-- ---------------------------------------------------------------------------
CREATE TABLE users (
    id            UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
    username      VARCHAR(100) NOT NULL UNIQUE,
    email         VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,   -- bcrypt hash; never store plaintext
    role          VARCHAR(20)  NOT NULL DEFAULT 'user' CHECK (role IN ('admin', 'user')),
    created_at    TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    last_login    TIMESTAMPTZ
);

COMMENT ON TABLE  users               IS 'Dashboard users; passwords are bcrypt-hashed by the application layer';
COMMENT ON COLUMN users.role          IS 'admin = full config access; user = read-only / chat only';

-- ---------------------------------------------------------------------------
-- Documents  (knowledge-base index; vector chunks live in ChromaDB)
-- ---------------------------------------------------------------------------
CREATE TABLE documents (
    id          UUID         PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_id    UUID         NOT NULL REFERENCES agent_configs(id) ON DELETE CASCADE,
    filename    VARCHAR(500) NOT NULL,
    file_type   VARCHAR(50),               -- pdf | docx | txt | md | url
    chunk_count INTEGER      NOT NULL DEFAULT 0 CHECK (chunk_count >= 0),
    ingested_at TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    metadata    JSONB        NOT NULL DEFAULT '{}'
);

COMMENT ON TABLE  documents             IS 'Index of documents ingested into the RAG knowledge base';
COMMENT ON COLUMN documents.chunk_count IS 'Number of text chunks stored in ChromaDB for this document';
COMMENT ON COLUMN documents.metadata    IS 'Source URL, page count, language, ingestion parameters, etc.';

CREATE INDEX idx_documents_agent ON documents (agent_id);

-- ---------------------------------------------------------------------------
-- Seed: default admin user (password MUST be changed at first login)
-- Password 'changeme' — bcrypt hash included here for bootstrap only.
-- The setup wizard will prompt for a real password and update this row.
-- ---------------------------------------------------------------------------
INSERT INTO users (username, email, password_hash, role)
VALUES (
    'admin',
    NULL,
    '$2b$12$placeholder_hash_replace_at_first_boot_wizard_startup',
    'admin'
);
