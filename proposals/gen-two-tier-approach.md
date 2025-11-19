A Generalizable Two-Tier Voluntary Security Attestation Guideline
===

_**Editor's Notes**_:
- We have adopted "VSA" as an acronym for "voluntary security attestation"
  to provide disambiguation from other technical meanings of "attestation"
  commonplace in our industry today (e.g., Remote Attestation, Hardware 
  based Attestations, and RSAA-compliance Attestations in U.S. Federal
  procurement).
- _**TODO:**_ add a definition/citation for "Project."
- _**TODO:**_ complete various TODO's throughout this draft.


Edit History
---

| Revision | Date | Summary of Changes |
| --- | ---------- | --- |
| 0.1 | 18.11.2025 | Initial proposal by Æva Black to the ORC WG |



Overall Recommendations
---
1. Stewards should produce VSAs only for projects to which they offer 
   "sustained and ongoing support." 
1. Stewards may produce VSAs for their project's dependencies; if done, the
   Steward should clearly document the relationship between the subject of the
   VSA and the project which the Steward supports.
1. Stewards should not produce VSAs for projects that are not associated with
   the Steward's activities.
1. Stewards may publish VSAs in multiple ways, including:
   1. By placing a `COMPLIANCE.MD` file in the project's root directory (i.e.,
      alongside the `LICNESE.MD` file)
   1. By providing a digitally-signed file to members of the non-profit legal
      entity.
   1. By providing a digitally-signed file in exchange for a reasonable fee.
   1. By uploading an appropriate file to a central or national attestation
      repository, if such exists in the future.
   1. By writing a relevant entry in non-repudiable public digital records,
      such as in a Rekor or SCITT log entry.
1. Considering that manufacturers are responsible for all components used in
   their products, including 3rd party FOSS components, manufacturers may
   significatly reduce their compliance efforts by selecting FOSS components
   with proactive Stewards. 
    1. To do this, manufacturers should review the relevant documentation from
       Stewarded FOSS projects and either: 
       (a) rely on the FOSS project's VSA if it is sufficient, or 
       (b) provide support to the FOSS project to
       produce a VSA sufficient for the manufacturer's compliance requirements.


Assumptions
---
1. Some FOSS projects are not intended for commercial use.
1. Some FOSS projects do not have a Steward and have no intention of becoming
   associated with, or supported by, a Steward.
1. Some FOSS projects will not produce their own VSA, even if the project has
   commercial applications.
1. Some FOSS projects, which have a Steward and are intended for commercial
   use, are similar in scope and complexity to commercial products placed on
   the market. Such FOSS projects may fall under specific categories of
   Important Class I or II products, or they may be generic products. In such a
   case, applying a full conformity assessment may be feasible and desirable to
   those manufacturers who rely upon the FOSS project.
1. Some FOSS projects, which have a Steward and are intended for commercial
   use, would be unduly burdened by the application of a full conformity
   assessment


Attestations for Non-Stewarded Projects
---
1. Considering that a Steward who fulfils its Obligations and issues VSAs will
   provide market actors -- CSIRTs, MSAs, and Manufacturers, and cybersecurity
   researchers -- with a trustworthy coordination point for their open source
   projects;
1. Considering that an open source project which has neither manufacturer nor
   steward has no legal entity capable of claiming to fulfill said obligations
   (for if it did, that entity would be its steward or its manufacturer);
1. Considering that there are numerous examples of non-stewarded projects which
   none the less provide significant economic and societal value;
1. Therefore, a path must be defined which either: 
    1. enables currently-non-stewarded to become stewarded in a reasonable time
       frame, without undue burdens, and without causing disruption to the
       community responsiblef or their development and maintenance; or
    1. creates an attestation scheme which adequately addresses manufacturers'
       needs with respect to their compliance obligations for such
       non-stewarded projects as they rely on today.


Attestations from Parties who are not the Steward
---
1. Considering that the community of developers who actively maintains an open
   source project constitutes the most knowledgeable experts with respect to
   addressing the obligations of a steward;
1. ...

_**TODO: Finish This Section**_


Light Weight VSAs
=== 

Summary
---

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

Mapping to the Articles
---

By providing a light-weight VSA, an open source project supports manufacturers fulfilling the following specific obligations:
- **13.1:** It is not expected that a light-weight VSA will address Annex I Part I. 
- **13.2:** Manufacturers must select open source projects appropriate for their product context and foreseeable use. To support this, open source projects should clearly document their projects usage and intended functionality (GV.03). Projects which remediate vulnerabilities in a timely manner (VM.02), maintain repeatable test procedures (QA.04), mitigate memory-safety vulnerabilities (QA.06), require code review (QA.07), and distribute updates in a cryptograhically-verifiable way (BR.03) support the manufacturer's requirement to minimize cybersecurity risks and prevent incidents.
- **13.3:** To fulfil their update obligations, Manufacturers should select open source projects that are actively maintained (EL.01) and which are supported by coordinated vulnerability disclosure efforts (QA.03, VM.01, VM.02). If using open source projects which do not fulfil those requirements, the Manufacturer must take on these responsibilities.
- **13.4:** Manufacturers who do not wish to disclose the open source projects used in their products must still consider open source when developing their risk assessment. By providing documentation (GV.03), license transparency (LE.01), and SBOMs (LE.02), open source projects help manufacturers fulfill this requirement.
- **13.5:** Manufacturers must exercise due diligence when integrating third party open source components. All activities contemplated herein support this.
- **13.6:** By providing a reliable point of contact for vulnerability disclosures (VM.01, VM.02), open source projects can support manufacturer's obligation to report identified vulnerabilities and share relevant fixes.
- **13.7:** By providing a cybersecurity risk assessment, open source projects can support manufacturers obligation to document the relevant cybersecurity aspects and update the cybersecurity risk assessment of their products. _**Not addressed.**_  
- **13.8:** By disclosing information regarding vulnerabilities and their remediation (VM.02), and providing notice when ending support for the project or versions thereof (EL.01), open source projects support manufactuers obligation to effectively handle vulnerabilities in the product throughout its support period.
- **13.12:** By providing documentation regarding usage (GV.03), testing (QA.04), and build (BR.01) procedures, open source projects support manufacturers requirement to draw up technical documentation.
- **14.1:** By publishing information about discovered vulnerabilities in a timely fashion (VM.02), open source projects support manufacturers obligation to detect exploitable vulnerabilities and report on them.



