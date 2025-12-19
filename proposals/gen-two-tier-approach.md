# A Generalizable Two-Tier Voluntary Security Attestation Guideline

_**Status of this document**_

**This is a draft document and may be updated, replaced or obsoleted at any
time. It is inappropriate to cite this document as other than a work in
progress. Publication of this document as a draft does not imply endorsement
by the Eclipse Foundation, Open Regulatory Working Group Members, or
contributors.**

# Revision History

| Revision | Date       | Summary of Changes                          |
| -------- | ---------- | ------------------------------------------- |
| 0.2      | 19.12.2025 | Integrated feedback from ORC WG and GH discussions             |
| 0.1      | 18.11.2025 | Initial proposal by Æva Black to the ORC WG |

## Editor's Notes

- We have adopted "VSA" as an acronym for "voluntary security attestation"
  to provide disambiguation from other technical meanings of "attestation"
  commonplace in our industry today (e.g., Remote Attestation, Hardware
  based Attestations, and RSAA-compliance Attestations in U.S. Federal
  procurement).

- _**TODO:**_ remove "VSA" acronym usage, relegating the disambiguation to
  an annex, and replace the acronym with an approachable term.
- _**TODO:**_ complete various TODO's throughout this draft.
- _**TODO:**_ add citations to explanatory and supportive information (guides, FAQs, etc) in an appendix, and link throughout this proposal.

# Introduction

## Context

1. VSAs primarily benefit Manufacturers by reducing the compliance burden when
   integrating third-party FOSS projects into commercial products, aligning with
   CRA Article 13 and Annex I requirements for due diligence in third-party
   component integration.
1. VSAs may benefit open source maintainers _IF_ they incentivize sustained and
   ongoing support (financial or otherwise) for FOSS projects from manufacturers
   who depend on them, without jeopardizing the non-profit nature of open source
   foundations or stewards or requiring individual open source maintainers to
   form new or burdensome legal entities or commercial endeavours.
1. Enabling this exchange of value will support market dynamics that promote
   both regulatory compliance and long-term sustainability of open source
   ecosystems, addressing the CRA's need for secure and resilient products while
   acknowledging the critical role of open source in modern software supply
   chains.
 
## Why Two Tiers? 
  
1. Open source ecosystems and projects vary widely in every way. Our analysis of
   this diversity, based on feedback gathered before and during the October 2025
   Code & Compliance event, suggests that there is a natural grouping into two
   tiers: projects that have significant institutional support, and projects
   that do not. Therefore, we propose a two-tier approach to VSAs to meet the
   needs of all projects that might wish to issue VSAs.
1. Light-weight VSAs will be designed based on the reasonably foreseeable
   capabilities of the maintainers of open source projects that do not have
   significant commercial support, or those projects which are unlikely to
   require extensive conformity assessments or cryptographic analysis for
   downstream integration.
1. Heavy-weight VSAs will be designed based on the reasonably foreseeable
   capabilities of the maintainers of open source projects that benefit from
   significant commercial support, or those projects which are likely to require
   extensive conformity assessments (e.g. due to their functional equivalence to
   commercial products).
1. This two-tier structure supports both the needs of manufacturers and the
   capabilities of maintainers of open source projects by aligning attestation
   effort with project complexity and available support. 
1. We hope that these tiers may also create an incentive for manufacturers to
   increase support to project maintainers when there is mutual interest in a
   greater security assurance.

## Editor's Assumptions

1. Neither the CRA nor any open source license requires or obliges a maintainer
   of a non-stewarded project to make available a VSA nor to surface the data
   needed for someone else to create one.
1. Some FOSS projects have no commercial use.
1. Some FOSS projects' maintainers have no intention for their code to be used
   commercially, regardless of downstream actions.
1. Some FOSS projects will not produce their own VSA, even if the project has
   commercial applications.
1. Some commercially-popular FOSS projects do not have a steward and their
   maintainers may have no intention of becoming associated with, or supported
   by, a steward.
