---
Task force: CRA Attestations
Document type: Minutes
Status: 📝 Draft
Date: 2026-11-03
---

## Agenda

| Min | Agenda Topics | Moderator |
| ----- | ----- | ----- |
| 0 | Welcome & approve agenda |  |
| 5 | Approval of the [minutes from the previous meeting](https://github.com/orcwg/cra-attestations/pull/41) |  |
| 10 | Review of Code & Compliance |  |
| 15 |  |  |
| 20 | Attestations and ENISA Playbook alignment [\#40](https://github.com/orcwg/cra-attestations/pull/40) |  |
| 25 |  |  |
| 30 |  |  |
| 35 | Next steps |  |
| 40 |  |  |
| 45 |  |  |
| 50 |  |  |
| 55 |  AOB |  |


## Participants

- Timo Perälä (Nokia)  
- Sebastian Tiemann  
- Tobias Frech (iJUG)  
- Matt Albrecht (Zilliant)  
- Juan Rico (Eclipse Foundation)  
- William Janssen  
- Alistair Woodman (Erlang Ecosystem Foundation (EEF))  
- Æva Black (Null Point Studio)

## Notes

### Welcome & approve agenda

- We agreed to add a summary of Code and Compliance as an agenda item

### Approval of the minutes from the previous meeting

- Approved and will be merged

### Review of Code & Compliance

Industry Awareness Gap

* Eight industry associations were contacted; only UNIFE and Agoria are actively engaging with open source compliance, attestations, and due diligence. The others are interested in the topic but not mature enough to join the discussion.  
* A third group assumes their compliance tool provider handles open source compliance,  but those tools analyse current code state, not community health, project activity, or integration suitability. 

Compliance Tooling Shortfall

* We heard from a real case that after introducing due diligence checks into their open source component intake tool, more than 90% of projects failed the new criteria.   
* The checks had to be switched off temporarily because the result would have been that the majority of desired components could not be used.   
* This aligns with the broader observation that existing tools evaluate code state, not project healthiness or sustainability before integration. 

Commission Updates

- European Commission recognised that Standards is one way to comply, but not the only.  
- The European Commission acknowledged it has not forgotten volunteer security attestations; the topic deprioritised over summer has now risen near the top of their list.  
- Attendees expect movement soon, potentially via a webinar in coming weeks for the AI SIG.

AI Act and Regulatory Overlap  
Open-Weight Models and Steward Obligations

* It was presented that a legal entity maintaining an open-weight model, with knowledge it will be used in commercial products on the European market, likely qualifies as both a CRA steward and has AI Act obligations simultaneously.   
* Key nuance: AI Act exemptions for open-weight models are narrow, they are voided if the use falls under Article 5, Article 50, or if the model qualifies as high-risk (based on training size and model complexity).   
* A non-profit foundation whose members commercialise a model it maintains may have obligations attach back to the foundation, even without direct commercialisation. 

Counterpoint

* The AI Act attaches obligations primarily to the entity deploying the system, not to a steward-equivalent.   
* There is no steward role defined in the AI Act; Matthias questioned which specific scenarios would create AI Act obligations for a typical CRA steward. 

Resolution

* The gap is not about the deploying entity but about upstream information requirements: downstream deployers often cannot fulfill their AI Act obligations unless the upstream open-weight model provider supplies the right documentation. 26  
* This creates a de facto obligation on the upstream provider, even if not explicitly named in the regulation. 2426  
* Eva invited the group to discuss how attestations or similar mechanisms could address this intersection via Slack or the mailing list.

### Attestations and ENISA Playbook alignment \#40

* Sebastian created a [PR](https://github.com/orcwg/cra-attestations/pull/40/changes) mapping the ENISA playbook, Secure by Design and Default principles, and the existing lightweight attestation measures.   
* The goal is to demonstrate that the attestation framework is grounded in business-relevant, established security guidance, not invented from scratch.   
* Key design principle maintained: maintainers should not have to do more than maintaining the project; the guidance adds flesh to the bone without adding burden.   
* Feedback received in the Github PR; open questions remain at the end of the document.   
* It was noted the ENISA playbook GitHub repository accepts external contributions, so the group could contribute directly to ENISA's artifact, not only to internal documents.  
* For Linux Foundation community projects targeting commercial adoption, the attestation serves as a signal that the project is "CRA-ready", making integration easy and demonstrating intent to support compliance.   
* Existing signals (SBOMs, OpenSSF scorecards) are good but incomplete; a versioned attestation per release would add the missing layer.

### Next steps

- TBD next steps

### 

### Supporting links:

* [https\://github.com/orcwg/cra-attestations/pull/40/changes](https://github.com/orcwg/cra-attestations/pull/40/changes)  
* [https\://www\.enisa.europa.eu/sites/default/files/2026-07/ENISA\_Secure\_By\_Design\_and\_Default\_Playbook\_v1.pdf](https://www.enisa.europa.eu/sites/default/files/2026-07/ENISA_Secure_By_Design_and_Default_Playbook_v1.pdf)  
* [https\://github.com/ietf-scitt](https://github.com/ietf-scitt)  
* [https\://ecma-international.org/publications-and-standards/standards/ecma-428/](https://ecma-international.org/publications-and-standards/standards/ecma-428/)  
* [https\://tc54.org/cle/](https://tc54.org/cle/)  
* [https\://tc54.org/tea/](https://tc54.org/tea/)  
* [https\://www\.tc54.org/contributing-yaml/](https://www.tc54.org/contributing-yaml/)
