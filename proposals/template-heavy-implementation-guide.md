Heavy Weight VSA Implementation Guide
===

Edit History
---

| Revision | Date | Summary of Changes |
| --- | ---------- | --- |
| 0.2 | 06.01.2026 | Added Annex G: Tiered Evidence Model per COM guidance |
| 0.1 | 22.12.2025 | Initial draft, extracted from template-heavy.md |

Introduction
---

This guide provides supporting material for implementing heavy-weight Voluntary Security Attestations (VSAs). It includes:

1. Guidance on requirement inheritance and direct assessment
2. Due diligence procedures for downstream integrators
3. Modification-triggered reassessment criteria
4. Update flow procedures
5. Machine-readable format specification
6. Guidance for conformity assessment bodies
7. Tiered evidence model (low/medium/high risk)
8. CRA requirement mappings

This document accompanies the [Heavy Weight VSA Template](template-heavy.md).

---

# Annex A: Inheritable vs. Direct-Assessment Requirements

## A.1 Purpose

This annex identifies which requirements may be inherited by downstream integrators versus which must be directly assessed by the integrating manufacturer.

## A.2 Requirement Classification

| Category | Requirements | Classification | Notes |
|----------|-------------|----------------|-------|
| **Inheritable** | Core security implementations, protocol handling, cryptographic operations | May be relied upon by downstream manufacturers | Subject to due diligence per Annex B |
| **Conditional** | Configuration-dependent security features | Inheritable if unmodified | Returns to direct assessment if modified |
| **Direct-Assessment Required** | Support commitments, update delivery, vulnerability handling operations, backend services, data handling | Must be assessed by each manufacturer | Cannot be inherited regardless of upstream quality |

## A.3 Project-Specific Classification

When completing a heavy-weight VSA, fill in this table for the specific project:

| Requirement | Classification | Conditions/Notes |
|-------------|----------------|------------------|
| _example: TLS implementation_ | Inheritable | |
| _example: Secure defaults_ | Direct-Assessment | Configuration is integrator decision |
| _example: Certificate validation_ | Conditional | Inheritable if validation logic unmodified |

## A.4 Classification Principles

### A.4.1 Inheritable Requirements

Requirements are inheritable when:

1. The security property is implemented entirely in code
2. The implementation does not depend on integrator decisions
3. The functionality can be integrated without modification
4. The upstream project has demonstrated competence through due diligence

Examples:
- Cryptographic algorithm implementations
- Protocol handling (TLS, HTTP/2, etc.)
- Memory safety mechanisms
- Input validation routines

### A.4.2 Conditional Requirements

Requirements are conditional when:

1. The security property depends on configuration choices
2. The functionality may be modified by integrators
3. Inheritance is valid only if specific conditions are met

Examples:
- Certificate validation (inheritable if validation logic unmodified)
- Permission enforcement (inheritable if permission model unmodified)
- Sandboxing mechanisms (inheritable if isolation boundaries unmodified)

### A.4.3 Direct-Assessment Requirements

Requirements require direct assessment when:

1. They depend on integrator commitments (support periods, response times)
2. They involve integrator-operated infrastructure (update servers, backend services)
3. They involve integrator decisions (default configurations, data handling)
4. They cannot be inherited regardless of upstream quality

Examples:
- Support period commitments
- Update delivery mechanisms
- Vulnerability disclosure contacts
- Backend service security
- Data handling practices

---

# Annex B: Due Diligence Guidance for Downstream Integrators

## B.1 Purpose

This annex provides guidance for manufacturers integrating open source projects on how to perform due diligence and rely on heavy-weight VSAs.

## B.2 Attestation Verification

Manufacturers relying on a heavy-weight VSA should:

1. **Verify the attestation signature** (if signed)
   - Obtain the public key from the project's well-known location
   - Validate the JWS signature per RFC 7515
   - Confirm the signing key is authorised by the project

2. **Confirm version coverage**
   - Verify the attestation covers the specific version being integrated
   - Check both version numbers and commit hashes if provided

