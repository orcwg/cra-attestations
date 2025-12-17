---
Task force: CRA Attestations
Document type: Minutes
Status: ✅ Approved
Date: 2025-12-02
---


## Agenda

| Min | Agenda Topics |
| ----- | ----- |
| 0 | Welcome & approve agenda |
| 5 | Approval of the minutes from the previous meeting [here](https://github.com/orcwg/cra-attestations/blob/main/minutes/2025-11-18-mom-cra-attestations.md) |
| 10 | Status of the [action items from the previous meeting](#action-points-from-the-previous-meeting) |
| 15 | First draft of a 2-tier proposal discussion |
| 20 |  |
| 25 |  |
| 30 |  |
| 35 |  |
| 40 |  |
| 45 |  CRA Attestation work focus |
| 50 |  |
| 55 | AOB |

### Action points for the next meeting

- [ ] AP1 \- Share and compare your attestation plan/programs/activities  
- [ ] AP2 \- Sub-group to form to get clarity on legal guidance regarding 501c3’s collecting compensation for VSAs. “not earning money”, “recovering costs”, “supporting mission or community”. Lead: Seth Larson (PSF). Contributing ideas: Dirk, Simon. \- Æva: follow up with Dirk and Seth re: 501c3 guidance  
- [x] AP5 \- All participants to the Code\&Compliance workshop to check the summary [here](https://github.com/orcwg/cra-attestations/tree/main/events/workshop-2025-10-code-and-compliance)

### Participants

- Æva Black (Null Point Studio)  
- Juan Rico (Eclipse Foundation)  
- Georg Link (Bitergia)  
- Seth Larson (Python Software Foundation)  
- Greg Wallace (FreeBSD Enterprise WG Lead)  
- Alistair Woodman (Erlang Ecosystem Foundation (EEF))  
- Salve J. Nilsen (CPANSec)  
- Timo Perälä (Nokia)  
- Anne Dickison (FreeBSD Foundation)  
- Adrian OSullivan (Huawei)

## Notes

### Approval of the minutes from the previous meeting here

- Reviewed, no objection

### Status of the action items from the previous meeting

* Seth kicked off the US 501c3 sub-group with a list of topics and members. To create a meeting soon with folks who signaled interest and create a meeting plan based on topics.

### Presentation of FreeBSD Attestation program by Greg Wallace

  - Assessment process  
      - Trigger \- CISA RSAA requirements \+ NIST SSDF standard
      - \~12 questions in the SSDF Self-Attestation  
  - How long did it take  
    - needed to consult with most of the team to verify the answers. Took a few (non-exclusive) weeks, \~40hrs total.  
  - How to engage with FreeBSD corporate users.
    - Made available to anyone donating at “partner” level (tiered cost based on organization size) inclusive of in-kind donations. 
      - E.g., support/funding for development of essential features  
    - [https://freebsdfoundation.org/news-and-events/latest-news/freebsd-foundation-announces-ssdf-attestation/](https://freebsdfoundation.org/news-and-events/latest-news/freebsd-foundation-announces-ssdf-attestation/)   

- Q\&A  
  - Salve: what sort of success or pushback did you have?  
    - Greg: engaged companies increased engagement, others reacted towards regulators objecting to what they saw as “unfair burden”  
  - Mathias: your attestations are recipient-bound; by what legal instrument?  
    - Greg: specified to whom & for what version, stated on document cover & footer of each page. Minimal technical effort for an MVP.  
  - Salve: What FreeBSD attest?  
    - Greg: NIST SSDF self attestation \- how the software was developed \- [https://www.cisa.gov/sites/default/files/2024-04/Self\_Attestation\_Common\_Form\_FINAL\_508c.pdf](https://www.cisa.gov/sites/default/files/2024-04/Self_Attestation_Common_Form_FINAL_508c.pdf)   
    - FreeBSD only attested to the content of the Appendix, which contains a partial mapping to the SSDF.   
  - Alistair: There isn’t a specific set of things that need to be attested to, but you select the ones you want to attest to and you do it.

Originally required certifying FOSS included in products. This was later watered down in later versions of the US requirements.

### First draft of a 2-tier proposal discussion

- Mathias: after a lengthy discussion about Issue \#14, including making the point that both legal and natural persons are not exempt from liability (regardless of CRA),  then suggests we do not need to consider questions of tort or individual liability as relates to the CRA  
- Alistair: if issuing attestations does not change individual liability, but may lead to funding for individual / natural persons …   


### FOSDEM status

- Aeva: submitted 3 talks: summarizing this working group, a panel on attestations in use now, and a panel on what we’d like to see attestations become  
- Salve: also submitted 3 talks: packaging metadata, ideal shape of a steward, sustainability metadata (incidentally related)  
- Eclipse’s event on Thursday (Juan: EF may publish the agenda as soon as next week)  
- AboutCode’s event on Friday related to SBOM tooling

### AOB

Mathias shared that he has recently started diving into SBOMs.