1. Some FOSS projects, which have a steward and are intended for commercial
   use, are similar in scope and complexity to commercial products placed on
   the market. Such FOSS projects may fall under specific categories of
   Important Class I or II products, or they may be generic products. In such a
   case, applying a full conformity assessment may be feasible and desirable to
   those manufacturers who rely upon the FOSS project.
1. Some FOSS projects, which have a steward and are intended for commercial
   use, would be unduly burdened by the application of a full conformity
   assessment.
1. Some FOSS projects could have a steward who would not issue VSAs now or in
   the future for that project. Therefore, any proposal must account for VSAs
   issued by projects who are in this situation.

# Considerations

## Regarding Maintainers of Open Source Projects

1. Considering the authoritative nature of a maintainer's role in the secure
   development of an open source projects, maintainers are the most reliable
   parties capable of issuing VSAs.

## Regarding Non-Stewarded Projects

1. Considering that a steward who both fulfills the Article 24 obligations and
   issues VSAs will provide market actors -- CSIRTs, MSAs, and Manufacturers,
   and cybersecurity researchers -- with a trustworthy coordination point for a
   scoped set of open source projects;
1. Considering that many open source projects do not currently have this support
   from a _legal entity_ that could be deemed either its manufacturer or
   steward;
1. Considering that such projects none the less provide significant economic and
   societal value;
1. Considering that VSAs could enable new business models and revenue
   streams while protecting the non-manufacturer status of non-stewarded projects, building on the strengths of open source, and providing market actors -- CSIRTs, MSAs, and Manufacturers, and cybersecurity researchers -- with a known coordination point for open source projects.

Therefore, we recommend defining new mechanisms that:
1. Enable currently-non-stewarded projects to become stewarded in a reasonable
   time frame, without undue burdens, and without causing disruption to the
   community responsible for their development and maintenance; and
1. Create an attestation mechanism and business model that adequately address
   manufacturers' needs with respect to their compliance obligations for
   non-stewarded projects and adequately enable project maintainers to be
   compensated fairly and adequately, if desired.

For example, fiscal hosts endowed with sufficient capabilities and expertise may
act as intermediaries to collect and distribute VSA fees from manufacturers to
non-stewarded projects and to provide a trustworthy coordination point between
these non-stewarded projects and CSIRTs, MSAs, manufacturers, and cybersecurity
researchers.

Other models may emerge to facilitate equitable and efficient transactions
between Non-stewarded projects and Manufacturers

All such models should support maintainers' essential role in sustaining their
respective projects and recognize that they are uniquely empowered to decide
how, and under what terms, any attestation, or artifacts needed for an
attestation, will be produced.


## Attestations from Unaffiliated Third Parties

1. Considering that the community of developers who actively maintain an open
   source project constitutes the most knowledgeable experts with respect to
   addressing either the obligations of a steward or the contents of a VSA;
1. Considering that some maintainers may not desire to become stewards;
1. Considering that non-stewarded projects may be used in commercial products
   and their maintainers may desire this;
1. And considering that Manufacturers may wish to continue using these projects;
1. Therefore one or more third parties may wish to produce a VSA for these
   projects.

In these cases, it is beneficial for the necessary project information to be
made publicly available such that third parties can generate VSAs through
machine automatable means, thereby minimizing any burden on the open source
maintainers.

## Attestations for Dependencies

1. Given that it is common for projects to incorporate dependencies into
   distributed binaries, it may be valuable to include VSAs for those
   dependencies. Alternatively, a comprehensive SBOM may enable manufacturers to
   acquire the relevant VSAs for dependencies.
1. If a Steward is issuing VSAs, it should only do so for dependencies that fall
   within their scope of support and for which they have obtained the necessary
   cooperation and commitment from the respective maintainers.
1. Project maintainers must be willing and capable of adhering to documented
   security policies, as the attestation of a project's security practices is
   only meaningful if the individuals with commit access are committed to
   following those practices.
