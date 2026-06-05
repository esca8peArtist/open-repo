---
title: "Phase 5 Meshtastic Bridge — Status and Contingency Architecture"
project: systems-resilience
phase: 5
status: RESEARCH COMPLETE — bridge available; deployment deferred to Phase 6/7
bridge_status: ACTIVE (v1.3.7, released May 3 2026)
confidence: 88%
created: 2026-06-05
version: 1.0
cross_references:
  - PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP_v2.md
  - NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md
  - PHASE_5_DEPLOYMENT_CHECKLIST_AND_ONBOARDING.md
---

# Phase 5 Meshtastic Bridge — Status and Contingency Architecture

---

## Lead Finding

The Matrix-Meshtastic relay bridge (`meshtastic-matrix-relay` by jeremiah-k) is **actively maintained** as of June 2026, with version 1.3.7 released May 3, 2026. It supports Docker deployment and bidirectional relay between Meshtastic LoRa radio networks and Matrix rooms. The bridge is technically deployable alongside the Phase 5 stack.

**Deployment recommendation for Phase 5**: Defer the bridge to Phase 6 or Phase 7. The bridge requires physical Meshtastic hardware (radio nodes) and at minimum one community member with a configured device. Deploying the bridge without hardware validation and a radio operator to test it creates unnecessary Phase 5 complexity. The Matrix+Element stack alone provides offline message queuing for the current Phase 5 author coordination use case.

**Confidence level**: 88% — bridge code is verified active; hardware availability and community readiness are the uncertain variables.

---

## Section 1: Current Bridge Status

### 1.1 meshtastic-matrix-relay (jeremiah-k)

| Attribute | Value |
|-----------|-------|
| Repository | https://github.com/jeremiah-k/meshtastic-matrix-relay |
| Current version | 1.3.7 (released May 3, 2026) |
| Total releases | 83 |
| Total commits | 1,163+ |
| License | Open source (MIT) |
| Docker support | Yes (Dockerfile + Docker Guide in docs) |
| Kubernetes support | Yes |
| Maintenance status | Actively maintained |
| Community | Active public relay room at #mmrelay-relay-room:matrix.org |

**What changed in v1.3.7**: Added vodozemac-backed E2E encryption support for Matrix rooms (via matrix-nio fork). This means the relay now correctly participates in end-to-end encrypted Matrix rooms rather than transmitting as unencrypted.

**Alternative bridges**:
- `mmrelaynode` (mate71pl) — Meshtastic/Matrix relay via MQTT, native Meshtastic node integration. Less mature but an alternative if the primary relay has issues.

### 1.2 What the Bridge Does

The relay provides **bidirectional message relay** between:
- **Meshtastic LoRa radio network**: mesh of radio nodes communicating peer-to-peer over unlicensed radio frequencies (915 MHz in North America). No internet required between nodes.
- **Matrix rooms**: standard Matrix homeserver rooms, bridged via a bot account.

**Message flow:**
```
[Field radio node]  ←→  [LoRa mesh]  ←→  [Relay node with USB/TCP connection]
                                                    |
                                         [meshtastic-matrix-relay]
                                                    |
                                         [Matrix Synapse homeserver]
                                                    |
                                         [Element Web / Matrix clients]
```

**What this enables**: Community members in the field with Meshtastic radios (Heltec LoRa v3, T-Echo, RAK4631, etc.) can exchange messages with Matrix users even when internet infrastructure is down, as long as at least one relay node has connectivity to the Matrix homeserver. This is a store-and-forward model.

**What it does not enable**: Pure peer-to-peer internet-free communication between Matrix users. Matrix still requires the homeserver to relay messages between clients.

### 1.3 Hardware Requirements

To activate the bridge, at minimum the following hardware is needed:

| Item | Description | Approximate Cost |
|------|-------------|-----------------|
| Meshtastic node (USB/serial) | e.g., Heltec LoRa 32 v3, LILYGO T-Echo | $30–$80 |
| Antenna | 915 MHz (North America) or 868 MHz (Europe) | $10–$40 |
| Host machine | Raspberry Pi or any Linux machine running the relay daemon | (raspby1 can host both) |
| Field nodes (per participant) | Each community member needs their own Meshtastic device | $30–$80 each |

Range per node: 2–10 km line-of-sight; less in urban/forested environments. Mesh topology extends range: each additional node can relay messages.

---

## Section 2: Integration Steps (When Hardware Is Available)

