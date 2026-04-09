---
Task force: CRA Attestations
Document type: Minutes
Status:  ⚠️ Draft
Date: 2026-04-07
---

## Agenda

| Min | Agenda Topics | Moderator |
| ----- | ----- | ----- |
| 0 | Welcome & approve agenda |  |
| 5 | Approval of the [minutes from the previous meeting](https://github.com/orcwg/cra-attestations/pull/28)|  |
| 10 | Joint Statement Status | | 
| 15 | Heavyweight Attestations |   |
| 20 |  |  |
| 25 |  |  |
| 30 |  |  |
| 35 |  |  |
| 40 |  |  |
| 45 |  |  |
| 50 |  |  |
| 55 |  AOB |  |

## Participants

-  Æva Black  
-  Markus Stahl (Robot Framework Foundation)  
-  Dirk-Willem van Gulik / Apache Software Foundation (ASF)  
- Mathias Schindler (GitHub)  
- Salve J. Nilsen (CPANSec)  
- Florian Lukavsky (SignPath)  
- Alistair Woodman (Erlang Ecosystem Foundation (EEF))  
- Anne Dickison (FreeBSD Foundation)  
- Pierre Pronchery (FreeBSD Foundation)  
- Timo Perälä (Nokia)  
- Juan Rico (Eclipse Foundation)  
- Seth Larsin (Python Software Foundation)

## Notes

Gathering list of events:
- OCX  
- RustWeek  
- OSS-NA and OSS-EU  
- Perl Toolchain Summit (23-26 April, Vienna)  
- [https://owasp.glueup.com/event/owasp-global-appsec-eu-2026-vienna-austria-162243/](https://owasp.glueup.com/event/owasp-global-appsec-eu-2026-vienna-austria-162243/)  
- ElixirConf EU (22-24 April)

### Welcome & approve agenda

### Approval of the minutes from the previous meeting
- Minutes from the previous meeting were approved


### Heavyweight Attestations
- Aeva: shares concern that we haven’t made progress on the topic in a few months, so we will focus on it today.  
- DW: this seems almost like a more extreme version of the FIPS cert. Usually happens downstream. Requires too much product context not available upstream.  
- Aeva: and yet, context is known for some product-like projects (Spark, OpenOffice, …). Could project articulate expected use cases, quantified risks and mitigations, and then downstreams can have reduced compliance burdens IFF adhering to that?  
- DW: this might force communities to fork. Many projects have a great diversity of use cases and risk models, in which case downstreams can’t collaborate effectively. Taking the example of Spark, probably very few companies using it have the same risk model.  
- Alistair: OpenWRT might be a better example.  
- Mathias: is there any scenario where the existence of VSA could negatively affect manuf.’ compliance obligations? What about “negative attestation”?  
- DW: FIPS certification processes has led to community friction. So I can see a too-narrow attestation statement becoming a hurdle.  
- Aeva: gave summary and examples of negative attestations and summary of discussions with the regulators  
- DW: comparison between negative attestations and CE marking disputes. It’s common and there are ways to handle it.  
- Jonatan: what if conflicting signals (Attestations) from first party (maintainer) and third party? Integrators probably have a hard time then in proving diligence but should probably trust first party.  
- Mathias: the opposite can be true in some cases, e.g. where maintainer makes exaggerated claims  
- Juan Rico: it sounds like all this should be part of Due Diligence process. VSA should only contain “Facts” that can be verified.  
- Aeva: agreed. Should focus on things which can be verified, even if it is not free or cheap to do so.  
- DW: agreed, but missing something. Light-weight is just a convenient bundle of facts, but heavy-weight could require specific and technical work to create and change the project code / documentation / content. “We’re not just providing *some* facts, we need to be able to change our reality to provide the *right facts*, and that will collide with the desires of others.” A proper attestation is like writing good documentation; one may change the software to be able to achieve certification. This could contradict the openness of a community and result in project’s constrained by downstream users.  
- Aeva: I can see the contradiction – narrowing the project scope to achieve compliance could alienate a broader community, contravening the very openness which has led to open source innovation.  
- Alistair: it seems like all of this won’t matter anyway until an attestation ends up in court. Could third-party attestors end up in court to defend their attestations?  
- Mathias: if Delegated Act creates the reality where VSA creates presumption of conformity, we could end up there, but this is entirely unknown now. Better to focus on whether this is possible than the ramifications of a hypothetical.  
- Aeva: Considering the wide reliance on e.g. linux, if there is no possibility of an attestation contributing to a presumption of conformity, then much of the industry is going to struggle, so it is worth contemplating.  
- Juan: worth considering the relationship between stewardship and non-profit roles.  
- DW: hey aeva, I think you opened the right can of worms… Considering the state of the software industry, and particularly open source, we’ve only barely been able to achieve this by making certain components extremely specific, whereas the things you mentioned are extremely generic – the “nuts and bolts” of software engineering. To solve this manuf. Accept the inefficiencies of re-engineering to specific products.   
- Seth: difficulty for language like Python, almost have to treat every submodule like a separate project b/c they all have different use-cases.  
- August: not a lot of changes in the vertical standards over the past few months. Some addition of new low-risk use cases, but compliance is still tied to use-cases so unlikely to be particularly useful for generic FOSS projects..  
- August: guidance on upstreaming patches to FOSS is evolving, now states that fixes should be shared in the manner preferred by the upstream maintainer.

### Juan’s Update (Joint Statement Status?)

- Will share the current draft of the ORC statement in support of Attestations on the mailing list before EOD. Requesting feedback and supporting statements from organizations.   
- Reminds the group that discounts to group members are available for Eclipse OCX conference.  

### AOB
- None
