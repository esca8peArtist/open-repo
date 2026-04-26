import os
# Set required Settings fields for test environment before anything imports agentcore
os.environ.setdefault("POSTGRES_URL", "postgresql+asyncpg://test:test@localhost/testdb")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379/0")
os.environ.setdefault("API_SECRET_KEY", "test-secret-key-that-is-long-enough")
