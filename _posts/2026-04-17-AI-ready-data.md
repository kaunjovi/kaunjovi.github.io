


# AI-Ready Data: Architecting for the Agentic Era


## Day 0–30: Foundation & Governance
## Day 31–60: Core Capability Build

## Day 61–90: MVP Demo & Hardening
1. **Goal**: Polish the user experience, conduct a red‑team security review, and prepare the live demonstration for the executive steering committee.

1. Complete integration testing of all three capabilities.	
   1. Owner 
      1. QA & Integration - Who is going to do QA? Is there a UAT? 
   2. Success criteria 
      1. 100% of defined test cases pass; What are the test cases? 
      2. average response latency < 3 seconds. Is that a concern? Should be. How do we measure? 
2. Execute a formal AI TRiSM (Trust, Risk, Security Management) review, as recommended by Gartner.	
   1. CISO / Risk	
   2. No high‑severity findings open; 
   3. full audit trail of every LLM interaction is captured in CloudTrail / S3.
   4. There will be a pre PROD go live review and approval. 
   5. 
3. Onboard a pilot group of 20 “Data Ambassadors” (business and technical users) for a 2‑week feedback loop.	
   1. Data Office	
   2. Net Promoter Score (NPS) ≥ 30 collected via in‑app survey.
4. Executive Demo: 
   1. Conduct a live, 30‑minute walkthrough covering all three use cases, including a SQL generation challenge posed by the committee.	
   2. Asok & Team	
   3. Formal approval to move from “MVP” to “Phase 2 production rollout.”

Absolutely, Asok. Here is the full strategy—Northstar vision, 30/60/90 day tactical plan for EDNA, and the 12‑month roadmap—all laid out without any markdown tables, using a clean narrative and bulletised structure.

---

## EDNA: Enterprise Data Navigation Assistant
### Northstar Vision (The Agentic Data Ecosystem)

Our long‑term target is simple to state but transformative to execute: evolve our Data Lakehouse from a human‑centric query engine into a platform that treats AI agents as first‑class consumers. Industry momentum confirms this is not a “nice‑to‑have” but a necessity for survival as a Fortune 100 BFSI leader. Gartner’s 2025 Hype Cycle places AI agents and AI‑ready data at the very peak of enterprise priorities, while IDC reports that 40% of enterprises now rank an AI‑ready architecture as their top investment. Yet McKinsey’s sobering finding—that only 5% of enterprise Gen AI projects scale into production—is a direct warning: the ones that fail do so because of weak data foundations. We will ensure ACME lands squarely in the 5% that succeed.

So what does it mean to treat AI agents as first‑class?

- **Unified semantics, not just schemas:** Agents need business context—“revenue booked” vs. “projected revenue”—to avoid hallucination. We will extend Collibra with an AI‑readable semantic catalog that encodes definitions, lineage, quality flags, and ownership.
- **Governance‑by‑design:** In BFSI, governance cannot be a post‑hoc audit. It must be the execution layer that agents run against in real time, ensuring every data access is authorised, classified, and auditable.
- **Data Products as atomic units:** Agents will consume governed, certified Data Products, never raw tables. This is the pattern Microsoft Fabric has championed, where data products are the only interface exposed to downstream consumers.
- **Operational efficiency through autonomy:** Dremio’s Agentic Lakehouse shows that self‑optimising compaction, auto‑tagging of sensitive data, and AI‑based query routing can slash operational overhead ten‑fold. We will embed similar autonomous capabilities into our Iceberg ingestion pipelines.

EDNA is our deliberate first step onto this playing field. She is a read‑only “shopping assistant” that helps new data consumers discover and understand the 100+ Data Products in our catalog, search our handbooks, and even draft complex SQL—without ever being able to execute a query or touch a single row of data. The semantic layer, user feedback, and governance patterns we establish with EDNA will become the blueprint for every subsequent agent we deploy.

---

## EDNA MVP: Tactical Delivery Plan (30 / 60 / 90 Days)

Our principle for the next 90 days is simple: ship a secure, demonstrable chatbot that maps Collibra’s existing metadata into an AI‑native semantic catalog, and use it to build trust with business stakeholders inside a single quarter. No data execution, no shortcuts on security.