Template
---

Mapping table between CRA Requirements and the attached "Light Weight Template".


| CRA Requirement | Template Section | Author's Notes |
| --------------- | ---------------- | -------------- |
| Annex I Part I.1    | _not addressed_ | risk assessment |
| Annex I Part I.2(a) | _not addressed_ | no known exploitable vulns |
| Annex I Part I.2(b) | _not addressed_ | secure by default configs  |
| Annex I Part I.2(c) | _not addressed_ | automatic updates |
| Annex I Part I.2(d) | _not addressed_ | enforce IAM and SIEM controls |
| Annex I Part I.2(e) | _not addressed_ | protect data confidentiality  |
| Annex I Part I.2(f) | _not addressed_ | protect program and data integrity     |
| Annex I Part I.2(g) | _not addressed_ | data minimisation |
| Annex I Part I.2(h) | _not addressed_ | protect availability |
| Annex I Part I.2(i) | _not addressed_ | minimize impact on other products | 
| Annex I Part I.2(j) | _not addressed_ | limit attack surfaces |
| Annex I Part I.2(k) | _not addressed_ | include exploit mitigation techniques |
| Annex I Part I.2(l) | _not addressed_ | monitor security-relevant activity |
| Annex I Part I.2(m) | _not addressed_ | secure delete functionality |
| Annex I Part II.1   | LE.02, QA.01 | SBOM |
| Annex I Part II.2   | VM.02, BR.04 | vuln remediation & security patches |
| Annex I Part II.3   | QA.04, QA.05 | testing procedures |
| Annex I Part II.4   | QA.04, BR.04 | vuln disclosure  |
| Annex I Part II.5   | VM.02 | CVD policy |
| Annex I Part II.6   | QA.03, VM.01 | vuln information sharing |
| Annex I Part II.7   | BR.03 | secure distribution of updates |
| Annex I Part II.8   | BR.04 | timely and free security updates |
| Annex II.1 | AU.01, AU.02 | registered entity information |
| Annex II.2 | VM.01, QA.03 | vulnerability reporting contact point |
| Annex II.3 | AU.03, QA.02, BR.02 | project identification |
| Annex II.4 | GV.03 | intended purpose and essential functions |
| Annex II.5 | _not addressed_  | foreseeable cybersecurity risks |
| Annex II.6 | _not applicable_ | EU declaration of conformity |
| Annex II.7 | _not applicable_ | technical support docs | 
| Annex II.8 (a) - (e) | _not adressed_ | product lifecycle docs |
| Annex II.8(f) | _not addressed_ | integration docs |
| Annex II.9    | QA.01 | public SBOM URL |
| Annex VII.1(a) & (d) | GV.03 | intended purpose and user docs |
| Annex VII.1(b) | BR.04, VM.02, EL.01 | version history |
| Annex VII.1(c) | _not applicable_ | hardware architecture |
| Annex VII.2(a) | GV.01, GV.02, LE.01, LE.02, QA.02, QA.04, QA.05, BR.01 | internal design documentation |
| Annex VII.2(b) | QA.03, LE.01, LE.02, BR.03, VM.01, VM.02 | vulnerability handling documentation |
| Annex VII.2(c) | GV.01, GV.02, QA.04, QA.06, QA.07, BR.01 | development process documentation |
| Annex VII.3    | _not addressed_ | cybersecurity risk assessment |
| Annex VII.4    | EL.01 | support period |
| Annex VII.5    | _not applicable_ | list of applied harmonized standards |
| Annex VII.6    | _not addressed_ | conformity assessment & test reports |
| Annex VII.7    | _not applicable_ | copy of EU declaration of conformity |
| Annex VII.8    | LE.02, QA.01 | SBOM available upon request |



Heavy Weight VSAs
===

Summary
---

Whereas larger and more "product-like" open source projects are likely to require a substantially greater relative effort, compared to individual open source components, when a manufacturer seeks to demonstrate conformity to Annex I Part I and thereby fulfill obligations under Article 13.1;

Whereas the performance of, and authoring documentation regarding, a cybersecurity risk assessment is most appropriately done by the community of maintainers and developers of an open source project;

It is therefore recommended that heavy-weight VSAs demonstrate conformity to the essential requirements of Annex I Part I, and where applicable, document conformity to one or more relevant Annex III Class I or Class II products and the relevant harmonized standards.


Template
---

Template: [template-heavy.md]