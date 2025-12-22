Proposed Template for Heavy Weight VSAs
===

Edit History
---

| Revision | Date | Summary of Changes |
| --- | ---------- | --- |
| 0.2 | 22.12.2025 | Moved annexes and appendices to implementation guide |
| 0.1 | 22.12.2025 | Initial draft based on two-tier approach and EN 304 617 derivative browser model |

Introduction
---

Heavy-weight Voluntary Security Attestations (VSAs) are designed for open source projects that:

1. Have significant institutional or commercial support
2. Are functionally equivalent to commercial products placed on the market
3. May fall under Important Class I or Class II product categories
4. Require extensive conformity assessments for downstream integration

Unlike light-weight VSAs which provide a minimalist checklist, heavy-weight VSAs provide comprehensive security documentation that enables downstream manufacturers to rely on the attestation for specific CRA requirements, similar to how Upstream Security Documentation (USD) functions in the derivative browser conformity model.

_**Editor's Note: This template is derived from the derivative browser conformity model currently in development for EN 304 617, generalized for broader application to product-like open source projects. The derivative browser conformity model in turn, will be able to depend upon this Heavyweight Template**_

**See also: [Heavy Weight VSA Implementation Guide](template-heavy-implementation-guide.md)** for guidance on requirement inheritance, due diligence, modification-triggered reassessment, update flow, machine-readable format specification, CAB guidance, and CRA requirement mappings.

Scope and Application
---

### When to Use This Template

This template is appropriate when:

1. The project provides functionality equivalent to a product with digital elements
2. Downstream manufacturers require assurance regarding Annex I Part I essential requirements
3. The project has sufficient resources to maintain comprehensive security documentation
4. The project community can commit to ongoing security governance practices

### Relationship to Light-Weight VSAs

Heavy-weight VSAs extend rather than replace light-weight VSAs. A project issuing a heavy-weight VSA should also satisfy all light-weight VSA requirements. The additional content addresses:

1. Detailed security requirement coverage
2. Security governance practices
3. Ongoing maintenance commitments
4. Machine-readable format for automation

---

# Part I: Core Attestation (Normative)

## Section 1: Identification

### 1.1 Project Identification

```
Project Name:           _________________________________________
Project Version Range:  From _____________ To _______________
Repository Location:    _________________________________________
```

### 1.2 Attestation Metadata

```
Attestation Issue Date:     _________________________________________
Attestation Validity End:   _________________________________________
Attestation Version:        _________________________________________
```

### 1.3 Publisher Identification

```
Publisher Name:             _________________________________________
Publisher Type:             [ ] Governance Body  [ ] Steward  [ ] Third Party
Publisher Contact:          _________________________________________
Publisher Website:          _________________________________________
```

NOTE: The publisher type indicates the relationship to the project:
- **Governance Body**: The project's own governance structure (e.g., core maintainers, project steering committee)
- **Steward**: An open source software steward per CRA Article 3(14)
- **Third Party**: An entity conducting assessment on behalf of the governance body or steward

---

## Section 2: Security Governance

### 2.1 Vulnerability Handling

```
- [ ] SG.01: The project maintains a coordinated vulnerability disclosure (CVD) policy.
      CVD Policy URL:       _________________________________________

- [ ] SG.02: The project provides a security contact mechanism.
      Security Contact:     _________________________________________

- [ ] SG.03: The project publishes security advisories for known vulnerabilities.
      Advisory Feed URL:    _________________________________________
      CVE Assignment:       [ ] Yes, via ________________  [ ] No

- [ ] SG.04: The project maintains historical vulnerability response data.
      Median Response Time (Critical/High): _______ days
      Supporting Data URL:  _________________________________________
```

### 2.2 Development Practices

```
- [ ] SG.05: Dependencies are documented in machine-readable format.
      SBOM/Manifest URL:    _________________________________________
      Format:               [ ] SPDX  [ ] CycloneDX  [ ] Other: _______

- [ ] SG.06: Contribution provenance is traceable.
      Mechanism:            [ ] Signed Commits  [ ] DCO  [ ] CLA  [ ] Other: _______

- [ ] SG.07: The project demonstrates active maintenance.
      Last Commit Date:     _________________________________________
      Last Release Date:    _________________________________________

- [ ] SG.08: Security-relevant changes undergo review.
      Review Policy URL:    _________________________________________
```

### 2.3 Project Stability

```
- [ ] SG.09: Governance structure is documented.
      Governance Doc URL:   _________________________________________

- [ ] SG.10: Maintainer succession is addressed.
      [ ] No single point of failure for security-critical components
      Succession Plan URL:  _________________________________________

- [ ] SG.11: Resources for continued development are visible.
      Sustainability Model: [ ] Foundation  [ ] Corporate Sponsorship  [ ] Other: _______
      Sustainability URL:   _________________________________________
```

NOTE: Projects may reference established project health metrics such as OpenSSF Scorecard or SLSA levels as supporting evidence.

```
OpenSSF Scorecard:      _________________________________________
SLSA Level:             _________________________________________
Other Certifications:   _________________________________________
```

---

## Section 3: Requirement Coverage

### 3.1 Coverage Declaration

For each CRA requirement addressed by this attestation, the following information is provided:

| Requirement Reference | Implementation Description | Configuration Prerequisites | Known Limitations |
|-----------------------|---------------------------|----------------------------|-------------------|
| _example: Annex I Part I.2(b)_ | _Secure defaults are enforced via..._ | _None_ | _Does not apply to..._ |

