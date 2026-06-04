---
title: "Phase 5 Author Onboarding Guides — Nextcloud + Matrix"
project: systems-resilience
phase: 5
audience: Wave 1 Authors (18 contributors)
status: PRODUCTION-READY — send with onboarding email June 5 06:00 UTC
created: 2026-06-04
version: 1.0
cross_references:
  - PHASE_5_NEXTCLOUD_MATRIX_CONFIGURATION_TEMPLATES.md
  - PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md
  - NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md
---

# Phase 5 Author Onboarding Guide
## Nextcloud + Matrix — Wave 1 Contributor Access

Welcome to the Phase 5 collaboration platform. This guide has four parts:
1. **Quick Start** (page 1–2): Get connected in 15 minutes
2. **Platform Features** (page 3): What you can do and how
3. **Working Offline** (page 4): Editing without internet connection
4. **Troubleshooting** (page 5): Common problems and fast fixes

---

# Page 1: Quick Start — Connecting in 15 Minutes

## Before You Start

You will need:
- Your login email (the one you used to accept this invitation)
- Your temporary password (in the invitation email)
- Access to the Tailscale network (required; see below)
- A modern web browser (Chrome, Firefox, or Safari)

**Tailscale is required** to access the platform. Tailscale creates a private encrypted network between your computer and the server. It is free, installs in under 5 minutes, and does not route your regular internet traffic.

---

## Step 1: Install Tailscale (5 minutes)

1. Download Tailscale: **https://tailscale.com/download**
2. Install for your operating system:
   - **Windows**: Run the `.exe` installer, sign in or create a free account
   - **macOS**: Install from the App Store or download from the site
   - **Linux**: Follow the instructions at https://tailscale.com/download/linux
   - **iOS / Android**: Install from your app store, then sign in
3. After installing, Tailscale runs in the background. You will see a Tailscale icon in your system tray or menu bar.
4. **Tell your platform contact you've installed Tailscale** (reply to the invitation email with "Tailscale installed") — the admin needs to approve your device to join the private network.
5. Once approved, you will see a green icon indicating you are connected.

---

## Step 2: Access Nextcloud (Your Document Workspace)

Nextcloud is where you write and store your article draft, access the editorial calendar, and read author guides.

1. Open your browser and go to: **https://100.70.184.84**
   - Your browser may show a security warning ("Your connection is not private"). This is expected — the server uses a private certificate. Click **Advanced → Proceed to 100.70.184.84** (or "Accept Risk and Continue" in Firefox).
2. You will see the Nextcloud login screen. Enter:
   - Username: *[from your invitation email]*
   - Password: *[from your invitation email]*
3. On first login, Nextcloud will ask you to change your password. **Choose a strong password** and store it in a password manager.
4. You will land on the Nextcloud home screen. Your files dashboard is the default view.

**What you see when you first log in**:
- A folder called `Phase5_Wave1` has been shared with you. This is your workspace.
- Inside, you will find a folder for your assigned domain (e.g., `Domain1_Governance`).
- Inside that folder is an `Article_Template.md` file — this is your starting point.

---

## Step 3: Find Your Article Template

1. In Nextcloud, click **Files** (the folder icon in the left sidebar)
2. Navigate to: `Phase5_Wave1` → `Domain[N]_[Name]` (your assigned domain)
3. Click `Article_Template.md`
4. Nextcloud will open the file in the **Text** editor (the built-in Markdown editor)
5. You can start editing immediately. Changes save automatically every few seconds.

**Important**: The `_Administration` folder contains Author Guides and Editorial Calendar. You can read these but not edit them.

---

## Step 4: Access Matrix Chat (Real-Time Coordination)

Matrix is the messaging platform for coordinating with other authors and editors.

1. In your browser, go to: **https://100.70.184.84** (same address as Nextcloud — both are on the same server)
   - Note: The Nextcloud login and the Matrix login are separate. You may be logged into Nextcloud but still need to log into Element (the Matrix chat client).
