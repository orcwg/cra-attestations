---
SIG: ORC Attestation SIG
Document Type: Deliverable
Number: XX
Status: Drafting
Group: European Commission
Date: XX
---

# Contemplating Mechanisms for Article 25 in Support of Open Source Stewards


## Introduction

Article 25 enables the European Commission to adopt a delegated act specifying
the nature and structure of voluntary "security attestations" made by Open
Source Stewards in relation to the software projects for which they "provide
sustainable support" and in support of compliance-related activities of
manufacturers that use those projects.

We believe this can create a beneficial feedback mechanism which will help to
sustain open source project security, maintenance, and infrastructure, and to
fund the fulfilment of Steward's obligations as laid out in Article 24.

### Obligations of Stewards

Below is a list of obligations of open source stewards defined in the CRA,
primarily in Article 24. References to Article 14 have been included for
completeness.

1. document[ing] ... a cybersecurity policy to foster the development of a
   secure product 
1. [documenting the] effective handling of vulnerabilities by the developers of
   that product
1. voluntary reporting of vulnerabilities as laid down in Article 15
1. cooperat[ing] with the market surveillance authorities
1. notif[ying of] any severe incident ... that it becomes aware of
   simultaneously to the CSIRT ... and to ENISA.
1. After becoming aware of an actively exploited vulnerability or a severe
   incident ... inform[ing] the impacted users ... of that vulnerability or
   incident and, where necessary, of any risk mitigation and corrective
   measures

### Contextualizing the present effort

To contextualize this work and determine where to focus our efforts, we begin- a panel with different foundations sharing their 
by grouping Open Source Stewards along several perspectives, while remembering
that the CRA is a _product_ regulation -- it has no direct bearing on the act
of publishing source code under an open source license whatsoever.

**Perspective: Economic Interests**
1. A for-profit manufacturer of PwDE, or a for-profit service provider, may
   either (1a) produce or publish F/OSS in the course of a commercial activity
   related to its products or services, or (1b) incidentally publish F/OSS
   outside of commercial activities and without compensation.
1. A Trade Association which supports F/OSS that its members rely on in the
   course of their business.
1. A Public Benefit Non-Profit which supports F/OSS.
1. A Public Sector entity (e.g., a government body) which produces F/OSS in the
   course of its funded activities.
1. An individual Natural Person.
1. A project that has definite legal owner, and where all contributions remain
   owned by contributors.

Based on current understandings of the Cyber Resilience Act, of the above, only
(1b), (2) and (3) may be considered a Steward. However, security attestations
made by, or in regards to, open source projects may be beneficial for any open
source project and should be authorable by any interested party. Additionally,
it is paramount that attestations also support the sustainable maintenance of
single-maintainer projects (category 5) and projects without a legal
representative (category 6) if doing so would have value to manufacturers.

**Perspective: Manufacturer's Use of Attestations**

In contemplating Article 25 and the value of Attetations to manufacturers of PwDE's,
we consider that Attestations:
- may or may not be stored or distributed alongside the source code or binaries of a
  project
- may be limited in their distribution, such as by being copyrighted separately
  or only distributed to members of a particular group or legal class
- may contain information regarding the compliance of the Project with respect
  to norms or standards, may be self-declared, or may be the result of an external
  audit.
- may be exchanged for value, including as part of a commercial activity
- may be published openly and without cost
- may be digitally signed


Attestations regarding an Open Source Project should be authorable by any
market actor, including unaffiliated third parties such as researchers and
manufacturers who use the Project. Therefore, a system for the distribution and
verification of the authenticity of attestations should also be contemplated.
This will also necessitate a mechanism to resolve disputed third-party
attestations.

## Identified barriers to adoption

1. Many projects are not affiliated with or supported by a legal entity, and
   thus do not have a steward today.
1. It is unclear whether a "fiscal host" would qualify as a Steward, since most
   fiscal sponsors are not involved in the day-to-day management of, or
   security response activities of, the open source projects they host.
1. Fragmentation of laws regarding non-profit legal entities across the 27
   Member States may lead to some confusion about possible (or optimal) legal
   structures to support Stewards, including how to receive compensation for
   provision of Attestations, without jeopardizing non-profit status.
1. Considering the complexity and depth of open source supply chains, how can
   an attestation programme ensure that projects "deeper" in the supply chain
   are also accounted for, able to issue attestations to manufacturers that
   utilize them, and able to be compensated by said manufacturers?
1. Considering the hundreds or thousands of open source projects generally
   integrated into every commercial product, and the burden on SMEs and
   manufacturers were there to be a sudden requirement to separately track
   attestations for every nested dependency, is there a machine-readable
   and automatable means for such deep supply chain traceability and the
   commensurate attestations?

## Recommendations for policy and practice

TBD

## Conclusion

TBD

---
## Acknowledgments

The following people have contributed to this document either directly or
indirectly (e.g. by raising questions, reviewing...):

1. Æva Black

If you have contributed to this document and aren't properly acknowledged or if
you want to edit or remove your name, please let us know by [opening an
issue](https://github.com/orcwg/orcwg/issues/new) and we will fix this right
away.
