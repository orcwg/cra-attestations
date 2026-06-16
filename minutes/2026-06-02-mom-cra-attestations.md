---
Task force: CRA Attestations
Document type: Minutes
Status:  ✅ Approved
Date: 2026-06-02
---

## Agenda

| Min | Agenda Topics | Moderator |
| ----- | ----- | ----- |
| 0 | Welcome & approve agenda |  |
| 5 | Approval of the [minutes from the previous meeting](https://github.com/orcwg/cra-attestations/pull/33) |  |
| 10 | Manufacurers' pain points |  | 
| 15 |  |  |
| 20 |  |  |
| 25 |  |  |
| 30 | Continuation of tiers discussion |  |
| 35 |  |  |
| 40 |  |  |
| 45 |  |  |
| 50 |  |  |
| 55 |  AOB |  |



## Participants

- Æva Black (Null Point Studio)  
- Mark Thomas (ASF)    
- Juan Rico (Eclipse Foundation)    
- Sebastian Tiemann (Open Elements)   
- Tobie Langel (UnlockOpen)  
- Mathias Schindler (GitHub)  
- Pierre Pronchery (FreeBSD Foundation)  
- Christian Pfaab  
- Arman Bilge (Typelevel Foundation)  
- Timo Perälä (Nokia)  
- Salve J. Nilsenn (CPANSec)
- Jan Zizka (Nokia)

## Notes

### Welcome & approve agenda

### Approval of the minutes from the previous meeting

- [https://github.com/orcwg/cra-attestations/pull/33/changes](https://github.com/orcwg/cra-attestations/pull/33/changes)   
- (skipped at meeting start, will cover at end)

### Manufacturers' pain points

- \+3 Hard to see how different tiers help manufacturers with anything specific to the CRA obligations  
- \+1 Needs to have clear value relationship between the actual CRA obligations to tiers  
- General concern about how the market will react & whether this topic relates to *everything else* … in particular AI’s security impact  
- \+1 Also ensure that attestations appear to be a “product” which companies can buy, in order to reduce due diligence costs  
- A small extract from the CEN/CENELEC draft standard for OSS component integration was shared.  

Discussion pivots to the PT1 draft text – but it’s a 1,531 line document, so we will defer it  … 

- It’s a good start, outlining what manufacturers should be able to find regarding the open source they use  
- If “check” fails, is it still OK to use? Probably, but it increases the burden.  
- Theoretically… but how many manufacturers will actually do this???

Tobie shared the Javascript ecosystem project-to-steward ratio: 
- 3M packages  
- 300k in widespread use  
- But only 35 projects / stewards…

Juan: due diligence is more than just the PT1 base guidelines

Salve: what information can maintainers uniquely provide that is meaningful to the due diligence process? Proposes that it is a *commitment* from the maintainer, e.g. to follow their own documented process, to monitor for vuln reports and address them in a timely manner, to not include feature changes in security releases, and so on…

Tobie: This sounds more like a mid-tier attestation, still not a full-product-like analysis. Almost like a 2x2 matrix of requirements\!

### Continuation of tiers discussion

Aeva asks Salve if this *commitment* is generally applicable or more specifically applicable to a subset of open source

Salve: Multiple tiers are useful to help manufacturers determine what information is needed based on the specific use case they are building for. Lightweight / baseline is useful; ways to step up attestations for use-cases more stringent requirements, are also useful. But two tiers might be too simplistic. 

Q: Could coding agents provide appropriate due diligence that could satisfy CRA requirements of manufacturers?

Mark \- not yet, but maybe soon… Aeva \- 09/26 or 12/27? … Mark – 12/27.   
Tobie \- AI can do a lot of the automated checking that is required, but it’s expensive…. Socket.dev is a good example today. Also patching is a governance problem, not an AI capability problem. Bigger problem is day-two operations to keep products secure after market.  
Salve \- highlights that commitments aren’t reliably inferable by LLMs in the absence of the human maintainers’ signals, and that those commitments are the valuable component of the attestation  
Sebastian \- we should not conflate *technical ability* with *accountability*. Supports Salve’s ideas around commitments.  
Mathias \- proposes that due diligence can be satisfied entirely by automated review of a codebase, and contemplates how divergent our proposals are from the legal text of the CRA.  
Tobie \- while Salve and Sebastian point out that LLMs cannot be *accountable*, but on the other hand, the CRA clearly excludes maintainers from accountability as well. Some people want to avoid liability, and some people want to accept liability in exchange for money. We should clearly allow both approaches.  
Tobie \- Article 13(5) makes clear that ‘due diligence’ is context-specific and risk-based. It’s not all-high or all-low.

### AOB
None


#### *Aditional notes*

Draft Harmonised Horizontal \- CEN/CENELEC PT1 says 
>*If the third-party component is FOSS check if:  
>1\. the FOSS project is actively maintained, including evidence of recent development or maintenance activity;  
>2\.  a vulnerability disclosure process is defined and publicly available;  
>3\.  the FOSS is stewarded for commercial use by a foundation or organization acting as an open-source software steward;  
>4\.  there are indicators of cybersecurity-by-design practices, such as documented secure development practices;  
>5\. regular cybersecurity patches or security updates are made available.*
