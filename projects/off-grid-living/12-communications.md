---
title: "Domain 12: Communications"
project: off-grid-living
status: complete
created: 2026-04-13
cross-refs: [06-energy-power, 08-medical-health, 11-shelter-construction, 13-community-organization, 15-disaster-scenarios]
---

# Domain 12: Communications

> Information is a survival resource. Without it, you cannot know whether a
> storm is approaching, whether a neighbor needs help, whether a regional
> emergency has been declared, or whether your family in another state is
> alive after a catastrophic event. The grid-connected world takes for granted
> a constant stream of information from cell towers, internet, and broadcast
> stations. When those fail — and they will, at the worst possible times —
> the person with a working radio and the skills to use it has an enormous
> advantage over everyone else.
>
> This chapter covers the full communications stack for off-grid life: from
> the $30 handheld walkie-talkie to a $600/year satellite subscription, from
> analog Morse code to digital mesh networking over amateur radio. The goal
> is a layered, redundant system that continues to function when the cell
> network is down, when the internet is out, and even when a nuclear EMP has
> fried everything without Faraday cage protection.
>
> **The central principle**: No single communications technology is reliable
> enough to stake your life on. Build layers. Test them regularly. Train on
> them before you need them.

---

## Quick-Reference Decision Matrix

| Your situation | Minimum kit | Step-up kit | Full kit |
|---|---|---|---|
| Solo homestead, limited budget | NOAA weather radio + FRS/MURS handheld | Add GMRS license + mobile radio | Add Technician ham license + VHF/UHF transceiver |
| Family homestead, $500 budget | GMRS family radios + NOAA | Add SW receiver + Garmin inReach | Add ham Technician + HF radio |
| Remote retreat, grid-down focus | Ham General + HF transceiver + GMRS | Add Garmin inReach + SW receiver | Add Starlink + Iridium backup |
| Community hub (5+ households) | Ham General + HF + GMRS repeater | Add digital modes (JS8Call, Winlink) | Add AREDN mesh + Starlink |
| Mobile / nomadic | GMRS handheld + Garmin inReach | Add ham Technician + VHF mobile | Add Iridium satellite phone |
| CBRN/nuclear concern | EMP-hardened Faraday kit + tube SW radio | Add battery HF transceiver in cage | Full stack, all gear doubled in Faraday storage |

---

## 12.1 Why Communications Matter Off-Grid

### 12.1.1 Information as Survival Resource

Most homesteaders think of communications as a convenience. It is not. It is
a critical system with the same priority as water and shelter in emergencies.

The information you need to survive falls into these categories:

**Immediate threat warning**
- Severe weather: tornado warning, flash flood, blizzard — a NOAA weather
  alert received 20 minutes before a tornado can save your life. Received
  after the funnel is visible, it cannot.
- Wildfire approach: wind direction changes, evacuation orders, road closures.
- Civil unrest: knowing whether a protest has turned violent, whether roads
  are blocked, whether law enforcement is overwhelmed.

**Operational intelligence**
- Is the road passable? Is the fuel station open? Did the supply chain for
  propane fail this week?
- What is the regional weather forecast for the next two weeks? Relevant to
  harvest timing, travel decisions, and energy budgeting.
- What happened to a neighbor who was expected two days ago and hasn't arrived?

**Coordination and mutual aid**
- Scheduling work parties, equipment sharing, medical assistance.
- Alerting your community network when you need help.
- Coordinating barter and trade — knowing who has surplus corn, who needs
  eggs, who can weld.

**Grid-down situational awareness**
- During extended grid failure, no internet and no cell service means
  most of the population is information-blind. Ham radio nets, shortwave
  broadcast, and satellite services continue to function. The person
  monitoring these has a decisive advantage.

### 12.1.2 The Failure Modes of Normal Communications

Understanding why normal communications fail helps you plan your redundancy.

**Cell network failures:**
- Cell towers run on backup generators. Most have 4–8 hours of battery;
  generator fuel must be delivered. In a regional emergency, towers fail
  within 24–72 hours if grid power is not restored.
- Cell networks are also capacity-limited: during a declared emergency,
  the network may be overwhelmed by call volume and become unusable even
  when technically operational.
- Geographic coverage: large portions of rural America have no cell service
  at all in normal times.

**Internet failures:**
- Internet infrastructure depends on grid power at multiple points: your
  router, the ISP's local node, the upstream backbone. Any of these failing
  breaks the chain.
- Satellite internet (Starlink) is more resilient but still requires your
  local power and the Starlink ground station network to function.

**Broadcast radio (AM/FM):**
- FM: line-of-sight propagation; local stations go off air if grid fails
  and they lack generator backup. Station survival varies enormously.
- AM: ground wave reaches 50–200 miles; sky wave at night can reach
  1,000+ miles. More resilient than FM for regional information.
- NOAA Weather Radio: dedicated government network with backup power;
  often among the last broadcast services to fail.

**The gap**: When cell, internet, and local broadcast all fail — a scenario
that happens in major hurricanes, ice storms, and would certainly happen in
any large-scale CBRN event — only amateur radio, shortwave, and satellite
devices continue to function for most people.

### 12.1.3 OPSEC Considerations

Not everything about communications is about reaching out. Sometimes it is
about not being heard.

**Radio transmissions are one-way secrets**: When you transmit, anyone with
the right receiver and frequency can hear you. This has implications:

- Do not broadcast your food stocks, fuel quantity, or security weaknesses
  over any unencrypted radio channel.
- FRS, GMRS, and most ham transmissions are legally prohibited from using
  encryption. Treat all transmissions as public.
- Develop code words or coded check-in signals for sensitive information.
  "The harvest is good" meaning "we are not under duress" is legal; it is
  not encryption, it is just an agreed convention.
- Direction-finding (DF) equipment can locate transmitters. In a hostile
  scenario, regular transmissions from a fixed location reveal your location
  to anyone with a directional antenna. Minimize transmission time; vary
  location if practical.
- RECEIVE-only equipment (SW receiver, scanner) reveals nothing about you
  while providing intelligence. Build your listening capability first.

**Digital trail discipline:**
- Starlink generates traffic that could theoretically be associated with
  your account location.
- Winlink (radio email) is logged and traceable in ways that voice radio
  is not.
- In genuine civil unrest or authoritarian scenarios, consider which
  communications technologies leave records and which do not.

---

## 12.2 Radio Fundamentals

Understanding the physics of radio propagation lets you choose the right
tool for the right job. You do not need a deep technical education, but
you do need the core concepts.

### 12.2.1 The Electromagnetic Spectrum and Relevant Bands

Radio waves are electromagnetic radiation. The key variable is frequency,
measured in hertz (Hz). Higher frequency = shorter wavelength = different
propagation behavior.

```
Frequency Range    Band Name    Wavelength    Off-Grid Relevance
-----------------  -----------  ------------  ------------------------------------------
3 kHz – 300 kHz    LF/VLF       1000–100 km   Time signals (WWVB), submarine comms
300 kHz – 3 MHz    MF           1000–100 m    AM broadcast; 630m/160m amateur bands
3 MHz – 30 MHz     HF           100–10 m      Ham radio long-range; shortwave broadcast
30 MHz – 300 MHz   VHF          10–1 m        Ham 6m/2m; GMRS/FRS/MURS; FM broadcast
300 MHz – 3 GHz    UHF          1–0.1 m       Ham 70cm/33cm; GMRS; GPS; cell phones
3 GHz – 30 GHz     SHF          100–10 mm     Satellite (Starlink Ku-band); Wi-Fi
```

### 12.2.2 HF Propagation (3–30 MHz)

HF is the band that makes worldwide communication possible without
satellites or infrastructure. The key mechanism is ionospheric reflection.

**How it works**: The ionosphere — a layer of charged particles at
50–1,000 km altitude — reflects HF radio waves back to earth. The signal
travels from your antenna upward, reflects off the ionosphere, and comes
down hundreds or thousands of miles away. Then it may reflect off the
earth and back up again ("hops"), extending range further.

**Skip zone**: There is a region between your local groundwave coverage
(typically 0–50 miles) and where the first ionospheric reflection lands
(typically 100–500+ miles). In this "skip zone" you cannot be heard.
This is why HF radio requires knowing your distances.

**Propagation varies with:**
- **Solar activity**: Sunspot cycle (~11 years) drives ionospheric density.
  Solar maximum (next peak ~2025–2026) enables higher-frequency HF bands
  (15–10 MHz) for global communication. Solar minimum degrades these bands.
- **Time of day**: Ionosphere thickens at night, enabling lower-frequency
  bands (40m, 80m) to travel farther. Daytime favors higher bands (20m, 15m, 10m).
- **Season**: Summer propagation differs from winter; equinoctial openings
  (March, September) are often excellent for DX (long-distance) contacts.

**Practical band guide for off-grid HF:**

| Band | Frequency | Wavelength | Best for | Notes |
|---|---|---|---|---|
| 80m | 3.5–4.0 MHz | 80m | Regional (0–500 mi) at night | Best for statewide emergency nets; noisy daytime |
| 60m | 5.330–5.405 MHz | 60m | Regional; interoperability | Limited channels; shared with federal agencies |
| 40m | 7.0–7.3 MHz | 40m | Regional to DX (day), long-range (night) | Workhorse emergency band; always reliable |
| 20m | 14.0–14.35 MHz | 20m | Worldwide daytime; 1,000+ miles | Primary DX band; best during solar max |
| 17m | 18.068–18.168 MHz | 17m | Worldwide, less crowded | Good when 20m is busy |
| 15m | 21.0–21.45 MHz | 15m | Worldwide during solar max | Closes at night; excellent when open |
| 10m | 28.0–29.7 MHz | 10m | Very long range when open | Inconsistent; spectacular during solar max |

### 12.2.3 VHF/UHF Propagation (30 MHz – 3 GHz)

VHF and UHF do not reflect off the ionosphere under normal conditions.
They travel in straight lines (line of sight). This fundamentally changes
how they are used.

**Line-of-sight range formula:**
```
Range (miles) = 1.415 × (√antenna height in feet)
```
Examples:
- Antenna at 6 ft (handheld): 1.415 × √6 = 3.5 miles to similar antenna
- Antenna at 25 ft (rooftop): 1.415 × √25 = 7 miles
- Antenna at 100 ft (tower): 1.415 × √100 = 14 miles
- Both antennas elevated: add the two ranges

For a handheld talking to a hilltop repeater at 1,000 ft elevation:
- Your contribution: 3.5 miles + repeater contribution: 1.415 × √1000 = 45 miles
- Total range: ~48 miles

**VHF tropospheric ducting**: Under certain atmospheric conditions
(temperature inversions), VHF signals can travel hundreds of miles.
Unpredictable but useful for regional intelligence gathering.

**UHF behavior**: Similar to VHF but attenuates more through foliage
and buildings. 70cm (UHF) is slightly shorter range than 2m (VHF)
in typical terrain, but suffers less multipath interference.

### 12.2.4 Antenna Fundamentals

The antenna is the most important component of any radio system. A good
antenna with a mediocre radio will outperform a mediocre antenna with an
expensive radio.

**Key concepts:**

**Gain (dBd or dBi)**: Gain is not amplification — it is directional
focusing of the transmitted power. A dipole has 0 dBd (reference) gain.
A directional Yagi might have 6–14 dBd. Every 3 dB doubles the effective
radiated power (ERP) in the favored direction — but reduces it elsewhere.

**dBd vs. dBi**: dBi (referenced to isotropic) = dBd + 2.15 dB. Manufacturers
prefer dBi because the number looks larger. When comparing, normalize to dBd.

**Feedline loss**: Coaxial cable attenuates the signal between the radio
and antenna. Loss increases with frequency and cable length.

```
Cable type     Loss at 100 MHz     Loss at 450 MHz    Loss at 14 MHz
-------------  ------------------  -----------------  ---------------
RG-58/U        6 dB per 100 ft     13 dB per 100 ft   1.8 dB per 100 ft
RG-8X          3.5 dB per 100 ft   7 dB per 100 ft    1.1 dB per 100 ft
RG-213         3 dB per 100 ft     6 dB per 100 ft    0.9 dB per 100 ft
LMR-400        1.5 dB per 100 ft   3 dB per 100 ft    0.5 dB per 100 ft
LMR-600        1.0 dB per 100 ft   2 dB per 100 ft    0.3 dB per 100 ft
```

