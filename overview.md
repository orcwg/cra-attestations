# Contemplating Mechanisms for Article 25 in Support of Open Source Stewards

## Introduction

The Cyber Resilience Act (CRA) represents a pivotal shift in the European
Union’s approach to cybersecurity—one that recognizes open source software not
as a compliance risk, but as a strategic asset capable of strengthening Europe’s
digital sovereignty, resilience, and innovation capacity. Central to this vision
is Article 25, which empowers the European Commission to adopt a Delegated Act
specifying the nature and structure of *voluntary security attestations* for
free and open source software (FOSS), issued by Open Source Stewards and others,
for the purpose of supporting manufacturers’ due diligence obligations under the
Act.

Article 25 presents a rare opportunity: to align regulatory intent with
ecosystem realities. If implemented well, it coulc transform stewardship from a
legal question into a funded and trusted role — enabling Open Source Stewards to
deliver on their Article 24 responsibilities (see below) while fostering a more
resilient, transparent, and secure digital supply chain for all.

These Attestations are not a new regulatory burden on Maintainers, nor are they
a proposal from the Open Source community. They are *a key part of the Act*
which allows the Commission to adopt a structured mechanism to translate
existing open source security best practices into credible, verifiable evidence
that manufacturers can use to meet their own obligations under the Act -- and
which could help to financially support the obligations of Open Source Stewards,
if implemented well.

We believe that the attestation programme contemplated in Article 25 could
create a pathway for maintainers of projects *which are inteded for commercial
use* to gain sustainable funding, to fund the vital work of supporting open
source project infrastructure, assisting with coordinated vulnerability
disclosure, and ensuring the longevity of these projects and their dependencies.

## Obligations of Stewards

While the Cyber Resilience Act defines many obligations for manufacturers --
including potential for proportional penalties if those obligations are not met
-- the obligations for open source projects are *entirely voluntary*, only
applicable to open source software *intended for commercial use*, and do not
include financial penalties.

Lengthier articles have been written elsewhere, but to assist in understanding
this project, we have summarized those obligations below --

1. documenting a cybersecurity policy to foster secure development
1. documenting the effective handling of vulnerabilities
1. commiting to supporting the voluntary reporting of vulnerabilities as laid
   down in Article 15
1. cooperating with reasonable requests from market authorities
1. simultaneously notifying ENISA and, if appropriate, their national CSIRT of
   any severe cybersecurity incident affecting the project(s).
1. informing impaced users of actively exploited vulnerabilities or severe
   incidents and, where necessary, of any risk mitigation and corrective
   measures

_**TODO**_: Add references to FAQ or other articles describing the obligations
of stewards in more detail.

## A Two-Tier Attestation Framework

Following discussions held during and after the Code&Compliance Workshop in
October, 2025, we adopted a two-tier framework. This reflects the risk-based
approach mandated by the CRA and an emergent division among open source projects
intended for commercial use:
- some projects are only usable as "components" of more complex systems -- e.g.
  programming languages, rendering libraries, command-line utilities, and so on
  -- and do not meet the definitions of product categories in Annex III or Annex
  IV. 
- some projects are functionally equivalent to "products placed on the market".
  These projects may meet the definitions of products defined in Annex III or
  Annex IV, and may be only slightly modified, or not modified at all, by
  manufacturers prior to being placed on the market.

To accomodate these two tiers of open source project and facilitate
manufacturer's due diligence obligations under the CRA, we propose the adoption
of a tiered attestation system:

1. Tier 1 (Light-Weight) is a self-declaration process aligned with
   *BSI-TR-03185-2*, supported by documentation. It requires no third-party
   audit and is intended for projects of all sizes. 
2. Tier 2 (Heavy-Weight) has been proposed to build on Tier 1 with a full
   conformity assessment (Module B+C or Module H), including the potential for
   independent third-party audits. **However, the group has not agreed upon this
   path yet, and continues to discuss potential alternatives and analyze the
   ramifications of encouraging this approach.**

Our goal is that Light-Weight attestations reflect current & widespread
best-practices, should be documented in a consistent or machine-readable file
format, while Heavy-Weight attestations will require coordination and, likely,
funding to accomplish them. This reflects the proportional compliance effort
which manufacturers would shoulder, were they to attempt to acquire a
comprehensive independent audit of Tier 2 open source projects. 

While Tier 1 may not be entirely automatable -- it should be nearly so.


## Complications Arising from Third-Party Issuance of Attestations

According to Article 25, attestations regarding an Open Source Project should be
authorable by any market actor, including unaffiliated third parties such as
researchers and manufacturers, as well as national bodies. Therefore, a system
for the distribution and verification of the authenticity of attestations should
be contemplated. This also necessitates a mechanism to resolve disputed
third-party attestations. 

Additionally, it is necessary to comtemplate potential market-distoring effects, were
manufacturers to be permitted to issue and profit from a mechanism intended to
support open source software stewards.

---
## Acknowledgments

The following people have contributed to this document either directly or
indirectly (e.g. by raising questions, reviewing...):

1. Æva Black


If you have contributed to this document and aren't properly acknowledged or if
you want to edit or remove your name, please let us know by [opening an
issue](https://github.com/orcwg/orcwg/issues/new) and we will fix this right
away.
