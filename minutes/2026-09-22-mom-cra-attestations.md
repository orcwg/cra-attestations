---
Task force: CRA Attestations
Document type: Minutes
Status:  📝 Draft
Date: 2026-09-22
---

## Agenda

| Min | Agenda Topics | Moderator |
| ----- | ----- | ----- |
| 0 | Welcome & approve agenda |  |
| 5 | Approval of the [minutes from the previous meeting](https://github.com/orcwg/cra-attestations/pull/36) |  |
| 10 | Use of attestations during the due diligence process for CRA Compliance |
| 15 |  |  |
| 20 |  |  |
| 25 |  |  |
| 30 |  |  |
| 35 |  |  |
| 40 |  |  |
| 45 |  |  |
| 50 |  |  |
| 55 |  AOB |  |

## Participants

- Juan Rico (Eclipse Foundation)  
- Salve J. Nilsen (CPANSec)  
- Greg Wallace (NetActuate)  
- Mathias Schindler (GitHub)   
- Matt Albrecht (Zilliant)  
- William Janssen  
- Alistair Woodman (Erlang Ecosystem Foundation (EEF))  
- Æva Black (Null Point Studio)  
- Timo Perälä (Nokia)

## Notes

### Approval of the minutes from the previous meeting

- The minutes from the prior meeting were formally approved and will be merged after the meeting.  
- Article 25 Delegated Acts: No official updates or concrete timelines have been released regarding delegated acts under Article 25\.  
- Regulatory Clarification: It was emphasised that the implementation of CRA attestations is not contingent upon Article 25 delegated acts, and work on attestation frameworks can proceed independently.

### Use of attestations during the due diligence process for CRA Compliance

- Liability Gap: A central challenge for manufacturers is reconciling strict legal liability and financial penalties under the CRA with the voluntary "gift economy" nature of open source development.  
- Maintainer Intent: open source maintainers generally want their projects widely adopted, but often lack clear guidance or tooling to meet CRA compliance requirements. Attestations offer a mechanism to bridge this gap.  
- Usage over Production: The group agreed to shift focus away from how attestations are created, funded, or monetised, and instead concentrate on how manufacturers practically ingest and utilise attestation data during product integration.  
- Automation Requirement: Manual inspection of attestations across deep dependency graphs is impossible; attestation formats must be standardised, machine-readable, and integrated into automated pipelines.  
- Trust as the Bridge to Compliance: Trust acts as the critical link between attestation content and legal risk, as manufacturers must justify why and how relying on a given attestation or metric fulfils their specific CRA due diligence obligations.  
- A distinction was highlighted between strict statutory obligations and prudent, risk-mitigating actions taken by manufacturers. While checking component health may not eliminate liability, it provides essential due diligence artefacts required under CRA compliance frameworks.  
    
#### Key questions we need to address

- **Workflow & Automation:** How can manufacturers practically ingest and automatically evaluate attestations within their existing software development lifecycles and build pipelines?
- **Liability & Voluntary Risk:** How can manufacturers legally rely on voluntary attestations from maintainers or stewards while bearing full legal liability and statutory fines under the CRA?

### AOB

None