3. **Confirm validity period**
   - Verify the current date is within the attestation's validity period
   - Plan for attestation renewal before expiry

4. **Confirm non-withdrawal**
   - Check the attestation publication location for withdrawal notices
   - Subscribe to project security notifications

5. **Subscribe to updates**
   - Register for attestation update notifications
   - Monitor the project's security advisory feed

6. **Document verification**
   - Record the verification steps performed
   - Retain evidence of verification for technical documentation

## B.3 Integration Integrity

For inherited requirements, manufacturers should:

1. **Identify inherited vs. modified functionality**
   - Document all modifications to upstream code
   - Categorise modifications per Annex C
   - Maintain traceability between upstream and derivative code

2. **Confirm unmodified integration**
   - Verify security-relevant functionality is integrated without modification
   - Use automated tools where possible to detect unintended changes
   - Document the integration process

3. **Verify configuration consistency**
   - Confirm configuration matches any prerequisites stated in the attestation
   - Document any configuration deviations and their justification

4. **Document the integration process**
   - Record upstream version integrated
   - Record integration date
   - Record any build-time configuration choices
   - Maintain SBOM entries for upstream components

## B.4 Ongoing Due Diligence

Manufacturers should:

1. **Subscribe to project security notifications**
   - Monitor security advisory feeds
   - Track CVE assignments related to the project
   - Respond promptly to security notifications

2. **Monitor for material changes**
   - Track changes to project governance
   - Monitor for maintainer transitions
   - Watch for changes to security practices

3. **Reassess project health periodically**
   - Perform reassessment at intervals not exceeding 12 months
   - Use consistent criteria (e.g., OpenSSF Scorecard)
   - Document reassessment findings

4. **Reassess promptly after incidents**
   - If significant security incidents reveal process failures, reassess immediately
   - Evaluate whether continued reliance is justified
   - Document decisions and rationale

## B.5 Due Diligence Without Attestation

Where no heavy-weight VSA exists, manufacturers should assess the upstream project against observable criteria:

### B.5.1 Security Governance
- Coordinated vulnerability disclosure policy is published
- Security contact mechanism exists and is responsive
- Security advisories are published with CVE references

### B.5.2 Vulnerability Handling Track Record
- Median response time for critical/high vulnerabilities does not exceed 90 days
- Security patches are available for supported versions
- No pattern of critical vulnerabilities remaining unaddressed beyond 180 days

### B.5.3 Development Practices
- Dependencies are documented in machine-readable format
- Contribution provenance is traceable
- Active maintenance demonstrated through recent commits and releases

### B.5.4 Project Stability
- Governance structure is documented
- No single point of failure for security-critical components
- Resources for continued development are visible

---

# Annex C: Modification-Triggered Reassessment

## C.1 Principle

Requirements satisfied through inheritance remain satisfied only if inherited functionality is unmodified. Modifications to security-relevant functionality bring associated requirements back into direct assessment scope.

## C.2 Modifications NOT Requiring Reassessment

The following modifications do not trigger reassessment of inherited requirements:

- **Branding changes**: Icons, names, about pages, visual themes
- **Additive functionality**: New features that do not interact with inherited security features
- **Configuration within parameters**: Changes within documented acceptable ranges
- **Localisation**: Translation and regional adaptation
- **Feature removal**: Removing features where removal does not affect security properties of remaining functionality

## C.3 Modifications Requiring Reassessment

The following modifications trigger reassessment of affected requirements:

- **Security policy enforcement**: Modification of CSP, CORS, same-origin policy, or similar enforcement logic
- **Credential handling**: Modification of credential storage, transmission, or validation
- **Certificate validation**: Modification of certificate chain validation or trust anchor management
- **Sandboxing**: Modification of process isolation, sandboxing boundaries, or privilege separation
- **Permission systems**: Modification of permission grant, revocation, or enforcement
- **Cryptographic implementations**: Modification of encryption, hashing, signing, or key management
- **Security bypass**: Addition of functionality that bypasses inherited security controls
- **Security disabling**: Disabling or weakening inherited security features

