---
title: "Journalist Field Reporting Scenarios: Photojournalism and Protest Coverage Security Procedures"
project: cybersecurity-hardening
created: 2026-06-22
phase: Phase 2
version: 1.0
type: scenario-playbook
depends_on:
  - phase-2-journalist-security-playbook.md
  - opsec-playbook.md
  - phase-2-activist-organizing-security-playbook.md (Sections 4–5 on physical countermeasures)
audience: Photojournalists, visual reporters, field reporters, assignment editors, news organizations covering enforcement actions and protests
---

# Journalist Field Reporting Scenarios: Photojournalism and Protest Coverage

This document provides worked decision trees for two of the highest-threat journalist activities in 2026: photojournalism at enforcement actions and protest coverage during potential law enforcement operations.

---

## Scenario A: Photojournalist Covering an Enforcement Action (ICE Raid, Police Activity, or Protest Enforcement)

**Threat context** (from `phase-2-journalist-security-playbook.md` Section 2.1):
- Clearview AI facial recognition: 50B+ scraped images, including news photos and public social media profiles
- Mobile Fortify: ICE agents capture photos of journalists covering enforcement; faces matched against HART database (150M+ records)
- Cellebrite seizure: If detained or arrested, personal devices are subject to forensic extraction in AFU (After First Unlock) state
- CBP port-of-entry search: Electronic devices can be searched without warrant at borders
- Metadata extraction: EXIF data in photos contains timestamp, location, device identifier

**Decision timeline**: Pre-assignment (24 hours before), en route (30 minutes before), on scene (during coverage), post-scene (after leaving the location)

---

### Pre-Assignment Phase (24 Hours Before)

**Decision Point 1A: Device Selection**

You have three options for the primary reporting device (camera or phone with camera).

**Option A — Dedicated Reporting Device (Recommended for high-risk assignments)**

- **What it is**: A phone or camera owned by you or your news organization that is used ONLY for field reporting and contains no personal identity, no personal data, no personal communications
- **Setup**:
  - [ ] If phone: factory reset to clean install; Android running GrapheneOS (Pixel 6–9) or iOS with all iCloud disabled
  - [ ] If dedicated camera: standard DSLR or mirrorless; disable built-in Wi-Fi; disable built-in GPS if present
  - [ ] No SIM card in the device; no cellular connectivity
  - [ ] No email account on the device; no personal accounts (no Signal, no Gmail, no iCloud)
  - [ ] No applications except camera app and file management
  - [ ] Full device encryption enabled (default on GrapheneOS and modern iOS)
  - [ ] BFU auto-reboot enabled (GrapheneOS: 18 hours recommended; Apple: use Erase iPhone Data option)

- **Justification**: If detained and your device is seized:
  - [ ] No contacts that identify your sources
  - [ ] No messages to editors (metadata that could identify your story pitch)
  - [ ] No device identification that ties the phone to you
  - [ ] No personal data that could be used to compel disclosure of source information
  - [ ] Auto-reboot returns the device to BFU state if not accessed immediately, defeating Cellebrite extraction in AFU

- **Limitation**: You cannot check email or messages during the assignment; you cannot communicate with your editor except by borrowed device or public phone
- **Cost**: $400–800 for a dedicated phone; $0 if using organization-owned camera

**Option B — Segmented Personal Phone with Secondary Profile**

- **What it is**: Your personal phone with a separate user profile (Android) or a dedicated secure container (iOS Guided Access mode) containing only the camera app and no personal data
- **Setup (Android with multiple user accounts)**:
  - [ ] Create a secondary user account on your personal Android device (Settings → Users)
  - [ ] Do not sign into any Google account on the secondary user
  - [ ] Secondary user profile contains only the camera app and file management
  - [ ] Switch to secondary user profile before going into the field
  - [ ] All photos are saved to the secondary user's storage, not your personal storage

- **Setup (iOS with Guided Access)**:
  - [ ] Enable Guided Access (Settings → Accessibility → Guided Access)
  - [ ] Open the Camera app and activate Guided Access
  - [ ] Lock the device to the Camera app only
  - [ ] This prevents access to Photos, Messages, or any app except Camera
  - [ ] To exit Guided Access, you need the access code (set to a value only your editor or security team knows)