### Days 0–30: Foundation & Governance

**Goal:** Lock down the governance rules, pick our AWS‑native toolchain, and enrich the top 20 most‑used Data Products with AI‑consumable semantics.

- **AI Agent Governance Framework:** We will publish a BFSI‑specific framework covering data classification levels, allowed agent contexts, audit trail requirements, and responsible AI guardrails. Success means a document signed off by the CISO, Chief Data Officer, and Head of Compliance.
- **LLM & RAG stack selection:** Using Amazon Bedrock as our foundation, we will choose a frontier model (Claude or Llama 3.1) and a vector store (OpenSearch Serverless or pgvector on RDS). All of this will be deployed inside ACME’s AWS production VPC, integrated with Okta SSO and encrypted with KMS.
- **Semantic enrichment pipeline:** We will extract metadata from Collibra—business glossary terms, Data Product descriptions, full lineage, and ownership details—and ingest it into our vector store. For the top 20 Data Products we will add human‑curated definitions and a library of sample queries. The measurable outcome is that these 20 products are fully described and achieve manual semantic search accuracy of at least 85%.
- **Trusted execution environment:** Engineering will configure strict IAM roles, comprehensive CloudTrail logging, and network boundaries so that EDNA has absolutely zero path to Snowflake, Starburst, or any S3 bucket. A penetration test will formally confirm that no SQL execution or data read is possible.

### Days 31–60: Core Capability Build

**Goal:** Deliver the three core capabilities—discovery, handbook search, and SQL drafting—inside a functional prototype our internal team can test.

- **Data Product discovery:** Platform engineering will wire the semantic catalog to the LLM so that a natural‑language question like “Which Data Products contain FICO scores for US customers?” returns ranked, accurate results drawn solely from the enriched metadata.
- **Handbook semantic search:** The knowledge management team will ingest all ACME Data Handbooks (access policies, onboarding guides, data standards) into the same vector store. The success bar is that for a pre‑defined set of 50 FAQ queries, the correct handbook passage appears in the top three results at least 90% of the time.
- **SQL copilot (no‑execute):** Our advanced analytics squad will build a Text‑to‑SQL chain that leverages the semantic catalog to generate syntactically correct queries, including complex joins across Data Products. Thirty benchmark questions must be answered with SQL that a senior data architect judges at least 80% accurate on first attempt—a benchmark we know is achievable, as tigerData demonstrated a 27% accuracy gain from a similar approach.
- **EDNA chat interface:** UI/UX will deliver a Streamlit‑based (or lightweight React) frontend that sits behind ACME’s existing authentication reverse proxy and persists every conversation for audit.

### Days 61–90: MVP Demo & Hardening

**Goal:** Polish the user experience, survive a red‑team security review, and present a live demo to the executive steering committee.

- **Full integration testing:** QA will verify that all three capabilities pass every defined test case and that average response latency stays under three seconds.
- **AI TRiSM review:** Per Gartner’s guidance, the CISO and risk team will conduct a formal trust, risk, and security management review. The exit criteria are zero high‑severity findings and a full, immutable audit trail of every LLM interaction captured in CloudTrail and S3.
- **Pilot feedback:** We will onboard twenty “Data Ambassadors” from business and technical teams for a two‑week trial. In‑app surveys must yield a Net Promoter Score of at least 30.
- **Executive demo:** I will personally lead a thirty‑minute live walkthrough covering all three use cases. The committee will be invited to pose an impromptu SQL generation challenge. The goal is formal approval to move from MVP to Phase‑2 production rollout.

---

## The Larger AI‑Ready Data Strategy (12‑Month Roadmap)

Once EDNA has proved that an AI‑native semantic layer can work safely inside ACME, we will expand aggressively along four pillars.

### Pillar 1: AI‑Native Data Product Ownership
In the quarter immediately after MVP (Q2–Q3), we will introduce Data Product Service Level Indicators—freshness, completeness, semantic coverage—and tie them directly to the existing Collibra ownership assignments. An agent will continuously monitor for drift and automatically alert the designated owner. By Q4 we will shift to a true product mindset where every Data Product carries a published SLO, and any AI agent that attempts to consume a non‑compliant product will simply be refused. This directly addresses the current ownership vacuum and quality concerns.