## C.4 Assessment Method

When assessing whether a modification triggers reassessment, consider:

1. **Does the modification change behaviour addressed by a specific requirement?**
   - Map the modification to attestation requirements
   - Identify which requirements might be affected

2. **Could the modification introduce a vulnerability not present upstream?**
   - Analyse the modification for security implications
   - Consider both direct and indirect effects

3. **Could the modification weaken a protection provided upstream?**
   - Compare security properties before and after modification
   - Document any reduction in security assurance

If any answer is yes, reassessment is required for affected requirements.

## C.5 Scope of Reassessment

Reassessment is limited to requirements affected by the modification. Unaffected inherited requirements remain satisfied through due diligence.

## C.6 Documentation Requirements

Manufacturers should document:

1. All modifications to inherited functionality
2. For each modification, the assessment of whether reassessment is triggered
3. For modifications triggering reassessment, the conformity assessment performed and results

---

# Annex D: Update Flow

## D.1 Principle

Due diligence attaches to the project's processes, not individual updates. Updates from a project satisfying ongoing due diligence criteria flow through without per-update reassessment for inherited requirements.

## D.2 Normal Update Integration

For updates from a project meeting due diligence criteria:

1. No additional conformity assessment is required for inherited requirements
2. Verify the update does not conflict with derivative modifications
3. Verify configuration remains consistent with attestation prerequisites
4. Document update integration including upstream version and date

## D.3 Security Update Integration

Security updates should be integrated promptly. Delay for conformity assessment of inherited functionality is not required and may conflict with CRA obligations requiring security updates "without delay."

The manufacturer remains responsible for:

1. Verifying security updates do not break derivative functionality
2. Testing derivative-specific features after integration
3. Delivering updates to users through manufacturer's update mechanism

## D.4 Attestation Version Transitions

If an update falls outside the version range covered by the relied-upon attestation:

1. **Updated attestation available**: Continue reliance if attestation is updated to cover new version
2. **No updated attestation**: Perform due diligence per Annex B.5 for the new version
3. **Documentation**: Document the basis for continued reliance on inheritance

## D.5 Project Status Changes

If due diligence monitoring reveals the upstream project no longer meets criteria:

1. Assess the impact on inherited requirements
2. Determine whether continued reliance is justified based on nature and severity of degradation
3. If reliance is no longer justified:
   - Perform direct assessment of affected requirements, or
   - Migrate to an alternative upstream
4. Document the assessment, decision, and rationale

## D.6 Major Version Transitions

When integrating major version transitions (architectural changes, engine replacements):

1. Reassess whether attestation or prior due diligence findings remain applicable
2. Evaluate whether the transition constitutes a modification per Annex C
3. Perform targeted reassessment of requirements affected by significant architectural changes

## D.7 Documentation

Maintain records of:

1. Upstream versions integrated, with dates
2. Issues encountered during integration affecting security functionality
3. Ongoing due diligence monitoring results
4. Project status changes affecting reliance
5. Decisions regarding continued reliance or reassessment

---

# Annex E: Machine-Readable Format Specification

## E.1 Purpose

This annex specifies the machine-readable format for heavy-weight VSAs to enable automated processing by manufacturers and tooling.

## E.2 JSON Schema

