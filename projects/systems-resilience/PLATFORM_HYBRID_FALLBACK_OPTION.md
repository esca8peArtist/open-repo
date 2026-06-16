# Platform Hybrid Fallback Option: Jitsi for Immediate Collaboration
## Rapid Deployment Path If Platform Decision Delayed

**Version**: 1.0 (Interim Solution Only)  
**Last Updated**: June 16, 2026  
**Deployment Time**: 15 minutes  
**Status**: ⚠️ NOT A REPLACEMENT for Nextcloud+Matrix or Discourse

---

## WHEN TO USE THIS

**Use Jitsi IF:**
- User cannot decide between Nextcloud+Matrix vs Discourse by June 17
- Need immediate video collaboration capability for Phase 5.1 testing
- Want to unblock Wave 2 team coordination while full platform decision pending

**DO NOT Use Jitsi IF:**
- Need persistent document storage
- Need offline editing capability
- Need E2E encryption for sensitive content
- Need discussion forums or threaded conversations
- Need file versioning and sync

---

## WHAT JITSI PROVIDES

### ✅ Capabilities

- **Video conferencing**: 5-10 concurrent participants (Pi5 limited)
- **Screen sharing**: Desktop/window sharing for presentations
- **Chat**: Real-time text during calls (not persistent)
- **Recording**: Optional video recording to disk
- **No account required**: Join meetings by URL link
- **Fast deployment**: 15 min to live

### ❌ Missing (Why It's Fallback Only)

- **No persistent storage**: No file repository, no version history
- **No document collaboration**: Cannot co-edit docs in real-time
- **No offline capability**: Must be connected to join
- **No encryption**: Open to public (can be mitigated with complex URL)
- **No forums/discussion**: No threading, no moderation
- **No calendar/mail**: No integration with admin tools
- **Stateless**: No user accounts, no permission management

---

## DEPLOYMENT SOP (15 minutes)

### 0.1 Pre-Flight Check

```bash
ssh pi@100.70.184.84

# Check resources
free -h | grep Mem
df -h /

# Expected: 6GB+ RAM available, 40GB+ disk
```

### 0.2 Create Directory

```bash
sudo mkdir -p /opt/jitsi
sudo chown pi:pi /opt/jitsi
cd /opt/jitsi
```

### 0.3 Create Environment File

```bash
cat > .env << 'EOF'
DOMAIN=your-domain.com
JITSI_HOST=your-domain.com
JICOFO_AUTH_PASSWORD=$(openssl rand -base64 12)
JVB_AUTH_PASSWORD=$(openssl rand -base64 12)
JITSI_VIDEOBRIDGE_RTC_PORTS=40000:57000
TZ=UTC
EOF

nano .env  # Replace your-domain.com
```

### 0.4 Create docker-compose.yml

Save as `/opt/jitsi/docker-compose.yml`:

```yaml
version: '3.9'

services:
  # Prosody: XMPP server for chat
  prosody:
    image: jitsi/prosody:latest
    container_name: jitsi-prosody
    expose:
      - '5222'
      - '5347'
      - '5280'
    environment:
      DOMAIN: ${DOMAIN}
      JICOFO_AUTH_PASSWORD: ${JICOFO_AUTH_PASSWORD}
      JVB_AUTH_PASSWORD: ${JVB_AUTH_PASSWORD}
      JIGASI_XMPP_PASSWORD: none
      JIBRI_XMPP_PASSWORD: none
      JIBRI_RECORDER_PASSWORD: none
      JIBRI_BREWING_PASSWORD: none
      XMPP_AUTH_DOMAIN: auth.${DOMAIN}
      XMPP_DOMAIN: ${DOMAIN}
      XMPP_MUC_DOMAIN: muc.${DOMAIN}
      XMPP_INTERNAL_MUC_DOMAIN: internal-muc.${DOMAIN}
      LDAP_URL: none
      LDAP_BASE: none
      LDAP_BINDDN: none
      LDAP_BINDPW: none
      LDAP_FILTER: none
      LDAP_AUTH_METHOD: none
      LDAP_VERSION: none
      LDAP_USE_TLS: none
      LDAP_TLS_CIPHERS: none
      LDAP_TLS_CHECK_PEER: none
      LDAP_TLS_CACERT_FILE: none
      LDAP_TLS_CACERT_DIR: none
      LDAP_START_TLS: none
    volumes:
      - prosody_data:/var/lib/prosody
    networks:
      - jitsi-net
    restart: unless-stopped

  # Jicofo: Focus controller
  jicofo:
    image: jitsi/jicofo:latest
    container_name: jitsi-jicofo
    depends_on:
      - prosody
    environment:
      DOMAIN: ${DOMAIN}
      XMPP_DOMAIN: ${DOMAIN}
      XMPP_AUTH_DOMAIN: auth.${DOMAIN}
      XMPP_INTERNAL_MUC_DOMAIN: internal-muc.${DOMAIN}
      JICOFO_AUTH_USER: focus
      JICOFO_AUTH_PASSWORD: ${JICOFO_AUTH_PASSWORD}
      JICOFO_COMPONENT_SECRET: ${JICOFO_AUTH_PASSWORD}
      JVB_BREWERY_MUC: jvbbrewery
      JIGASI_XMPP_USER: jigasi
      JIBRI_XMPP_USER: jibri
      JIBRI_XMPP_PASSWORD: ${JIBRI_XMPP_PASSWORD}
      JIBRI_BREWERY_MUC: jibribrewery
      JVB_RTC_PORT: 4443
    networks:
      - jitsi-net
    restart: unless-stopped

  # JVB: Video bridge
  jvb:
    image: jitsi/jvb:latest
    container_name: jitsi-jvb
    ports:
      - '127.0.0.1:4443:4443/tcp'
      - '127.0.0.1:4443:4443/udp'
      - '127.0.0.1:10000:10000/udp'
    depends_on:
      - prosody
    environment:
      DOMAIN: ${DOMAIN}
      XMPP_AUTH_DOMAIN: auth.${DOMAIN}
      XMPP_INTERNAL_MUC_DOMAIN: internal-muc.${DOMAIN}
      XMPP_SERVER: prosody
      JVB_AUTH_USER: jvb
      JVB_AUTH_PASSWORD: ${JVB_AUTH_PASSWORD}
      JVB_BREWERY_MUC: jvbbrewery
      JVB_RTC_PORT: 4443
      JITSI_VIDEOBRIDGE_RTC_PORTS: ${JITSI_VIDEOBRIDGE_RTC_PORTS}
      JICOFO_AUTH_USER: focus
    networks:
      - jitsi-net
    restart: unless-stopped

  # Web: Jitsi Meet frontend
  web:
    image: jitsi/web:latest
    container_name: jitsi-web
    ports:
      - '127.0.0.1:80:80'
      - '127.0.0.1:443:443'
    depends_on:
      - prosody
    environment:
      DOMAIN: ${DOMAIN}
      TZ: ${TZ}
      JICOFO_AUTH_USER: focus
      XMPP_AUTH_DOMAIN: auth.${DOMAIN}
      XMPP_BOSH_URL_BASE: http://prosody:5280
      XMPP_DOMAIN: ${DOMAIN}
      XMPP_MUC_DOMAIN: muc.${DOMAIN}
      XMPP_INTERNAL_MUC_DOMAIN: internal-muc.${DOMAIN}
    volumes:
      - ./web.env:/etc/jitsi/web/env.js:ro
    networks:
      - jitsi-net
    restart: unless-stopped

volumes:
  prosody_data:
    driver: local

networks:
  jitsi-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.22.0.0/16
```

### 0.5 Create Web Configuration

```bash
cat > web.env << 'EOF'
window.config = {
  hosts: {
    domain: 'YOUR_DOMAIN'
  },
  bosh: '//YOUR_DOMAIN/http-bind',
  clientNode: 'http://jitsi.org',
  focusUserJid: 'focus@auth.YOUR_DOMAIN'
};
EOF

sed -i "s/YOUR_DOMAIN/$(grep '^DOMAIN=' .env | cut -d= -f2)/g" web.env
```

### 0.6 Setup SSL (Let's Encrypt)

```bash
DOMAIN=$(grep '^DOMAIN=' .env | cut -d= -f2)
EMAIL=$(whoami)@example.com

docker run --rm --name certbot \
  -v $(pwd)/ssl:/etc/letsencrypt \
  -p 80:80 \
  certbot/certbot certonly \
    --standalone \
    --email "$EMAIL" \
    -d "$DOMAIN" \
    --agree-tos \
    --non-interactive

mkdir -p ./certs
cp ssl/live/$DOMAIN/fullchain.pem ./certs/cert.pem
cp ssl/live/$DOMAIN/privkey.pem ./certs/key.pem

echo "✅ SSL certificate installed"
```

### 0.7 Start Jitsi

```bash
docker-compose up -d

# Monitor startup
for i in {1..30}; do
  if docker-compose ps | grep -q "Up"; then
    running=$(docker-compose ps --filter "status=running" -q | wc -l)
    echo "[$((i))/30] Services running: $running/4"
    
    if [ "$running" -ge 4 ]; then
      break
    fi
  fi
  sleep 2
done

echo ""
echo "Service Status:"
docker-compose ps
```

### 0.8 Access Jitsi

```bash
DOMAIN=$(grep '^DOMAIN=' .env | cut -d= -f2)

echo ""
echo "=== JITSI WEB ACCESS ==="
echo "📱 URL: https://$DOMAIN"
echo ""
echo "✅ Jitsi is running"
echo ""
echo "To start meeting:"
echo "  1. Visit https://$DOMAIN"
echo "  2. Click 'Start Meeting'"
echo "  3. Enter meeting name"
echo "  4. Share link with team"
```

---

## RESOURCE USAGE

### Memory Footprint (Pi5)