2. Look for the **Chat** or **Element** link, or navigate to **https://100.70.184.84/element/** if provided.
3. Log in with the same username and password as Nextcloud.
4. You will be automatically joined to several rooms. Look for:
   - **#general** — Introduction and announcements
   - **#domain-[N]-[name]** — Your domain's working room
   - **#technical** — Platform support

5. **First action**: Send a message in **#general** introducing yourself. This confirms your account is working.

---

## Step 5: Confirm Your Setup

Send a reply to the onboarding email with:
- [ ] Tailscale connected (green icon)
- [ ] Nextcloud login works
- [ ] Can see your domain folder
- [ ] Element Web login works
- [ ] Sent intro message in #general

You are now fully onboarded. See Page 2 for how to get started on your article.

---

# Page 2: Your First 48 Hours

## What to Do After Setup

### Day 1 (June 5–6):
1. Read the `Article_Template.md` in your domain folder
2. Read `_Administration/Author_Guides/` — contains the editorial standards and citation format
3. Say hello in your domain room (e.g., `#domain-1-governance`)
4. Check the shared calendar — key dates are listed there (CalDAV sync instructions on Page 3)

### Day 2–3 (June 7–8):
1. Create your own working document in your domain folder:
   - Click the `+` button in the file browser
   - Name it: `[YourLastName]_Draft_v01.md`
   - Copy the Article Template content into it
2. Begin filling in your sections — even a rough outline counts
3. The **#coordination** room has a daily async check-in at 09:00 UTC. If you have blockers, post there.

### Deadline Reminder
- **Draft due**: June 30, 2026
- **Peer review due**: July 15, 2026
- **Questions**: Post in `#domain-[N]-[name]` or email the lead editor

---

# Page 3: Platform Features

## Nextcloud — File Collaboration

### What Nextcloud Does

- **Document storage and sync**: All your files are stored on the server. You can edit them in the browser or sync them to your local computer (see Page 4 for offline access).
- **Real-time collaborative editing**: Multiple authors can edit the same Markdown document simultaneously. You will see other editors' cursors.
- **Version history**: Every time you save, Nextcloud keeps a version. You can revert to any earlier version via the three-dot menu → "Details" → "Versions".
- **Comments**: You can leave inline comments on a document. Highlight text → click the comment bubble → leave a note. Other authors receive a notification.
- **Sharing**: You can share a document or folder with a link (read-only or edit access). Use this to share a draft with external reviewers who do not have an account.

### How to Collaborate on a Document

1. Open any `.md` file in the file browser
2. The Nextcloud **Text** editor opens automatically
3. Click the share icon (top right) → type your co-author's username → click "Share"
4. Both of you can now edit simultaneously — you will see each other's text appear in real time

### Uploading Files

- Drag and drop files into the file browser to upload them
- Maximum upload size: 512 MB per file
- Supported file types: all common formats (`.md`, `.pdf`, `.docx`, `.png`, etc.)

### Shared Calendar (CalDAV)

Add the editorial calendar to your own calendar app to see deadlines alongside your personal schedule.

**Calendar URL** (add as a CalDAV subscription):
```
https://100.70.184.84/remote.php/dav/calendars/admin/editorial-calendar/
```

**Setup**:
- **macOS Calendar**: File → New Calendar Subscription → paste URL → enter your Nextcloud username/password
- **Thunderbird Lightning**: Calendar → New Calendar → "On the network" → CalDAV → paste URL
- **iOS**: Settings → Calendar → Accounts → Other → Add CalDAV Account → Server: `100.70.184.84`, username/password as above

---

## Matrix / Element — Encrypted Messaging

### What Matrix Does

- **Real-time chat**: Send and receive messages instantly in dedicated rooms
- **End-to-end encryption**: All private room messages are encrypted. Only room members can read them. The server cannot read them.
- **File sharing**: Send files in chat up to 50 MB
- **Notifications**: Desktop and mobile notifications (configure in Settings → Notifications)
- **Message history**: All previous messages in a room are available when you join