### 3.2 Annex I Part I Coverage

_For each applicable requirement, describe how the project addresses the security concern._

#### 3.2.1 Risk Assessment (Annex I Part I.1)

```
- [ ] RI.01: The project maintains a cybersecurity risk assessment.
      Risk Assessment URL:  _________________________________________
      Last Updated:         _________________________________________
```

#### 3.2.2 Security Properties (Annex I Part I.2)

```
- [ ] SP.01: (a) The project is designed to be placed on the market without
      known exploitable vulnerabilities.
      Vulnerability Tracking URL: ____________________________________

- [ ] SP.02: (b) The project provides secure by default configuration.
      Secure Defaults Documentation: _________________________________

- [ ] SP.03: (c) The project supports security updates.
      Update Mechanism Documentation: ________________________________

- [ ] SP.04: (d) The project enforces appropriate access controls.
      Access Control Documentation: __________________________________

- [ ] SP.05: (e) The project protects data confidentiality.
      Confidentiality Documentation: _________________________________

- [ ] SP.06: (f) The project protects data and program integrity.
      Integrity Documentation: _______________________________________

- [ ] SP.07: (g) The project minimizes data processing.
      Data Minimisation Documentation: _______________________________

- [ ] SP.08: (h) The project protects availability.
      Availability Documentation: ____________________________________

- [ ] SP.09: (i) The project minimizes negative impact on other products.
      Impact Minimisation Documentation: _____________________________

- [ ] SP.10: (j) The project limits attack surfaces.
      Attack Surface Documentation: __________________________________

- [ ] SP.11: (k) The project includes exploit mitigation techniques.
      Mitigation Documentation: ______________________________________

- [ ] SP.12: (l) The project supports security monitoring.
      Monitoring Documentation: ______________________________________

- [ ] SP.13: (m) The project supports secure data deletion.
      Deletion Documentation: ________________________________________
```

#### 3.2.3 Vulnerability Handling Requirements (Annex I Part II)

```
- [ ] VH.01: (1) The project provides SBOM documentation.
      SBOM URL:             _________________________________________

- [ ] VH.02: (2) Vulnerabilities are addressed and remediated.
      Remediation Policy URL: ________________________________________

- [ ] VH.03: (3) Testing procedures validate security properties.
      Testing Documentation: _________________________________________

- [ ] VH.04: (4) Vulnerability information is disclosed appropriately.
      Disclosure Policy URL: _________________________________________

- [ ] VH.05: (5) The project has a CVD policy.
      CVD Policy URL:       _________________________________________

- [ ] VH.06: (6) Vulnerability information is shared effectively.
      Information Sharing URL: _______________________________________

- [ ] VH.07: (7) Updates are distributed securely.
      Distribution Documentation: ____________________________________

- [ ] VH.08: (8) Security updates are provided in a timely manner.
      Update Timeline Policy: ________________________________________
```

---

## Section 4: Maintenance Commitment

### 4.1 Update Cadence

```
Expected Release Frequency:    _________________________________________
Security Update Policy:        _________________________________________
```

### 4.2 Version Support

```
Support Policy URL:            _________________________________________
Currently Supported Versions:  _________________________________________
```

### 4.3 Attestation Maintenance

```
- [ ] MC.01: This attestation will be updated when:
      [ ] Covered version range expands
      [ ] Requirement coverage changes
      [ ] Implementation changes affect accuracy
      [ ] Security governance practices change materially

Attestation Update Notification: _________________________________________
```

---

## Section 5: Requirement Classification

### 5.1 Purpose

This section identifies which requirements may be inherited by downstream integrators versus which shall be directly assessed by the integrating manufacturer. See the [Implementation Guide](template-heavy-implementation-guide.md) for detailed guidance.

### 5.2 Project-Specific Classification

_Complete this table for the specific project:_

| Requirement | Classification | Conditions/Notes |
|-------------|----------------|------------------|
| | [ ] Inheritable [ ] Conditional [ ] Direct-Assessment | |
| | [ ] Inheritable [ ] Conditional [ ] Direct-Assessment | |
| | [ ] Inheritable [ ] Conditional [ ] Direct-Assessment | |

Classification definitions:
- **Inheritable**: May be relied upon by downstream manufacturers, subject to due diligence
- **Conditional**: Inheritable if unmodified; returns to direct assessment if modified
- **Direct-Assessment**: Shall be assessed by each manufacturer regardless of upstream quality

---

# Document Notes

## Relationship to Light-Weight VSAs

Heavy-weight VSAs build upon the foundation of light-weight VSAs. Projects issuing heavy-weight VSAs should also satisfy all light-weight requirements (AU.*, GV.*, LE.*, QA.*, BR.*, VM.*, EL.*).

## Relationship to Harmonized Standards

This template is designed to align with anticipated CRA harmonized standards. As standards such as the EN 40000-1-x series are finalized and published, this template may be updated to provide explicit mappings.

## Voluntary Nature

Nothing in this template creates an obligation for open source projects to produce heavy-weight VSAs. Publication is voluntary. The template provides a structure for projects that choose to provide comprehensive security documentation.

## Implementation Guidance

For detailed guidance on:
- Requirement inheritance and direct assessment criteria
- Due diligence procedures for downstream integrators
- Modification-triggered reassessment
- Update flow procedures
- Machine-readable format (JSON schema)
- Guidance for conformity assessment bodies
- CRA requirement mappings

See the [Heavy Weight VSA Implementation Guide](template-heavy-implementation-guide.md).
