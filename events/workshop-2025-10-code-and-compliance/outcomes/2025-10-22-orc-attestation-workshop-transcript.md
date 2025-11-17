## Economic Support

* **Economic Viability of Attestations:** Clarification is needed on whether an attestation is for a specific industry use or for compliance with future certifications (e.g., Common Criteria levels).  
* **Addressing "Freeloaders":** The discussion focused on how to address open source users who benefit without contributing. Mechanisms like licensing and copyleft have been used, but new models are needed given the Cyber Resilience Act (CRA).  
* **Incentivized Funding Sources:** Three potential revenue streams to incentivize investment in open source security/attestation were identified:  
  * **Public Procurement:** Governments could mandate that software providers demonstrate "good open-source community citizen" status as part of their procurement process (e.g., the German federal government spends €17 billion annually).  
  * **Insurance:** Insurers could require a healthy open-source supply chain as a condition for product insurance.  
  * **Financial Regulation:** European companies above a certain maturity (e.g., an LLC) must set aside money for external business risks; the open source supply chain qualifies as such a risk, encouraging investment in mitigating measures to avoid a 2.5% punishment.

![Outcomes of the Economic Support team displayed in the board][../pictures/2-economic-support.jpg "Economic Support Outcomes"]


## Transmission verification

* **Practicality of Delivery:** While sending signed PDFs might meet the strict letter of the law, it is not a practical strategy for open source projects.  
* **Proper Attestation Transmission:** The goal is to provide manufacturers and Market Surveillance Authorities (MSAs) with the tools and data to prove due diligence.  
* **Proposed Mechanism:**  
  * Define what is being attested to in a structured format (e.g., JSON).  
  * Use existing standards (e.g., **in-toto** with **Sigstore**, or **skit**) to format and sign the statements.  
  * Send statements to a service for timestamping and getting receipts.  
  * The manufacturer receives the whole package to prove they received the information at a certain time.  
* **Handling Changes:** A mechanism is needed to notify users when statements (e.g., "no vulnerabilities right now") might change, potentially requiring manufacturers to re-fetch the attestation periodically.

![Outcomes of the Transmission Verification team displayed in the board][../pictures/3-transmission-verification-group.jpg "Transmission verification Outcomes"]

## Identifying Minimums

* **Defining the Goal:** The project needs to determine the audience for the minimum attestation requirements: is it the small, one-person project maintainer, or a larger company?  
* **Nailing Down Requirements:** The key is to start listing requirements and focusing on a constructive, manageable subset.  
* **Possession of Information:** The most useful question is who possesses the required information. For example, the maintainer must decide the security contact point.  
* **Metadata/Stewardship Challenge:** Many smaller projects lack a steward or project organization, making it a "hairy problem" to help them provide the required documentation and metadata fields. This highlights the need for good guidance.

![Outcomes of the Identifying minimums Support team displayed in the board][../pictures/4-identifying-minimums.jpg "Identifying Minumims Outcomes"]

## Transitive dependencies