Use LMR-400 for VHF/UHF runs over 30 feet. RG-213 is acceptable for HF.
Never use RG-58 for anything permanent — the loss is too high.

**Half-wave dipole length formula:**
```
Length (feet) = 468 / frequency (MHz)
```
Examples:
- 40m dipole (7.2 MHz): 468 / 7.2 = 65 feet total (32.5 ft each leg)
- 20m dipole (14.1 MHz): 468 / 14.1 = 33.2 feet total (16.6 ft each leg)
- 2m dipole (146 MHz): 468 / 146 = 3.2 feet total (19 inches each leg)
- 70cm (446 MHz): 468 / 446 = 1.05 feet total (6.3 inches each leg)

**Quarter-wave vertical (for verticals and ground-plane antennas):**
```
Length (feet) = 234 / frequency (MHz)
```

**SWR (Standing Wave Ratio)**: Measures impedance mismatch between feedline
and antenna. SWR 1:1 is perfect; SWR below 2:1 is acceptable; above 3:1
causes excessive reflected power and can damage radios. Tune with an antenna
analyzer or SWR meter, not by guesswork.

---

## 12.3 Ham Radio (Amateur Radio)

Amateur radio is the backbone of off-grid communications. No other system
offers the same combination of range, reliability, independence from
infrastructure, and operator control.

### 12.3.1 License Tiers

The FCC issues three amateur radio license classes in the United States.

**Technician Class**
- Exam: 35 multiple-choice questions from public question pool
- Study time: 10–20 hours
- Exam cost: $15 (through ARRL or W5YI VE groups); some clubs offer free exams
- What it unlocks:
  - Full privileges on all VHF and UHF amateur bands (above 50 MHz)
  - Limited HF privileges: 10m phone above 28.3 MHz, 15m/40m/80m CW only
  - All digital modes on authorized frequencies
- Practical capability: local/regional comms via VHF/UHF handhelds and
  mobiles, repeater access, APRS tracking, digital modes on 2m/70cm
- License valid: 10 years, free renewal

**General Class**
- Exam: Additional 35 questions (taken same day as Technician if desired)
- Study time: 1–2 additional weeks
- What it unlocks: Most HF bands — 40m, 20m, 17m, 15m, 12m, 10m phone,
  plus limited segments of 80m and 160m
- Practical capability: Worldwide communication, emergency HF nets,
  Winlink, JS8Call long-range, international information gathering
- This is the target license for serious off-grid preparedness

**Amateur Extra Class**
- Exam: 50 additional questions; advanced technical topics
- Study time: Several weeks of serious study
- What it unlocks: All remaining HF privileges, including the lower (less
  crowded) phone subbands; international reciprocal operating
- For most off-grid purposes, General is sufficient

**License resources:**
- HamStudy.org — free, adaptive flashcard system; tracks your progress
- ARRL Ham Radio License Manual ($30) — comprehensive study guide
- HamExam.org — free practice exams
- YouTube: Ham Radio Crash Course channel — excellent free video curriculum
- ARRL exam locator: arrl.org/find-an-amateur-radio-license-exam-session

### 12.3.2 HF Transceivers for Long-Range Communication

HF radios are the tool for communication beyond your immediate area —
statewide, nationwide, and worldwide depending on band and conditions.

**Key specifications to understand:**
- **Output power**: 100W is standard; many rigs go to 200W with linear amplifier.
  More power helps but antenna and location matter more.
- **Receiver sensitivity**: Measured in dBm MDS (minimum discernible signal).
  Better receivers hear weak signals. Matters most for DX.
- **Modes**: SSB (phone), CW (Morse), AM, FM, and digital (RTTY, FT8, etc.)
- **Band coverage**: Most modern radios cover 160m–10m; some include 6m

| Radio | Type | Power | Bands | Modes | Price (2025-26) | Notes |
|---|---|---|---|---|---|---|
| Icom IC-7300 | HF desktop | 100W | 160m–10m + 6m | SSB/CW/AM/FM/digital | $950–$1,050 | Best receiver in class; built-in SDR; top recommendation |
| Yaesu FT-991A | HF/VHF/UHF desktop | 100W HF; 50W VHF | 160m–70cm | SSB/CW/AM/FM/C4FM digital | $1,100–$1,200 | All-band all-mode; good for consolidation |
| Yaesu FT-DX10 | HF desktop | 100W | 160m–6m | SSB/CW/AM/FM/digital | $1,400–$1,600 | Superior receiver; for serious HF operators |
| Xiegu G90 | HF portable | 20W | 160m–10m | SSB/CW/AM/digital | $380–$420 | Budget HF; built-in auto-tuner; excellent for the price |
| Xiegu X6100 | HF portable/QRP | 10W | 160m–6m | SSB/CW/AM/FM/digital | $550–$600 | Battery-integrated portable; excellent field radio |
| Icom IC-705 | HF/VHF/UHF portable | 10W | 160m–70cm | All modes + D-STAR | $1,200–$1,350 | Premium portable; D-STAR digital; internal battery |
| Yaesu FT-891 | HF mobile | 100W | 160m–10m | SSB/CW/AM/FM | $500–$560 | Compact 100W HF; good vehicle/off-grid install |
| Kenwood TS-590SG | HF desktop | 100W | 160m–6m | SSB/CW/AM/FM/FSK | $1,100–$1,200 | Strong receiver; popular with contesters |

**Recommendation by scenario:**
- Primary homestead HF station: **Icom IC-7300** — best value in the $1,000
  range; unmatched receiver for price; excellent digital mode support
- Budget HF: **Xiegu G90** — 20W limits long-range performance but adequate
  for regional comms on 40m; built-in auto-tuner saves external expense
- Portable/mobile: **Yaesu FT-891** at 100W or **Xiegu X6100** at 10W with
  battery; depends whether you need portability or power
- All-in-one for Technician to General path: **Yaesu FT-991A** covers
  everything from 160m to 70cm in one radio

### 12.3.3 VHF/UHF Handhelds

Handhelds ("HTs") are the first radio most people buy and the one they use
most daily. For local communications, farm-to-farm coordination, and
repeater access, an HT is indispensable.

| Radio | Bands | Power | Battery | Price (2025-26) | Notes |
|---|---|---|---|---|---|
| Baofeng UV-5R | 2m/70cm | 5W | 7.4V Li-ion | $25–$35 | Extremely cheap; acceptable for learning; known receiver overload issues |
| Baofeng BF-F8HP | 2m/70cm | 8W | 7.4V Li-ion | $45–$55 | Higher power UV-5R variant; same receiver issues |
| Yaesu FT-60R | 2m/70cm | 5W | 7.4V Ni-MH | $130–$150 | Military-grade durability; excellent receiver; top recommendation |
| Yaesu VX-6R | 2m/70cm/6m | 5W | 7.4V Li-ion | $200–$230 | Waterproof (JIS7); 3-band; extremely durable |
| Kenwood TH-D74A | 2m/70cm/6m | 5W | 7.4V Li-ion | $500–$550 | APRS built-in; D-STAR; best-in-class receiver; for serious use |
| AnyTone AT-D878UV | 2m/70cm | 7W | 7.4V Li-ion | $120–$140 | DMR digital + analog; dual-band; good value for digital ops |
| Wouxun KG-UV9D | 2m/70cm + more | 5W | 7.4V Li-ion | $70–$90 | Multi-band; better receiver than Baofeng |

**The Baofeng question**: Baofeng radios work and cost very little.
They are appropriate for learning, as a second radio, or as a disposable
spare in a Faraday cage. Their receiver selectivity is poor — in areas
with strong nearby signals, they can be desensitized. For daily use as
your primary HT, the Yaesu FT-60R is the recommendation: it costs four
times as much and is worth every dollar.

**Legality note**: Baofeng radios in the US are legal to transmit on
licensed amateur frequencies with a valid amateur license. They are NOT
legal to transmit on GMRS/FRS frequencies despite what the packaging
implies, because they do not have FCC Part 95 type acceptance for those
services.

### 12.3.4 VHF/UHF Mobile Radios

Mobile (vehicle or base-station-mounted) radios provide more power and
better receive performance than handhelds.

| Radio | Bands | Power | Price (2025-26) | Notes |
|---|---|---|---|---|
| Yaesu FT-7900R | 2m/70cm | 50W/45W | $180–$210 | Dual-band; simple; reliable; popular |
| Yaesu FT-8900R | 10m/6m/2m/70cm | 50W | $320–$360 | Quad-band; 10m useful for Technicians |
| Kenwood TM-V71A | 2m/70cm | 50W | $280–$320 | Dual-band; APRS capable; excellent receiver |
| Icom IC-2730A | 2m/70cm | 50W | $230–$260 | Dual-band; head separation; easy install |
| Kenwood TM-D710G | 2m/70cm | 50W | $450–$500 | APRS built-in; TNC built-in; D-STAR capable |

### 12.3.5 Power Requirements

Understanding power consumption is essential for solar/battery sizing.

```
Radio / Mode              Current @ 13.8V    Watts    Notes
-----------------------   ---------------    ------   ---------------------------
IC-7300 receive           ~1.0–1.5A          14–21W   Backlight, DSP active
IC-7300 transmit (100W)   ~20A               276W     100W RF output
IC-7300 transmit (50W)    ~13A               179W     
IC-7300 transmit (25W)    ~9A                124W     Good balance power/battery
Yaesu FT-991A receive     ~1.5A              21W      
Yaesu FT-991A TX (100W)   ~22A               304W     
Xiegu G90 receive         ~0.7A              10W      Efficient portable radio
Xiegu G90 TX (20W)        ~5.5A              76W      
Yaesu FT-60R HT receive   ~0.14A             1.0W     
Yaesu FT-60R TX (5W)      ~0.9A              6.7W     
VHF mobile 50W TX         ~12A               166W     Receive ~0.9A
VHF mobile 25W TX         ~7A                97W      
```

**Duty cycle matters**: In normal voice operation, you transmit 20–30%
of the time and receive 70–80%. An HF station operating for 2 hours in
a net transmits perhaps 20–25 minutes. Power budget accordingly.

**Realistic daily power budget (HF station, moderate use):**
- Receive 4 hours: 1.5A × 4h = 6 Ah
- Transmit 30 min at 50W: 13A × 0.5h = 6.5 Ah
- Total: ~13 Ah per day active operation

A 100Ah LiFePO4 battery provides 7+ days without recharging at this rate.

### 12.3.6 Digital Modes

Digital modes transform HF radio from voice-only to a capable data link.
For off-grid preparedness, three modes stand out.

**FT8 (Weak Signal / Contact-Making)**
- Developed by Joe Taylor (K1JT) and Steve Franke (K9AN)
- Encodes call sign, locator, and signal report into 13-second transmissions
- Can decode signals 20 dB below the noise floor — extraordinary weak-signal
  performance; contacts possible when voice would fail completely
- Limitation: FT8 is a contact mode, not a message mode. Conversations are
  not possible beyond signal reports. Valuable for propagation assessment
  and proving your station works.
- Software: WSJT-X (free, Windows/Mac/Linux)
- Audio interface: connect radio to computer via USB audio (IC-7300 has
  built-in USB audio; older rigs need a Signalink USB or similar, $120)

**JS8Call (Grid-Down Messaging)**
- Derived from FT8 by Jordan Sherer (KN4CRD)
- Allows free-text messaging, store-and-forward relay, and mesh-like
  operation — a message can hop through multiple stations to reach
  a destination even if you can't hear it directly
- Heartbeat mode allows stations to announce their presence automatically
- Groups allow broadcast messages to multiple recipients
- This is the critical grid-down messaging technology for ham operators:
  email-style comms without infrastructure over HF
- Software: JS8Call (free, js8call.com)
- Typical operation: 40m (7.078 MHz) or 20m (14.078 MHz) during day

