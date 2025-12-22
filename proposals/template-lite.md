
Proposed Template for Light Weight VSAs
===

Edit History
---

| Revision | Date | Summary of Changes |
| --- | ---------- | --- |
| 0.1 | 18.11.2025 | Initial proposal by Æva Black to the ORC WG |

Introduction
---
_**TODO: Write introductory verbiage**_

_**Editor's Note: The checklist below is derived from [BSI
TR-03185-2](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03185/BSI-TR-03185-2.html).**_

Template
---

```
Authorship
- [ ] AU.01: Information regarding the software producer issuing the attestation:
      Name of Issuing Entity: _________________________________________
      Registered Address:     _________________________________________
      Website:                _________________________________________
- [ ] AU.02: State your name and role in the organization: 
      Primary Contact:        _________________________________________
      Organizational Role:    _________________________________________
- [ ] AU.03: List all project(s) to which the attestation applies:
      Project Name:           _________________________________________
      Project URL:            _________________________________________
      Valid For Version(s):   _________________________________________
      Valid For Date(s):      _________________________________________

Governance
- [ ] GV.01: The Project shall include a contribution guideline. 
      Documentation Link:     _________________________________________
- [ ] GV.02: The Project's contribution guideline should set a 
      quality standard for contributions. Check this box to confirm.
- [ ] GV.03: The Project shall include documentation about its usage and
      intended purpose or functionality.
      Documentaiton Link:     __________________________________________

Licensing
- [ ] LE.01: All Project components, including binaries and documentation, 
      shall be publicly available under an open source license.
      License File Link:      _________________________________________
- [ ] LE.02: The Project's dependencies, including requirements for 
      reproducing the project's distributed binaries, should available under 
      an open source license. If this is true, check this box.
      If this is not true, please explain: ____________________________

Quality 
- [ ] QA.01: The Project shall document, or otherwise include a list of,
      all direct third-party dependencies. This list should include
      cryptographically unique identifiers (checksums) where applicable.
      Link to SBOM or lockfile: _______________________________________
- [ ] QA.02: The Project's source code, including change history, shall be
      publicly available. 
      Link to source control: _________________________________________
- [ ] QA.03: The Project shall include documentation describing how to file a
      vulnerability report.
      Link to reporting guide:  _______________________________________
- [ ] QA.04: The Project shall include repeatable test procedures. 
      These may be automated in a CI/CD pipeline, but do not need to be. 
      Link to test procedure documentation: ___________________________
- [ ] QA.05: If the project relies on code written in non-memory-safe languages, 
      the Project shall include mitigations for memory safety vulnerabilities.  This
      may include, for example, minimum contribution guidelines or automated tests to
      verify that changes do not introduce common types of memory safety errors.
      Check this box if there are mitigations for memory safety vulnerabilities.
- [ ] QA.06: Projects should have more than one active contributor.  Check this
      box to confirm that this is true.
- [ ] QA.07: Projects that have more than one active contributor should require
      change review.  Check this box to confirm that all changes are reviewed by at
      least one human non-author.

Build and Release
- [ ] BR.01: The Project shall document how to build it from source code.
      Link to build documentation here: _______________________________
- [ ] BR.02: All Project releases intended for use shall be assigned unique and 
      monotonically increasing version identifiers. 
      Check this box to confirm that this is true. 
      Link to release documentation or history: _______________________
- [ ] BR.03: All released assets shall be distributed in a way that maintains
      integrity, or at a minimum allows the verification thereof, and the means to
      verify this shall be documented. Check this box to confirm that this is true.
      Link to integrity verification instructions: ____________________
- [ ] BR.04: All releases shall include a descriptive log of functional and
      security changes.  Check this box to confirm that this is true.
      Link to release documentation or history: _______________________

Vulnerability Management
- [ ] VM.01: The Project shall indicate at least one security contact for
      reporting vulnerabilities.
      Reporting contact information: __________________________________
      If there is a way to report vulnerabilities privately and securely,
      provide a link to the instructions here: ________________________
- [ ] VM.02: The Project shall publish information about discovered
      vulnerabilities within a reasonable period of time, including mitigation
      instructions if available.  Check this box to confirm that there is such
      a policy in place.

End-of-Life
- [ ] EL.01: The discontinuation of support for the Project, parts of it, 
      or specific versions of it should be communicated adequately. 
      Check this box to indicate that the Project has such a policy.
      If this is publicly documented, 
      link to it here:    _____________________________________________

```