Heavy-weight VSAs should be published in JSON format conforming to the following schema:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Heavy-Weight Voluntary Security Attestation",
  "type": "object",
  "required": ["vsa_version", "identification", "security_governance"],
  "properties": {
    "vsa_version": {
      "type": "string",
      "const": "1.0",
      "description": "VSA schema version"
    },
    "identification": {
      "type": "object",
      "required": ["project_name", "version_range", "repository", "issue_date", "validity_end", "publisher"],
      "properties": {
        "project_name": {
          "type": "string",
          "description": "Open source project name"
        },
        "version_range": {
          "type": "object",
          "properties": {
            "from_version": { "type": "string" },
            "to_version": { "type": "string" },
            "from_commit": { "type": "string" },
            "to_commit": { "type": "string" }
          },
          "description": "Version or commit range covered"
        },
        "repository": {
          "type": "string",
          "format": "uri",
          "description": "Source repository location"
        },
        "issue_date": {
          "type": "string",
          "format": "date",
          "description": "Attestation issue date"
        },
        "validity_end": {
          "type": "string",
          "format": "date",
          "description": "Attestation validity end date"
        },
        "publisher": {
          "type": "object",
          "required": ["name", "type", "contact"],
          "properties": {
            "name": { "type": "string" },
            "type": {
              "type": "string",
              "enum": ["governance_body", "steward", "third_party"]
            },
            "contact": { "type": "string" }
          }
        }
      }
    },
    "security_governance": {
      "type": "object",
      "required": ["cvd_policy", "security_contact", "advisory_mechanism"],
      "properties": {
        "cvd_policy": {
          "type": "string",
          "format": "uri",
          "description": "URL of coordinated vulnerability disclosure policy"
        },
        "security_contact": {
          "type": "string",
          "description": "Security contact method"
        },
        "advisory_mechanism": {
          "type": "string",
          "format": "uri",
          "description": "URL of security advisory feed or page"
        },
        "median_response_days": {
          "type": "integer",
          "description": "Median vulnerability response time in days for critical/high severity"
        },
        "sbom_url": {
          "type": "string",
          "format": "uri"
        },
        "sbom_format": {
          "type": "string",
          "enum": ["spdx", "cyclonedx", "other"]
        },
        "provenance_mechanism": {
          "type": "string",
          "enum": ["signed_commits", "dco", "cla", "other"]
        },
        "governance_url": {
          "type": "string",
          "format": "uri"
        },
        "sustainability_model": {
          "type": "string",
          "enum": ["foundation", "corporate_sponsorship", "community", "other"]
        },
        "openssf_scorecard": {
          "type": "string",
          "format": "uri"
        },
        "slsa_level": {
          "type": "string"
        }
      }
    },
    "requirement_coverage": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["requirement_ref", "description", "risk_level"],
        "properties": {
          "requirement_ref": {
            "type": "string",
            "description": "CRA Annex reference (e.g., 'Annex I Part I.2(b)')"
          },
          "description": {
            "type": "string",
            "description": "How the project addresses the security concern"
          },
          "risk_level": {
            "type": "string",
            "enum": ["low", "medium", "high"],
            "description": "Risk level determining evidence requirements per Annex G"
          },
          "documentation_url": {
            "type": "string",
            "format": "uri"
          },
          "test_reference": {
            "type": "string",
            "format": "uri",
            "description": "URL to tests validating the requirement (required for medium/high risk)"
          },
          "evidence": {
            "type": "object",
            "description": "Evidence demonstrating compliance (required for high risk)",
            "properties": {
              "type": {
                "type": "string",
                "enum": ["test_results", "audit_report", "pentest_report", "formal_verification", "historical_data", "certification", "other"],
                "description": "Type of evidence provided"
              },
              "description": {
                "type": "string",
                "description": "Description of the evidence"
              },
              "url": {
                "type": "string",
                "format": "uri",
                "description": "URL to the evidence"
              },
              "date": {
                "type": "string",
                "format": "date",
                "description": "Date evidence was generated"
              }
            }
          },
          "classification": {
            "type": "string",
            "enum": ["inheritable", "conditional", "direct_assessment"],
            "description": "Whether this requirement can be inherited by downstream integrators"
          },
          "conditions": {
            "type": "array",
            "items": { "type": "string" },
            "description": "Conditions for inheritance (if conditional)"
          },
          "limitations": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    },
    "maintenance": {
      "type": "object",
      "properties": {
        "update_cadence": {
          "type": "string",
          "description": "Expected release frequency"
        },
        "support_policy_url": {
          "type": "string",
          "format": "uri"
        },
        "supported_versions": {
          "type": "array",
          "items": { "type": "string" }
        },
        "attestation_update_notification": {
          "type": "string",
          "description": "How to receive attestation updates"
        }
      }
    }
  }
}
```

## E.3 Signature Requirements

Heavy-weight VSAs should be signed using JSON Web Signature (JWS) per RFC 7515:

1. **Algorithms**: RS256 or ES256
2. **Key publication**: Public key published at a well-known location within the project's infrastructure
3. **Key rotation**: Projects should document key rotation procedures

## E.4 Distribution

VSAs should be published at a stable URL within the project's documentation or security resources.

**Recommended location**: `https://<project-domain>/.well-known/vsa.json`