### 2.1 Bridge Container Definition

Add this service to the Phase 5 `docker-compose.yml` when hardware is ready:

```yaml
  # ----------------------------------------------------------------
  # Meshtastic-Matrix Relay Bridge
  # Requires: Meshtastic node connected via USB or TCP
  # Activate in Phase 6/7 after hardware validation
  # ----------------------------------------------------------------
  mmrelay:
    image: ghcr.io/jeremiah-k/meshtastic-matrix-relay:latest
    container_name: community-mmrelay
    restart: unless-stopped
    depends_on:
      - synapse
    volumes:
      - ./mmrelay/config.yaml:/config/config.yaml:ro
      - ./data/mmrelay:/data
    # For USB-connected Meshtastic node:
    # devices:
    #   - /dev/ttyUSB0:/dev/ttyUSB0
    networks:
      - resilience-net
    mem_limit: 128m
    healthcheck:
      test: ["CMD-SHELL", "ps aux | grep mmrelay | grep -v grep || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### 2.2 Bridge Configuration (mmrelay/config.yaml)

```yaml
# mmrelay/config.yaml
# Replace all placeholder values before deployment

matrix:
  homeserver: "https://matrix.resilience-hub.local"
  access_token: "PASTE_BOT_ACCESS_TOKEN"
  bot_user_id: "@meshbridge:resilience-hub.local"

meshtastic:
  # Choose ONE of: serial (USB), network (TCP/IP), or ble
  connection_type: serial
  serial_port: /dev/ttyUSB0   # adjust for your device
  # For network-connected node:
  # connection_type: network
  # host: 192.168.1.100
  # port: 4403

# Map Meshtastic channels to Matrix rooms
# Get room IDs from: curl -H "Authorization: Bearer TOKEN" https://MATRIX/_synapse/admin/v1/rooms
matrix_rooms:
  - id: "!ROOM_ID_GENERAL:resilience-hub.local"
    meshtastic_channel: 0
    name: "General"

  - id: "!ROOM_ID_EMERGENCY:resilience-hub.local"
    meshtastic_channel: 1
    name: "Emergency"

relay_config:
  # Maximum message length to relay (LoRa packet limit is ~234 bytes)
  max_message_length: 200
  # Prefix messages from Matrix with [Matrix] to identify source
  matrix_to_mesh_prefix: "[Net]"
  # Prefix messages from Mesh with sender's node ID
  mesh_to_matrix_format: "[Mesh:{node}] {message}"

logging:
  level: INFO
  file: /data/mmrelay.log

database:
  filepath: /data/mmrelay.sqlite
```

### 2.3 Matrix Bot Account Creation

```bash
# Create a dedicated bot account for the relay
docker exec -it community-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u meshbridge \
  -p "$(python3 -c 'import secrets; print(secrets.token_urlsafe(24))')" \
  --no-admin \
  http://localhost:8008

# Get bot access token
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"type":"m.login.password","user":"meshbridge","password":"MESHBRIDGE_PASSWORD"}' \
  https://matrix.resilience-hub.local/_matrix/client/r0/login \
  | python3 -m json.tool
# Copy "access_token" into mmrelay/config.yaml

# Invite the bot to each room it should bridge
# (Do this from admin's Element client or API)
curl -s -X POST \
  -H "Authorization: Bearer $MATRIX_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "@meshbridge:resilience-hub.local"}' \
  "https://matrix.resilience-hub.local/_matrix/client/v3/rooms/!ROOM_ID:resilience-hub.local/invite"
```

### 2.4 Deployment Sequence

1. Obtain Meshtastic hardware and configure at least one node (Meshtastic app on mobile)
2. Connect node via USB to raspby1 or via TCP (Meshtastic WiFi mode)
3. Identify device path: `ls /dev/ttyUSB*` or `ls /dev/ttyACM*`
4. Create `./mmrelay/` directory and populate `config.yaml`
5. Add `mmrelay` service to docker-compose.yml (Section 2.1 above)
6. `docker compose up -d mmrelay`
7. Monitor logs: `docker logs community-mmrelay --tail=20 -f`
8. Send test message from Meshtastic app → verify it appears in Matrix room
9. Send message in Matrix room → verify it appears on Meshtastic device

### 2.5 Multi-Node Edge Deployment

For Phase 7 multi-node deployment, the relay can run on edge devices (not just raspby1):

```
Edge deployment model:
  [Remote community location]
    └─ Raspberry Pi (edge node) running mmrelay
         ├─ USB: Meshtastic radio node
         └─ Internet: connects back to Matrix homeserver (100.70.184.84)
         
  [Second remote location]  
    └─ Raspberry Pi (edge node 2) running mmrelay
         ├─ USB: Meshtastic radio node
         └─ Internet: connects to same Matrix homeserver

  Both sets of radio nodes can communicate with all Matrix users
  via their respective relay daemons.