**Winlink (Radio Email)**
- A global radio email network maintained by volunteers
- Send and receive internet email via HF or VHF radio — no internet connection
  needed at your end; Winlink gateway stations bridge to the internet
- Supports attachments (forms, images up to a few KB), ICS-213 forms
- Used by FEMA, Red Cross, and emergency management for exactly this purpose
- Can operate Vara HF (fast, requires audio interface), Vara FM (VHF),
  or Packet (VHF/UHF TNC)
- Software: Winlink Express (free, winlink.org)
- During full grid-down: Winlink Peer-to-Peer (P2P) mode works without
  any internet gateway — direct station-to-station HF email
- Setup requires: radio + audio interface + Winlink Express + sound card
  modem (VARA is software-based and free; best performance with licensed
  VARA HF modem, ~$69 one-time)

### 12.3.7 Mesh Networking

For community-scale local communications, mesh networks allow data
exchange without infrastructure.

**Meshtastic (LoRa-based, license-free)**
- Uses inexpensive LoRa (Long Range) radio modules operating in the
  915 MHz ISM band (no license required in the US)
- Devices: LILYGO T-Beam (~$35–$45), RAK WisBlock (~$40–$60),
  Heltec V3 (~$25–$35)
- Range: 1–5 miles typical; 10+ miles line-of-sight with elevated node
- Network: devices form a self-healing mesh — a message hops through
  intermediate nodes to reach its destination
- Capability: text messaging, GPS position sharing, telemetry
- Power: very low; T-Beam with 18650 battery runs 2–3 days on transmit,
  weeks in receive-only
- App: Meshtastic app (iOS/Android, free)
- Limitations: low bandwidth (text only, no voice); 915 MHz has limited
  foliage penetration
- Best use: community position tracking, text messaging between homesteads
  within 5–10 miles, silent comms

**AREDN (Amateur Radio Emergency Data Network)**
- Operates on licensed amateur frequencies (900 MHz, 2.4 GHz, 3.4 GHz, 5.8 GHz)
- Uses modified commercial Wi-Fi hardware (Ubiquiti, MikroTik, others)
  flashed with AREDN firmware
- Hardware cost: $50–$200 per node
- Capable of carrying voice (VoIP), video, and data over multi-hop
  links spanning 30+ miles with directional antennas
- Requires General or higher ham license
- A 3–5 node AREDN network covering a rural community enables truly capable
  IP communications independent of internet
- Setup complexity is moderate to high; documentation at arednmesh.org

**GoTenna Mesh**
- Commercial, no-license required
- 900 MHz; range 1–4 miles; app-based text and GPS
- Hardware: ~$100–$150 per unit
- Limitation: closed ecosystem; proprietary; subscription features;
  company dependent. For owned infrastructure, Meshtastic is preferable.

### 12.3.8 Emergency Nets and Organizations

**ARES (Amateur Radio Emergency Service)**
- ARRL-affiliated volunteer organization
- Trains hams for emergency communications service
- Activated during local disasters; works with county emergency management
- Joining your local ARES group is the best way to build skills and
  integration with official emergency response
- arrl.org/ares

**RACES (Radio Amateur Civil Emergency Service)**
- Operates under local civil defense authority
- Can be activated officially during declared emergencies
- Requires formal registration with local emergency management

**NTS (National Traffic System)**
- Structured message relay network; handles formal traffic (radiograms)
- Organized in cycles: local nets → section nets → national nets
- A message passed into NTS can reach anywhere in the US via radio relay
- Valuable in prolonged grid-down: formal record of welfare messages
- arrl.org/nts

**Key HF Net Frequencies (2025-26):**

| Net | Frequency | Time (UTC) | Purpose |
|---|---|---|---|
| ARRL Pacific Net | 14.285 MHz | 1900 | Traffic; NTS regional |
| 40m ARES nationwide | 7.285 MHz | Varies by section | Emergency; varies by region |
| Winlink gateway calling | 14.105 MHz | Continuous | Pactor/VARA gateway access |
| JS8Call community | 7.078 MHz | Continuous | Grid-down messaging |
| Marine SSB emergency | 8.291 MHz (USB) | Continuous | Coast guard monitoring |
| FEMA/NHC HF | 14.325 MHz | During hurricanes | National Hurricane Center |
| NOAA/WWV time signals | 2.5/5/10/15/20 MHz | Continuous | Time, propagation reports |

### 12.3.9 Antennas: Build Tables

Building your own antennas is cost-effective, educational, and produces
antennas tailored to your specific site.

**Basic Half-Wave Dipole (horizontal)**

The simplest effective HF antenna. Requires two supports (trees work well).
Feed at the center with 50-ohm coax.

| Band | Total length | Each leg | Wire | Cost (2025-26) |
|---|---|---|---|---|
| 80m (3.750 MHz) | 124.8 ft | 62.4 ft | 14 AWG stranded copper | $25–$40 |
| 40m (7.200 MHz) | 65.0 ft | 32.5 ft | 14 AWG stranded copper | $20–$30 |
| 20m (14.1 MHz) | 33.2 ft | 16.6 ft | 14 AWG stranded copper | $15–$20 |
| All-band (with tuner) | 135 ft total | 67.5 ft | 14 AWG stranded copper | $35–$55 |

Materials for a complete dipole: ~30 ft of LMR-400 feedline ($35–$50 depending
on length), center insulator/choke balun ($15–$25 DIY, $25–$60 commercial),
two end insulators ($5–$10), wire. Total cost per dipole: $60–$130.

**End-Fed Half-Wave (EFHW) Antenna**

Very popular for portable and off-grid use — requires only one support point
at the far end; feedpoint at the operating position.

Requires an EFHW transformer/unun (49:1 impedance transformer):
- DIY with T200-2 toroid ($8), 14 AWG wire, box: $20–$30 total parts
- Commercial (SOTA Beams, PAR Electronics): $35–$75
- Wire length for 40m EFHW: 66 feet (works on 40/20/15/10m with tuner)
- Wire length for 80m EFHW: 130 feet (works on 80/40/20/15/10m with tuner)

**Vertical Antenna (ground-mounted)**

Omnidirectional; works well with good ground plane. No horizontal space
needed — only vertical. Radials (horizontal wires buried or on ground)
form the ground plane.

- Quarter-wave vertical for 40m: 33 feet tall
- Install with minimum 16–32 radials, each 33 feet long, buried 2 inches
- Commercially available: Hustler 6-BTV ($200–$230) covers 6 bands with traps
- DX Commander (Callum M0MCX design): $160–$200; excellent multi-band vertical

**2m/70cm Yagi (directional VHF/UHF)**

For point-to-point links (farm to community center), a Yagi dramatically
increases range over an omnidirectional antenna.

- 5-element 2m Yagi: gain ~7 dBd; builds from aluminum rod and PVC for $15–$25
- 11-element 2m Yagi: gain ~11 dBd; excellent for 10+ mile links; $20–$40 materials
- Commercial 2m/70cm Yagi (Arrow Antenna): $45–$75; foldable for portable use

**J-Pole (2m/70cm, omnidirectional)**

Easy to build from 1/2-inch copper pipe. Excellent for a base station antenna.
- 2m J-Pole: ~5 ft of copper pipe + fittings; $15–$25 materials
- Can be mounted indoors in a pinch (attic, upper floor)
- Gain: ~3 dBd over a dipole

---

## 12.4 GMRS / FRS / MURS

These license-light or license-free services are the practical choice for
day-to-day family and community coordination, particularly for people who
do not (yet) hold amateur licenses.

### 12.4.1 GMRS (General Mobile Radio Service)

GMRS is the most capable non-amateur service available to civilians and the
right choice for community coordination within a homestead or small community.

**License**: $35 / 10-year, covers entire immediate family, no exam required.
Apply at fcc.gov/licensing/systems-tools/universal-licensing-system.

**Frequency range**: 462.5500–462.7250 MHz and 467.5500–467.7250 MHz (8 simplex
+ 7 output channels + 8 repeater input channels)

**Power**: Up to 50W on main channels; 5W on interstitial (shared FRS) channels

**Repeaters**: GMRS licensees may operate, use, and build repeater systems.
This dramatically extends range: a well-sited repeater at 500 ft elevation
can provide 40+ mile range from a handheld.

**CTCSS/DCS (tone squelch)**: Subaudible tones (67–254 Hz CTCSS or digital DCS)
used to selectively open squelch on a shared channel. Does NOT encrypt —
other stations still transmit on your channel; you just don't hear them
unless they send the right tone. Use to reduce chatter on shared repeaters.

| GMRS Radio | Power | Features | Price (2025-26) | Notes |
|---|---|---|---|---|
| Midland GXT1000VP4 | 50W (stated, ~5W actual*) | 50ch GMRS/FRS; NOAA weather | $55–$70 pair | *Handhelds limited to 5W by FCC; "50W" is repeater output spec mislead |
| Midland T77VP5 | 5W | 50ch; NOAA; rechargeable | $60–$75 pair | Good family HT kit |
| Wouxun KG-1000G | 10W | Full GMRS; repeater capable; cross-band | $170–$200 | Best GMRS HT; worthy upgrade; solid radio |
| Wouxun KG-805G | 5W | GMRS; compact; budget option | $65–$80 | Reliable; recommended starter |
| Rugged Radios R1 | 5W | GMRS handheld; rugged; helmet/headset compatible | $100–$130 | Popular with off-road community |
| Btech GMRS-V1 | 2W (FRS channels) / 5W | Budget; compact | $35–$45 | Acceptable; not repeater capable |
| Midland MXT500 | 50W | Mobile GMRS; full power; weather | $180–$220 | Primary recommendation for mobile/base station |
| Rugged Radios RDH16 | 16W | GMRS mobile; compact | $150–$180 | Good mid-power option |

**Practical GMRS setup for a homestead community:**
1. One Midland MXT500 (50W) base station per household node — $200 each
2. Wouxun KG-1000G handhelds for workers in the field — $175 each
3. Shared repeater on highest hill: Midland MXT400 + antenna at 50+ ft
   elevation — total cost $400–$600; extends range to 20–40 miles

### 12.4.2 FRS (Family Radio Service)

No license required; maximum 2W; no external antenna; simplex only (no
repeaters). FRS shares most GMRS channels.

**Realistic range**: 0.5–2 miles in open terrain; 0.25–0.5 miles in forest.
The packaging claims (35-mile range) are pure marketing fiction in any real
environment.

**Best use**: Short-range coordination on a farm or homestead — from garden
to barn, from house to outbuilding. Not suitable for community networking.

### 12.4.3 MURS (Multi-Use Radio Service)

5 channels in the VHF range (151–154 MHz); no license; 2W maximum; external
antennas are permitted.

VHF (151–154 MHz) propagates better through foliage and terrain than UHF
GMRS/FRS channels. In forested terrain, MURS may outperform FRS/GMRS by
a meaningful margin.

**MURS channels:**

| Channel | Frequency | Notes |
|---|---|---|
| 1 | 151.820 MHz | General |
| 2 | 151.880 MHz | General |
| 3 | 151.940 MHz | General |
| 4 | 154.570 MHz | Business and personal; formerly Blue Dot |
| 5 | 154.600 MHz | Business and personal; formerly Green Dot |

**MURS radios**: Dakota Alert MURS transmitters (~$100–$200) are commonly
used for entry alert sensors on rural driveways — a vehicle breaks a beam
and a MURS transmitter sends a signal to your receiver. Useful for perimeter
awareness.

MURS voice radios: Kenwood ProTalk TK-3230DX ($100–$130); Btech MURS-V1
($35–$45).

### 12.4.4 Range Tables

These are field-measured, realistic ranges — not manufacturer claims.