**Alternative locations**:
- Project repository root (e.g., `VSA.json`)
- Security documentation directory
- Release artifacts

## E.5 Versioning

When updating a VSA:

1. Increment the attestation version
2. Update version range to cover new releases
3. Maintain prior versions at accessible URLs
4. Publish update notification through documented channels

---

# Annex G: Tiered Evidence Model

## G.1 Purpose

This annex defines the tiered evidence model for attestation review, based on guidance from the European Commission regarding the level of detail required for downstream presumption of conformity.

## G.2 Evidence Tiers

Requirements are assessed according to three evidence tiers based on risk level:

| Risk Level | Evidence Required | Description |
|------------|-------------------|-------------|
| **Low** | Declaration | A checkmark confirming the requirement has been met is sufficient |
| **Medium** | Test Reference | Reference to tests that have been written to validate the requirement |
| **High** | Evidence | Demonstration of evidence or execution of tests showing the requirement is met |

## G.3 Risk Level Determination

### G.3.1 Factors for Risk Classification

The risk level for each requirement should be determined based on:

1. **Security impact**: What is the potential harm if the requirement is not met?
2. **Attack surface**: Is the functionality exposed to untrusted input or network access?
3. **Data sensitivity**: Does the requirement protect sensitive or personal data?
4. **Downstream context**: How is the project typically integrated?
5. **Product category**: Is the downstream product Important Class I, Class II, or default category?

### G.3.2 General Risk Classification Guidance

**Low Risk** - Declaration sufficient:
- Requirements with limited security impact
- Functionality not directly exposed to attack
- Administrative or process-oriented requirements
- Examples: documentation availability, governance structure, contribution guidelines

**Medium Risk** - Test reference required:
- Requirements with moderate security impact
- Functionality that could be exploited but with limited consequence
- Requirements where testing provides adequate assurance
- Examples: input validation, error handling, logging mechanisms, SBOM accuracy

**High Risk** - Evidence required:
- Requirements with significant security impact
- Functionality directly protecting against common attack vectors
- Cryptographic implementations
- Requirements where failure could lead to data breach or system compromise
- Examples: authentication mechanisms, cryptographic operations, certificate validation, sandbox enforcement, vulnerability remediation timelines

### G.3.3 Product Category Considerations

The downstream product category may influence risk classification:

| Product Category | Risk Adjustment |
|------------------|-----------------|
| Default (non-Important) | Standard risk levels as determined by G.3.2 |
| Important Class I | Consider elevating Medium risks to High |
| Important Class II | Elevate most requirements to High; comprehensive evidence expected |

## G.4 Evidence Requirements by Tier

### G.4.1 Low Risk - Declaration

For low-risk requirements, the attestation publisher provides:

- A checkbox indicating the requirement is met
- Optional: URL to supporting documentation

The downstream manufacturer may rely on the declaration without additional verification beyond due diligence on the project itself.

### G.4.2 Medium Risk - Test Reference

For medium-risk requirements, the attestation publisher provides:

- A checkbox indicating the requirement is met
- Reference to test suite or specific tests that validate the requirement
- Test location (URL to test files, CI pipeline, or test documentation)
- Optional: Test coverage metrics

The downstream manufacturer should:
- Verify tests exist at the referenced location
- Confirm tests are executed as part of the project's CI/CD
- Document reliance on upstream testing

