---
Task force: CRA Attestations
Document type: Minutes
Status: 📝 Draft
Date: 2026-10-20
---

## Agenda

| Min | Agenda Topics | Moderator |
| ----- | ----- | ----- |
| 0 | Welcome & approve agenda |  |
| 5 | Approval of the [minutes from the previous meeting](https://github.com/orcwg/cra-attestations/blob/main/minutes/2026-09-22-mom-cra-attestations.md) |  |
| 10 | Attestations and ENISA Playbook alignment https://github.com/orcwg/cra-attestations/pull/40 |
| 15 |  |  |
| 20 |  |  |
| 25 |  |  |
| 30 |  |  |
 35 | News from the Cyber Manual Movement  |  |
| 40 | Next steps of the work in this TF |  |
| 45 |  |  |
| 50 |  |  |
| 55 |  AOB |  |



## 

## Participants

-    
- Sebastian Tiemann (Open Elements)  
- Juan Rico (Eclipse Foundation)  
- Mathias Schindler (GitHub)  
- Æva Black  
- William Janssen  
- Gregor Bransky (Innovationsverbund Öffentliche Gesundheit e.V.)  
- Timo Perälä (Nokia)  
- Alistair Woodman (Erlang Ecosystem Foundation (EEF))  
- Anne Dickison (FreeBSD Foundation)  
- Salve J. Nilsen (CPANSec)

## Notes:x

### Approval of the minutes from the previous meeting

- No objections noted; therefore, approved

### Attestations and ENISA Playbook alignment \#40

- ENISA mapping: Sebastian created a pull request mapping lightweight and heavyweight attestations to the ENISA Secure by Design playbook and CRA articles.  
- The group aligned on using the ENISA Secure by Design playbook as a bridge for manufacturers until harmonised standards are available, with a focus on mapping attestations to CRA articles.  
- Secure by Design tension: Open source projects often prioritise developer ease over secure-by-default configurations, creating a gap between community defaults and end-user product requirements.  
- Community feedback path: The group will encourage direct contributions to the ENISA playbook via its GitHub space, as ENISA is actively seeking community feedback.   
- Sebastian’s proposal will be revisited in the next meeting in two weeks after the group has time to review and comment.

### News from the Cyber Manual Movement

- Cyber Manual Movement: A small group in industrial automation has developed drafts for a cyber manual mandated by the CRA, with a public launch planned for late November/early December.   
- CMM Go-live is planned for early December; whoever is interested in reviewing, reach out to Gregor.
- CRA Monday: An event is being organised for November 23rd where the Cyber Manual Movement initiative will be presented.


### Next steps of the work in this TF

- Potential activities:  
  - Further engagement with manufacturers to validate attestation concepts and their integration into operational workflows. It was considered to launch a survey to manufacturers relying on the network built preparing Code and Compliance.  
  - Development of attestation specification. Attestation was initially created as a specification project, so that path can also be followed.  
  - Integration into due diligence, some discussions already took place, but could be a potential way to speed up development.  
- It will be posted in the mailing list collecting feedback for it.

### AOB

- Open source project abandonment during a product's support period \- We discussed how stewards can provide signals of long-term viability, or if the manufacturers are the ones that should engage with the community to make sure that those projects are not abandoned.  
  - It was also considered as a “middle road” that stewards could sell time-limited attestations to fund maintainers, but the legal/business structure is unresolved.  
  - The topic was linked to the risk assessment exercise and the lack of risk measurement. Many companies are not currently measuring or mitigating the risk of upstream project abandonment  
- Interesting question: As stewards are not liable {citation\_needed} this might lead to a new openness when it comes to technical documentation. Does the lack of liability of stewards {citation\_needed} lead to a new usefulness of technical documentation in comparison to white washed lawyered down versions?
  - It is unclear how a steward’s technical documentation can be translated into manufacturer-facing documentation that complies with user obligations.  
  - Steward liability: The exact interplay between the Product Liability Directive (PLD) and the CRA regarding open source stewards remains unclear, as the PLD does not explicitly discuss stewards.  
  - The group also clarified that stewards are not shielded from liability for misleading documentation, though their role may differ from manufacturers in how they provide technical information.

#### References:

- [https\://alpha-omega.dev/blog/apache-trusted-releases-platform-begins-second-alpha/](https://alpha-omega.dev/blog/apache-trusted-releases-platform-begins-second-alpha/)   
- [https\://cyber-manual-movement.org/](https://cyber-manual-movement.org/) 
