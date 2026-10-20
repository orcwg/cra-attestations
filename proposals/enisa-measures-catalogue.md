# A Measures Catalogue for Voluntary Security Attestations

_Based on the ENISA Secure by Design and Default Playbook_

_**Status of this document**_

**This is a draft document and may be updated, replaced or obsoleted at any time. It is inappropriate to cite this document as other than a work in progress. Publication of this document as a draft does not imply endorsement by the Eclipse Foundation, Open Regulatory Compliance Working Group Members, or contributors.**

# Revision History
| Revision | Date       | Summary of Changes                                  |
| -------- | ---------- | --------------------------------------------------- |
| 0.1      | 20.10.2026 | Initial proposal by sebtiem to the ORC WG              |

## Editor's Notes
- _**TODO:**_ verify all CRA references against Annex C of the ENISA Playbook.
- _**TODO:**_ review the remaining design playbooks (4.1 to 4.12) for further
  Heavy-Weight measures.
- _**TODO:**_ agree on a versioning and governance model for the catalogue.

# Introduction
## Purpose
This proposal complements the [two-tier approach](./gen-two-tier-approach.md) and the [Light-Weight template](./template-lite.md). It does **not** change either of them.

Instead, it proposes a separate, versioned **measures catalogue**: a practical guide that explains, item by item, how a project can meet a template item, and which evidence a manufacturer can expect. An attestation stays short and stable; it simply references the catalogue version it was written against.