* **Definition of Dependencies:** The group agreed that for the CRA, dependencies should be defined exclusively as **"what is in a software digital product you distribute and everything that's in that product"** (what's in the box), excluding development or purely runtime requirements.  
* **SBOM Formats:** It was concluded that the solution is to **support all known SBOM formats** (SPDX, CycloneDX) as users will require different ones.  
* **Aggregated Attestations:** It was agreed that manufacturers should be able to aggregate attestations provided by their vendors (components), which would be a positive step.  
* **Unsolved Problem:** The challenge of attesting to and aggregating attestations for a large volume of packages (e.g., in Linux distributions, containers, or JavaScript applications) remains a problem.  
* **Funding Model:** A potential funding model discussed was to sell the attestations or their aggregation to interested manufacturers.  
* **Side Effect:** The large volume of dependencies is expected to drive a positive impact on **dependency minimization**.  
* **Attestation Content:** The attestation must include the correctness of the dependency set and be **actionable**, enabling vulnerability handling and providing minimal security contacts.  
* 

![Outcomes of the Transitive Dependencies team displayed in the board][../pictures/6-transitive-dependencies.jpg "Transitive Dependencies Outcomes"]

## Process-based attestations 

* **Scope:** These attestations are based purely on the process of the developing group and are likely within the reach of very small organizations.  
* **Content Inventory:** There should be an inventory of existing checklists, such as **Salsa, openSSF, and OWASP baseline**.  
* **Minimal Subset:** Existing checklists are too burdensome for small, three-person open-source projects, necessitating a minimal subset of factors that are:  
  * Deducible from the process, not the deliverables.  
  * Verifiable independently by a third party.  
  * Part of the developers' existing workflow, not requiring a quality officer or management.  
* **Periodicity:** Attestations would most likely be valid only on the day of download, as assertions cannot be guaranteed over the long term.  
* **Usefulness:** This level of attestation is considered a **hygiene factor** and a prerequisite, but not definitive. It is useful for aggregators (like Debian) to get ahead in their compliance process.

![Outcomes of the Process Based attestations team displayed in the board][../pictures/1a-process-based-attestations.jpg "Process based attestations Outcomes"]

## Outcome based attestations

* **Scope:** These attestations are related to a specific deliverable and are more likely to require a larger organization.  
* **Gap Identified: Open-Source Products:** A key gap is open-source projects that are themselves end-user products (e.g., LibreOffice). They face a challenge in proving safety to governments or administrators (e.g., schools) without a CE marking.  
* **Positive Side Effects:** Attestations can have positive side effects, like an attestation for LibreOffice allowing a school administrator to demonstrate the software is safe to parents.  
* **Standards & Definition:** Hopes were expressed that ETSI standards could be useful even outside their original context. There was also discussion about aligning the open-source definition with the CRA, particularly regarding licenses like GPL2.  
* **OSPO Sales Pitch:** A need for a sales pitch to help Open Source Program Offices (OSPOs) convince CFOs to fund compliance efforts.  
* **Example Framework:** The **Eclipse Trustable Software Framework** was mentioned as a good example of outcome-based attestation, following a structure of Provenance, Construction, Updatability, Confidence, and Human assessment of harm.

| Introduction By author that states that PDE is what is says it is Horror story: liability for the open source stewards OS wants to show attestation so that it is not liable   Natural person is most vulnerable in the supply chain. The natural person is vulnerable, they don't have money. They may be jointly liable. Looking at the cost; Focus on transparency\! One criterium as engineering team to choose OS is : is this project attested? Cheaper to attest a project than to trying to figure it. Is it cheaper to attest itself What exactly should be attested for?   Trustable software project, available on Eclipse website is good example of outcome-based attestation It follows this structure: Provenance Construction updatability confidence that it does what it does human assessment of harm possibly caused Outcome is like a credit score You can use Linux distro until A3. Attestation as a feature. So you can start to trust software. [Eclipse Trustable Software Framework | projects.eclipse.org](https://projects.eclipse.org/proposals/eclipse-trustable-software-framework)   Open source due diligence Manufacturers must address: What is the risk for the company to onboard the OS project? If component has attestation, it doesn't mean you don't need to test component. And if you choose them, do you fund it? Manufacturers will have to do heavy due diligence all the time. For open source stewards it's not an obligation   Open questions: If OS stewards gets donations and invests in attestation, do the freeriders just enjoy? OS stewards can offer their attestations for a fee. Will leveraging the attestation force the corporations to disclose the OS projects they are using (even if they don't have attestations)? Some OS projects will not fall under definition of CRA. Or they will do testing themselves.   Definition Article 3(48) provides a concerning definition Certain Projects will fall in a gap of CRA: What about projects that sell OS, but don't make it available on the market. Then is it not OS? What about forking the code : then you are changing the entity, and changing the attestation (if it has one). Does this impact qualification under CRA definition? Example: Open tofu Polyform non-commercial: states explicitly that this is not for commercial use. MIT/Apache 2 license require you to disclose the open source. Attestation for end users Another purpose for attestation is transparency towards end users Example: director of schools that need to show that software has attestation, "it's safe to use." Some OS projects are used by governments. Shouldn't they consider third party attestation, because of responsibility towards users? Certain OS projects could consider attestation because of moral responsibility rather than legal obligation What is heavy weight attestation?   Free access to standards Follows structure of vertical standards Example: VPNs. Standards that start from use case will be free. It will start from capability. These will be open source. CENELEC/ETSI: in practice it's 99% are the products relying on OS, not just 90%. No productivity suite in Libreoffice. You need a main type attestation that works for different OS projects. You need transparency for users. You don't want to end up with Linux distro. Problem is that big tech is out of this discussion   Concern is that big tech comes out with standard which is proprietary. Heavy weight attestation may bring in some heavy weight players. So that bigger manufacturers come in and pay most. Why would contributions for compliance be treated differently than contributions than adding features than code maintenance. Rules for attestation needed. Extra hands are needed to support compliance, rather than just throwing cash into it. Commons vs. proprietary attestation Nothing prevents open source steward from publicly publishing attestation. Commons: secure attestation is common responsibility Long term goal: clear requirements for guidance from stewards to manufacturers ASF: you cannot pay people to do something, to develop something. So you cannot support some projects financially. |
| :---- |

## Third-party attestations

* **The Problem:** Third-party testers will often act as an intermediary between a manufacturer and a very small, unorganized open-source community or individual.  
* **Balance of Power:** The major problem is the balance of power, where an organization could potentially monopolize attestation control and fees without compensating the developers ("money cow" scenario).  
* **Consent and Forkability Issues:** Enforcing a consent model (e.g., an individual developer agreeing to a sole provider) risks monopolistic control. Forking the code does not solve the problem, as the third party can also fork and continue their service.  
* **Potential Solutions:** Using **trademarks** to protect the project name, or having the project **indicate** what they are willing to accept from third parties.  
* **Manufacturer Trust:** Manufacturers would be "very picky" about the assurances and guarantees in third-party attestations. They prefer original developers/maintainers to be involved somehow.  
* **Marketplace Idea:** A "marketplace of foundations" was suggested where manufacturers could shop for attestations from trusted organizations.  
* **Trusted Third Parties:** Government bodies were crossed out as an option (too slow/not tech-friendly). Big corporations with project understanding were considered a possibility.  
* **Tiered Requirements:** Attestation should have different levels and requirements, with lower requirements for first-party assessments or non-critical open-source projects.


![Outcomes of the third party attestations team displayed in the board][../pictures/5-third--party-attestations.jpg "thisrd party attestations Outcomes"]