### Pillar 2: Agentic Consumption Gateway
Building on the EDNA semantics, we will deploy a secure Model Context Protocol (MCP) server—akin to Dremio’s approach—that allows approved, internal AI agents to discover and reason over Data Products without gaining raw SQL access. In the scaling phase (Q4+), we will curate a library of first‑party agents: a Regulatory Compliance Agent that scans transactions against policy logic in near real‑time, and a Customer 360 Agent that proactively alerts relationship managers to anomalies or cross‑sell opportunities.

### Pillar 3: Autonomous Operations
We will embed AI‑driven compaction, vacuuming, and intelligent partitioning recommendations directly into our Iceberg pipelines. Dremio’s autonomous Reflections and managed Iceberg tables have shown this can cut manual platform operations by a factor of ten. Our target for Q4 is a 60% reduction in manual operations tickets for the data platform team, freeing our engineers to work on higher‑value delivery.

### Pillar 4: Semantic Catalog Expansion
During Q2–Q3 we will scale the enrichment work from 20 to all 100+ Data Products, using the LLM itself to auto‑generate column‑level descriptions that are then validated by human stewards. By Q4, we aim for greater than 90% SQL generation accuracy across all Data Products. That level of semantic coverage is what will eventually allow us to safely introduce governed, agentic data querying in a future release—moving EDNA from a read‑only navigator to a trusted, gated conduit for agent‑driven insights.

This phased approach lets us build trust incrementally, starting with a fully governed, read‑only natural‑language interface, while systematically constructing the infrastructure for a complete agentic data ecosystem. All of this runs on our existing Snowflake‑Iceberg‑Starburst‑Collibra stack, on our preferred AWS environment, and follows the stringent governance posture that our BFSI regulators demand.

---

## References & Recommended Reading (Most Recent First)

1. **Google Cloud Blog** – “The shift to a System of Action: Architecting the Agentic Data Cloud” (April 2026)  
   https://cloud.google.com/transform/shift-system-of-action-architecting-the-agentic-data-cloud-AI

2. **CIO.com** – “8 tips for rebuilding an AI-ready data strategy” (December 2025)  
   https://www.cio.com/article/4104444/8-tips-for-rebuilding-an-ai-ready-data-strategy.html

3. **ET Edge Insights** – “Why BFSI needs a governance-first approach to scalable & explainable agentic intelligence” (December 2025)  
   https://etedge-insights.com/industry/bfsi/why-bfsi-needs-a-governance-first-approach-to-scalable-explainable-agentic-intelligence/

4. **Microsoft Cloud Adoption Framework** – “Data architecture for AI agents across your organization” (December 2025)  
   https://learn.microsoft.com/ga-ie/azure/cloud-adoption-framework/ai-agents/data-architecture-plan

5. **Dremio Cloud Announcement** – “Dremio Ushers in the Agentic Era with Launch of the Industry’s First AI-Driven Lakehouse” (November 2025)  
   https://www.dremio.com/newsroom/dremio-ushers-in-the-agentic-era-with-launch-of-the-industrys-first-ai-driven-lakehouse/

6. **McKinsey & Company** – “The State of AI” (2025 Global Survey, reported November 2025)  
   https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

7. **TigerData (Timescale)** – “The Database Has a New User—LLMs—and They Need a Different Database” (August 2025)  
   https://www.tigerdata.com/blog/the-database-new-user-llms-need-a-different-database

8. **Gartner Hype Cycle 2025** – “AI agents & data readiness top Gartner’s 2025 tech priorities” (August 2025)  
   https://itbrief.in/story/ai-agents-data-readiness-top-gartner-s-2025-tech-priorities

9. **IDC 2025 Survey** – “40% of respondents consider AI-Ready data architecture a key investment” (June 2025)  
   https://my.idc.com/getdoc.jsp?containerId=prCHC53557525

10. **Starburst / Techstrong.ai** – “Starburst Unveils ‘Lakeside AI’ Platform” (May 2025)  
    https://techstrong.ai/building-with-ai/starburst-unveils-lakeside-ai-platform-to-accelerate-enterprise-ai-without-data-migration/
