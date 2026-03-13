## Agenda

| Min | Agenda Topics | Moderator |
| ----- | ----- | ----- |
| 0 | Welcome & approve agenda |  |
| 5 | Approval of the minutes from the previous meeting [here](https://github.com/orcwg/cra-attestations/pull/21) |  |
| 10 | CRA Expert Group meeting prep  |  |
| 15 | Update to README & overview[https://github.com/orcwg/cra-attestations](https://github.com/orcwg/cra-attestations)  |  |
| 20 |  |  |
| 25 | [Tobie’s Paper](https://docs.google.com/document/d/1OvETnBXGYSpzlSYGG18eDhgLwP50WOD4LnGwPtp19Ak/edit?tab=t.0) \- presentation and discussion |  |
| 30 |  |  |
| 35 |  |  |
| 40 |  |  |
| 45 |  |  |
| 50 |  |  |
| 55 | AOB |  |

## Participants

- Æva Black  
- Mathias Schindler  
- Alice Sowerby (FreeBSD Foundation)  
- Pierre Pronchery (FreeBSD Foundation)  
- Sebastian Tiemann (Open Elements)  
- Greg Wallace (NetActuate, FreeBSD Enterprise WG)  
- Salve J. Nilsen (CPANSec)  
- Georg Kunz (Ericsson)  
- Tobie Langel  
- Jordan Maris (OSI)  
- Seth Larson (PSF)  
- Timo Perälä (Nokia)  
- Dirk-Willem van Gulik (ASF) \-- arrived 30 mins late.  
- GANitak (Open Source contributor)

## Notes

### Welcome & approve previous minutes

- Please comment on Greg’s VSA Access Terms Proposal if interested. If you plan to review, please let Greg know  
- Æva has cleaned up and added to the docs on the repo \- please review: [https://github.com/orcwg/cra-attestations](https://github.com/orcwg/cra-attestations) and also please keep the proposals coming\!  
- Expert Group [meeting](https://ec.europa.eu/transparency/expert-groups-register/screen/meetings/consult?lang=en&meetingId=68505&fromExpertGroups=3967) is next week. Æva will be attending as an invited expert to present on open source attestations. The list of participants is public. See: [https://cra.orcwg.org/faq/cra-itself/cra-expert-group/](https://cra.orcwg.org/faq/cra-itself/cra-expert-group/)  and the minutes will be published here as well.  
  - Any input?:  
    - Has Jordan submitted questions regarding Steward Opt-out and Economic Operators?  
      - Has not submitted yet.   
        - Spoke to Tommasso \- if you meet requirements, you are a Steward, but there are very specific things you must do to meet requirements, and so if you don’t do them, you’re not a Steward.   
        - RE: Economic Operators \- OSI not involved, AEva has had some conversations \- it’s a complex topic.  
        - Is a Steward an Economic Operator? Some conflicting guidance according to different regulations. This is important since, if Steward \= EO, then things that CRA does not address, but other regs DO address may apply. It’s better to get this clarified now, versus in 5 years when things are more consolidated than they are now  
        - This group is seeking clarity on the topic. 

- Tobie’s paper \- Security Attestations Under the EU CRA ([https://docs.google.com/document/d/1OvETnBXGYSpzlSYGG18eDhgLwP50WOD4LnGwPtp19Ak/edit?tab=t.0](https://docs.google.com/document/d/1OvETnBXGYSpzlSYGG18eDhgLwP50WOD4LnGwPtp19Ak/edit?tab=t.0))   
  - Paper based on Tobie’s presentation at FOSDEM ([https://fosdem.org/2026/schedule/event/AATKG8-cra-security-attestations-in-practice/](https://fosdem.org/2026/schedule/event/AATKG8-cra-security-attestations-in-practice/))   
  - Based on need for Manus to do due diligence on one end, and the desire of OSS community (and by EU) to be able to rely on secure open source software.  
  - What are economically reasonable options to shift security left to Maintainers, where there is expertise and efficiencies, and have that work be funded by Manus.  
  - Manus have to demonstrate that they’ve done Due Diligence. And they need a credible way to maintain the security of their PDEs regardless of what happens upstream  
  - Addresses perception that Stewards will “solve” this.   
    - in many/most ecosystems, there are vastly more OSS projects that are NON stewarded than that are.  
    - And Stewards will do a subset of things Manus need under CRA  
    - (third point)  
    - Attestations fill this gap  
  - Attestations are a unique token of exchange to make the relat between maintainers and Manus work.   
  - 4 ways Manus can fulfill their CRA obligations  
    - 1: Big Tech (and others) do this in house via mirror/fork  
    - 2: Commercial contract \- either service or vendors that package OSS and “sell” to you  
    - 3: Rely on Stewards (insufficient)  
    - 4: Attestations  
    - Manus can pick and choose \- they will choose the one with greatest utility (fastest, cheapest, best…)  
      - So, Attestations operate in a competitive market  
  - Question \- The delegated acts will shape this reality. How do you anticipate this effect? And, does the end of the paper address the question?  
    - Public signals (non monetizable)  
    - Private security info (low monetization) \- maybe useful for large stewards  
      - Volume of security incidents/PRs/  
      - Question about the legality of sharing embargoed info about in-process CVE remediation in exchange for membership fees or such  
      -   
    - Manus do not have to use Attestations to meet their requirements, and public signals are public, so that doesn’t leave much for Maintainers to provide that Manus will pay for. So, the real value if long-term maintenance of OSS. Attestations should be the mechanism to enable this, while being protective of Maintainers and avoiding turning liability to them  
    - Paper proposes Maintainer Pods as a potential solution that are effectively Stewards, but from the point of the view of the law are not.  
  - Alistair \- some projects should get marked as “Depricated” could be a large percent of all OSS packages, which would then reduce the size of the population of “viable” projects, so perhaps the burden for the remaining ones to become stewarded would be lower   
  - Jordan \- Commission has wide purview with the delegated act and the delegated act will likely change the current state of play in terms of Maintainers, Stewards, and Attestations. Some projects may want to move under a Steward based on the Delegated Act. There may even be some tax breaks for Stewards / Maintainers  
    - Mathias \- took a deep dive into article \*\* to see what the EU might do in a delegated act. Their leeway is not unlimited. Document available in the Matrix channel \- please review and provide feedback.  
    - GDPR reference is interesting \- implementation in Germany was trivial since there was an existing privacy law in place. But elsewhere in Europe it was a bit harder.  
- Mathias wrote a Draft Delegated Act \- Ping Mathias if you want to read it

### 