```

This requires:
- A Raspberry Pi (or similar) at each community location
- USB Meshtastic node at each location
- Internet connectivity (even intermittent) at each location to sync with homeserver

---

## Section 3: Contingency Architecture (Bridge Deferred)

If the Meshtastic bridge is not deployed in Phase 5, the following architecture provides maximum offline resilience without radio hardware:

### 3.1 Contingency Stack (No Bridge)

```
Primary comms (network available):
  Element Web ←→ Matrix Synapse
  - Encrypted group messaging
  - Offline message queue (IndexedDB, ~1000 msg/room)
  - E2E encryption with local key storage

File collaboration (any connectivity state):
  Nextcloud Desktop Client (local sync folder)
  - All drafts available offline on author's machine
  - Edits queue and sync when connection returns
  - CalDAV calendar accessible offline in native calendar app

Out-of-band fallback (no server connectivity):
  - Pre-exported contact list (phone numbers, Signal IDs)
  - Printed coordination schedule distributed at last sync
  - Designated check-in frequency via out-of-band channel
```

### 3.2 Phase-by-Phase Deferral Plan

| Phase | Comms Capability | Meshtastic Status |
|-------|-----------------|-------------------|
| Phase 5 (current) | Element Web + Nextcloud offline sync | Not deployed |
| Phase 6 | Same + LDAP SSO | Evaluate hardware acquisition |
| Phase 7 | Full stack + Meshtastic bridge | Deploy if hardware secured |

The deferral costs nothing in Phase 5 — the Matrix stack is fully functional without the bridge. The bridge adds value only for scenarios where the homeserver itself is unreachable (complete infrastructure failure), which is out of scope for Phase 5's author coordination use case.

### 3.3 Offline-First Degradation Levels

| Network State | Nextcloud | Matrix | Coordination Method |
|---------------|-----------|--------|---------------------|
| Full network | Real-time sync | Real-time messaging | Normal operation |
| Intermittent | Queued sync | Queued messages | Same, delayed |
| Server down (network up) | Local files only | Cached messages only | Phone/Signal fallback |
| Network down | Local files only | Cached messages only | Phone/Signal + printed schedule |
| All infra down | Local files only | — | Radio (Meshtastic, if deployed) |

---

## Section 4: Timeline Impact Assessment

### 4.1 If Bridge Is Deployed in Phase 5

- Additional setup time: 2–4 hours (after hardware is in hand)
- Hardware acquisition lead time: 1–2 weeks (online order) or same-day (local electronics store)
- Risk: bridge configuration errors could delay Phase 5 go-live if debugging takes longer than expected
- **Recommendation**: Deploy the base stack first (June 5-15), add bridge as a separate task in the same window if hardware is available

### 4.2 If Bridge Is Deferred to Phase 6

- No timeline impact on Phase 5
- Phase 6 adds bridge as a parallel workstream, not a dependency
- Hardware can be sourced and tested during Phase 5 publication cycle
- Bridge deployment can be validated in isolation before connecting to production Matrix

### 4.3 If Bridge Is Permanently Deferred

- No operational impact for Phase 5 or Phase 6 author coordination
- Only relevant for Phase 7+ scenarios (community members in field during infrastructure failure)
- Element Web + Nextcloud offline sync covers the Phase 5-6 use case completely

---

## Sources

- [meshtastic-matrix-relay GitHub repository](https://github.com/jeremiah-k/meshtastic-matrix-relay)
- [mmrelaynode (MQTT-based alternative)](https://github.com/mate71pl/mmrelaynode)
- [Matrix.org public relay room](https://matrixrooms.info/room/meshtastic-relay-room:matrix.org)
- [Meshtastic hardware overview 2026](https://smartnmagic.com/blogs/solutions/meshtastic-hardware-the-complete-guide)

**Status**: Bridge verified active (v1.3.7, May 3 2026). Deployment deferred to Phase 6/7 pending hardware availability.
**Confidence**: 88% — code confirmed; hardware acquisition and community readiness are the remaining uncertainties.
