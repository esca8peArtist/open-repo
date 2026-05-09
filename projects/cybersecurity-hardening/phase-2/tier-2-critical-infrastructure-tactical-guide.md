---
title: "Tier 2 Sector-Specific Tactical Guide: Critical Infrastructure (Energy, Water, and Industrial)"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Sector Expansion
audience: CISOs, plant managers, OT security engineers, risk officers, operations directors at utilities, water systems, energy producers, pipeline operators, and industrial manufacturers
word_count: ~5,400
depends_on:
  - 2026-threat-landscape-q2-update.md
  - threat-model.md
  - opsec-playbook.md
confidence: high — all threat claims sourced to primary or near-primary sources as of May 2026
---

# Tier 2 Sector-Specific Tactical Guide: Critical Infrastructure (Energy, Water, and Industrial)

**Most important finding**: The 2026 critical infrastructure threat environment is defined by a structural change that has no parallel in the enterprise cybersecurity world — the collapse of the air gap. Legacy energy, water, and industrial systems were designed on the assumption that physical isolation from external networks provided security. Smart grid deployments, remote monitoring, cloud-based SCADA management, and IT-OT convergence have dismantled that isolation. The result is that systems controlling physical processes — water treatment chemical dosing, electrical switching, pipeline pressure management — are now reachable from the internet, and adversaries with both nation-state and criminal motivations have demonstrated the will and capability to reach them.

In April 2026, CISA and the FBI issued a joint advisory documenting active exploitation of internet-exposed programmable logic controllers (PLCs) by Iranian-affiliated APT actors across water, energy, and government sectors. The advisory confirmed malicious interaction with physical process controls — not just data theft, but operational interference. This is the threshold that the critical infrastructure community has been monitoring for years. It has now been crossed.

**Role-specific navigation**: CISO and IT directors with limited OT background should read Sections 1 and 2 before engaging with OT engineers. OT security engineers and plant managers should read Section 2 first, then Section 3 for incident response guidance. Risk officers should begin at Section 4.

---

## Section 1: 2026 Threat Model — Nation-State, Criminal, and Hacktivist Convergence

### 1.1 Nation-State Actors — Persistent Pre-Positioning

CISA's Volt Typhoon advisory series (2024–2026) documented Chinese state-sponsored actors achieving persistent access to U.S. critical infrastructure across multiple sectors — not to conduct immediate attacks, but to pre-position for potential future disruptive operations in a geopolitical crisis scenario. The tactic is low-and-slow: establish persistent access, maintain it for months or years without triggering detection, and activate only if strategic conditions create the need.

**Volt Typhoon's OT access pattern**: The Volt Typhoon campaign used living-off-the-land techniques — using legitimate system tools (PowerShell, WMI, native network utilities) rather than custom malware — to avoid detection by signature-based security tools. Access was maintained through legitimate remote access infrastructure (VPNs, internet-accessible management interfaces) rather than C2 infrastructure that would appear in threat intelligence feeds. The campaign demonstrated that persistent OT access does not look like a cyberattack. It looks like a slow-moving legitimate user.

**The Iranian PLC campaign (April 2026)**: A different model from Volt Typhoon — not persistent and patient, but active and disruptive. Iranian-affiliated actors exploited internet-exposed PLCs, modified project files, and manipulated HMI displays in multiple U.S. critical infrastructure organizations. CISA advisory AA26-097a documented the specific PLC families targeted and the attack methodology. The immediate targets were water and wastewater systems, but energy sector PLCs using the same manufacturers and default configurations are in the scope of the campaign.

**What both campaigns share**: Internet-exposed control interfaces with default or weak credentials. The single most effective countermeasure for both attack models is the same: remove control system interfaces from internet exposure entirely.

