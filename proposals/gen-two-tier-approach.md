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
1. Doing this satisfies the following CRA obligations:
- _**TODO: Complete this list of citations**_

Template
---

Template: [template-lite.md]

Heavy Weight VSAs
===

Summary
---

_**TODO: make a formal proposal**


Template
---

Template: [template-heavy.md]