---
Task force: CRA Attestations
Document type: Minutes
Status:  📝 Draft
Date: 2026-07-14
---

## Agenda

| Min | Agenda Topics | Moderator |
| ----- | ----- | ----- |
| 0 | Welcome & approve agenda |  |
| 5 | Approval of the [minutes from the previous meeting](./2026-07-14-mom-cra-attestations.md) |  |
| 10 | Status after summer break |  | 
| 15 |  |  |
| 20 |  Single Reporting Platform status and next steps|  |
| 25 |  |  |
| 30 |  |  |
| 35 | Software Supply Chain Communication |  |
| 40 |  |  |
| 45 |  |  |
| 50 |  |  |
| 55 |  AOB |  |

## Participants  

- Greg Wallace (NetActuate)  
- Juan Rico (Eclipse Foundation)  
- Æva Black (Null Point Studio)  
- Mathias Schindler (GitHub)  
- Timo Perälä (Nokia)  
- Salve J. Nilsen (CPANSec)  
- Gerardo Lisboa (ESOP)  
- Alistair Woodman (Erlang Ecosystem Foundation (EEF))  
- Anne Dickison (FreeBSD Foundation)

## Notes

### Welcome & approve agenda

- Agenda approved

### Approval of the minutes from the previous meeting

- No objections voiced  
- N.B.: minutes were recorded \~2 months ago

### Status after summer break

- Before the summer break, it was presented to the European Commission the Attestations report. We are still waiting for confirmation on next steps and whether they will make it public or not.  
- It was introduced in the last meeting the Cybersecurity and AI interplay document released by the EC. Eclipse submitted feedback to the interplay of the CRA and the AI Act, but there has been no follow up after the release of the report (available in the last meeting minutes).  
- [Due diligence work](https://github.com/orcwg/cra-due-diligence) was identified as the primary area of progress during the second half of August after meetings were relaunched; this is expected to be one of the next deliverables the working group releases. It includes several sections touching upon attestations so it is suggested to check and contribute to it.

### Single Reporting Platform status and next steps

- ENISA says Stewards should not use SRP (it’s only for Manuf.) to report cyber incidents until December 2027\.   
  - ENISA plans to continue changing/updating the SRP platform for next \~6 mo (at least)  
  - Open Goal: identify goals and means of working to have any positive effect on ENISA/SRP’s direction … it seems like we have very limited options right now.  
- “SolarWinds”-style gap is created by this new guidance – if an OSS Steward’s build system gets breached, how are they supposed to ask for support from public sector?  
- Aeva asked the group if *anyone* is aware of ENISA, or other EU public entities, taking a participatory role in supporting OSS stewards during cyber incidents  
  - Answer: *No.*  
- Gregor: Are stewards even allowed to use SRP?  
  - Juan: No, Stewards should go thru CSIRT  
- Gregor: significant backlash to German federal efforts to capture-and-use vuln reports, perhaps some of this has also affected ENISA’s approach?  
  - Mathias responds: updated parliamentary Bill was stripped of these provisions   
  - Aeva: asks for clarification if the backlash is about vuln data & KEVs, which should have nothing to do with SRP  
  - Mathias clarifies: intelligence reform bill has nothing to do with CRA specifically, and is focused on exploits.  
  - Aeva proposes we close the topic since the SRP has no relationship to the German bill proposal just discussed.

### Software Supply Chain Communication

The presentation can be found [here](./2026-09-08-software-supply-chain-communication-ietf-126-1.pdf)

- Regulatory Context & Objective: Driven by CRA and NIS2 compliance demands, the proposal uses IETF SCITT standards to create decentralised, globally interoperable communication channels between open-source stewards, downstream commercial users, and regulators.   
- Repository Badges & Authority PKI: Repositories would publish machine-readable badges detailing security certifications for forge filtering. Market Surveillance Authorities would adopt a PKI, allowing stewards to authenticate incoming regulatory communications against impersonation.   
- Forge Credibility & Donation Tracking: Inbound security communications utilise forge-published message hashes alongside sender centrality scores for prioritisation. Downstream dependents verify identity and build trusted channels via time-series donation UIDs without centralised identity infrastructure.   
- IETF Scope & Governance Boundaries: IETF standardization is restricted strictly to technical protocols, security guardrails, and interoperability. Payload data formats, governance choices, payment mechanisms, and legal interpretations fall out of scope (slated for groups like OVAS and Koala).   
- Security Risks & Open Questions: Identified risks include malicious bug fixes, relay attacks, package impersonation fraud, and money laundering vectors via high-volume micro-donations. Non-European regulatory alignment and robust detection of AI-generated security reports remain open challenges.   
- Community Alignment & Next Steps: NixOS serves as a primary European CRA steward case study. The initiative is already collaborating with other open source initiatives.

### AOB

- None.