1. When a Steward attests to a project's security policy, it is the
   responsibility of the maintainers to ensure that the policy is implemented
   and followed, as they possess the actual control and ability to effect
   changes.
1. Attestations for dependencies should be limited to those associated with the
   steward, as it is unreasonable to expect a steward to attest to the security
   practices of dependencies that are not supported or maintained by the same
   steward.
1. If a project is not associated with a steward, the responsibility for
   attesting to its dependencies lies with the project maintainers themselves,
   who must ensure that the necessary documentation is made available to enable
   a third party to produce an attestation.
1. Stewards may include a statement in their VSA indicating which dependencies
   are covered by their attestation and which are not, in order to avoid
   confusion and to clearly delineate the scope of their support and
   responsibility.
   
**[ FIXME: there are more edge cases that need to be covered here ]**

# Recommendations 

**[ FIXME: integrate more recommendations from other sections into this one ]**

## Recommendations for Maintainers of Projects Used in Products

1. Maintainers may wish to produce VSAs for projects they are responsible for.
1. Maintainers may wish to explore options to associate with a steward or
   a fiscal host that can act as an intermediary.
1. Maintainers may wish to make publicly available the necessary artifacts to
   enable the automated creation of third-party attestations for their projects.

## Recommendations for Stewards

1. Due to the obligations of stewards described in CRA Article 24, and their
   relationship to specific open source projects, stewards should produce VSAs
   for projects to which they offer "sustained and ongoing support."
1. Stewards should support tasks associated with producing VSAs that maintainers
   do not wish to perform.
1. Stewards who produce VSAs for second-party projects (i.e., those their
   projects depend on) should indicate the nature of the relaionship.

## Recommendations for both Maintainers and Stewards

1. Maintainers and Stewards may produce VSAs for their project's dependencies;
   if done, they should clearly document the relationship between the issuer of
   the VSA and the subject of the VSA.
1. Maintainers and Stewards should not produce VSAs for projects that are not
   associated with their activities.