| Service | Radio type | Terrain | Realistic range |
|---|---|---|---|
| FRS | 2W HT | Open/flat | 1–2 miles |
| FRS | 2W HT | Light forest | 0.25–0.75 miles |
| FRS | 2W HT | Heavy forest / hilly | 0.1–0.3 miles |
| GMRS | 5W HT | Open/flat | 2–5 miles |
| GMRS | 5W HT | Light forest | 0.5–2 miles |
| GMRS | 5W HT | Heavy forest / hilly | 0.25–0.75 miles |
| GMRS | 50W mobile | Open/flat | 8–20 miles |
| GMRS | 5W HT to repeater | Open; repeater at 500 ft | 20–40 miles |
| MURS | 2W HT | Open/flat | 1–3 miles |
| MURS | 2W HT | Forest | 0.5–1.5 miles |
| Ham VHF | 5W HT | Open/flat | 3–8 miles |
| Ham VHF | 50W mobile | Open/flat | 15–30 miles |
| Ham VHF | 5W HT to repeater | Open; repeater at 500 ft | 30–60 miles |

---

## 12.5 Satellite Communications

Satellite comms are the backstop when all terrestrial systems fail or when
you are operating beyond the range of any repeater or HF contact. The
service options span an enormous range of capability and cost.

### 12.5.1 Starlink

Starlink is SpaceX's low-earth-orbit (LEO) broadband satellite internet.
For off-grid use, it provides genuine broadband (download speeds typically
50–200 Mbps, sometimes higher) without any terrestrial infrastructure.

**Specifications (2025-26):**
- Hardware: Gen 3 standard dish — $599 one-time purchase
- Service plans: Residential $120/month; Portability (move dish
  between addresses) $120/month + $25/month portability add-on;
  RV/Roam (mobile, no fixed address) $150/month; Starlink Mini
  (smaller dish, $599) with $50/month or $150/month data plans
- Latency: 25–60 ms typical; significantly better than geostationary
  (which runs 600+ ms)
- Data: Unlimited on residential plans (though Priority Data tiers apply
  at congested locations); Starlink Mini has data caps
- Power draw: Gen 3 standard dish: 50–75W during operation; peak 100W
  during startup/snow melt
- Weight/size: Gen 3 standard — ~5 lbs, 22" diameter circular dish
- Coverage: Continental US, Alaska, Hawaii, most global coverage 53° N–S
  latitude with some polar gaps

**Off-grid implications:**
- 50–75W continuous is a meaningful power load. Plan for it in your solar
  sizing: 50W × 8 hours/day = 400 Wh/day, or ~30 Ah from a 13.8V supply
- Dish requires a clear view of the sky — obstructions (trees, roof) degrade
  service; use the Starlink app obstruction checker before siting
- Functions as a full internet connection, enabling VoIP calls, email,
  weather data, map downloads, and remote access to your property systems
- Physical security risk: the dish is obvious and expensive. Consider
  concealment in hostile scenarios.
- Starlink is a company dependency: if SpaceX changes pricing, discontinues
  service, or experiences orbital problems, your internet goes with it.
  Treat as primary convenience, not sole dependency.

**Starlink flat-mount vs. pivot mount:**
- Gen 3 dish self-adjusts orientation; mount on a roof or pole
- Permanently mounted dishes require solid base; wind loading matters
  (Gen 3 rated to 30 mph winds)

### 12.5.2 Iridium Satellite Phone

Iridium operates a constellation of 66 LEO satellites with global coverage
including poles. It is the only commercial voice/data system with true global
coverage (no dead zones, including oceans and polar regions).

**Specifications:**
- Devices: Iridium 9555 (~$800 used, $1,100–$1,400 new); Iridium Extreme
  ($1,200–$1,600, ruggedized); Iridium GO! ($700–$900, hotspot for phones)
- Voice: $0.80–$1.30 per minute depending on plan
- Data: 2,400 bps standard; up to 9,600 bps with Iridium burst data
- Plans: Pay-as-you-go (~$1.10/min); monthly ($60–$100/mo for 75–200 minutes);
  annual maintenance plan ($30/month keeps number active with monthly allotment)
- Coverage: 100% global
- SOS: Iridium Extreme has dedicated SOS button with GEOS response center
- Power draw: <0.5W standby; 3–4W in call
- Battery life: ~30 hours standby; 4 hours talk

**When to choose Iridium over Starlink:**
- You need guaranteed coverage regardless of location (Starlink has gaps
  at extreme latitudes and during satellite outages)
- You need voice communication, not data
- Power budget is extremely constrained
- You need the radio to survive rough conditions (Extreme model MIL-STD-810F)
- You need a device that fits in a pocket and works anywhere on earth

**Practical role**: Iridium is your "if everything else fails" voice link.
An annual maintenance plan ($30/month) keeps a device active and available
without running up voice bills. The device itself, properly stored in a
Faraday cage with spare battery, can sit unused for years and be available
when needed.

### 12.5.3 Garmin inReach

The inReach series (inReach Mini 2, inReach Explorer+) uses the Iridium
network for 2-way messaging and SOS but at lower cost than voice.

**Specifications:**
- inReach Mini 2: $350–$400; 1.8 oz; 13-day battery (10-minute tracking)
- inReach Explorer+: $450–$500; GPS + digital compass + altimeter; 100-hour battery
- Plans: Safety ($15/month; 10 messages); Recreation ($35/month; unlimited
  messages); Expedition ($65/month; 40 messages + 10-minute tracking)
- Messages: 2-way SMS to any phone number; message via Garmin app
- SOS: 24/7 GEOS emergency response center; GPS coordinates transmitted
- No voice call capability
- Weather: downloadable forecasts via satellite connection
- Power: rechargeable lithium; USB-C charging

**Best use case**: Mobile and traveling. A person hiking out to check
the water system, a vehicle run to town, a courier between communities.
The inReach Mini 2 slips into a shirt pocket and provides emergency SOS
capability anywhere on earth for $15/month. This is the highest value-per-
dollar satellite option for most homesteaders.

### 12.5.4 SPOT

SPOT (Globalstar satellite network) offers a simpler, cheaper alternative
to Garmin inReach.

- SPOT X: $150–$200 device; 2-way messaging; keyboard input; $12–$20/month
- SPOT Gen4: $100–$150 device; one-way tracking + SOS only; $12–$30/month
- Network: Globalstar — not global; coverage gaps at high latitudes
  and some ocean areas
- SOS: SPOT Emergency Response Center

**Limitation**: Globalstar's coverage is inferior to Iridium (used by Garmin).
SPOT is adequate for North America, Europe, and most populated areas but
unreliable at latitudes above 70°N or in remote oceanic regions.

### 12.5.5 Satellite Communications Comparison Table

| Service | Coverage | Monthly cost | Device cost | Voice | Data/SMS | SOS | Power draw | Best for |
|---|---|---|---|---|---|---|---|---|
| Starlink Residential | US + global (excl. poles) | $120 | $599 | Via VoIP | Broadband | No native | 50–75W | Primary internet at homestead |
| Starlink RV/Roam | US + global | $150 | $599 | Via VoIP | Broadband | No native | 50–75W | Mobile use; traveling |
| Iridium 9555 (PAYG) | Global 100% | $30–$60 (maint.) | $900–$1,400 | Yes | 9,600 bps | SOS button (Extreme) | <0.5W standby | Voice fallback; global |
| Garmin inReach Mini 2 | Global 100% | $15–$65 | $350–$400 | No | 2-way SMS | Yes (GEOS) | Minimal | Mobile SOS + messaging |
| Garmin inReach Explorer+ | Global 100% | $15–$65 | $450–$500 | No | 2-way SMS + weather | Yes (GEOS) | Minimal | Field work, expeditions |
| SPOT X | N. America, Europe, partial global | $12–$20 | $150–$200 | No | 2-way SMS | Yes | Minimal | Budget satellite messaging |
| SPOT Gen4 | N. America, Europe | $12–$30 | $100–$150 | No | One-way tracking | Yes | Minimal | Tracking only; lowest cost |
| Iridium GO! | Global 100% | $60–$130 | $700–$900 | Via app | Data hotspot | Yes | ~2W active | Team use via smartphones |

---

## 12.6 Shortwave Listening (SWL)

Shortwave listening requires no license, produces no RF emissions, and
provides access to information that will continue to be broadcast during
grid-down scenarios. It is the most underrated item in a communications kit.

### 12.6.1 Value in Grid-Down Scenarios

International broadcasters transmit on HF shortwave with powerful (100–500 kW)
directional antennas. A modest shortwave receiver can hear:

- **VOA (Voice of America)**: US government broadcaster; multiple languages;
  transmits on dozens of HF frequencies; does not have US-domestic coverage
  requirement but signals often receivable in US on propagation
- **BBC World Service**: Transmits from Woofferton, Ascension Island, and
  other relay sites; extensive English-language programming; historically
  has been the "ground truth" source in emergencies worldwide
- **Radio France Internationale (RFI)**: French; strong in Africa and Europe
- **Deutsche Welle (DW)**: German; English broadcasts; reliable European signal
- **Radio Free Europe / Radio Liberty**: Eastern Europe and Central Asia
  targeted; receivable in US during favorable propagation
- **WWV / WWVH**: NIST time signals; transmitted continuously at 2.5, 5, 10,
  15, and 20 MHz; not speech programming but critical for time synchronization
  and propagation assessment; include brief solar/geophysical reports
- **NOAA Weather Radio (NWR)**: VHF (162.4–162.55 MHz); not shortwave but
  a critical receive-only resource; 1,000 transmitters cover 95% of the US

### 12.6.2 Shortwave Receiver Recommendations

| Receiver | Type | Price (2025-26) | Sensitivity | Notes |
|---|---|---|---|---|
| Tecsun PL-880 | Portable; SSB capable | $85–$100 | Excellent | Best portable for the money; SSB allows ham monitoring; 3.7V Li-ion built-in |
| Tecsun PL-990X | Portable; SSB capable | $130–$160 | Excellent | Upgraded PL-880; better audio; more memory presets |
| CountyComm GP-5 DSP SSB | Micro portable; SSB | $80–$95 | Good | Military contractor; rugged; excellent small form factor |
| Grundig G3 (Eton G3) | Portable; SSB | $100–$130 | Good | User-friendly; solid build; well-regarded |
| Sangean ATS-909X2 | Portable; SSB | $160–$180 | Very good | Multiple inputs; external antenna jack; serious hobbyist |
| Icom IC-R75 | Desktop; SSB | $600–$700 used | Excellent | Professional desktop receiver; hear very weak signals |
| SDRPlay RSP1C | SDR (software defined) | $130–$150 | Excellent | Requires laptop; covers 1 kHz–2 GHz; extraordinary flexibility |
| RTL-SDR V4 | SDR dongle | $35–$45 | Good | Dirt cheap entry to SDR; cover HF–1.7 GHz with appropriate antenna |

**SSB (Single Sideband) capability is important**: Many shortwave broadcasts
use AM (amplitude modulation), which simple radios receive. But amateur radio
traffic on HF uses SSB. If you want to monitor ham emergency nets, you need
a radio with SSB mode. The Tecsun PL-880 has SSB; the simpler Tecsun PL-310ET
does not.