- **Justification**: If device is seized, law enforcement sees only camera; your personal messages and contacts are not accessible without exiting the restricted mode, which requires an action they cannot perform on the spot (password entry for secondary user, or Guided Access code entry for iOS)

- **Limitation**: Requires switching user profiles (Android) or losing full phone access (iOS Guided Access); if you need to verify a fact quickly or check signal strength, you are switching back to the primary profile and breaking the segmentation

- **Cost**: $0 (use your existing phone)

**Option C — News Organization Device**

- **What it is**: A phone or camera owned by your news organization, provisioned for field reporting with the same segmentation as Option A
- **Setup**: Identical to Option A
- **Advantage**: If seized, the device is the organization's property; law enforcement must follow organizational data retention policies; attorney is more readily available because the organization is a party to the seizure
- **Disadvantage**: Organizational MDM (mobile device management) may require location tracking or messaging integration that undermines the security model
- **Cost**: $0 to $400 (organization bears cost)

---

**Decision for this assignment**:
- [ ] High risk (enforcement action targeting journalists, CBP environment, arrest likelihood): Use Option A (dedicated device)
- [ ] Medium risk (public protest, no specific targeting of press, good legal support available): Use Option B (segmented personal phone)
- [ ] Ongoing assignment (daily news coverage, multiple events): Use Option C (organization device with segmentation)

---

**Decision Point 1B: Camera Settings and Metadata**

Metadata in your photos creates a permanent record of time, location, and device. This metadata can be extracted and queried by law enforcement.

- [ ] **EXIF metadata**: Disable all EXIF data collection on your camera or phone
  - [ ] Android camera: Settings → Advanced → Disable location
  - [ ] iPhone camera: Settings → Privacy → Location Services → Camera → Never
  - [ ] DSLR/mirrorless: Menu → Setup → Record location → Off (if present)
  - [ ] Alternative: Remove EXIF data from photos after capture using ExifTool or equivalent before transmitting

- [ ] **Device identifier**: Your camera or phone has a unique identifier (MAC address for Wi-Fi, IMEI for cellular, serial number). Law enforcement can use this to query carrier or manufacturer records.
  - [ ] If using a dedicated reporting device: explain to your editor that the device should be treated as a field-only asset with no personal identity attached
  - [ ] If using a personal phone: photos are already timestamped with your device ID; exif removal is your primary countermeasure

- [ ] **Filename strategy**: Your camera names files sequentially (IMG_0001.jpg, etc.) or with date stamps. If photos are discovered in law enforcement custody, the filenames alone create a timeline of your movements.
  - [ ] Rename photos immediately upon upload (before sharing with editor): ASSIGNMENT_DESCRIPTOR_SCENE_FRAME.jpg (e.g., ICE_RAID_2026_06_22_DETENTION_CENTER_003.jpg)
  - [ ] This removes the sequential filename that implies you were taking pictures in real-time

---

**Decision Point 1C: Data Transmission Plan**

You have photos from the field. How do you get them to your editor?