### G.4.3 High Risk - Evidence

For high-risk requirements, the attestation publisher provides:

- A checkbox indicating the requirement is met
- Detailed description of how the requirement is satisfied
- Evidence demonstrating compliance, which may include:
  - Test results or reports
  - Security audit findings
  - Penetration test results
  - Formal verification outputs
  - Historical vulnerability data
  - Third-party certifications

The downstream manufacturer should:
- Review the provided evidence
- Verify evidence is current and applicable to the integrated version
- Document the evidence review in technical documentation
- Consider independent verification for critical integrations

## G.5 Relationship to Inheritance Classification

The evidence tier (risk level) is orthogonal to the inheritance classification:

| | Inheritable | Conditional | Direct-Assessment |
|---|-------------|-------------|-------------------|
| **Low Risk** | Declaration in VSA | Declaration in VSA | Declaration by manufacturer |
| **Medium Risk** | Test reference in VSA | Test reference in VSA | Test reference by manufacturer |
| **High Risk** | Evidence in VSA | Evidence in VSA | Evidence by manufacturer |

For inherited requirements, the VSA provides the evidence. For direct-assessment requirements, the manufacturer provides the evidence regardless of what the VSA states.

## G.6 Documentation in VSA

When completing a heavy-weight VSA, for each requirement:

1. Determine the appropriate risk level using G.3
2. Provide evidence appropriate to the tier per G.4
3. Document the risk level in the attestation
4. Include references to tests or evidence as required

## G.7 CAB Verification

Conformity Assessment Bodies should verify:

1. Risk levels are appropriately assigned based on G.3
2. Evidence provided matches the required tier per G.4
3. For medium-risk requirements, tests exist and are executed
4. For high-risk requirements, evidence is substantive and current
5. Downstream manufacturers have documented their review of evidence

---

# Annex F: Guidance for Conformity Assessment Bodies

## F.1 Purpose

This annex provides guidance for notified bodies and conformity assessment bodies evaluating manufacturer claims based on reliance on heavy-weight VSAs.

## F.2 Assessment of Inheritance Claims

When a manufacturer claims inheritance of requirements based on a heavy-weight VSA, the CAB should verify:

1. **Project identification**: The upstream project is identified with specific version or commit reference
2. **Attestation coverage**: The VSA exists and covers claimed requirements
3. **Integration documentation**: Manufacturer integration process is documented per Annex B
4. **Functionality presence**: Claimed inherited functionality is present in the manufacturer's product
5. **Modification documentation**: Manufacturer has documented which functionality is inherited vs. modified per Annex C
6. **Direct assessment**: Direct-assessment requirements per Annex A are directly assessed with appropriate evidence

## F.3 Verification of Unmodified Inheritance

The CAB need not independently audit the upstream implementation. The upstream implementation is not the subject of conformity assessment; the manufacturer's product is.

The CAB verifies:

1. Manufacturer documentation identifies which functionality is inherited
2. Manufacturer modification documentation is consistent with inheritance claims
3. Sample testing confirms claimed inherited functionality operates as described
4. No evidence suggests security-relevant modifications were made but not documented

## F.4 Attestation Evaluation

The CAB is not required to validate attestation accuracy. Accuracy is the publisher's responsibility.

The CAB verifies:

1. Attestation exists and is accessible at documented location
2. Attestation authenticity is verified through signature validation (if signed)
3. Attestation version range covers the integrated version
4. Attestation has not been withdrawn
5. Manufacturer has documented subscription to attestation updates

## F.5 Due Diligence Evaluation (Absence of Attestation)

Where manufacturer relies on due diligence per Annex B.5 rather than a VSA, the CAB verifies:

1. Manufacturer documentation addresses all criteria in Annex B.5
2. Observable evidence supports manufacturer findings
3. Quantitative thresholds are assessed with supporting data
4. Ongoing due diligence is established

The CAB need not independently assess the upstream project. The CAB verifies the manufacturer performed appropriate due diligence and documented findings.

## F.6 Modification Assessment

