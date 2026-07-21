
### I. Threat Landscape & Urgency (Recap)

- **Prompt Injection / Data Exfiltration:** Malicious actors using LLMs to bypass natural language query interfaces and extract HC (Highly Confidential) data from our Data Products.
- **Poisoned Training Data:** Compromised data entering our Raw/Validated layers, corrupting our internal AI/ML models.
- **Privilege Escalation via AI:** AI agents given "read" access misinterpreted as "write" or "export" permissions, leading to data leaks.
- **Shadow AI:** Business users plugging ACME data into unauthorized public AI tools, bypassing our governance.

### II. The Five-Pillar Strategy

#### Pillar 1: Zero-Trust Data Access & Entitlement Refactoring
*Current State:* Access is role-based but largely static. AI tools currently inherit human privileges.

| Task ID | Task Description | Deliverable | Timeline |
| :--- | :--- | :--- | :--- |
| **P1-01** | Implement **Dynamic Data Masking (DDM)** at the Snowflake view layer for all AI-consumed Data Products. Queries returning HC columns (PII, SSN, Account #) will be redacted based on the *AI Agent's* role, not just the user's. | Production-ready masking policies for Top 50 DPs | Q1 (Months 1-3) |
| **P1-02** | Enforce **Just-In-Time (JIT)** elevated access for AI training pipelines. No AI model gets persistent write access to Conformed/Iceberg layers; access must be requested and approved via ServiceNow integration. | Automated approval workflow | Q2 |
| **P1-03** | Implement **Attribute-Based Access Control (ABAC)** in Iceberg, using tags (e.g., `Confidentiality=High`) to enforce filters at the storage layer before data even reaches Snowflake. | ABAC policies in Iceberg REST catalog | Q2-Q3 |

**Human Resources:** 3 Security Engineers (Snowflake/Iceberg experts) + 1 Identity & Access Management (IAM) lead.

#### Pillar 2: Data Encryption & Tokenization Upgrade
*Current State:* Data at rest is encrypted, but data in *transit* to AI inference endpoints is not fully tokenized.

| Task ID | Task Description | Deliverable | Timeline |
| :--- | :--- | :--- | :--- |
| **P2-01** | Enable **end-to-end encryption** for all data pipelines from Iceberg Raw to Snowflake DP, specifically focusing on data extracted for LLM Retrieval-Augmented Generation (RAG). | TLS 1.3 + field-level encryption | Q1 |
| **P2-02** | Deploy **Format-Preserving Tokenization (FPT)** for all PII in the Conformed Layer. If a token is exfiltrated via an AI prompt, it is useless to the attacker. | Tokenization vault integration | Q2 |
| **P2-03** | Conduct a **crypto-agility audit** to ensure we can rotate keys immediately in case of a breach, without taking down production DPs. | Key rotation playbook tested | Q3 |

**Human Resources:** 2 Cryptography/Cloud Security Specialists (leveraging shared SecOps for infrastructure).

#### Pillar 3: Collibra "AI Sentinel" Governance Upgrade
*Current State:* Collibra holds metadata, but it is *passive*. We are not actively using it to police AI queries.

| Task ID | Task Description | Deliverable | Timeline |
| :--- | :--- | :--- | :--- |
| **P3-01** | Activate **Collibra Data Lineage & Impact Analysis** for AI workflows. If an AI model is fed from a Data Product, we must map that lineage to block queries if the source data is under a security advisory. | Active lineage map for all AI use cases | Q1-Q2 |
| **P3-02** | Build a **"Sensitive Data Radar"** using Collibra APIs. Automatically scan all AI-generated SQL/Python queries for references to HC-tagged columns and block them if the user lacks a specific "AI-HC" clearance. | Custom Python microservice integrated with Snowflake | Q2 |
| **P3-03** | Enforce **Data Expiration Policies** for AI training datasets. No training data older than 90 days is valid for real-time AI inference, reducing the "blast radius" of a leak. | Automated purging jobs | Q3 |

**Human Resources:** 2 Data Governance Engineers + 1 Collibra SME.

#### Pillar 4: AI Threat Monitoring & Anomaly Detection (The "SIEM for AI")
*Current State:* We monitor infrastructure, but we don't monitor *behavior* of AI agents or unusual data access patterns.

| Task ID | Task Description | Deliverable | Timeline |
| :--- | :--- | :--- | :--- |
| **P4-01** | Implement **AI Behavioral Monitoring** – track metrics like `rows_returned_per_query`, `export_frequency`, and `time_of_access`. Flag queries that return >10,000 HC records from an AI endpoint at 2 AM. | Snowflake Query History + custom dashboards (Splunk/DataDog) | Q2 |
| **P4-02** | Deploy a **"Honeytoken"** system. Inject fake "Highly Confidential" records into the Conformed layer that are never used by real business processes. If an AI model queries or exports these, it triggers an immediate security incident. | Honeytoken tables + alerting | Q3 |
| **P4-03** | Conduct **bi-weekly "Red Teaming"** of our own AI endpoints to test for prompt injection and SQL injection vulnerabilities. | Vulnerability report & patching cycle | Ongoing (Monthly) |

**Human Resources:** 1 Security Data Analyst + 1 MLOps Engineer (part-time) + External Red Team vendor (quarterly).

#### Pillar 5: Training, Culture & "Shadow AI" Policy
*Current State:* Data stewards and business users are unaware of the specific risks of AI.

| Task ID | Task Description | Deliverable | Timeline |
| :--- | :--- | :--- | :--- |
| **P5-01** | Roll out mandatory **"AI Hygiene"** certification for all 200+ Data Product owners and data stewards. Covers: Prompt Engineering risks, Data Lineage responsibilities, and Incident Reporting. | Online LMS course + quarterly refreshers | Q1 (Launch) |
| **P5-02** | Launch an internal **"AI Yellow-Light"** policy. Any business user wishing to use a third-party AI tool (ChatGPT, Claude, etc.) with ACME data must route it through a "Secure Sandbox" we control, not public portals. | Secure sandbox deployment | Q1-Q2 |
| **P5-03** | Host a **"Cyber-AI Wargame"** – a half-day tabletop exercise with the BFSI board and IT leadership simulating a successful AI-driven data exfiltration to test our response times. | Incident response runbook update | Q4 |

**Human Resources:** 1 Training & Change Management Lead + Vendor for Wargame facilitation.

### IV. Summary Budget Request (FY 2026-27)

| Category | FY Request (USD) |
| :--- | :--- |
| **Personnel** (New Hires: 9.5 FTEs incl. Security Eng, Gov Eng, Analysts, Trainers) | $1,350,000 |
| **Software/Tools** (Tokenization, Collibra Premium, SIEM upgrades, Sandbox) | $525,000 |
| **External Services** (Red Team, Wargames, Threat Intel) | $200,000 |
| **Contingency** (Unforeseen zero-day AI patches/hotfixes) | $150,000 |
| **Total** | **$2,225,000** |

---

### V. Finally 

Furthermore, I am ensuring **operational stability** by:
1.  **Phasing:** No changes to the Core Data Products in Q1; we focus only on Access and Encryption at the *view* level before touching the physical Conformed layer.
2.  **Rollback Plans:** Every security measure (DDM, Tokenization) has an automatic "fail-open" kill-switch in case of performance degradation, ensuring business continuity takes precedence.

We are not just defending against today's threats; we are future-proofing ACME for the generative AI era. 