**Approach 1: Air-gapped (Most Secure)**
- [ ] After leaving the scene, power off your reporting device
- [ ] Go to a location with trusted Wi-Fi (news organization office, secure location) that is NOT the location where you were photographing
- [ ] Power on the device
- [ ] Upload photos to a secure cloud folder (ProtonMail Drive, Tresorit, or organization's encrypted server) via Wi-Fi only
- [ ] Verify upload is complete
- [ ] Power off the device
- [ ] Do NOT use the device for any other activity (messaging, email, browsing)
- [ ] Time: 15–30 minutes between leaving scene and upload
- [ ] Advantage: Geolocation services never see your device at the scene; the device has never connected to a carrier network that logs location; law enforcement attempting to find you via carrier tower location history will see only the office location, not the scene

**Approach 2: Delayed Cloud Sync (Moderate Security)**
- [ ] Phones with cloud backup (OneDrive, Google Drive, iCloud) automatically sync photos
- [ ] This happens through cellular data in real-time (location-tagged)
- [ ] Do NOT use automatic sync; disable it before field assignment
- [ ] Instead, connect only to trusted Wi-Fi after leaving the scene, then trigger manual sync
- [ ] Advantage: Uses the same device; disadvantage: real-time sync is compromised
- [ ] Time: Same as Approach 1

**Approach 3: Multi-Device Handoff (Practical for Large Teams)**
- [ ] Photographer uses the dedicated reporting device
- [ ] An accompanying team member (not the photographer) has a secondary device (second phone or tablet)
- [ ] Photos are transferred from reporting device to the secondary device via USB or local Wi-Fi transfer (not internet)
- [ ] The secondary device uploads the photos from a different location (not the scene, using a different network)
- [ ] Advantage: Photographer's device never connects to the internet while in the field or at the scene; location metadata does not place the device at the scene
- [ ] Disadvantage: Requires two devices and coordination; not viable for solo freelancers

---

**Select the transmission approach for your assignment**:
- [ ] Solo assignment: Approach 1 or Approach 2
- [ ] Team assignment: Approach 3
- [ ] Time constraints (photos needed immediately): Approach 3 with pre-positioned upload location

---

**Decision Point 1D: Legal Support Preparation**

Before going into the field, prepare for the possibility of arrest or detention.

- [ ] **Contact Information**: Create a physical card (not in your phone) with:
  - [ ] News organization's legal contact name and phone
  - [ ] Local media law attorney or RCFP (Reporters Committee for Freedom of the Press) emergency line: 1-844-RC-LEGAL
  - [ ] Your editor's name and phone
  - [ ] Your organization's bail/emergency fund contact if applicable

- [ ] **Legal Brief**: Your attorney has provided you with:
  - [ ] Your constitutional rights if stopped or arrested (right to remain silent, right to refuse device unlock, right to legal counsel)
  - [ ] Your journalist's privilege protections in your jurisdiction (state shield law protections if applicable; federal PRESS Act coverage if working for a large organization)
  - [ ] Instructions for device handling if seized (what to say, what not to say, how to notify your organization)

- [ ] **Device Unlock**: Before field assignment, decide your device unlock strategy
  - [ ] If using a dedicated device: Use a strong passphrase only you know (if your organization device is seized, you cannot be compelled to unlock it with a password; biometric unlock is weaker because you can be compelled to provide fingerprint/face)
  - [ ] If using a personal device in restricted mode (Option B): The device is locked to Camera app; they cannot access your personal data without exiting the restricted mode

- [ ] **Detention Response Protocol**: Prepare what you will say if questioned
  - [ ] "I am a journalist with [organization]. I am exercising my right to remain silent and I want to speak with my lawyer before answering any questions."
  - [ ] If asked for device password: "I cannot unlock this device without my attorney present."
  - [ ] If asked if you are recording: "I assert my constitutional rights under the First Amendment. My attorney will address your questions."

---

### En Route Phase (30 Minutes Before Arrival)

- [ ] **Verify your device settings**:
  - [ ] Reporting device has cellular disabled (airplane mode if using Option B personal phone in Guided Access)
  - [ ] Location services disabled
  - [ ] Camera app verified working
  - [ ] Battery charged to 100%
  - [ ] Backup battery or power bank available
  - [ ] Storage capacity verified (clear old files if needed)

- [ ] **Notify your editor**:
  - [ ] "En route to [location]. Using [device type]. Photos will be uploaded [transmission method] within [timeframe, e.g., 2 hours]."
  - [ ] Establish check-in protocol: when you will next contact the office (e.g., "I will text you from a borrowed phone when I leave the scene")

- [ ] **Final legal verification**:
  - [ ] Confirm legal contact phone number is visible (on your physical card or briefly reviewed)
  - [ ] Confirm you have memorized the emergency legal number (Reporters Committee: 1-844-RC-LEGAL)

---

### On-Scene Phase (During Coverage)

**Physical presence decisions** (see `phase-2-activist-organizing-security-playbook.md` Sections 4–5 for detailed countermeasures):

- [ ] **Position yourself clearly as press**: Vest or visible press credential to distinguish from protesters or participants
  - [ ] Clearview AI facial recognition will occur regardless of your credential
  - [ ] Physical credential distinguishes you from subjects in legal proceedings (you are a witness documenting, not a participant)

- [ ] **Limit device visibility**: Hold the camera in a way that does not invite confrontation
  - [ ] Large professional cameras are more obviously press; phones can be mistaken for participant documentation
  - [ ] Position yourself in areas less likely to be targets for police enforcement (behind police lines if possible; not in the path of advancing officers)

- [ ] **Photograph subjects, not faces (where possible)**:
  - [ ] In a protest, you want to document actions (someone being arrested, enforcement techniques, crowd response)
  - [ ] Full-face photographs of protesters are higher risk for Clearview AI matching
  - [ ] Photograph the scene, law enforcement actions, and interaction context rather than individual face-front portraits of participants
  - [ ] This is not a technical countermeasure (Clearview uses crowd photos); this is a legal and ethical one (photographers protect protest participants' identities where possible)

- [ ] **If approached by law enforcement**:
  - [ ] Assert your identity immediately: "I am a journalist with [organization]. My credentials are [on lanyard/in pocket]."
  - [ ] Comply with directions to move or clear an area (this is not a violation of press freedom; failure to comply creates arrest exposure unrelated to journalism)
  - [ ] If they demand access to your device or photos: "I will not surrender or unlock this device without a warrant or my attorney present. You can serve a legal process at my organization's legal contact: [phone number]."
  - [ ] If they attempt to physically take your device: "You are taking evidence of your own conduct. This will be preserved and provided to my attorney."
  - [ ] Do not resist physically; do not obstruct; comply with clear directives while asserting your legal position clearly

- [ ] **If detained or arrested**:
  - [ ] Immediately invoke your right to silence: "I am invoking my right to remain silent and I want to speak with my attorney."
  - [ ] Do not answer questions without attorney present
  - [ ] Provide your legal contact information and your organization (one of the three)
  - [ ] Your reporting device is evidence of your journalistic activity; it may be seized as potential evidence or as part of a device search

---

### Post-Scene Phase (After Leaving Location)

**Immediate actions (next 15–30 minutes after departing)**:

- [ ] **Power down the reporting device** if you will not be uploading immediately
  - [ ] If using Option A (dedicated device): power down after photos are taken
  - [ ] If using Option B (segmented personal phone): exit Guided Access mode and switch back to primary user only after you have left the scene location and moved to a different geographic area

- [ ] **Establish secure check-in with editor**:
  - [ ] If you can use a borrowed phone (colleague's phone, newsroom line from a public location): call or text your editor
  - [ ] Message: "I am safe. Exiting [location]. Photos in progress. Will upload within [time]."
  - [ ] Do NOT use your reporting device for communication

- [ ] **Upload photos** (using the transmission approach selected in 1C):
  - [ ] Move to a secure location (news organization office, trusted Wi-Fi location)
  - [ ] Power on the reporting device (if powered off)
  - [ ] Connect to trusted Wi-Fi (NOT public/open Wi-Fi)
  - [ ] Upload photos to the secure folder
  - [ ] Verify upload is complete
  - [ ] If removing EXIF data: do this BEFORE uploading
  - [ ] Power down the device

**Post-assignment actions (within 4 hours)**:

- [ ] **Verify photo integrity** with your editor:
  - [ ] Are all photos accounted for (number matches your count)
  - [ ] Are all photos readable and not corrupted
  - [ ] Do any photos need legal review before publication (e.g., photos containing identifiable faces of protesters for whom arrest risk is elevated)

- [ ] **Document the assignment for future reference**:
  - [ ] Date, location, and summary in your reporting log
  - [ ] Any incident of note (if stopped by police, if detained, if device demands, if technical issues)
  - [ ] Lessons learned for future similar assignments

- [ ] **Discuss with your editor whether you should be notified** if law enforcement inquires about the assignment or photos:
  - [ ] If a subpoena is served, your organization's legal team should notify you immediately
  - [ ] You may have grounds to quash the subpoena under journalist's privilege (state law) or federal First Amendment protection
  - [ ] Early notification is critical because you may have 10–14 days to respond before being compelled to provide the photos

---

## Scenario B: Protest Coverage During a Potential Law Enforcement Operation

**Threat context** (from `phase-2-journalist-security-playbook.md` Section 1):
- **NSA PRISM metadata**: If you contact a source about the protest, metadata shows the timing and frequency of communication (who you called, when, duration)
- **DHS administrative subpoenas**: If you have sources at the protest, DHS may issue a subpoena to you to identify sources
- **Flock Safety ALPR**: Your vehicle's license plate is recorded if you drive to/from the protest; if you park nearby, the plate is recorded multiple times
- **Grand jury subpoena for notes**: Federal prosecutors can subpoena your notebooks, recordings, and photos to identify sources or participants
- **State shield law gap**: Your state may have limited protections (some shield laws exclude source identity from protection; few protect unpublished photos)

**Scope**: You are covering a protest; law enforcement is present and may initiate enforcement action at any point (arrests, dispersal orders, chemical agents)

**Decision timeline**: Pre-event planning (1 week before), assignment briefing (1 day before), en route (2 hours before), on scene (during event), post-event (24 hours after)

---

### Pre-Event Phase (1 Week Before)

**Decision Point 2A: Assignment Risk Assessment**

Your editor assigns you to cover a protest. Your first decision is to assess the actual risk level.

**Information gathering**:
- [ ] What is the protest issue (political protest, labor action, ICE enforcement counter-protest, environmental action)?
- [ ] What is the history of law enforcement response to similar protests in your jurisdiction?
- [ ] Has the organizer made statements about expecting arrests or enforcement?
- [ ] Are specific organizers or speakers flagged as enforcement targets by prior legal action?
- [ ] What is the anticipated size (small community gathering, 100 people, 1,000+ people)?
- [ ] Is the location city/county/federal property (affects which law enforcement has jurisdiction)?
- [ ] Are there documented reports of surveillance or threats against this organizer or this protest specifically?

**Risk level determination**:

**Low Risk** (Community gathering, low enforcement likelihood):
- [ ] Lawful assembly with permit or historical precedent of lawful operation
- [ ] No prior enforcement action against this organizer or event
- [ ] No specific threat intelligence suggesting targeting
- [ ] Outdoor location with clear exits
- Example: City council meeting with a public comment period; scheduled march with police presence

**Medium Risk** (Potential enforcement action; participants at some risk):
- [ ] Demonstration without permit, but on public property; organized peaceful protest
- [ ] Prior enforcement history but current event appears lawful
- [ ] Some participants may be at ICE/CBP enforcement risk (immigration status vulnerable)
- [ ] Traffic control or device seizure risk is present but not imminent
- Example: Immigration advocacy rally; anti-ICE demonstration; labor action

**High Risk** (Likely enforcement action; journalists at direct risk):
- [ ] Demonstration explicitly opposing police or law enforcement (defund police, anti-CBP, anti-ICE protest)
- [ ] Location is sensitive (federal building, police precinct, immigration facility, border)
- [ ] Prior enforcement action against this organizer or similar events
- [ ] Police presence is heavy, checkpoints are established, or enforcement action has already begun
- [ ] Participants include vulnerable populations (undocumented immigrants, people with prior convictions)
- Example: Direct action against ICE enforcement; protest outside a federal detention facility

**Risk determination for this assignment**: 
- [ ] Low Risk → Proceed with standard coverage; standard device (Option B or C from Scenario A applies)
- [ ] Medium Risk → Increase precautions; consider dedicated reporting device; plan secure upload; brief on device seizure response
- [ ] High Risk → Full protocol engagement; dedicated device; team coordination; legal coordination; contingency for arrest

---

**Decision Point 2B: Source Identification Strategy**

As a reporter covering a protest, you will likely speak with protest participants. These conversations may be on the record or off the record.

**Key principle**: Distinguish between published reporting and source confidentiality.

- [ ] **On-the-record participants** (named sources, attributable statements):
  - [ ] These are the participants you intend to quote or identify in your story
  - [ ] Get their name, affiliation, and contact information (they volunteer it)
  - [ ] Record or take notes (standard journalism)
  - [ ] This information will be published; it is not protected by source confidentiality
  - [ ] They accept the risk of identification

- [ ] **Off-the-record or background sources** (anonymous, protected sources):
  - [ ] These are participants who provide information contingent on anonymity
  - [ ] Establish the off-the-record agreement clearly before the conversation: "What you tell me will not be attributed to you by name, and I will keep your identity confidential."
  - [ ] Note their description or identifier (person in red shirt, local organizer, police officer) instead of their name
  - [ ] Do NOT record their conversation (recording is a stronger form of identification)
  - [ ] Do NOT take their photo
  - [ ] If they are sources for sensitive information (ICE cooperation, police intelligence), your organization's legal team should pre-approve the confidentiality agreement

- [ ] **Crowd observations vs. source communications**:
  - [ ] Photographing the crowd is not the same as sourcing from individuals
  - [ ] You can photograph enforcement action, crowd responses, and police conduct without identifying individuals
  - [ ] Identifying a specific individual in your reporting creates a source relationship for that person — they become a witness to events you are documenting

---

**Decision Point 2C: Vehicle and Communications Plan**

If you are driving to the protest, your vehicle is a tracking point.

- [ ] **Vehicle considerations**:
  - [ ] Park your car outside the immediate protest zone (minimum 3 blocks away if possible)
  - [ ] Do NOT have your car's location visible on your phone's maps (disable location history in Google Maps, Apple Maps)
  - [ ] Walk to the protest from your car; this breaks the Flock Safety correlation between your plate and the scene (your plate is recorded at a distant location, not the protest)
  - [ ] Note the location where you parked (on your person, not in a device with location enabled) so you can retrieve your car later

- [ ] **Communications plan**:
  - [ ] Brief your editor on the following: (1) your expected arrival time, (2) your expected departure time, (3) check-in protocol (when will you call/text the office), (4) escalation procedure (what to do if you do not check in as expected)
  - [ ] Establish a code word or phrase if you need to signal emergency or detention (e.g., "The meeting is running late" as code for "law enforcement is present and may arrest me")
  - [ ] Do NOT use commercial text/call if you suspect surveillance; use a pre-established secure channel (Signal with your editor if your editor has Signal)

---

**Decision Point 2D: Legal Research and Shield Law Assessment**

Before the assignment, understand your legal protection in your jurisdiction.

- [ ] **Research your state's shield law**:
  - [ ] Does your state have a journalist's privilege statute?
  - [ ] What is the scope? (Does it protect your sources' identities? Does it protect unpublished materials? Photos? Notes?)
  - [ ] What are the limits? (Are there exceptions for crime or national security?)
  - [ ] Is your news organization large enough or established enough to be protected? (Some shield laws are narrower for freelancers or non-traditional media)

- [ ] **Research federal protections**:
  - [ ] If a federal subpoena is served (FBI, federal prosecutors), your state shield law does NOT apply
  - [ ] First Amendment protection for source confidentiality is limited but present (see `phase-2-journalist-security-playbook.md` Section 3.1 for detail)
  - [ ] The PRESS Act (S.2074) would provide federal shield law protection, but as of June 2026 it has not been enacted

- [ ] **Establish your organization's legal support**:
  - [ ] Your organization's attorney should brief you on what to do if subpoenaed
  - [ ] Your organization should have a policy on source confidentiality (do you have a duty to protect all sources, or are there exceptions?)
  - [ ] Understand your organization's data retention policy (how long do you keep notes, recordings, unused photos?)

---

### Assignment Briefing Phase (1 Day Before)

**Decision Point 2E: Risk Mitigation Briefing**

Your editor and your organization's legal team brief you before the assignment.

**Briefing checklist**:

- [ ] **Device and data plan** (based on risk level):
  - [ ] Medium/High Risk: Use a dedicated reporting device (Option A, Scenario A)
  - [ ] Low/Medium Risk: Segmented personal device (Option B) is acceptable
  - [ ] All risk levels: Do NOT carry multiple personal phones (carries phones are evidence of coordination); carry one reporting device only

- [ ] **Source confidentiality agreement**:
  - [ ] Any off-the-record sources are protected
  - [ ] You will not identify off-the-record sources by name or identifying characteristic in your notes
  - [ ] Your notes distinguishing on-the-record vs. off-the-record sources are critical (a subpoena may compel your notes; clear labeling shows which sources agreed to be identified and which did not)

- [ ] **Arrest and detention response**:
  - [ ] What to say if stopped or arrested
  - [ ] How to identify yourself and invoke your rights
  - [ ] What happens to your device if seized (your organization's legal team will attempt to retrieve it; you should not resist)
  - [ ] What happens next (your organization will provide bail/legal support)

- [ ] **Post-event obligations**:
  - [ ] How long will you retain raw footage/notes (your organization may have a policy)
  - [ ] What is your obligation to preserve evidence if law enforcement requests it (your organization's counsel will advise)
  - [ ] How will your organization respond to a subpoena for your reporting materials?

---

### En Route Phase (2 Hours Before)

- [ ] **Device preparation** (same as Scenario A Phase 2):
  - [ ] Reporting device has cellular disabled / location disabled
  - [ ] Camera app functional, storage cleared, battery full
  - [ ] Legal contact information on a physical card in your pocket

- [ ] **Notation system setup**:
  - [ ] If using a notebook (physical, not digital):
    - [ ] Use shorthand or initials for source identifiers (don't write full names)
    - [ ] Mark clearly: "OFF THE RECORD" or "OTR" for any source who requested anonymity
    - [ ] Mark "FOR PUBLICATION" or "ATTRIBUTED" for sources who agreed to be on the record
  - [ ] If using a digital device for notes:
    - [ ] Use the same notation system
    - [ ] Understand that if the device is seized, all notes are discoverable (including off-the-record notations if a court compels disclosure of your reporting methodology)

- [ ] **Check-in with your editor**:
  - [ ] Confirm: "I am departing for [location]. Expected arrival [time]. Check-in protocol: [method and time]."

---

### On-Scene Phase (During Event)

**Decision Point 2F: Real-Time Adaptation to Escalation**

If the event escalates (police presence increases, arrests begin, enforcement action is imminent), adjust your behavior in real time.

**Low escalation** (police observing; no enforcement action):
- [ ] Continue normal coverage
- [ ] Maintain position as press (credential visible)
- [ ] Position yourself away from potential escalation points (don't stand directly in front of police lines if a confrontation is likely)

**Medium escalation** (police are present and addressing violations; some arrests or dispersals underway):
- [ ] Move to the perimeter; maintain clear sight lines to the action
- [ ] Stop approaching individual participants; use zoom lens or long lens if photographing
- [ ] Avoid wearing the same clothing as participants (distinguish yourself as press)
- [ ] Keep your device in hand and visible (less likely to be mistaken for a participant's device)
- [ ] If a police officer addresses you, immediately assert: "I am a journalist with [organization]. These are photos/notes for [publication]. Do you have a legal process?"

**High escalation** (police are making arrests, using crowd control measures, moving toward dispersal):
- [ ] Document the police action from the safest available position
- [ ] Do NOT run from police; do NOT try to "escape" — this invites pursuit and arrest
- [ ] Move deliberately toward an exit route (do not block yourself in a dead end)
- [ ] If police move toward you, move away deliberately but not in a panicked manner
- [ ] Continue documenting until you are in a position of safety
- [ ] When reaching safety (clear exit area), check in with your editor immediately (using a borrowed phone if necessary): "I am safe. Police action ongoing. Photos secure. I am leaving the area."

**If arrested**:
- [ ] Immediately assert your rights: "I am a journalist. I have a right to remain silent and I want an attorney. You can reach my organization at [legal contact]."
- [ ] Do NOT attempt to explain your reporting or your presence
- [ ] Your organization's legal team will respond and attempt to secure your release
- [ ] Your device will likely be seized as evidence; your organization will attempt to retrieve it through legal process

---

**After law enforcement action is complete**:

- [ ] **Security review**: Before leaving the area, assess whether you are being followed or under surveillance
  - [ ] Take a non-direct route to your vehicle (do not walk the direct path you took arriving; take a different street)
  - [ ] Note whether the same individuals or vehicles are present in both locations
  - [ ] If you believe you are being followed, do NOT go directly to your car; go to a public location (coffee shop, store) and wait, or contact police non-emergency to report surveillance

- [ ] **Upload photos immediately** (if not already uploaded):
  - [ ] Move to a secure location (office or trusted Wi-Fi)
  - [ ] Follow the transmission approach from Scenario A (Approach 1 or 2)
  - [ ] Verify upload is complete before logging off the device

- [ ] **Check in with your editor**:
  - [ ] Confirm: "Assignment complete. Safe. Photos uploaded. Heading back to office."

---

### Post-Event Phase (Next 24 Hours)

**Decision Point 2G: Source Protection and Note Organization**

After the event, organize your notes and identify your sources clearly.

- [ ] **Create a source index**:
  - [ ] List each on-the-record source by name and attribution
  - [ ] List each off-the-record source by identifier (Person A, Organizer B, etc.)
  - [ ] Maintain a separate key that connects identifiers to real names (stored separately, encrypted, in attorney or editor custody if needed)
  - [ ] This separation is your defense against a subpoena: you can release the story (with OTR sources identified only as "local organizer") without compromising your source's identity

- [ ] **Review photos for inadvertent source identification**:
  - [ ] Any photos containing the faces of off-the-record sources should be deleted or marked "DO NOT PUBLISH"
  - [ ] If you photographed a police officer or official at the event, that is fair game for publication (they are in a public role)
  - [ ] If you photographed an off-the-record source whose face appears in a crowd photo, consider whether that photo can be published without identifying them (crop, blur, or do not use)

- [ ] **Prepare for subpoena response**:
  - [ ] Your organization's counsel will advise on retention policy
  - [ ] Typically: save the published story, delete or mark for deletion raw footage and notes that were not published (news organizations destroy raw materials after a period)
  - [ ] If you received a subpoena during the event (rare but possible), flag this to your legal team immediately

---

## Integration with Core Playbooks

These scenarios integrate with the following sections of `phase-2-journalist-security-playbook.md`:

- **Section 1.2** (FISA 702): If contacting foreign sources about the protest, review metadata protection in the main playbook
- **Section 1.3** (CBP Border Search): If you are a photojournalist covering border enforcement or immigration, extend these scenarios with CBP-specific procedures
- **Section 1.4** (Clearview AI): The "photograph the action, not individuals' faces" principle in Scenario A directly countermeasures Clearview AI
- **Section 2** (Role-based threats): Scenario A covers photojournalists; Scenario B covers assignment reporters
- **Section 3** (Legal framework): Both scenarios assume your organization has counsel and a shield law policy
- **Section 4** (SecureDrop): If a source contacts you via SecureDrop about a protest you are covering, review source communication protocols in the main playbook
- **Checklists A–C**: Use these checklists for each assignment

---

## Tools and Resources

### Device Setup
- **GrapheneOS**: grapheneos.org (dedicated Android device)
- **VeraCrypt**: veracrypt.fr (encrypted cloud storage for photos before transmission)
- **ExifTool**: exiftool.org (remove EXIF data from photos)

### Communications
- **Signal**: signal.org (secure check-in with editor; verify safety numbers in person)
- **Tor Browser**: torproject.org (if researching protest organizers securely)

### Legal Resources
- **Reporters Committee for Freedom of the Press**: rcfp.org, 1-844-RC-LEGAL (emergency legal line)
- **State Shield Laws**: Contact your state's press association for shield law details
- **ACLU Journalists' Rights**: aclu.org/issues/freedom-press (legal guide by state)
- **Freedom of the Press Foundation**: freedom.press (journalist security resources)

### Photographer-Specific
- **National Press Photographers Association**: nppa.org (legal advocacy for photojournalists)
- **Getty Images Photographer Rights**: getty.edu/rights (resources on photographer IP and rights in field situations)

---

## Summary: Five Principles for Field Reporting

1. **Pre-assignment legal briefing is non-negotiable** — your organization's counsel must brief you on shield law scope and your rights before high-risk assignments

2. **Device segmentation is your strongest defense against data seizure** — a dedicated reporting device with no personal data is better than any legal argument after the fact

3. **Upload immediately after leaving the scene** — the longer photos are on your personal device, the longer they are exposed to seizure and subpoena

4. **Source confidentiality is documented in real time** — mark off-the-record sources clearly in your notes; this marking is your evidence of agreement if a subpoena arrives

5. **Metadata removal is a technical baseline** — EXIF data is automatically extracted and used; remove it from photos before they are uploaded to any platform

---

**Version**: 1.0  
**Created**: June 22, 2026  
**Author**: Cybersecurity-Hardening Project  
**Next Review**: September 22, 2026 (quarterly)

---

**Cross-references**: 
- `phase-2-journalist-security-playbook.md` (full threat model)
- `phase-2-activist-organizing-security-playbook.md` (physical countermeasures for crowd environments)
- `opsec-playbook.md` (device hardening)
- `rights-assertion-legal-playbook.md` (First Amendment protections)

**Integration note**: These scenarios are designed to be printed and given to field reporters as standalone guidance. The checklist sections can be excerpted into field reporter briefing templates.