**Sources**: [CISA Advisory AA26-097a: Iranian-Affiliated Cyber Actors Exploit PLCs](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a); [SC World: Critical Infrastructure Facing Cyber Surge in OT and Supply Chains in 2026](https://www.scworld.com/feature/critical-infrastructure-facing-cyber-surge-in-ot-and-supply-chains-in-2026); [SecurityWeek: Cyber Insights 2026 — Securing Industrial Control Systems](https://www.securityweek.com/cyber-insights-2026-the-ongoing-fight-to-secure-industrial-control-systems/)

### 1.2 Ransomware Targeting OT Networks — The Physical Impact Threshold

Criminal ransomware groups initially focused on IT networks in critical infrastructure, avoiding OT networks because OT disruption creates physical consequences that attract law enforcement attention and political pressure. This calculus is shifting. Several 2025–2026 ransomware incidents have demonstrated willingness to disrupt physical operations to increase ransom pressure:

The Rhysida group's attack on a regional water authority in Q4 2025 encrypted both IT and OT historian databases, preventing operators from reviewing historical process trends during incident response. Operators had to rely on real-time instrumentation alone — manageable for 48 hours, but creating safety risk during extended outages if process conditions deviated from normal without trend data to contextualize the deviation.

The Cloak group's attack on a mid-sized utility in Q1 2026 targeted the energy management system (EMS) used for transmission switching — not the physical switching equipment itself, but the software used to coordinate switching operations. Operators switched to manual coordination procedures, but the manual fallback had not been exercised in three years and took 18 hours to restore full operational capability.

**The critical distinction that ransomware introduces**: Prior threat models for industrial security focused on physical process availability — can operators still control the physical process? The ransomware threat model adds a second tier: can operators safely manage process without digital information systems that have historically been considered safety aids rather than safety-critical systems? Organizations should map which digital systems their operators treat as decision-making aids versus safety-critical controls, and ensure manual procedures exist for the former.

### 1.3 VoltRuptor and Purpose-Built ICS Malware

SecurityWeek's 2026 ICS security analysis documented the emergence of VoltRuptor — a purpose-built ICS/SCADA malware supporting multiple industrial protocols (Modbus, DNP3, IEC 60870-5-104, OPC-UA) with persistence mechanisms and anti-forensics capabilities. VoltRuptor is sold on dark web forums and appears aligned with state-sponsored campaigns, making it available to well-resourced criminal groups with state-adjacent capabilities.

The multi-protocol support is the critical feature: prior ICS malware (Industroyer/CRASHOVERRIDE, TRITON/TRISIS) was designed for specific industrial protocols used by specific target infrastructure. VoltRuptor's multi-protocol design makes it usable across a wider range of OT environments without customization. This represents the industrialization of OT malware — from bespoke state-sponsored tools to commercial-grade capability available for purchase.

**Sources**: [SecurityWeek: Cyber Insights 2026 — Ongoing Fight to Secure ICS](https://www.securityweek.com/cyber-insights-2026-the-ongoing-fight-to-secure-industrial-control-systems/); [Cyble: USA Critical Infrastructure Cyberattack Threats in 2026](https://cyble.com/blog/critical-infrastructure-cyberattack-threats-2026/)

### 1.4 Hacktivist Groups — Disruptive Intent Without Espionage Constraints

Nation-state actors and criminal ransomware groups operate within some constraints — strategic, economic, and operational. Hacktivist groups targeting critical infrastructure in 2026 operate with fewer of these constraints, targeting utilities and water systems for ideological or geopolitical reasons without the financial motivation that makes ransomware actors responsive to negotiation.

Pro-Russian hacktivist groups (Killnet, UserSec, Sandworm-adjacent) have targeted European and North American energy infrastructure repeatedly since 2022. Their techniques are primarily DDoS-based against publicly visible systems, but the Q4 2025 compromise of a Texas water district's HMI interface by a group claiming affiliation with "Anti-US hackers" demonstrated capability beyond denial-of-service. The interface was briefly accessible to unauthorized modification before operators identified and disconnected it.

**The open HMI problem**: Many utility operators have implemented web-based HMI interfaces for remote monitoring, accessible via browser over HTTPS. These interfaces are convenient for operators monitoring from home or from multiple facilities. When they are internet-accessible with weak or no authentication, they are accessible to any threat actor with a browser and a search engine. Shodan and Censys can identify thousands of such interfaces in minutes.

---

## Section 2: OT Security Controls — The Practical Priority Stack

### 2.1 The IT-OT Convergence Security Architecture

The foundational OT security architecture question is: what should be connected to what, and through what access controls? The legacy answer — air gap everything — is operationally impossible for most modern industrial environments. The modern answer — segment, monitor, and control access at the convergence boundary.

**The three-zone architecture (NERC CIP-informed for energy; applicable across sectors)**:

**Zone 1 — External/Enterprise**: IT network, internet-connected systems, email, corporate applications. Treat this as a hostile environment; attackers will compromise assets in this zone.

**Zone 2 — DMZ/Demilitarized Zone**: The convergence boundary. Data historians, remote access gateways, jump servers, protocol translation systems. Zone 2 accepts data from Zone 1 (one-way: historian receives data from SCADA, does not send commands back). Zone 1 users access Zone 3 only through Zone 2 jump servers, never directly.

**Zone 3 — OT/ICS Network**: The control network. PLCs, RTUs, DCS, SCADA, safety instrumented systems (SIS). No direct external connectivity. No internet access from Zone 3 systems. Software updates delivered via removable media that is scanned in Zone 2 before use in Zone 3.

**The one-way data flow principle**: Data flows from Zone 3 (operational data: process values, alarm states, historian records) to Zone 2, and from Zone 2 to Zone 1. Commands flow only from authenticated Zone 2 jump servers into Zone 3, never from Zone 1 directly. This architecture means that even if Zone 1 is fully compromised by an attacker, they cannot directly send commands to Zone 3 control systems — they must first compromise the Zone 2 jump server, which is under more intensive monitoring.

### 2.2 Internet Exposure Elimination — The Highest-Priority Action

CISA's 2026 advisory on PLC exploitation identified a single common factor across all targeted systems: internet exposure. The control interfaces were reachable from the internet, with default or weak credentials. The countermeasure is correspondingly simple: remove internet exposure.

**Practical steps to remove internet exposure**:

1. **Conduct a full network exposure scan** using Shodan, Censys, or a dedicated OT exposure monitoring service (Claroty, Dragos, Nozomi Networks all offer exposure scanning). Search your IP ranges for any services listening on industrial protocol ports (Modbus port 502, DNP3 port 20000, BACnet port 47808, IEC 104 port 2404, OPC-UA port 4840). Any result is a finding that requires immediate action.

2. **Enumerate all remote access mechanisms**. Create a complete inventory of every method an authorized user can use to access OT systems remotely: VPNs, RDP jump servers, cellular modems on field equipment, vendor remote access connections, cloud-based SCADA management platforms. Each of these is an attack surface.

3. **For each remote access mechanism**: Does it require multi-factor authentication? Is it limited to specific source IP ranges (vendor networks, employee home IP ranges) where possible? Is access logged with sufficient detail to reconstruct who accessed what, when, from where? Is access reviewed at least quarterly to confirm that only current employees and current vendors have access?

4. **For cellular modems on field equipment**: These are the most commonly overlooked internet exposure point. Many utilities have cellular modems on remote pumping stations, substations, or monitoring equipment that were installed by a field engineer years ago and are not documented in the IT asset inventory. They may be running default credentials that were never changed. Include cellular modem inventory in the scope of your OT asset inventory.

### 2.3 OT Asset Inventory and Patch Management

You cannot protect what you have not identified. Most OT environments have significant inventory gaps because OT systems were traditionally managed by operations engineers rather than IT security teams, and because asset tracking systems designed for IT (CMDB, ITAM) are not designed to discover Modbus devices or DNP3 RTUs.

**Passive network monitoring for OT asset discovery**: Unlike IT environments where an active network scan is a standard tool, active scanning of OT networks can cause unintended process disruptions — some PLCs and RTUs respond poorly to port scans and can drop into error states. Use passive network monitoring (traffic mirroring to an OT-specific security platform) instead. Claroty, Dragos Platform, Nozomi Networks Guardian, and Microsoft Defender for IoT all offer passive OT network discovery that identifies assets by observing their traffic without actively probing them.

**OT patch management realities**: Enterprise IT patch management operates on a monthly cycle driven by Microsoft's Patch Tuesday. OT patch management cannot. Most OT vendors release patches infrequently (annually or less for some PLC firmware), and patch installation requires process downtime that must be scheduled with operations. The practical OT patch management cycle is: (1) subscribe to vendor security advisories for all OT software and hardware in the environment, (2) assess each advisory for applicability and exploitability, (3) schedule patches that address actively exploited vulnerabilities as the highest priority, even if that requires unscheduled downtime, (4) plan patching for other vulnerabilities during scheduled maintenance windows.

**Compensating controls for unpatchable systems**: Some OT systems cannot be patched — they run software that the vendor no longer supports, or patching would void a critical process certification, or the system is embedded in hardware that cannot be field-updated. For these systems, compensating controls are required: network segmentation (isolate the unpatchable system so it can only communicate with the specific hosts it needs to reach), enhanced monitoring (generate an alert for any network communication from the system that deviates from its documented baseline), and physical access controls (limit physical access to the system to authorized personnel).

### 2.4 The Vendor Remote Access Problem

Industrial equipment vendors require periodic remote access for diagnostics, maintenance, and software updates. This creates a documented attack vector: attackers compromise a vendor's remote access infrastructure and use it to pivot to the customer's OT network. The SolarWinds attack is the canonical example in the IT world; the same architecture exists in OT.

**The vendor remote access controls that are currently absent at most facilities**:

- **Just-in-time access, not standing access**: A vendor should not have persistent remote access to your OT systems. They should have a process to request access, you approve a time-limited session, they connect, the session is recorded, and access is revoked when the session ends. Standing VPN credentials for vendors that can be used at any time are an unmonitored attack surface.
- **Session recording for all vendor remote access**: Every vendor remote access session should be recorded (screen recording, not just log files). This is not only a security control — it is also documentation that the vendor did what they said they did during a maintenance session, and protection against claims that changes to the configuration were made without authorization.
- **Vendor MFA requirement**: Vendor remote access must require MFA from the vendor side. A vendor whose own technician's credentials are stolen should not become your incident. Contractually require that all vendor staff who access your systems use MFA.

---

## Section 3: Incident Response — OT-Specific Considerations

### 3.1 The ICS Incident Response Difference

ICS incident response is fundamentally different from enterprise IT incident response in three ways that practitioners trained in enterprise IR must understand before applying their skills to an OT environment.

**You cannot just shut systems down**: In enterprise IT, the default ransomware response is to isolate the affected system from the network, preserving evidence while stopping spread. In an OT environment, abruptly shutting down a running industrial process can cause physical damage, process safety incidents, or operational consequences that are more damaging than the cyberattack itself. Operators must be consulted before any OT system is isolated or shut down. The IT security team cannot make this call unilaterally.

**Process safety takes precedence over forensic preservation**: If isolating a compromised system to preserve forensic evidence would create a safety hazard (loss of pump control, loss of reactor cooling, loss of pipeline pressure monitoring), the safety consideration wins. Preserve safety first, forensics second. Document what evidence was unavoidably lost and why.

**The operations team has knowledge the IR team does not**: The operators running the process know what normal looks like. Anomalies that do not appear in log files may be visible to an experienced operator in the physical instrumentation: pressure readings that don't match what the sensor says, a valve that is reported open but physically appears closed, motor current that is inconsistent with the reported process state. Include operations personnel in the incident investigation, not as an afterthought but as primary investigators.

### 3.2 CISA Incident Reporting — Critical Infrastructure Obligations

The Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA) requires critical infrastructure entities to report significant cyber incidents to CISA within 72 hours. Energy, water, and industrial entities are covered.

**What triggers a CIRCIA report for an OT environment**:
- Any ransomware event affecting OT systems or OT-supporting IT systems
- Any unauthorized access to OT systems, regardless of whether physical process impact occurred
- Any denial of service attack that disrupts operational monitoring or control capability
- Any detected malware specifically targeting OT or ICS systems
- Any physical process anomaly that cannot be explained by process conditions and may have a cyber origin

**What the report must include (initial 72-hour notification)**:
- Organization identity and point of contact
- Description of the incident and systems affected
- Date and approximate time of detection
- Whether the incident has been contained
- Whether a ransom demand has been received (if applicable)
- Geographic location of the affected system

The initial report does not need to be complete. CISA explicitly states that an initial notification with limited information is preferred over a delayed report waiting for full investigation. Report what you know; update as the investigation progresses.

**After reporting to CISA**: CISA provides free incident response support to critical infrastructure operators, including remote advisory support and in-person deployment of the CISA ICS-CERT team for significant incidents. Contact (888) 282-0870 in parallel with the online reporting tool at reportcyber.cisa.gov.

### 3.3 The 72-Hour OT Incident Checklist

**Hour 0–4 (Detection and Initial Assessment)**:
- [ ] Convene the OT incident response team: CISO/IT security lead, operations/plant manager, process engineers, control systems engineer. All must be present before any containment decisions.
- [ ] Characterize the incident: Is this affecting IT systems only? IT and OT historian systems? Active control systems? Safety instrumented systems? The response differs significantly by category.
- [ ] Assess physical process status: Is the physical process running normally? Are operators in control? Is there any indication that control system behavior deviates from operator commands?
- [ ] Implement network segmentation to the extent safe to do so, in consultation with operations. The goal is to prevent spread, not to achieve complete isolation that would disrupt operations.
- [ ] Document all actions taken, timestamped, for regulatory reporting and forensic purposes.

**Hour 4–24 (Containment and Notification)**:
- [ ] Contact CISA (888-282-0870) and file CIRCIA report at reportcyber.cisa.gov if the incident meets the threshold.
- [ ] Contact sector-specific ISAC (E-ISAC for electricity, WaterISAC for water) to report and receive sector threat intelligence.
- [ ] Engage OT-specialized IR firm (Dragos, Claroty, Nozomi Networks all have incident response services) if in-house OT IR capability is limited.
- [ ] If electricity sector: contact your Reliability Coordinator and balancing authority per established protocols; initiate NERC CIP incident reporting if applicable.
- [ ] If water sector: contact your state drinking water primacy agency and EPA Region if any physical process impact occurred or is suspected.
- [ ] Preserve network traffic captures and OT historian data before any restoration activities. These are the primary forensic evidence in an OT incident.

**Hour 24–72 (Stabilization and Recovery)**:
- [ ] Conduct forensic analysis with OT-specialized IR support before restoring any affected systems to service. A compromised PLC restored without forensic analysis may retain attacker persistence.
- [ ] Verify physical process integrity before returning systems to automated control. A process that was manually managed during the incident may have drifted from documented setpoints; verify and correct before re-enabling automation.
- [ ] Prepare summary for regulatory reporting: NERC CIP reports, state public utility commission reports (if applicable), EPA notification (if water quality impact occurred).

---

## Section 4: Regulatory Compliance — Critical Infrastructure Requirements

### 4.1 NERC CIP Standards — Electricity Sector

The North American Electric Reliability Corporation's Critical Infrastructure Protection (CIP) standards are mandatory for bulk power system operators (utilities, generators, transmission providers) in North America. The CIP standards relevant to 2026 threats:

**CIP-007 (Systems Security Management)**: Requires documented ports and services management (only necessary ports/services enabled), security patch management (track, assess, and apply patches), and malware prevention for applicable systems.

**CIP-010 (Configuration Change Management and Vulnerability Management)**: Requires configuration baselines for all OT systems and a process to detect unauthorized changes. A compromised PLC whose program has been modified without authorization violates CIP-010 if the change management process would not have detected it.

**CIP-013 (Supply Chain Risk Management)**: Effective since 2020, CIP-013 requires utilities to implement a supply chain risk management plan addressing software integrity verification, vendor remote access controls, and notification requirements when vendors identify vulnerabilities in their products. The Iranian PLC campaign specifically targeted PLCs from vendors whose software the affected organizations had not verified for integrity.

**CIP-008 (Incident Reporting and Response)**: Requires documented cyber security incident response plans and mandatory reporting to E-ISAC for Reportable Cyber Security Incidents. The definition of "Reportable Cyber Security Incident" is narrower than CIRCIA's "substantial cyber incident" — both thresholds may apply to the same event.

### 4.2 America's Water Infrastructure Act (AWIA) and EPA Requirements

Water and wastewater utilities serving more than 3,300 people are required under AWIA to conduct a Risk and Resilience Assessment (RRA) and develop or revise an Emergency Response Plan (ERP). The EPA has provided guidance that cybersecurity is a required element of both documents.

**The 2024 EPA cybersecurity memorandum**: EPA issued guidance in 2024 recommending that public water systems treat cybersecurity as a formal element of their AWIA risk assessments, specifically covering: the identification of cyber assets (SCADA, HMI, PLCs, chemical dosing systems), the assessment of cyber vulnerabilities in those assets, and the development of cyber-specific emergency response procedures. The guidance is advisory, not regulatory, but regulatory status is likely to change given the April 2026 PLC exploitation advisory.

**WaterISAC membership**: The Water Information Sharing and Analysis Center (WaterISAC) provides threat intelligence, incident reporting infrastructure, and training resources specifically for water sector operators. Membership costs $750-$2,500 per year depending on system size. The threat intelligence value significantly exceeds the cost — WaterISAC issued a specific advisory about the Iranian PLC campaign three days before CISA's public advisory. Organizations that are WaterISAC members received 72+ additional hours of advance warning.

### 4.3 TSA Pipeline Security Directives

Natural gas and liquid pipeline operators are subject to the Transportation Security Administration's Pipeline Cybersecurity Directives, which were updated in 2022-2023 and represent the most prescriptive OT security regulation outside of NERC CIP. Key requirements:

- Mandatory annual OT penetration testing
- Network segmentation between OT and IT networks
- Access control requirements for OT systems
- Mandatory incident reporting to TSA within 24 hours for significant cyber incidents
- Annual cybersecurity assessment and plan submission to TSA

Pipeline operators who have not received their most recent TSA directive update should contact their TSA corporate security review coordinator.

---

## Section 5: Worked Examples by Role

### 5.1 CISO — Explaining OT Risk to a Board Without Industrial Background

Board members at utilities and industrial companies often have financial or legal backgrounds rather than operational or engineering backgrounds. The physical consequence language resonates in a way that technical language does not.

**The water utility scenario**: "If an attacker gains access to our chemical dosing control system and increases the chlorine dosing rate above safe parameters, we could deliver water that causes health harm to customers before operators identify and correct the anomaly. This is not a theoretical scenario — it has happened. In February 2021, an attacker gained access to the water treatment plant in Oldsmar, Florida, and attempted to increase lye levels to a dangerous concentration. An operator caught the change manually. We need controls that would detect that kind of change before an operator has to."

**The electric utility framing**: "If a substation's control system is compromised during peak demand, the attacker can create conditions that lead to equipment failure. The physical damage to a large power transformer takes 12-18 months to repair because transformers of that scale are custom-built. The cost of a single large transformer replacement is $3-7 million, plus the power purchase cost during the outage, plus regulatory fines for reliability violations. Our security program is protection against losses that dwarf its cost."

### 5.2 OT Security Engineer — Immediate Vulnerability Mitigation

For an OT engineer who needs to reduce exposure immediately while a larger remediation program is underway:

**Week 1**: Change all default credentials on every internet-accessible or remotely accessible OT device. Use the manufacturer's documentation to identify the default credentials, then change them. Document the new credentials in a secure, offline vault. This single action closes the most commonly exploited attack vector against OT systems.

**Week 2**: Conduct a Shodan/Censys scan of your organization's IP ranges. Any result showing an industrial protocol port accessible from the internet is an immediate finding. Implement firewall rules to block external access to those ports while a longer-term architecture change is planned.

**Week 3**: Review all vendor remote access connections. For each standing VPN or remote access credential: verify the vendor still actively uses it, verify MFA is required, and document the access in a registry. Any standing access that cannot be verified as currently needed should be temporarily revoked pending verification.

### 5.3 Plant Manager — The Downtime Negotiation

The most common friction point in OT security programs is the plant manager's legitimate concern that security controls and patch implementation will create operational downtime. The CISO's position is that unpatched systems create a higher probability of unplanned downtime caused by an attacker. The resolution is a structured negotiation:

**The downtime calculus**: A patch window that creates 4 hours of planned downtime has a known cost. A ransomware event creates typically 2-6 weeks of partial or full downtime, at costs that typically range from $500,000 to several million dollars for an industrial facility. The planned downtime is the lower cost option.

**The risk-tiered patch schedule**: Not all patches require the same urgency. Patches for actively exploited vulnerabilities (documented in CISA's Known Exploited Vulnerabilities catalog) require expedited installation — even if that means unscheduled downtime. Patches for vulnerabilities with no known exploitation can be scheduled for the next maintenance window. Presenting this framework to plant managers as a risk-tiered schedule rather than a blanket "we need to patch everything immediately" request produces more cooperative negotiations.

---

## Sources

- [CISA Advisory AA26-097a: Iranian-Affiliated Cyber Actors Exploit PLCs](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)
- [SecurityWeek: Iran-Linked Hackers Disrupt US Critical Infrastructure via PLC Attacks](https://www.securityweek.com/iran-linked-hackers-disrupt-us-critical-infrastructure-via-plc-attacks/)
- [SecurityWeek: Cyber Insights 2026 — Ongoing Fight to Secure ICS](https://www.securityweek.com/cyber-insights-2026-the-ongoing-fight-to-secure-industrial-control-systems/)
- [SC World: Critical Infrastructure Facing Cyber Surge in OT and Supply Chains in 2026](https://www.scworld.com/feature/critical-infrastructure-facing-cyber-surge-in-ot-and-supply-chains-in-2026)
- [Cyble: USA Critical Infrastructure Cyberattack Threats in 2026](https://cyble.com/blog/critical-infrastructure-cyberattack-threats-2026/)
- [TTMS: Cyber Security Threats in Energy Sector 2026 Guide](https://ttms.com/guide-to-cybersecurity-threats-in-the-energy-sector/)
- [Industrial Cyber: Ongoing Cyberattacks Targeting Internet-Connected PLCs](https://industrialcyber.co/cisa/ongoing-cyberattacks-targeting-internet-connected-plcs-disrupt-us-critical-infrastructure-agencies-warn/)
- [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [WaterISAC: Water Sector Threat Intelligence](https://www.waterisac.org)
- [E-ISAC: Electricity Sector Information Sharing](https://www.nerc.com/pa/CI/ESISAC/Pages/default.aspx)

---

*Created: 2026-05-09. Threat currency current as of May 9, 2026. NERC CIP compliance requirements vary by registered entity type — consult your Compliance Monitoring and Enforcement Program (CMEP) coordinator for entity-specific applicability. TSA pipeline directive applicability is asset-specific. Quarterly review checkpoint: July 26, 2026.*