The catalogue draws on the [ENISA Secure by Design and Default Playbook v1.0](https://www.enisa.europa.eu/sites/default/files/2026-07 ENISA_Secure_By_Design_and_Default_Playbook_v1.pdf) (July 2026), whose playbooks each define a checklist, minimum evidence and a release gate. Many of these map directly onto practices open source projects already follow.

## Why a Separate Catalogue?
1. **Stable attestations.** Template items do not change when guidance evolves. A new catalogue version can tighten or relax measures without invalidating attestations issued against an earlier version.
2. **Automatable evaluation.** The group agreed (22.09.2026) that manufacturers must be able to ingest and evaluate attestations automatically. Concrete measures with defined evidence can be checked by tools; abstract statements cannot.
3. **Replaceable reference.** Once harmonised standards under the CRA are cited in the Official Journal, the Heavy-Weight part of the catalogue can be aligned with them, without touching the templates.

## Design Principles
1. **No new obligations.** The catalogue is guidance. Nothing in it obliges a maintainer to do anything; maintainers decide how, and under what terms, an attestation is produced.
2. **Complement, not replace, BSI TR-03185-2.** The Light-Weight template is derived from [BSI TR-03185 part 2](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03185/tr-03185.html).
    Catalogue entries reference template item IDs, so the link to the TR is kept.
3. **Do not raise the Light-Weight bar.** Each Light-Weight entry defines a **baseline** measure that reflects current, widespread practice. Stricter measures from the ENISA Playbook are listed as **enhanced** and are always optional.
4. **Heavy-Weight is interim.** Heavy-Weight measures are offered as input until harmonised standards are available. They do not pre-empt the group's open decision on whether Heavy-Weight attestations should involve a full conformity assessment.
5. **Tool-neutral.** Tools and formats are named as examples. Any equivalent means of meeting a measure is acceptable.

## Two Axes: Tier and Evidence Level
The catalogue keeps the existing tiers and adds an evidence level, so that a claim can be strengthened without starting over.

| Axis           | Values                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------ |
| Tier           | **Light-Weight** (CRA Annex I Part II) · **Heavy-Weight** (adds Annex I Part I)            |
| Evidence level | **E1** self-declared, with link · **E2** machine-verifiable artefact (signature, SBOM, provenance, CI result) · **E3** independently verified |

This reflects ENISA's own distinction: an attestation is a claim, while verification is a separate step.

## How an Attestation References the Catalogue
The template remains unchanged. An issuer may add the catalogue version and, per item, the evidence level:

```
Catalogue: ORC WG VSA Measures Catalogue, version 0.1
- [x] QA.01: The Project must document [...] all direct third-party dependencies.
      Link to SBOM or lockfile: https://example.org/releases/1.4.0/sbom.cdx.json
      Measure: M-QA.01 (enhanced), Evidence level: E2
```

# Catalogue Entry Format
| Field          | Meaning                                                        |
| -------------- | -------------------------------------------------------------- |
| ID             | `M-<template item>` for Light-Weight, `H-<topic>` for Heavy-Weight |
| Question       | The practical question a maintainer or manufacturer asks       |
| Baseline       | Minimum measure that satisfies the item                        |
| Enhanced       | Optional, stricter measure from the ENISA Playbook             |
| Evidence       | What is attested, and at which evidence level                  |
| References     | ENISA Playbook section, CRA reference (indicative)             |

# Part A: Light-Weight Measures (Annex I Part II)

### M-VM.01 / M-QA.03: Security Contact and Reporting
**Question:** How can someone report a vulnerability to the project?

- **Baseline:** A `SECURITY.md` (or equivalent) names at least one security contact and explains how to report privately, for example via a forge's private vulnerability reporting or a dedicated e-mail address.
- **Enhanced:** A documented coordinated vulnerability disclosure process with expected response times; contact data also published in an [OpenSSF Security Insights](https://github.com/ossf/security-insights-spec) file.
- **Evidence:** E1 link to the document; E2 Security Insights file.
- **References:** ENISA Playbook 4.13; CRA Annex I Part II (5), (6).

### M-VM.02: Publishing Vulnerability Information
**Question:** How does the project inform users about fixed vulnerabilities?

- **Baseline:** Advisories are published within a reasonable period, including mitigation instructions where available, for example as forge security advisories or on a mailing list.
- **Enhanced:** Machine-readable advisories (CSAF) and affectedness statements (VEX, for example CSAF VEX, CycloneDX VEX or OpenVEX).
- **Evidence:** E1 link to advisories; E2 CSAF/VEX documents.
- **References:** ENISA Playbook 4.13; CRA Annex I Part II (2), (4).

### M-QA.01: Dependencies and SBOM
**Question:** How does a manufacturer learn what a release contains?

- **Baseline:** A lockfile or dependency list with checksums, as required by QA.01.
- **Enhanced:** An SBOM per release in CycloneDX (1.6 or later) or SPDX (3.0.1 or later), linked to the release and ideally signed. ENISA notes that pinning improves reproducibility but does not establish trust in a component.
- **Evidence:** E1 link; E2 SBOM file bound to the release artefact.
- **References:** ENISA Playbook 4.7, 4.14; CRA Annex I Part II (1).

### M-BR.03: Release Integrity
**Question:** How can a user verify that a release has not been tampered with?

- **Baseline:** Checksums are published and the verification procedure is documented, as required by BR.03.
- **Enhanced:** Release artefacts are signed, for example with Sigstore or OpenPGP, and verification instructions are published.
- **Evidence:** E1 link to instructions; E2 signature verifiable by tooling.
- **References:** ENISA Playbook 4.14; CRA Annex I Part II (7).

### M-QA.07: Change Review

**Question:** How does the project ensure that changes are reviewed?

- **Baseline:** Every change is reviewed by at least one human non-author, as required by QA.07 (where QA.06 applies).
- **Enhanced:** Protected default branch, no force pushes, mandatory review enforced by the forge, `CODEOWNERS` for sensitive areas. These can be checked automatically, for example with [OpenSSF Scorecard](https://github.com/ossf/scorecard) (Branch-Protection, Code-Review).
- **Evidence:** E1 statement; E2 forge settings or Scorecard result.
- **References:** ENISA Playbook 4.9; CRA Annex VII 2(c).

### M-QA.04 / M-QA.05: Testing and Memory Safety
**Question:** How does the project prevent common classes of defects?

- **Baseline:** Repeatable, documented test procedures (QA.04) and mitigations for memory-safety issues where non-memory-safe languages are used (QA.05).
- **Enhanced:** Automated tests, static analysis and dependency scanning in CI; fuzzing where appropriate; AI-generated contributions are subject to the same review and analysis as any other code.
- **Evidence:** E1 link to documentation; E2 CI configuration and results.
- **References:** ENISA Playbook 4.9; CRA Annex I Part II (3).

### M-EL.01: Support Period and End of Life
**Question:** How long will a version receive security fixes?

- **Baseline:** A documented support policy; discontinuation is communicated adequately, as required by EL.01.
- **Enhanced:** Lifecycle information published in machine-readable form, for example using the Common Lifecycle Enumeration (ECMA-428).
- **Evidence:** E1 link to policy; E2 machine-readable lifecycle data.
- **References:** ENISA Playbook 4.7; CRA Annex VII (4).

# Part B: Heavy-Weight Measures (Annex I Part I)
These measures have no counterpart in the Light-Weight template. They are
proposed as interim content for the Heavy-Weight template.

### H-TM: Threat Model
**Question:** Which threats has the project considered?
- **Measure:** A minimal, maintained threat model covering the five to ten most relevant threats, using a method such as STRIDE, revisited on significant change. The gen-two-tier mapping currently marks 13.7 and Annex VII.3 as "not addressed"; this measure would address them.
- **Evidence:** E1 document in the repository; E2 structured threat model, for example a CycloneDX TM-BOM.
- **References:** ENISA Playbook chapter 2; CRA Annex I Part I (1), Annex VII (3).

### H-PROV: Build Provenance
**Question:** Can a manufacturer trace a release back to its source and build?
- **Measure:** Signed build provenance at a declared SLSA Build level, for example as in-toto attestations.
- **Evidence:** E2 provenance verifiable by tooling.
- **References:** ENISA Playbook 4.14; CRA Annex I Part I 2(f).

### H-BUILD: Build Environment
**Question:** How is the build protected against tampering?
- **Measure:** Builds run in isolated, ephemeral environments; hermetic or reproducible builds where feasible.
- **Evidence:** E1 documented build setup; E2 reproducibility evidence.
- **References:** ENISA Playbook 4.14; CRA Annex I Part I 2(f).

### H-DEP: Dependency Evaluation
**Question:** How does the project decide which dependencies to trust?
- **Measure:** Dependencies are evaluated before adoption and periodically, beyond pinning, for example using the OWASP SCVS questionnaire or Scorecard results of the dependencies.
- **Evidence:** E1 documented policy; E2 evaluation records.
- **References:** ENISA Playbook 4.14; CRA Annex I Part I 2(a).

### H-CRYPTO: Cryptography
**Question:** How does the project use cryptography?
- **Measure:** No self-developed cryptographic primitives; used cryptographic libraries and algorithms are documented.
- **Evidence:** E1 documentation; E2 cryptography inventory, for example a CycloneDX CBOM.
- **References:** ENISA Playbook 4.6; CRA Annex I Part I 2(e), 2(f).

### H-COMM: Secure Communication
**Question:** Is communication protected by default?
- **Measure:** No fallback to plaintext protocols; cryptographic agility; an assessment whether the support period requires preparation for post-quantum cryptography.
- **Evidence:** E1 documentation; E2 configuration or test results.
- **References:** ENISA Playbook 4.17; CRA Annex I Part I 2(e), 2(f).

## Out of Scope
ENISA Playbooks 4.18 to 4.22 (device identity, mandatory onboarding, automatic updates, security status display, recovery and ownership transfer) concern the finished product and remain the manufacturer's responsibility.

# FAQ
**Does this catalogue create new obligations for maintainers?**
No. It describes ways to meet template items. Maintainers choose which measures
and evidence levels they attest, and to whom.

**Why the ENISA Playbook and not the harmonised standards?**
No harmonised standard under the CRA has been cited yet. The Playbook is a
current, EU-level reference whose measures map onto CRA Annex I. Once standards
are cited, the Heavy-Weight part should be aligned with them.

**What if a project only meets the baseline?**
That is a complete Light-Weight attestation. Enhanced measures are optional
and only strengthen individual claims.

**How does a manufacturer use the catalogue?**
For each component, a manufacturer can check which measures are attested and at
which evidence level, and decide per its own risk assessment whether this is
sufficient for its due diligence under Article 13(5). E2 evidence can be
verified automatically.

**How will attestations become machine-readable?**
Out of scope for this proposal. Possible building blocks are CycloneDX
Attestations (CDXA) as a format, Rekor or SCITT for non-repudiation, and the
Transparency Exchange API (TEA) for discovery and distribution.

# Open Questions

1. Who maintains the catalogue, and how are new versions agreed?
2. Should the evidence levels become part of the template itself?
3. Which further ENISA design playbooks belong in the Heavy-Weight part?
4. Do the indicative CRA references match Annex C of the ENISA Playbook?
