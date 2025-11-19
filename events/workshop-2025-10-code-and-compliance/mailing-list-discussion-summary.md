# **CRA Article 25 Attestations: Community Discussion Summary from ORC mailing list**

*This summary reflects discussions from the [ORC mailing list](https://www.eclipse.org/lists/open-regulatory-compliance/) October-November 2025 that followed from, and explored topics raised during, the Code & Compliance Workshop (October 23-24, 2025).*


## **Executive Overview**

The Open Regulatory Compliance Working Group (ORC-WG) has been actively developing frameworks for voluntary security attestations under Article 25 of the EU Cyber Resilience Act. Through facilitated workshops and extensive mailing list discussions, the community has discussed key challenges and proposed several models for sustainable implementation. This summary highlights themes and actionable proposals emerging from October-November 2025 discussions.

## **Core Challenges Identified**

### **1\. Scope and Authority of Attestations**

The community debates fundamental questions about attestation scope and authority. **Mathias Schindler** ([msg00948](https://www.eclipse.org/lists/open-regulatory-compliance/msg00948.html)) crystallized three critical questions: whether Recital 34 defines sufficient due diligence, who should be authorized to issue attestations, and whether attestations are recipient-bound. **Jordan Maris** ([msg00963](https://www.eclipse.org/lists/open-regulatory-compliance/msg00963.html)) argues that while Recital 34 may suffice for low-risk uses, higher-risk products require more comprehensive attestations, warning that without restrictions, "dozens of companies pop up whose entire mission is to harass Open Source developers."

### **2\. Economic Sustainability vs. Open Access**

A central tension exists between ensuring sustainable funding and maintaining open source principles. **Greg Wallace** ([msg01005](https://www.eclipse.org/lists/open-regulatory-compliance/msg01005.html)) advocates treating OSS as a natural resource requiring sustainability fees rather than cost-recovery pricing, noting the vast gap between OSS production costs ($4.15B) and replacement value ($8.8T). **Elizabeth Mattijsen** ([msg00970](https://www.eclipse.org/lists/open-regulatory-compliance/msg00970.html)) points out that public attestations could undermine steward business models, while **Scott Lewis** ([msg00953](https://www.eclipse.org/lists/open-regulatory-compliance/msg00953.html)) reminds everyone and re-centers the truism that "Community is inseparable from Open Source."

### **3\. Implementation Complexity**

The technical and organizational complexity of implementation presents significant challenges. **Tobie Langel** ([msg01013](https://www.eclipse.org/lists/open-regulatory-compliance/msg01013.html)) notes that successful programs must accommodate widely different ecosystems—from single-maintainer plugins to corporate-led projects like Chromium. **Martin von Willebrand** ([msg00994](https://www.eclipse.org/lists/open-regulatory-compliance/msg00994.html)) cautions against inadvertently raising the bar on existing projects and communities beyond existing good practices like git usage, transparency, and code review.

## **Proposed Models**

### **Two-Tier Attestation Framework**

**Æva Black** ([msg00998](https://www.eclipse.org/lists/open-regulatory-compliance/msg00998.html)) returns the discussion in a two-tier system encouraged by the commission:

* **Light/Process-based**: For low-complexity libraries demonstrating secure development practices  
* **Heavy/Outcome-based**: For product-like projects requiring near CE-mark equivalent attestations

**Tobie Langel** ([msg01022](https://www.eclipse.org/lists/open-regulatory-compliance/msg01022.html)) suggests the BSI's TR-03185-2 guidelines could serve as a foundation for the light tier, providing immediate actionable standards.

### **Hybrid Funding Model**

**Jordan Maris** ([msg00965](https://www.eclipse.org/lists/open-regulatory-compliance/msg00965.html)) outlines a possible crowdfunding approach where attestations become public once funding goals are met, with early supporters receiving discounted access. **Victoria Risk** ([msg00971](https://www.eclipse.org/lists/open-regulatory-compliance/msg00971.html)) expands this concept to include non-monetary commitments like code contributions or data sharing.

### **Centralized Registry Approach**

**Alice Sowerby** ([msg00975](https://www.eclipse.org/lists/open-regulatory-compliance/msg00975.html)) proposes a non-profit registry where manufacturers upload SBOMs to automatically select and purchase required attestations. While this addresses the dependency complexity problem, **Elizabeth Mattijsen** ([msg00977](https://www.eclipse.org/lists/open-regulatory-compliance/msg00977.html)) warns against creating "yet another organization" that could become a rent-seeking intermediary.

### **Natural Resource Management Model**

Building on **Greg Wallace's** fishery fee analogy ([msg01005](https://www.eclipse.org/lists/open-regulatory-compliance/msg01005.html)), **Scott Lewis** ([msg01006](https://www.eclipse.org/lists/open-regulatory-compliance/msg01006.html)) references Elinor Ostrom's commons governance work, suggesting community-created rules and local enforcement mechanisms. **Jeremy Stanley** ([msg01012](https://www.eclipse.org/lists/open-regulatory-compliance/msg01012.html)) adds the utility cooperative model as a potential governance structure.

## **Key Considerations**

### **Legal and Organizational**

* **U.S. 501(c)(3) organizations** may face specific challenges in charging for attestations (Seth Larson leading sub-group investigation)  
* **Fiscal hosts** may not qualify as stewards since they typically don't manage day-to-day security responses  
* **Fragmentation** across 27 EU member states' non-profit laws complicates implementation

### **Technical Requirements**

* **Machine-readability** essential for managing hundreds/thousands of dependencies  
* **SBOM integration** critical for automation  
* **Dispute resolution** mechanisms needed for third-party attestations  
* **Verification systems** must avoid creating "ICANN 2.0" (**Alistair Woodman**, [msg00978](https://www.eclipse.org/lists/open-regulatory-compliance/msg00978.html))

### **Community Principles**

* **Maintainer autonomy**: Stewards have "NO LEVERAGE over the Maintainer's project" and must not encumber the project more than absolutely necessary. (**Salve J. Nilsen**, [msg00997](https://www.eclipse.org/lists/open-regulatory-compliance/msg00997.html))  
* **Contributor recognition**: **Pierre Pronchery** ([msg01021](https://www.eclipse.org/lists/open-regulatory-compliance/msg01021.html)) advocates for discounts based on contributions  
* **Avoiding harm**: **Jordan Maris** ([msg01018](https://www.eclipse.org/lists/open-regulatory-compliance/msg01018.html)) notes CRA impacts are inevitable; focus should be on mitigation

## **Recommended Path Forward**

The community appears to be converging on a hybrid approach combining:

1. **A two-tier technical framework** with   
   1. BSI guidelines for the light tier  
   2. conformity assessments for the heavy tier, based on the as-yet-unpublished CEN and ETSI standards   
2. **Flexible funding models** allowing both public funding sources and fee-based approaches to support FOSS project’s operational overhead  
3. **Recognition of existing best-practices** as a baseline for compliance  
4. **Community governance** approaches must respect ecosystem diversity

With a 6-7 month timeline for EC recommendations and FOSDEM presentations planned for January, the focus is shifting from theoretical debates to practical pilots. Organizations like FreeBSD, Python Software Foundation, and CPAN are already developing attestation programs that will inform the final framework.

## **Next Steps**

* Complete legal analysis for U.S. non-profits (Seth Larson sub-group)  
* Develop template for the light tier, collect feedback from community and commission  
* Pilot attestation programs with willing stewards  
* Create machine-readable standards for deep supply chain coverage  
* Develop concrete pricing guidelines based on risk class and project complexity  
* Prepare anti-FUD messaging for FOSDEM to address community concerns