The CAB should review manufacturer documentation per Annex C to verify:

1. Modifications are identified and categorised
2. Categorisation under C.2 or C.3 is reasonable
3. Where C.3 modifications exist, corresponding requirements are directly assessed
4. The C.4 assessment questions are addressed for each modification

## F.7 Competence Considerations

CABs assessing products relying on heavy-weight VSAs should have competence in:

1. Open source software supply chain practices
2. Version control, release processes, and dependency management
3. Software bill of materials evaluation
4. The specific upstream projects commonly used in the product category

CABs need not have competence equivalent to auditing upstream implementations. Competence should be sufficient to evaluate whether manufacturer due diligence was appropriately performed and whether inheritance claims are plausible.

---

# Appendix: Mapping to CRA Requirements

This appendix maps CRA requirements to heavy-weight VSA template sections.

| CRA Requirement | Template Section | Notes |
|-----------------|------------------|-------|
| Annex I Part I.1 | Section 3.3.1 (RI.01) | Risk assessment |
| Annex I Part I.2(a) | Section 3.3.2 (SP.01) | No known exploitable vulnerabilities |
| Annex I Part I.2(b) | Section 3.3.2 (SP.02) | Secure by default |
| Annex I Part I.2(c) | Section 3.3.2 (SP.03) | Security updates |
| Annex I Part I.2(d) | Section 3.3.2 (SP.04) | Access controls |
| Annex I Part I.2(e) | Section 3.3.2 (SP.05) | Confidentiality |
| Annex I Part I.2(f) | Section 3.3.2 (SP.06) | Integrity |
| Annex I Part I.2(g) | Section 3.3.2 (SP.07) | Data minimisation |
| Annex I Part I.2(h) | Section 3.3.2 (SP.08) | Availability |
| Annex I Part I.2(i) | Section 3.3.2 (SP.09) | Impact minimisation |
| Annex I Part I.2(j) | Section 3.3.2 (SP.10) | Attack surface |
| Annex I Part I.2(k) | Section 3.3.2 (SP.11) | Exploit mitigation |
| Annex I Part I.2(l) | Section 3.3.2 (SP.12) | Security monitoring |
| Annex I Part I.2(m) | Section 3.3.2 (SP.13) | Secure deletion |
| Annex I Part II.1 | Section 3.3.3 (VH.01) | SBOM |
| Annex I Part II.2 | Section 3.3.3 (VH.02) | Vulnerability remediation |
| Annex I Part II.3 | Section 3.3.3 (VH.03) | Testing |
| Annex I Part II.4 | Section 3.3.3 (VH.04) | Vulnerability disclosure |
| Annex I Part II.5 | Section 3.3.3 (VH.05) | CVD policy |
| Annex I Part II.6 | Section 3.3.3 (VH.06) | Information sharing |
| Annex I Part II.7 | Section 3.3.3 (VH.07) | Secure distribution |
| Annex I Part II.8 | Section 3.3.3 (VH.08) | Timely updates |
| Article 13.5 | Annex B | Due diligence guidance |
| Article 24 | Section 1.3 (Steward identification) | Steward obligations |
| — | Section 3.1 / Annex G | Tiered evidence model (low/medium/high risk) |

---

# Document Notes

## Relationship to Template

This implementation guide accompanies [template-heavy.md](template-heavy.md). The template contains the attestation form itself; this guide provides supporting material for completing and using the attestation.

## Relationship to Light-Weight VSAs

Heavy-weight VSAs build upon light-weight VSAs. Projects issuing heavy-weight VSAs should also satisfy all light-weight requirements (AU.*, GV.*, LE.*, QA.*, BR.*, VM.*, EL.*).

## Relationship to Harmonized Standards

This guide is designed to align with anticipated CRA harmonized standards. As standards such as the EN 40000-1-x series are finalized, this guide may be updated to provide explicit mappings.

## Voluntary Nature

Nothing in this guide creates an obligation for open source projects to produce heavy-weight VSAs. Publication is voluntary.