### Room Guide

| Room | Purpose | Who Is In It |
|------|---------|-------------|
| **#general** | Announcements, introductions | All authors + editors |
| **#coordination** | Deadlines, check-ins, blockers | All authors + editors |
| **#domain-1-governance** | Domain 1 working discussion | Domain 1 authors + editor |
| **#domain-2-food** | Domain 2 working discussion | Domain 2 authors + editor |
| **#domain-3-infrastructure** | Domain 3 working discussion | Domain 3 authors + editor |
| **#domain-4-security** | Domain 4 working discussion | Domain 4 authors + editor |
| **#domain-5-scaling** | Domain 5 working discussion | Domain 5 authors + editor |
| **#peer-review** | Cross-domain review discussion | All authors |
| **#technical** | Platform help | All authors + admin |

### Useful Features in Element

- **Reply to a message**: Hover over a message → click the reply arrow → type your response
- **Reactions**: Hover over a message → click the emoji icon → add a reaction
- **Pin a message**: Hover → three dots → "Pin". Pinned messages appear at the top of the room.
- **Format messages**: Use Markdown. Type `/help` in the message box for a cheat sheet.
- **Notifications**: Settings (gear icon) → Notifications → configure per-room notification level

---

# Page 4: Working Offline

This platform is designed for contributors who may have intermittent internet connections. Both Nextcloud and Matrix support offline-first workflows.

## Nextcloud Desktop Sync (Recommended for Offline Work)

The Nextcloud Desktop client syncs your assigned folders to your local hard drive. You can edit files while offline and they sync automatically when you reconnect.

### Install the Desktop Client

1. Download: **https://nextcloud.com/install/#install-clients**
2. Choose your operating system (Windows, macOS, or Linux)
3. Install and open the application

### Connect to the Server

1. Open Nextcloud Desktop
2. Click **Log in** → **Log in with credentials**
3. Server address: `https://100.70.184.84`
4. Accept the security certificate warning (same as in the browser)
5. Enter your username and password
6. Choose which folders to sync:
   - At minimum: sync your domain folder (`Phase5_Wave1/Domain[N]_[Name]`)
   - Optionally: sync `_Administration/Author_Guides` for offline reference

### Offline Editing Workflow

1. **Make sure your folder is synced** before going offline (green checkmark icon on your Nextcloud folder)
2. Disconnect from the internet or switch off Tailscale
3. **Edit your files normally** in any text editor, Word, or your preferred Markdown editor
4. When you reconnect, Nextcloud Desktop automatically uploads your changes
5. If two people edited the same file simultaneously, Nextcloud creates a conflict file (e.g., `Article_Draft_v01 (conflicted copy).md`). You merge the two versions manually and delete the conflict file.

### Mobile Offline Access (iOS / Android)

1. Install the Nextcloud mobile app (App Store or Google Play)
2. Log in with the same credentials
3. Browse to your domain folder
4. Tap the three-dot menu on a file → **Keep offline** (Android) or **Make available offline** (iOS)
5. The file downloads to your device for offline editing in the app

---

## Matrix / Element Offline (Message Queuing)

Element stores recent message history locally in your browser. When you are offline:

- **Reading messages**: The last ~1,000 messages per room are cached locally. You can read them without a connection.
- **Sending messages**: If you send a message while offline, it appears with a pending indicator (clock icon). When you reconnect, it sends automatically in order.
- **Encryption keys**: Your E2E encryption keys are stored locally. You can decrypt and read existing encrypted messages offline.

**Limitation**: Matrix requires the server to be reachable to deliver new messages. If raspby1 is offline, messages cannot be delivered until it comes back online. For truly off-grid scenarios, use the Nextcloud Desktop sync as your primary communication tool (leave notes in a shared document).

### Preventing Lost Messages

To avoid losing messages if your browser cache clears:
1. In Element, go to Settings → Security & Privacy → **Export E2E room keys**
2. Save the key file to a secure location
3. To restore on a new device: Settings → Security & Privacy → **Import E2E room keys**