```
Prosody:     64MB idle
Jicofo:      128MB idle
JVB:         256MB idle
Web:         32MB idle
──────────────────────
Total:       480MB (0.5GB)

With 5 concurrent users: ~800MB
With 10 concurrent users: ~1.2GB (limit reached)
```

### CPU Usage

```
Idle:        5-10%
1 meeting:   25-30%
3 meetings:  45-50%
5+ meetings: 70-85% (CPU bottleneck)
```

### Disk Usage

```
Images: ~800MB (downloaded)
Data:   ~100MB (logs, recordings if enabled)
Total:  ~1GB
```

---

## LIMITATIONS & TRADE-OFFS

### Why Jitsi Is NOT Suitable for Phase 5.1 Long-Term

1. **No Persistent Storage** ❌
   - Cannot store published documents
   - No version history
   - No file repository

2. **No Document Collaboration** ❌
   - Cannot co-edit docs
   - Cannot share files
   - No offline sync

3. **No Security Features** ❌
   - No E2E encryption
   - No permission management
   - No user authentication

4. **Scalability Issues** ❌
   - Max 5-10 concurrent users on Pi5
   - Phase 6 needs 50+ simultaneous collaborators
   - CPU/RAM bottleneck reached quickly

5. **No Moderation Tools** ❌
   - No message history
   - No access control
   - No audit trail

### Acceptable Use Cases

- **Interim solution** while deciding between Nextcloud+Matrix vs Discourse
- **Supplementary tool** for team video meetings (with full platform)
- **Testing capability** for Wave 2 onboarding
- **Temporary** (2-3 weeks max, then migrate to full platform)

---

## TIMELINE: HYBRID APPROACH

### If Using Jitsi as Fallback

```
June 16     Jitsi decision
June 17     Deploy Jitsi (15 min)
June 18-30  Use for collaboration while deciding platform
June 30     Final platform decision (Nextcloud+Matrix vs Discourse)
July 1      Deploy chosen platform + migrate data
July 2+     Full Phase 5.1 publication + Phase 6 Wave 2
```

### Total Project Impact

```
Jitsi setup:           15 min
Jitsi operations:      2-3h (monitoring, user support)
Platform deployment:   4-6h (Nextcloud) or 3h (Discourse)
Data migration:        1-2h
Total delay:           ~8-10h vs direct platform choice (~6h)

COST OF DELAY: 2-4 hours additional effort
BENEFIT: Unblock team collaboration immediately
RISK: Additional complexity, data migration effort
```

---

## IF YOU CHOOSE JITSI FALLBACK

### What to Do in Parallel

1. **Week 1 (June 18-24)**: Use Jitsi for team video calls
2. **Week 1 (June 18-24)**: Finalize platform decision (Nextcloud or Discourse?)
3. **Week 2 (June 25-July 1)**: Prepare full platform deployment
4. **Week 3 (July 2+)**: Deploy full platform + migrate collaboration

### Jitsi → Nextcloud+Matrix Migration

```bash
# No direct data migration needed (Jitsi is stateless)
# Process:
# 1. Export Jitsi recordings (if any) to storage
# 2. Copy recording files to Nextcloud /uploads/
# 3. Create Nextcloud folders for project content
# 4. Invite team to Nextcloud + Matrix
# 5. Archive Jitsi (keep for reference only)
```

### Jitsi → Discourse Migration

```bash
# No direct data migration needed
# Process:
# 1. Export Jitsi recordings to external storage
# 2. Create Discourse categories for projects
# 3. Create forum topics summarizing Jitsi discussions
# 4. Archive Jitsi (reference only)
# 5. Invite team to Discourse
```

---

## ROLLBACK / CLEANUP

```bash
cd /opt/jitsi

# Stop services
docker-compose down

# Remove volumes
docker volume prune -f

# Remove directory (optional)
rm -rf /opt/jitsi

echo "✅ Jitsi removed"
```

---

## RECOMMENDATION

**ONLY choose Jitsi IF:**
- Decision timeline is impossible (user unavailable)
- Need immediate video collaboration (24-48h only)
- Plan to deploy full platform within 2 weeks
- Accept additional complexity

**STRONGLY RECOMMEND instead:**
- Choose Nextcloud+Matrix (8/10 confidence)
- Deploy immediately (4-6 hours)
- Begin Phase 5.1 publication by June 19
- Avoid double work of deploying twice

---

## SUMMARY

| Aspect | Jitsi | Nextcloud+Matrix | Discourse |
|--------|-------|------------------|-----------|
| Deploy time | 15 min | 4-6h | 3h |
| Setup complexity | Very easy | Medium | Medium |
| Feature completeness | 20% | 95% | 60% |
| Phase 5.1 ready? | No | Yes | Yes (with workaround) |
| Scalability to 50 users | No | Yes | Yes |
| E2E encryption | No | Yes | No |
| Offline editing | No | Yes | No |
| **Recommendation** | Fallback only | ⭐ PRIMARY | Alternative |

---

**Document Version**: 1.0  
**Last Updated**: June 16, 2026  
**Status**: ⚠️ INTERIM SOLUTION ONLY (use Nextcloud+Matrix for production)