**SDR (Software Defined Radio)**: An SDR dongle connected to a laptop (or
Raspberry Pi with SDR# or GNU Radio) turns a $35 RTL-SDR into a receiver
covering 100 kHz to 1.7 GHz. This is remarkable value but requires power
for the computer. For backup, a battery-powered portable like the Tecsun is
preferable.

### 12.6.3 Key Shortwave Frequencies

| Station | Language | Frequency (MHz) | Target/Notes |
|---|---|---|---|
| WWV (NIST time) | Time tones + voice | 2.5, 5.0, 10.0, 15.0, 20.0 | Continuous; listen for solar flux index |
| WWVH (NIST, Hawaii) | Time tones + female voice | 2.5, 5.0, 10.0, 15.0 | Same data; alternate site |
| BBC World Service | English | 5.875, 6.195, 9.410, 12.095, 15.400 | Varies by target region and season; check bbc.co.uk/worldservice for current schedule |
| VOA | English | 9.785, 15.580, 17.895 | Varies; afrts.dodlive.mil/AFN.html for current schedules |
| Radio Havana Cuba | English | 6.000, 6.060, 9.535, 11.760 | Strong signal in eastern US; 24-hour operation |
| WBCQ | English | 5.130, 7.490, 9.330 | US shortwave; various programming |
| WRMI | English/multi | 5.950, 7.570, 9.395, 11.580 | US shortwave relay; very strong |
| NHK World (Japan) | English | 9.625, 11.970 | Asia-Pacific news |
| All India Radio | English | 9.445, 11.620, 13.605 | Indian subcontinent target; often receivable in US |
| WTWW | English | 5.085, 9.479 | US shortwave; strong in eastern US |

Shortwave schedules shift seasonally and with propagation. Use the WRTH
(World Radio TV Handbook, ~$30/year) for current schedules or consult
short-wave.info online.

### 12.6.4 Antennas for SWL

**Long wire**: A 30–60 foot wire strung from your house to a tree or pole
makes an excellent shortwave receive antenna. Connect to the antenna jack
on your receiver via a simple long-wire adapter ($5–$15). This is the
single biggest improvement you can make to portable receiver performance.

**Loop antenna (indoor)**: A 3–10 foot diameter loop wound with 15–30 turns
of wire; can be tuned with a variable capacitor. Excellent for nulling out
local noise (rotate the loop to null a noise source). Can be built for
under $20.

**Magnetic loop antenna**: Commercial examples (Wellbrook ALA1530, $200–$250)
provide exceptional noise rejection for suburban or RFI-heavy environments.

---

## 12.7 CB Radio

CB (Citizens Band) radio operates on 40 channels in the 27 MHz range.
No license is required; maximum power is 4W AM or 12W SSB.

### 12.7.1 Capabilities and Limitations

**Normal range**: 1–5 miles on flat terrain between vehicles or mobile
stations. In hills and forest, expect 0.5–2 miles.

**Atmospheric skip (SSB)**: Under certain ionospheric conditions — most
commonly in spring and fall — CB signals can travel 500–1,500+ miles via
ionospheric skip. This happens unpredictably on AM but is most useful on
SSB (upper or lower sideband, channels 36–40 by convention). During solar
maximum (2025–2026), skip propagation on CB is more frequent and dramatic.
Skip contacts of 1,000+ miles are common during openings.

**Practical role in off-grid communications**: CB is mature technology with
enormous installed base. Almost every trucker, many farmers, and a large
portion of rural households have CB equipment. In a regional emergency,
monitoring CB channel 9 (emergency) and channel 19 (trucker/motorist) can
provide real-world ground-level intelligence from travelers on the road.

| Radio | Type | Power | Price (2025-26) | Notes |
|---|---|---|---|---|
| Cobra 29 LTD Classic | Mobile; AM/SSB | 4W AM / 12W SSB | $70–$90 | Benchmark CB; SSB capability is worth it |
| Uniden PRO510XL | Mobile; AM only | 4W AM | $35–$50 | Reliable budget; no SSB |
| Uniden BearCat 980SSB | Mobile; AM/SSB | 4W AM / 12W SSB | $100–$120 | More modern than Cobra 29; good ergonomics |
| Cobra HH50WXST | Handheld | 4W AM | $45–$60 | Portable; good for vehicle kit or pack |
| Galaxy DX-959 | Mobile; AM/SSB | 4W AM / 12W SSB | $120–$140 | Serious operator; adjustable power; popular |

**Channel reference:**

| Channel | Frequency | Use |
|---|---|---|
| 9 | 27.065 MHz | Emergency / motorist assistance (monitored by some CB users) |
| 17 | 27.165 MHz | Alternate truckers channel (east-west roads by convention) |
| 19 | 27.185 MHz | Primary truckers / motorist channel; best real-time road info |
| 36–40 | 27.365–27.405 MHz | SSB operations; long-range skip contacts |

---

## 12.8 EMP Hardening

An electromagnetic pulse (EMP) — whether from a nuclear high-altitude burst
or a severe solar storm (Carrington-type event) — could disable unprotected
electronics across a wide area. The probability of a full HEMP event is low
but nonzero, and the consequence of having no communications afterward is
severe. Hardening is cheap insurance.

### 12.8.1 EMP Threat Overview

**Nuclear High-Altitude EMP (HEMP)**

A nuclear weapon detonated at 25–400 km altitude produces three overlapping
electromagnetic effects:

- **E1**: Extremely fast pulse (rise time <10 ns); amplitude up to 50 kV/m;
  affects semiconductors and solid-state electronics via induced voltage
  spikes. Duration: nanoseconds to microseconds. This is the component
  that fries circuit boards.
- **E2**: Slower pulse similar to lightning (microseconds to milliseconds);
  less dangerous to modern electronics because surge protectors designed
  for lightning largely handle E2. Often overlooked because E1 destroys
  surge protectors before E2 arrives.
- **E3**: Very slow, geomagnetic-like disturbance lasting seconds to minutes;
  affects long power lines and transformers (same mechanism as a geomagnetic
  storm). Responsible for grid transformer damage in HEMP scenarios.

**Geomagnetic Storm (Carrington Event model)**
- A large coronal mass ejection (CME) hitting Earth generates primarily E3-
  equivalent effects: long-line infrastructure damage (grid, pipelines) but
  minimal E1 effect on local electronics. Portable electronics largely
  survive Carrington-class events; the grid transformers do not.

**What survives E1 naturally:**
- Mechanical devices (no electronics)
- Older tube-type radios and equipment (vacuum tubes tolerate EMP much
  better than transistors; not immune, but more resistant)
- Equipment that is OFF and disconnected from antennas and power lines
  (disconnected equipment experiences much lower induced voltages)
- Equipment inside a Faraday cage

**What is vulnerable:**
- Anything with solid-state electronics (semiconductors)
- Anything connected to long wires (antennas, power lines, phone lines)
  when the pulse occurs — the wire acts as a collection antenna
- Modern vehicles with engine control units (ECUs)
- Starlink dishes, receivers, computers

### 12.8.2 Faraday Cage Construction

A Faraday cage is a conductive enclosure that attenuates electromagnetic
fields inside it. The attenuation depends on:
1. Conductivity of the cage material
2. Frequency of the threat signal
3. Completeness of the shielding (no gaps, no holes larger than the
   wavelength of the threat)
4. Grounding (reduces E3 but not necessary for E1/E2 attenuation)

**E1 threat frequency**: The E1 peak energy is in the 1 MHz – 1 GHz range.
Protecting against this range requires a cage with no apertures larger than
~1–3 cm (1/10 wavelength at 1 GHz = 3 cm).

**DIY Faraday cage options:**

**Option 1: Galvanized steel garbage can with lid**
- 20-gallon galvanized can with tight-fitting lid: $25–$40
- Line interior with cardboard or foam (prevents direct contact with the
  cage wall, which would conduct voltage to the device)
- Wrap devices in anti-static bags before placing inside
- Seal lid with aluminum HVAC tape around the entire circumference
- Performance: ~40–60 dB attenuation at 100 MHz — adequate for most scenarios

**Option 2: Military surplus ammo can**
- .50 cal ammo cans ($20–$35) or 30mm cans ($40–$60) — tight-fitting lids
  with rubber gaskets
- The rubber gasket is actually a problem: it breaks the conductive contact.
  Replace or supplement with conductive copper tape around the lid rim
- Very compact; fits in vehicle; waterproof after sealing
- Attenuation without modification: ~30–40 dB; with conductive lid seal: ~50–60 dB

**Option 3: Nested containers**
- Nested cages provide additive attenuation: inner container + outer
  container = combined attenuation
- Device in anti-static bag → inner ammo can → outer galvanized can
- Each 10 dB of attenuation reduces field strength by 3.2×; combined
  20 dB extra gives you 10× more headroom

**Option 4: DIY copper mesh cage**
- Copper or galvanized mesh (hardware cloth, 1/8" openings or smaller)
  constructed into a box with soldered or tightly folded joints
- Performance depends on joint quality; seams must be electrically continuous
- Materials cost: $40–$80 for a medium box
- Higher effort but can be sized to hold larger equipment (full radios,
  solar charge controllers)

**Attenuation reference table:**

| Cage type | Approximate attenuation (dB) at 100 MHz | Practical protection |
|---|---|---|
| Unmodified ammo can (rubber gasket) | 20–35 dB | Minimal; field 30–100× lower |
| Ammo can with conductive lid seal | 45–60 dB | Good; field 300–1,000× lower |
| Galvanized can, HVAC tape sealed | 40–55 dB | Good |
| Nested ammo + galvanized can | 60–80 dB | Excellent; field 1,000–10,000× lower |
| Professional shielded enclosure | 80–100 dB | Near-complete attenuation |

### 12.8.3 What to Store in a Faraday Cage

Prioritize items that would be impossible or very difficult to replace:

**Essential Faraday kit:**
- Baofeng UV-5R or similar simple HT radio (cheap, simple, likely to survive
  and function as backup) — with fully charged spare battery
- Spare crystals or programmable memory card if applicable
- AM/FM/SW battery portable receiver (Tecsun PL-880 or similar)
- Spare USB power banks (fully charged) — power source for devices
- Garmin inReach or SPOT — satellite messenger; your link to the outside world
- Spare solar charge controller (MPPT; 20–40A class) — expensive and hard
  to replace
- Spare USB cables, car adapters, battery chargers
- USB drives with maps, medical references, technical documents
- Spare laptop or Raspberry Pi (for digital modes, Winlink, etc.)
- Small MPPT controller and fused cable for emergency solar charging
- AA/AAA battery charger (NiMH) + 16× rechargeable AAs

**Optional additions (larger cage):**
- Spare HF transceiver (Xiegu G90 or similar compact unit)
- Spare VHF/UHF mobile radio (Yaesu FT-7900R)
- Spare engine control module for your primary vehicle (if replaceable;
  check model compatibility — not all ECUs are plug-and-play)
- Spare solar panels (partially folded; panels themselves are fairly
  robust but inverters and controllers are vulnerable)

### 12.8.4 Surge Protection and Grounding

While Faraday cages protect stored equipment, your installed antennas and
equipment need protection for the threat scenario of being connected during
the event.

**Whole-house surge suppression:**
- Install a whole-home surge arrestor at the main panel: $40–$150 parts
- This handles normal lightning and E2 but provides only partial E1 protection
- Eaton CHSPT2ULTRA, Siemens FS140, Leviton 51120-1 — all ~$50–$100

**Antenna lightning arrestors (coaxial)**:
- Every coaxial line entering the building should have a coaxial surge
  arrestor at the entry point: $15–$50 per line (PolyPhaser, Alpha Delta, ICE)
- Ground the arrestor body to a dedicated 8-foot ground rod at the entry point
- Bond all ground rods together with #4 AWG solid copper wire

**Radio disconnect protocol:**
- During a known threat (warning of solar CME, regional nuclear event),
  the most effective protection is to disconnect antennas and power before
  the pulse arrives
- Coaxial switches allow quick disconnect; keep them accessible
- An HF radio in receive mode with antenna connected is far more vulnerable
  than one powered off with antenna disconnected

**Tube radios:** Vacuum tube equipment tolerates EMP significantly better
than solid-state. Classic military surplus receivers (Collins, Hammarlund,
National, Hallicrafters) from the 1940s–1960s use tube technology and are
broadly available at hamfests for $50–$300. A functional tube shortwave
receiver as a backup (stored inside a Faraday cage when not in use) is an
elegant solution to post-HEMP receive capability.

---

## 12.9 Grid-Down Communication Protocols

Having the equipment is not enough. You need procedures — pre-agreed,
practiced, written down — that your community follows when normal
communications fail.

### 12.9.1 Information Hierarchy

Structure your communication responsibilities in concentric circles:

**Level 1 — Immediate household (daily)**
- Method: GMRS family radios on home channel; physical check-in at meals
- Every member physically accounted for at least twice daily
- If a member fails to appear, systematic search begins (see Level 2)

**Level 2 — Extended network (daily/weekly)**
- Your closest neighbors and mutual aid partners: 3–8 households
- Method: Scheduled GMRS or VHF net, once daily at agreed time
- If a member misses two consecutive check-ins without prior notice,
  a wellness check visit is dispatched (never send alone)

**Level 3 — Community region (weekly)**
- All households in your region with radio capability
- Method: HF net (40m or 80m depending on distance) or GMRS repeater net
- Net control rotates weekly — one station manages the net
- Traffic: weather reports, resource availability, health updates,
  requests for assistance, visitor/stranger activity alerts

**Level 4 — Information gathering (continuous)**
- Passive receive: NOAA Weather Radio, shortwave broadcast, AM
- No transmission required; pure intelligence

### 12.9.2 Check-In Schedules

Design your net schedule before you need it. Write it on paper. Distribute
copies to every member of the network.

**Example daily net schedule:**
```
0700 local: Household internal check (all family members, GMRS)
0800 local: Extended network net (GMRS or VHF; 10 min max)
0900 local: NOAA weather radio monitor (receive only)
1900 local: Evening community HF net (40m; 30 min)
2200 local: Household internal check (all family members present)
```

**Net format (HF or GMRS):**
1. Net control: "This is [call sign/name] net for [date], [time] UTC.
   Is the frequency in use? [pause] Net is open. Roll call." 
2. Each station checks in with call sign and status word
3. Traffic: announcements, needs, offers — each kept brief
4. Net control closes: "[time] UTC, net closed. Net control is [call/name]."

**Status words** (pre-agreed, simple, memorizable):
- **GREEN**: All well; no needs; no news
- **YELLOW**: Condition noted; no immediate need; will report more later
- **RED**: Need assistance; stay on frequency; send response
- **GREY**: Partial communication; reduced capability; check back next net

### 12.9.3 Signal Plans for OPSEC

For information that should not be broadcast clearly:

**Daily check-in coded signals:**
- Three short taps (keyer, DTMF, or verbal "3-tap"): All clear at this location
- Five short taps: Requests a visit (non-emergency, comfortable)
- One long tone / "long-tap": Duress — SEND HELP — transmitted if under
  coercion or in danger

**Duress word protocol:**
A pre-agreed word that, when included in a normal-sounding transmission,
signals duress. If your check-in call sounds normal but includes the word
"purple" in conversation, it means "I am under coercion; do not come here;
alert others; treat this location as compromised."

**Message drops (dead drops):**
For highly sensitive communication without any radio emissions:
1. Pre-agreed physical location (hollow in specific tree; rock cairn;
   specific fence post)
2. Message format: written on paper; placed in waterproof bag
3. Signal that drop has been made: chalk mark on agreed surface; specific
   object placed in view
4. Retrieval: person retrieves without radio; no confirmation transmitted

### 12.9.4 Emergency Contact Tree

Before any emergency, build a contact tree with primary, secondary, and
tertiary contacts for every person and household in your network.

```
Person: [Name]
Primary contact: [Name], [GMRS channel or freq], [physical address]
Secondary contact: [Name], [GMRS channel or freq], [physical address]
Tertiary contact (outside region): [Name], [Winlink address or Iridium number]
Medical notes: [blood type, allergies, medications, conditions]
Vehicle: [make/model/color/plate]
```

Print this document. Laminate it. Every household gets a copy. Store one
in the Faraday kit.

### 12.9.5 Comms-Out Protocols

What to do when someone goes silent:

**Day 1 missed check-in**: Attempt contact on all available frequencies
(primary, secondary, digital). Note in log.

**Day 1 second missed check-in**: Send a runner or vehicle to do a
wellness check. Two people minimum; do not go alone.

**Day 2 no contact**: Alert the community network (Level 2/3). Begin
coordinated search if person's last known location suggests they could
be in the field.

**Day 3 no contact**: Presume potential emergency. Activate ARES/SAR
contacts if available. Attempt Winlink relay to reach outside contacts.

### 12.9.6 Runner Protocols

When no radio communication is possible or safe:

- Runners travel in pairs whenever possible
- Runner carries: written message in sealed envelope; return message pre-addressed
- Runner carries: GMRS handheld on receive-only (so you can hear if they
  call for help, but they do not transmit their position)
- Agreed time windows: runner expected to arrive by [time]; if not arrived
  by [time + buffer], dispatch search
- Route pre-agreed and written on the message itself ("I left [origin]
  at [time] via [route]")

### 12.9.7 UTC and Time Synchronization

When operating multiple stations on a schedule, everyone must agree on
time. UTC (Coordinated Universal Time) is the universal standard for radio
operations.

**Why UTC matters:**
- Avoids confusion between time zones (critical for a regional net)
- Emergency net frequencies and scheduled contacts all reference UTC
- Log entries in UTC are unambiguous and useful to others

**How to synchronize to UTC:**
- **WWV**: Tune to 5.000, 10.000, or 15.000 MHz. Continuous tone with
  voice announcement of UTC at each minute mark. Solar flux index and
  geomagnetic field condition announced at 18 minutes past each hour (WWV)
  and 45 minutes past (WWVH). This works with any shortwave receiver.
- **WWVB**: 60 kHz; not shortwave; received by most radio-controlled clocks.
  Not useful for manual synchronization but syncs your clocks automatically.
- **GPS**: Every GPS device receives highly accurate UTC from GPS satellites.
  A handheld GPS, Garmin inReach, or phone with GPS will show UTC within
  microseconds. Cross-check your clocks against GPS periodically.

---

## 12.10 Power Sizing for Communications

Every radio in your kit must be powered. Planning this into your overall
energy budget prevents the scenario where your HF radio drains your
battery bank the night before a winter storm.

### 12.10.1 Power Consumption Table

| Device | Mode | Current | Voltage | Watts | Notes |
|---|---|---|---|---|---|
| Icom IC-7300 | Receive | 1.5A | 13.8V | 21W | DSP + backlight |
| Icom IC-7300 | TX 100W output | 20A | 13.8V | 276W | Short duty cycle in voice ops |
| Icom IC-7300 | TX 50W output | 13A | 13.8V | 179W | Good HF compromise |
| Icom IC-7300 | TX 25W output | 9A | 13.8V | 124W | Adequate for regional; low draw |
| Yaesu FT-891 | Receive | 0.7A | 13.8V | 10W | Mobile/compact form factor |
| Yaesu FT-891 | TX 100W | 22A | 13.8V | 304W | |
| Xiegu G90 | Receive | 0.7A | 13.8V | 10W | |
| Xiegu G90 | TX 20W | 5.5A | 13.8V | 76W | Max output |
| VHF mobile 50W | Receive | 0.8A | 13.8V | 11W | |
| VHF mobile 50W | TX 50W | 12A | 13.8V | 166W | Short duty cycle |
| VHF mobile 25W | TX 25W | 7A | 13.8V | 97W | |
| Yaesu FT-60R HT | Receive | 0.14A | 7.4V | 1.0W | From USB charger at 5V: 0.2A |
| Yaesu FT-60R HT | TX 5W | 0.9A | 7.4V | 6.7W | |
| Starlink Gen3 | Operational | 3.6–5.4A | 14V equiv | 50–75W | Continuous; includes dish heater |
| Starlink Gen3 | Snow melt | 7A | 14V equiv | 100W | Intermittent |
| Garmin inReach | Standby | <0.05A | 3.7V Li-ion | <0.2W | |
| Garmin inReach | Transmitting | ~0.5A | 3.7V | ~1.8W | 12-second bursts |
| SDR + laptop | Receive | ~2A | 12V | 24W | Depends on laptop |
| NOAA weather radio | Receive | 0.1A | 5V USB | 0.5W | Leave on always |
| CB radio mobile | Receive | 0.5A | 13.8V | 7W | |
| CB radio mobile | TX 12W SSB | 3A | 13.8V | 41W | |

### 12.10.2 Daily Power Budget: Receive-Heavy Operation

Scenario: monitoring weather radio, shortwave, and GMRS receive-only;
HF net 30 minutes/day; no Starlink.

```
Device               Hours/day    Avg watts    Wh/day
-----------------    ---------    ---------    ------
NOAA weather radio   24           0.5          12
HF radio RX          4            21           84
HF radio TX (30min)  0.25         150          37.5
GMRS mobile RX       4            11           44
HF radio + GMRS      standby 8h   5            40
Total                                           217.5 Wh
```

At 12V nominal, this is ~18 Ah/day. A 100Ah LiFePO4 (80% usable = 80Ah)
provides 4 days without solar. A 200W solar panel in average US conditions
(4 peak sun hours) produces 800 Wh/day — more than enough.

### 12.10.3 Daily Power Budget: Active Operations + Starlink

Scenario: 2-hour HF net with digital modes, GMRS community net, Starlink
for weather data download daily, Garmin inReach standby.

```
Device               Hours/day    Avg watts    Wh/day
-----------------    ---------    ----------   ------
Starlink             6            65           390
HF radio RX          6            21           126
HF radio TX (1hr)    1            179          179
VHF mobile RX        8            11           88
GMRS mobile TX 15min 0.25         166          41.5
Laptop (digital)     2            30           60
Garmin inReach       24           0.2          4.8
Total                                           889 Wh
```

At 12V: ~74 Ah/day. Requires 400W+ solar array with 200+ Ah LiFePO4
battery for single-day autonomous operation.

### 12.10.4 Battery Recommendations

**Minimum**: 100Ah LiFePO4 (12V nominal; 80Ah usable) — sufficient for
receive-heavy comms without Starlink; ~$200–$300 for a quality 100Ah cell
(Battle Born, Epoch, Ampere Time, Chins).

**Recommended for Starlink + radio**: 200Ah LiFePO4 (160Ah usable) — two
days of full operation without solar; ~$350–$500 for quality cells.

**Charging**: A 20–40A MPPT charge controller from a 200–400W solar array
handles the communications battery independently of your house bank. This
isolation means a communications failure in your house system does not take
comms offline.

---

## 12.11 Legal Landscape

Operating radio equipment in the US requires understanding FCC rules.
This section covers the relevant legal framework. It is not legal advice.

### 12.11.1 FCC Part 97 (Amateur Radio)

Amateur radio is governed by FCC Part 97, which sets out the fundamental
principles of amateur operation:

1. Recognition and enhancement of the value of the amateur service
2. Continuation and extension of the amateur's proven ability to contribute
   to the advancement of the radio art
3. Encouragement and improvement of the amateur service in both the
   communications and technical phases thereof
4. Expansion of the reservoir within the amateur radio service of trained
   operators, technicians, and electronics experts
5. Continuation and extension of the amateur's unique ability to enhance
   international goodwill

**Key prohibitions:**
- No broadcasting to the general public (one-way transmissions intended
  for general public reception are prohibited except incidental)
- No commercial activity on amateur frequencies
- **No encryption on amateur bands**: You may not use codes or ciphers to
  obscure the meaning of communications. This conflicts with OPSEC goals.
  The solution: pre-agreed code words are in a gray area (they are not
  encryption by the technical definition), but do not push this too far.
- No obscene or indecent language
- No music (with narrow exceptions for identification purposes)

**Station identification**: Must identify with call sign at end of
communication and at 10-minute intervals during a communication. Digital
modes embed identification in the protocol.

**Third-party traffic**: You may pass messages for non-licensed third
parties (your neighbor who has no license) on domestic calls. International
third-party traffic is only allowed with countries that have third-party
agreements with the US.

**Emergency exception**: In genuine emergencies threatening life or property,
the FCC allows use of any means necessary, including any frequency. This
is explicit in Part 97.405: "No provision of these rules prevents the use
by an amateur station of any means of radiocommunication at its disposal to
provide essential communication needs in connection with the immediate safety
of human life and immediate protection of property when normal
communication systems are not available."

### 12.11.2 FCC Part 95 (GMRS, FRS, CB)

**GMRS (Part 95E):**
- License required: $35, 10-year, covers immediate family, no exam
- Only type-accepted GMRS radios may be used (not Baofeng UV-5R, regardless
  of whether you can program GMRS frequencies into it)
- Maximum power: 50W on main channels; 5W on interstitial channels
- Repeater operation: permitted for licensees

**FRS (Part 95B):**
- No license required
- Maximum power: 2W; built-in antenna only (no external antenna connector)
- Simplex only (no repeater use)
- Radios must be type-accepted for FRS

**MURS (Part 95J):**
- No license required
- 5 specific VHF frequencies only (151.820, 151.880, 151.940, 154.570, 154.600 MHz)
- Maximum power: 2W
- External antennas permitted but no repeater use

**CB (Part 95D):**
- No license required
- 40 channels only; 27 MHz range
- Maximum power: 4W AM, 12W SSB
- No antenna modifications that increase gain above specified limits

### 12.11.3 Encryption on Ham Bands

The prohibition on encryption in Part 97 means:
- Encrypted voice (scrambled, AES, etc.) is prohibited
- Encrypted digital modes are prohibited
- Data compression is allowed (Winlink uses compression; legal)
- Agreed code words are technically not "encryption" — they obscure
  the meaning but the signal itself is in plain language

If you need genuinely private communications, use non-amateur services:
satellite messengers (Garmin inReach, Iridium) or commercial encrypted
services over Starlink. Ham radio is inherently public in this regard.

---

## 12.12 CBRN Communications Protocols

### 12.12.1 Communications After a Nuclear Event

A nuclear event — particularly a high-altitude EMP — could destroy much
of your communications infrastructure simultaneously. Your first actions:

**Hour 0 — Assess damage:**
1. If you felt no blast effects (you are beyond the immediate blast radius),
   try to power up your Faraday-stored backup receiver
2. Attempt to tune WWV (5 or 10 MHz) — if WWV is still transmitting, the
   US national infrastructure is still partially functional
3. Attempt AM broadcast frequencies — any station still transmitting is
   a positive sign
4. Attempt NOAA Weather Radio (162.4–162.55 MHz) — NOAA's transmitters have
   substantial backup power and hardening

**Hour 1–24 — Information gathering:**
- Do not transmit until you have a clear picture of what is happening.
  Transmitting unnecessarily exposes your location.
- Monitor continuously on rotate: SW broadcast bands, 40m amateur (7.0–7.3 MHz),
  2m calling frequency (146.520 MHz simplex), NOAA, AM broadcast.
- Note which stations are active; correlate with known transmitter locations
  to estimate EMP coverage and geographic scope.

**Hour 24+ — Cautious operation:**
- Once you understand the situation, begin scheduled check-ins with your
  network using pre-established protocols
- Minimize transmission time
- Use lowest effective power

### 12.12.2 Radiation Monitoring via Radio

The FEMA IPAWS (Integrated Public Alert and Warning System) broadcasts
Emergency Alert System (EAS) messages over:
- NOAA Weather Radio (VHF; 162.4–162.55 MHz) — most reliable in emergencies
- AM/FM broadcast stations (required by FCC to relay EAS alerts)
- Starlink-connected internet services (if internet still functional)

For a nuclear event, the EAS will (if transmitters are functional) provide:
- Detonation location(s)
- Projected fallout corridors
- Shelter-in-place or evacuation instructions
- Radiation dosage projections

**Monitoring protocol**: Keep a battery-powered or hand-crank NOAA-capable
receiver running continuously during any suspected nuclear event period.
Sangean PR-D7 ($50) or Midland ER210 ($40) are hand-crank + battery receivers
suitable for this role.

### 12.12.3 Contamination Zones and Runner Protocols

In a radiological environment, runners carry information but may carry
contamination. Protocol:

**Before dispatch:**
- Dose runner with potassium iodide per protocol (if thyroid risk from I-131)
- Equip with N95 minimum; P100 preferred; goggles; disposable outer layer
- Equip with dosimeter (RADTriage badge or Geiger counter)
- Brief runner on decontamination procedure on return

**On return:**
- Runner stops at decontamination station (outdoors; do not enter shelter)
- Remove outer clothing in specific order (shoes first; never let outer
  surface touch inner surface); bag and seal
- Wash exposed skin and hair thoroughly with soap and water
  (not the contaminated runoff — ideally shower from stored clean water)
- Check dosimeter; log reading
- Report before entering shelter

**Communication discipline in contaminated zones:**
- Use radio instead of runners when possible (saves dose accumulation)
- Runners are a last resort when radio is unavailable
- Establish relay stations at boundaries of known contamination zones
  — runners go from clean zone to relay point; radio transmits beyond

### 12.12.4 Biocontamination Comms Discipline

In a biological emergency (pandemic-scale or deliberate release):

**Quarantine boundaries use radio, not runners:**
- Communities under quarantine communicate with neighboring communities
  exclusively by radio during acute phase
- No physical exchange of materials or persons without decontamination protocol
- Welfare check-ins daily via radio replace in-person visits

**Information discipline:**
- False or panicked information on radio nets can cause deadly wrong decisions.
  Develop a protocol: all reports of disease or contamination carry a
  "confirmed/unconfirmed" status word.
- "Unconfirmed: illness reported at the Miller homestead" is different from
  "Confirmed: flu-like illness in 3 persons, onset 36h ago, symptoms A/B/C."
- Designate one person in your community as the medical information officer —
  the only person who reports health status on the air; prevents multiple
  conflicting reports.

**Operational security in hostile scenarios:**
- In a scenario involving deliberate attack (bioterrorism, civil conflict),
  broadcasting detailed information about your community's health status,
  population, or resources can provide tactical advantage to adversaries.
- Monitor; receive; share within your trust network. Do not broadcast to unknown parties.

---

## 12.13 Starter Kit Decision Matrix

Practical recommendations by scenario and budget. Prices are 2025–2026 USD.

| Scenario | Budget | Radios | Antenna | Power | Satellite | Priority |
|---|---|---|---|---|---|---|
| Solo homesteader, basic | $200 | FRS/GMRS pair HT ($50) + NOAA weather radio ($25) | Internal/rubber duck | AA batteries + USB power bank | None | NOAA radio first; GMRS for local ops |
| Solo homesteader, step-up | $500 | GMRS license ($35) + Midland MXT500 mobile ($200) + Tecsun PL-880 SW receiver ($95) | Mobile whip + longwire for SW ($30) | Vehicle + 20Ah LiPo bank ($60) | Garmin inReach Mini 2 ($350 — slight overage) | License + mobile GMRS is biggest capability jump |
| Family homestead, core | $1,000 | Ham Technician × 2 ($30 fees) + Yaesu FT-60R HTs × 4 ($550) + GMRS license ($35) + Midland MXT500 ($200) | J-pole 2m ($25) + mobile whip | 100Ah LiFePO4 + 200W solar ($400, separate from house bank) | None yet | VHF coverage + GMRS mobile for range |
| Family homestead, capable | $2,500 | Above + General license ($15) + Xiegu G90 HF ($400) + Tecsun PL-880 ($95) | G5RV or end-fed HF wire ($100) + existing VHF | Same bank; add 100W solar ($100) | Garmin inReach Mini ($360) | HF adds regional/national reach; inReach is emergency backup |
| Remote retreat, serious | $5,000+ | Ham General + Icom IC-7300 ($1,000) + Yaesu FT-991A or VHF mobile ($250) + Faraday kit with Baofeng spares ($80) | HF vertical + dipole + 2m/70cm Yagi ($350) | 200Ah LiFePO4 + 400W solar dedicated ($700) | Starlink ($599 hardware + $120/mo) + Garmin inReach ($360) | IC-7300 is the centerpiece; Starlink for normal ops; HF for backup |
| Community hub (5+ households) | $8,000+ | Everything above + AREDN mesh nodes × 4 ($600) + GMRS repeater setup ($600) + Winlink station ($200) | Repeater antenna + tower ($1,000) | Dedicated 400Ah bank + 600W solar ($1,200) | Starlink + Iridium backup ($900 device + $60/mo) | Repeater extends everyone's range; AREDN enables data |
| Mobile/nomadic | $1,500 | Ham Technician + Yaesu FT-60R HT ($140) + Icom IC-705 portable HF ($1,300) | Portable EFHW or vertical whip | 50Ah LiFePO4 portable ($150) + vehicle charging | Garmin inReach Mini 2 ($360) | IC-705 integrates HF + VHF in portable package |
| CBRN prep focus | $3,000 | Ham General + Xiegu G90 (Faraday stored) + Tecsun PL-880 (Faraday stored) + Garmin inReach (Faraday stored) + tube SW receiver | Portable EFHW wire (Faraday stored) | 100Ah LiFePO4 + 300W solar + spare MPPT controller (Faraday stored) | Garmin inReach; no Starlink for this tier (EMP vulnerable) | Faraday-stored spares are the core; primary kit adds active capability |

---

## 12.14 Cost Table

All prices 2025–2026 USD; used prices noted where typical.

| Item | Purpose | Approx. Cost | Notes |
|---|---|---|---|
| **Licensing** | | | |
| FCC GMRS license | Family GMRS ops, 10 years | $35 | Covers immediate family; no exam |
| Ham Technician exam fee | VHF/UHF license | $15 | Through ARRL/W5YI VE session |
| Ham General exam fee | HF license | $15 | Can take same day as Tech |
| ARRL Ham Radio License Manual (Tech) | Study guide | $30 | One-stop reference |
| **HF Transceivers** | | | |
| Icom IC-7300 | Primary HF desktop transceiver | $950–$1,050 | Best value HF radio |
| Yaesu FT-991A | All-band HF/VHF/UHF desktop | $1,100–$1,200 | Good consolidation option |
| Yaesu FT-891 | Compact 100W HF mobile | $500–$560 | Best for vehicle/portable 100W HF |
| Xiegu G90 | Budget 20W portable HF | $380–$420 | Built-in tuner; excellent value |
| Xiegu X6100 | Battery-integrated portable HF | $550–$600 | Field radio; 10W |
| **VHF/UHF Radios** | | | |
| Yaesu FT-60R | 2m/70cm handheld | $130–$150 | Top recommendation for durability |
| Yaesu VX-6R | 2m/70cm/6m HT; waterproof | $200–$230 | Field-hardened; 3-band |
| Baofeng UV-5R | Budget 2m/70cm HT | $25–$35 | Spare; Faraday cage; not for primary |
| AnyTone AT-D878UV | 2m/70cm; DMR digital + analog | $120–$140 | Good for digital modes |
| Yaesu FT-7900R | 2m/70cm mobile; 50W | $180–$210 | Base/vehicle; solid choice |
| Kenwood TM-V71A | 2m/70cm mobile; APRS | $280–$320 | APRS integrated; excellent receiver |
| **GMRS Radios** | | | |
| Wouxun KG-1000G | Full-power GMRS HT; 10W | $170–$200 | Best GMRS HT; recommended |
| Midland MXT500 | 50W GMRS mobile | $180–$220 | Primary base/vehicle GMRS |
| Midland GXT1000VP4 | GMRS HT pair | $55–$70 | Budget family starter |
| **CB Radios** | | | |
| Cobra 29 LTD | Mobile CB; AM/SSB | $70–$90 | Benchmark CB |
| Uniden PRO510XL | Budget mobile CB | $35–$50 | No SSB; basic |
| **Shortwave Receivers** | | | |
| Tecsun PL-880 | Portable SW/SSB receiver | $85–$100 | Best portable for price |
| Sangean ATS-909X2 | Portable; serious SWL | $160–$180 | Better than PL-880; higher cost |
| RTL-SDR V4 dongle | SDR receiver (needs computer) | $35–$45 | Extraordinary flexibility |
| SDRPlay RSP1C | Better SDR receiver | $130–$150 | 1 kHz–2 GHz; outstanding |
| **Satellite Comms** | | | |
| Starlink Gen3 dish + router | Broadband internet | $599 | One-time hardware |
| Starlink Residential monthly | Broadband service | $120/month | Ongoing |
| Garmin inReach Mini 2 | Satellite messenger + SOS | $350–$400 | Best value satellite device |
| Garmin inReach Explorer+ | Satellite messenger + GPS/compass | $450–$500 | Added navigation tools |
| Iridium 9555 (used) | Satellite voice phone | $700–$900 used | True SHTF voice backup |
| Iridium Extreme (new) | Ruggedized sat phone | $1,200–$1,600 | Military-grade; SOS built-in |
| **Antennas** | | | |
| 40m dipole (DIY) | HF regional/DX | $60–$100 materials | 65 ft wire + feedline + insulators |
| Hustler 6-BTV | HF multiband vertical | $200–$230 | 6 bands; good for limited space |
| DX Commander clone/build | HF vertical multi-band | $100–$200 | DIY or kit; excellent performer |
| Arrow Antenna dual-band Yagi | 2m/70cm portable Yagi | $45–$75 | Satellite/portable use |
| 2m J-pole (DIY copper pipe) | 2m omnidirectional base | $15–$25 materials | Easy to build; solid performer |
| VHF/UHF mobile whip (Tram 1185) | 2m/70cm vehicle/base | $25–$35 | Reliable; affordable |
| CB magnetic mount antenna | CB mobile use | $25–$45 | Firestik FS-4 or Wilson |
| **Feedline and Connectors** | | | |
| LMR-400 coax (per 50 ft) | Low-loss VHF/UHF feedline | $35–$55 | Do not cheap out here |
| RG-213 coax (per 100 ft) | HF feedline | $30–$50 | Adequate for HF lengths |
| PL-259 connectors (10-pack) | Coax connector (SO-239 mate) | $12–$20 | Use silver-plated; solder type |
| Coaxial lightning arrestor | Antenna surge protection | $15–$50 | PolyPhaser or Alpha Delta |
| **Power Supply and Battery** | | | |
| 13.8V DC regulated supply (30A) | Bench power for radios | $50–$90 | Samlex, Pyramid, Powerwerx |
| 100Ah LiFePO4 battery | Radio comms power bank | $180–$280 | Battle Born, Epoch, Ampere Time |
| 200Ah LiFePO4 battery | Larger radio + Starlink bank | $320–$480 | Same brands |
| 20A MPPT charge controller | Solar charging for radio bank | $35–$60 | Renogy, Victron SmartSolar |
| 200W solar panel | Power input for comms bank | $80–$120 | Generic monocrystalline |
| **Digital Mode Equipment** | | | |
| Signalink USB | Audio interface for digital modes | $110–$130 | Works with any radio |
| VARA HF license | Digital mode software license | $69 one-time | Optional but recommended |
| Raspberry Pi 4 (4GB) | Headless digital mode computer | $55–$70 | JS8Call, Winlink, WSJT-X |
| **EMP / Faraday** | | | |
| 20-gallon galvanized garbage can | Faraday outer cage | $25–$40 | With tight-fitting lid |
| .50 cal ammo can | Faraday inner container | $20–$35 | Seal with copper tape |
| Aluminum HVAC tape | Faraday lid seal | $8–$12 | 3M 3311 or similar |
| Copper conductive tape | Lid rim seal for ammo cans | $10–$18 | Better conductivity than foil tape |
| Anti-static bags (variety pack) | Device wrapping inside cage | $12–$20 | Pink anti-static; not regular plastic |
| **Meshtastic / Mesh** | | | |
| LILYGO T-Beam | Meshtastic LoRa node | $35–$45 | Solar + battery option available |
| Heltec LoRa V3 | Meshtastic compact node | $25–$35 | No GPS; good fixed node |
| **Miscellaneous** | | | |
| NOAA Weather Radio (Midland WR300) | Receive-only weather alerts | $30–$40 | SAME alerts; battery backup |
| Hand-crank emergency radio (Midland ER210) | Battery + crank; AM/FM/NOAA | $35–$50 | Power-out survival radio |
| SWR/power meter (Comet CM-330) | Antenna tuning, monitoring | $50–$70 | Essential for HF antenna work |
| Antenna analyzer (NanoVNA H4) | Antenna impedance + SWR | $50–$80 | Game-changer for DIY antennas |
| Morse code key (straight key) | CW operating; EMP-resistant mode | $20–$60 | Kent, Begali; used for CW practice |
| RADTriage 50 badge | Radiation dose monitoring | $25–$35 | 10-pack available; store in Faraday |
| Potassium iodide tablets (130mg) | Thyroid protection: nuclear events | $10–$20 for 14 tablets | IOSAT or ThyroShield; check expiry |
| Log book | Net log; frequency record | $8–$15 | Waterproof preferred |

**Total cost estimates by tier:**
- Basic (NOAA + FRS/GMRS): $100–$200
- Starter homestead kit: $400–$700
- Capable homestead (ham Technician + GMRS + SW): $800–$1,500
- Serious off-grid station (ham General + HF + satellite): $2,500–$4,500
- Full community hub with mesh, repeater, Starlink: $8,000–$15,000

---

## 12.15 Skills and Training

Equipment does not operate itself. The gap between owning a radio and being
effective during an emergency is significant and must be closed before the
emergency.

### 12.15.1 License Study Roadmap

**Technician Class**
- Study time: 10–20 hours for most adults
- Resources: HamStudy.org (free adaptive flashcards); ARRL Tech Manual ($30);
  YouTube: Ham Radio Crash Course, David Casler KE0OG
- Question pool: 423 questions; 35 on the exam; must score 26+ correct
- Topics: basic electronics, radio regulations (Part 97), VHF/UHF
  propagation, safety, operating procedures
- Find exam: arrl.org/find-an-amateur-radio-license-exam-session
  Most clubs run monthly exam sessions; cost $15
- Time from decision to license: 2–4 weeks if motivated

**General Class**
- Additional study time: 1–3 weeks
- Can be taken same day as Technician (take Tech first; if you pass, take General immediately)
- Question pool: 462 questions; 35 on exam; must score 26+ correct
- Additional topics: HF propagation, more FCC regulations, HF operating procedures,
  more advanced electronics
- This is the priority upgrade. Do it within your first year of licensing.

**Amateur Extra Class**
- Study time: 4–8 weeks of dedicated study
- 50 questions; must score 37+ correct
- Topics: advanced electronics, filter theory, propagation, advanced operating
- Benefit for off-grid: opens lower (less congested) phone subbands on HF;
  additional international privileges; prestige in the amateur community
- Not strictly necessary for off-grid preparedness

### 12.15.2 Practical Operating Skills

**Net operations**: Joining and running an HF or VHF net is a skill distinct
from just owning a radio. Practice by joining your local ARES or NTS net
weekly. Topics to master:
- Proper net check-in procedure
- Handling formal traffic (radiogram format)
- Running net control: managing the roster, managing the queue, handling
  out-of-sequence traffic
- Emergency traffic priority: how to interrupt a net for urgent traffic

**Antenna tuning**: Using an SWR meter or antenna analyzer to cut a dipole
to resonance and achieve SWR below 1.5:1. Practice before you need it.

**Emergency activation**: Simulated emergency tests (SETs) run by ARES
annually. Participate in at least one before a real event.

**HF operating**: HF radio is not intuitive if you have only used VHF/UHF.
Practice:
- Band selection based on time of day and distance
- Understanding propagation reports (solar flux index > 150 is good for HF DX;
  K-index below 3 means quiet geomagnetic conditions)
- SSB voice procedure: phonetic alphabet, signal reports (RST: Readability
  1–5, Signal strength 1–9, Tone 1–9 for CW)

### 12.15.3 Digital Mode Setup

**WSJT-X for FT8:**
1. Install WSJT-X on any Windows/Mac/Linux computer
2. Connect radio to computer via USB (IC-7300 requires only USB cable;
   older radios need Signalink USB audio interface)
3. Set WSJT-X to your radio model; configure audio input/output
4. Synchronize computer clock to within 2 seconds of UTC (critical for FT8;
   use internet time sync or WWV)
5. Tune to 7.074 MHz (40m FT8 calling frequency) or 14.074 MHz (20m)
6. Watch the waterfall; decode signals; you are now receiving FT8
7. Transmit: log on to LoTW or HamStudy to confirm your signal is heard

**JS8Call for grid-down messaging:**
1. Install JS8Call (js8call.com)
2. Same audio interface as WSJT-X
3. Configure: your call sign, grid square, heartbeat interval (default 15 min)
4. Primary frequencies: 7.078 MHz (40m) and 14.078 MHz (20m)
5. Practice: send messages to known contacts; experiment with relay (a message
   bounced through 2–3 intermediate stations to reach a distant destination)
6. Create a JS8Call "group" for your community network

**Winlink setup:**
1. Install Winlink Express (winlink.org)
2. Register for a Winlink account (tied to your call sign)
3. Configure Winlink Express for VARA HF (recommended; $0 evaluation,
   $69 for full version removes speed limits)
4. Connect radio and audio interface
5. Practice: send a test message to yourself via Winlink; receive it as email
6. Test P2P (peer-to-peer) with a neighbor for true off-network testing

### 12.15.4 Skill Acquisition Timeline

| Skill | Time to basic competence | Learning path | Notes |
|---|---|---|---|
| Ham Technician license | 2–4 weeks | HamStudy.org + exam | Do this first |
| Basic VHF/UHF ops | 1–2 weeks practice | Use the radio daily; join nets | Immediate after license |
| Antenna building (simple dipole/J-pole) | 1 weekend | ARRL Antenna Book + hands-on | Low cost; high reward |
| Ham General license | 4–8 weeks after Tech | HamStudy.org General pool | Priority upgrade |
| HF voice operations | 2–4 weeks practice | Tune 40m/20m; call CQ; join net | |
| FT8 digital mode | 1–3 hours to first QSO | WSJT-X setup guide; YouTube | Surprisingly easy once set up |
| JS8Call grid-down messaging | 2–4 hours to functional | js8call.com documentation | Practice with known contact |
| Winlink radio email | 4–8 hours | Winlink.org tutorials | Test P2P mode specifically |
| Net control operations | 2–4 runs as shadow | Volunteer with local ARES net | Practice makes comfortable |
| AREDN mesh networking | 2–4 days | arednmesh.org documentation | Technical; rewarding |
| Meshtastic node setup | 2–4 hours | meshtastic.org | Hardware setup + app config |
| EMP/Faraday cage construction | 4–8 hours | This guide + practice | Build it; then store gear |
| Morse code (CW) 5 WPM | 4–8 weeks daily practice | LCWO.net (Koch method) | Optional but remarkable skill |

### 12.15.5 The Skill-Building Path in Sequence

1. **Week 1–2**: Get GMRS license ($35); program GMRS radios; test with family
2. **Week 2–4**: Study and test for Technician ham license; get on the air
3. **Month 1–2**: Join local VHF/UHF nets; practice operating procedures
4. **Month 2–4**: Study and test for General; buy or build HF radio + antenna
5. **Month 4–6**: First HF contacts; join regional 40m net; practice daily
6. **Month 6–9**: Set up digital modes (FT8, JS8Call, Winlink); test P2P
7. **Month 9–12**: Assemble Faraday kit; build emergency contact tree; conduct
   a community practice drill (comms-out scenario)
8. **Year 2**: Consider AREDN mesh for community; Meshtastic nodes; expand
   antenna system

The amateur radio community is broadly helpful to newcomers. Your local
ham club almost certainly runs an Elmer program (mentoring new operators).
A few hours with an experienced ham will compress months of self-study.
Find local clubs at arrl.org/find-an-amateur-radio-club.

---

## Cross-References

- **[06-energy-power.md]**: Solar sizing for communications power budget;
  battery bank design; charge controller selection
- **[08-medical-health.md]**: Medical information distribution via radio;
  Winlink for medical consultation; CBRN health protocols
- **[11-shelter-construction.md]**: Antenna mounting on structure; Faraday
  cage integration; underground shelter comms penetrations; CBRN hardened
  shelter comms
- **[13-community-organization.md]**: Community radio net structure; net control
  rotation; information sharing protocols
- **[15-disaster-scenarios.md]**: EMP scenario planning; nuclear event
  communications; extended grid-down operations; communication hierarchy
  during societal disruption

---

*Prices in this document are 2025–2026 US market prices. Radio equipment
pricing is relatively stable but does fluctuate. Verify current prices at
time of purchase. Used equipment — available at hamfests (hamfests.com for
location finder), QRZ.com classifieds, and eHam.net — can reduce costs by
30–60% for many items.*