---

# Page 5: Troubleshooting

## "My browser says the connection is not private"

**This is expected.** The server uses a private certificate that your browser does not automatically trust.

Fix: Click **Advanced** → **Proceed to 100.70.184.84** (Chrome) or **Accept the Risk and Continue** (Firefox). You only need to do this once per browser.

If the error says "NET::ERR_CERT_AUTHORITY_INVALID" and the above steps do not work, try:
1. Check that Tailscale is connected (green icon)
2. Try in an incognito/private browser window
3. Ask in `#technical` for help

---

## "I can't reach https://100.70.184.84"

**Most likely cause**: Tailscale is not connected.

Fix:
1. Check the Tailscale icon in your system tray/menu bar — it should be green
2. If it is grey or red, click it and select **Connect**
3. If it shows "Needs approval": contact the admin (the invite was not accepted yet)
4. After connecting, wait 5–10 seconds and try again

If Tailscale is connected but the site still does not load:
1. Try pinging: open Terminal/Command Prompt and type `ping 100.70.184.84`
2. If ping fails: the server may be temporarily down. Check `#technical` in Matrix.

---

## "I forgot my password"

1. Go to `https://100.70.184.84` and click **Forgot password?** on the login screen
2. Enter your email address
3. Check your email for a password reset link (may take 2–3 minutes; check spam)
4. If no email arrives: post in `#technical` and the admin will manually reset your account

---

## "I can't see my domain folder in Nextcloud"

Your domain folder is shared with your account, but you need to accept the share:
1. Log into Nextcloud
2. Click the bell icon (top right) to see notifications
3. Find the share notification and click **Accept**
4. The folder should now appear in your file browser

If there is no notification, contact the admin via `#technical`.

---

## "Element says I'm not in any rooms"

This happens if you logged into Element before the admin sent your room invitations.

Fix:
1. Click the search icon in Element (top left)
2. Search for `#general:resilience-hub.local`
3. If you see "Accept invite", click it to join
4. Repeat for your domain room

If you cannot find the rooms: the admin may not have sent invitations yet. Post in `#technical` once you are in #general.

---

## "My Nextcloud Desktop client shows files with a red X"

A red X on synced files usually means a sync conflict or a permission error.

Fix:
1. Click the Nextcloud Desktop icon in your system tray/menu bar
2. Click **Open Log** to see the error
3. Common fixes:
   - **Conflict**: Two people edited the same file. Open both versions, merge changes manually, and delete the `(conflicted copy)` file.
   - **Permission error**: You may not have write access to that folder. Check with the admin.
   - **Out of disk space**: Free up space on your local drive and retry sync.

---

## "I can't send messages in Element — the send button is greyed out"

Usually a connectivity issue:
1. Check Tailscale is connected
2. Refresh the Element Web page
3. Try logging out and back in

If the room shows "Encryption error" or "Unable to decrypt":
1. Go to Settings → Security & Privacy → **Verify this device**
2. Complete the device verification process

---

## Contacts and Resources

| Channel | Use for |
|---------|---------|
| `#technical` (Matrix) | Platform bugs, access issues, urgent help |
| `#coordination` (Matrix) | Editorial questions, deadline changes |
| Platform admin email | Account problems that prevent you from accessing Matrix |
| Nextcloud official docs | https://docs.nextcloud.com |
| Element Web docs | https://element.io/help |
| Matrix Spec (advanced) | https://spec.matrix.org |

---

## Security Notes

- **Do not share your password** with anyone, including the platform admin. The admin can reset your password without knowing it.
- **Do not use the same password** as other services. Use a password manager.
- **E2E encryption is on by default** in private rooms. Your messages are private.
- If you ever suspect your account was compromised, change your password immediately and post in `#technical`.

---

*Document version 1.0 — June 5, 2026*  
*Prepared by the Phase 5 coordination team*  
*License: CC BY-SA 4.0 — free to share and adapt with attribution*