1. Maintainers and Stewards may publish VSAs in multiple ways, including but not
   limited to:
   1. By placing a `COMPLIANCE.MD` file in the project's root directory (i.e.,
      alongside the `LICENSE.MD` file)
   1. By providing a digitally-signed file publicly, to limited groups (e.g.,
      based on membership), or uniquely to individual entities.
   1. By uploading an appropriate file to a public or private attestation
      repository of appropriate scope, if such exists.
   1. By writing a relevant entry in non-repudiable public digital records,
      such as in a [Rekor](https://github.com/sigstore/rekor) or [SCITT](https://datatracker.ietf.org/wg/scitt/about/) log entry.

## Recommendations for Manufacturers

1. Manufacturers should include in their due diligence an assessment of the
   maintenance activities (e.g., active development, presence of vulnerability
   handling procedures, etc) of open source projects they rely on.
1. When possible, select open source projects that have already have a
   conformity self-assessment or third-party assessment in the form of a VSA.
1. Alternatively, support the maintainers of open source projects in creating
   such documentation, either directly or through a stewarding organization (if
   present).
   
# Light Weight VSAs

## Summary

**[ FIXME: reformat the Summary section ]**

1. A minimalist voluntary security attestation should clearly convey the
   following information:
- The legal entity authoring the attestation, and that entity's relationship to
  the project.
- The date the attestation was issued.
- The open source project(s) to which the attestation pertains, identified by
  name, version, and URL.
  - If the attestation pertains to a specific source code version, then it
    should include the relevant version control identifier, such as a Git
    Commit ID.
  - If the attestation pertains to a specific binary release, then it should
    include the cryptographic fingerprint, such as a SHA256 checksum, of that
    release.
- Where to find documentation regarding the project's cybersecurity policy,
  inculding how to report vulnerabilities to the project (e.g., CONTRIBUTING.md
  or SECURITY.md).
- Where to find documentation regarding the expected use and secure
  configuration of the project (e.g., README.md or INSTALLATION.md).
- How to subscribe to receive the project's public security notifications
  (e.g., an RSS feed or mailing list).

1. To simplify downstream compliance activities without disrupting current
   development practices, we recommend that projects adopt a new document, such as
   by placing the template below in a `COMPLIANCE.MD` file and filling out the
   relevant portions.

## Mapping to the Articles

By providing a light-weight VSA, an open source project supports manufacturers
fulfilling the following specific obligations:

- **13.1:** It is not expected that a light-weight VSA will address Annex I Part
  I.
- **13.2:** Manufacturers must select open source projects appropriate for their
  product context and foreseeable use. To support this, open source projects
  should clearly document their projects usage and intended functionality
  (GV.03). Projects which remediate vulnerabilities in a timely manner (VM.02),
  maintain repeatable test procedures (QA.04), mitigate memory-safety
  vulnerabilities (QA.06), require code review (QA.07), and distribute updates
  in a cryptograhically-verifiable way (BR.03) support the manufacturer's
  requirement to minimize cybersecurity risks and prevent incidents.
- **13.3:** To fulfil their update obligations, Manufacturers should select open
  source projects that are actively maintained (EL.01) and which are supported
  by coordinated vulnerability disclosure efforts (QA.03, VM.01, VM.02). If
  using open source projects which do not fulfil those requirements, the
  Manufacturer must take on these responsibilities.
- **13.4:** Manufacturers who do not wish to disclose the open source projects
  used in their products must still consider open source when developing their
  risk assessment. By providing documentation (GV.03), license transparency
  (LE.01), and SBOMs (LE.02), open source projects help manufacturers fulfill
  this requirement.
- **13.5:** Manufacturers must exercise due diligence when integrating third
  party open source components. All activities contemplated herein support this.
- **13.6:** By providing a reliable point of contact for vulnerability
  disclosures (VM.01, VM.02), open source projects can support manufacturer's
  obligation to report identified vulnerabilities and share relevant fixes.
- **13.7:** By providing a cybersecurity risk assessment, open source projects
  can support manufacturers obligation to document the relevant cybersecurity
  aspects and update the cybersecurity risk assessment of their products. _**Not
  addressed.**_
- **13.8:** By disclosing information regarding vulnerabilities and their
  remediation (VM.02), and providing notice when ending support for the project
  or versions thereof (EL.01), open source projects support manufactuers
  obligation to effectively handle vulnerabilities in the product throughout its
  support period.
- **13.12:** By providing documentation regarding usage (GV.03), testing
  (QA.04), and build (BR.01) procedures, open source projects support
  manufacturers requirement to draw up technical documentation.
- **14.1:** By publishing information about discovered vulnerabilities in a
  timely fashion (VM.02), open source projects support manufacturers obligation
  to detect exploitable vulnerabilities and report on them.

## Template

Mapping table between CRA Requirements and the attached "Light Weight Template".

| CRA Requirement      | Template Section                                       | Author's Notes                           |
| -------------------- | ------------------------------------------------------ | ---------------------------------------- |
| Annex I Part I.1     | _not addressed_                                        | risk assessment                          |
| Annex I Part I.2(a)  | _not addressed_                                        | no known exploitable vulns               |
| Annex I Part I.2(b)  | _not addressed_                                        | secure by default configs                |
| Annex I Part I.2(c)  | _not addressed_                                        | automatic updates                        |
| Annex I Part I.2(d)  | _not addressed_                                        | enforce IAM and SIEM controls            |
| Annex I Part I.2(e)  | _not addressed_                                        | protect data confidentiality             |
| Annex I Part I.2(f)  | _not addressed_                                        | protect program and data integrity       |
| Annex I Part I.2(g)  | _not addressed_                                        | data minimisation                        |
| Annex I Part I.2(h)  | _not addressed_                                        | protect availability                     |
| Annex I Part I.2(i)  | _not addressed_                                        | minimize impact on other products        |
| Annex I Part I.2(j)  | _not addressed_                                        | limit attack surfaces                    |
| Annex I Part I.2(k)  | _not addressed_                                        | include exploit mitigation techniques    |
| Annex I Part I.2(l)  | _not addressed_                                        | monitor security-relevant activity       |
| Annex I Part I.2(m)  | _not addressed_                                        | secure delete functionality              |
| Annex I Part II.1    | LE.02, QA.01                                           | SBOM                                     |
| Annex I Part II.2    | VM.02, BR.04                                           | vuln remediation & security patches      |
| Annex I Part II.3    | QA.04, QA.05                                           | testing procedures                       |
| Annex I Part II.4    | QA.04, BR.04                                           | vuln disclosure                          |
| Annex I Part II.5    | VM.02                                                  | CVD policy                               |
| Annex I Part II.6    | QA.03, VM.01                                           | vuln information sharing                 |
| Annex I Part II.7    | BR.03                                                  | secure distribution of updates           |
| Annex I Part II.8    | BR.04                                                  | timely and free security updates         |
| Annex II.1           | AU.01, AU.02                                           | registered entity information            |
| Annex II.2           | VM.01, QA.03                                           | vulnerability reporting contact point    |
| Annex II.3           | AU.03, QA.02, BR.02                                    | project identification                   |
| Annex II.4           | GV.03                                                  | intended purpose and essential functions |
| Annex II.5           | _not addressed_                                        | foreseeable cybersecurity risks          |
| Annex II.6           | _not applicable_                                       | EU declaration of conformity             |
| Annex II.7           | _not applicable_                                       | technical support docs                   |
| Annex II.8 (a) - (e) | _not adressed_                                         | product lifecycle docs                   |
| Annex II.8(f)        | _not addressed_                                        | integration docs                         |
| Annex II.9           | QA.01                                                  | public SBOM URL                          |
| Annex VII.1(a) & (d) | GV.03                                                  | intended purpose and user docs           |
| Annex VII.1(b)       | BR.04, VM.02, EL.01                                    | version history                          |
| Annex VII.1(c)       | _not applicable_                                       | hardware architecture                    |
| Annex VII.2(a)       | GV.01, GV.02, LE.01, LE.02, QA.02, QA.04, QA.05, BR.01 | internal design documentation            |
| Annex VII.2(b)       | QA.03, LE.01, LE.02, BR.03, VM.01, VM.02               | vulnerability handling documentation     |
| Annex VII.2(c)       | GV.01, GV.02, QA.04, QA.06, QA.07, BR.01               | development process documentation        |
| Annex VII.3          | _not addressed_                                        | cybersecurity risk assessment            |
| Annex VII.4          | EL.01                                                  | support period                           |
| Annex VII.5          | _not applicable_                                       | list of applied harmonized standards     |
| Annex VII.6          | _not addressed_                                        | conformity assessment & test reports     |
| Annex VII.7          | _not applicable_                                       | copy of EU declaration of conformity     |
| Annex VII.8          | LE.02, QA.01                                           | SBOM available upon request              |

# Heavy Weight VSAs

## Summary

**[ FIXME: reformat the Summary section ]**

Whereas larger and more "product-like" open source projects are likely to
require a substantially greater relative effort, compared to individual open
source components, when a manufacturer seeks to demonstrate conformity to Annex
I Part I and thereby fulfill obligations under Article 13.1;

Whereas the performance of, and authoring documentation regarding, a
cybersecurity risk assessment is most appropriately done by the community of
maintainers and developers of an open source project;

It is therefore recommended that heavy-weight VSAs demonstrate conformity to the
essential requirements of Annex I Part I, and where applicable, document
conformity to one or more relevant Annex III Class I or Class II products and
the relevant harmonized standards.

## Status 

Until there is clear and public guidance available regarding the CRA harmonized
standards which could be applied to provide a presumption of conformity, this
section is likely to be limited to providing only limited guidance based on
publicly available drafts of the in-development standards. 

**[ FIXME: draft guidance for heavy-weight attestations ]**
