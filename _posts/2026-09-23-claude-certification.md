---
layout: post
title: "Claude Certification - Exam Domain Breakdown"
date: 2026-09-23
categories: [AI, Certification, Claude]
---


## Running Claude on Windows, with proper isolation 

1. On Windows, Claude Code's built-in sandboxing (sandboxed Bash tool) is not supported on native Windows; you must use WSL2 or another isolation solution.
2. Claude Code's built-in sandboxing only covers shell commands; 
   1. file tools (Read/Edit/Write), MCP servers, and hooks run outside the sandbox.
3. **WSL2 + Claude Code's Built-in Sandbox (Official Recommended Path)**
   1. process-level sandboxing
   2. Confirm or install WSL2 in PowerShell: wsl -l -v to check the version, use wsl --install -d Ubuntu to install if needed.
   3. Enter the WSL2 environment, install dependencies (e.g., in Ubuntu): sudo apt install bubblewrap socat.
   4. Run claude in the WSL2 terminal, then execute the /sandbox command to enable and configure sandbox mode (auto-allow or regular permissions).
   5. Your Windows project files will be accessible under /mnt/c/... in WSL2, and you can operate on them directly.
4. **Option 2: Docker Sandboxes**
   1. Each agent runs in a dedicated microVM, with only the project workspace mounted in, keeping the host machine completely isolated;
   2. docker sandbox run claude [path]
5. **Option 3: Community Docker/WSL Solutions (Simpler Wrapping)**


## Docker Sandboxes

1. https://medium.com/@vasanthank29/docker-sandboxes-running-claude-code-and-other-coding-agents-in-isolated-microvms-94cff12b2342
2. Docker Sandboxes: Running Claude Code and Other Coding Agents in Isolated MicroVMs
3. Docker Sandboxes let you run Claude Code, Codex, Copilot CLI, Gemini CLI, Kiro and other coding agents with full autonomy inside a disposable microVM, so a mistake or an attack stays inside the box instead of reaching your machine.
4. Docker Sandboxes moves fast. This guide uses the standalone sbx CLI as documented in October 2026.
5. don’t ask the program to behave, put it somewhere it cannot do damage.
6. When you run claude in your terminal, it is just a process: a running program managed by your operating system's kernel (the core part of the OS that controls memory, files, network and hardware). A process inherits your user account. Whatever you can read, delete or upload, it can too. There is no wall at all.
7. A container (what docker run gives you) is still a normal process, but the kernel shows it a filtered view of the world
8. This is excellent for packaging and running trusted applications. But every container on the machine still talks to the same host kernel. 
9. Containers are a fence, not a wall.
10. A virtual machine (VM) goes further. A piece of software called a hypervisor uses hardware virtualization features built into modern CPUs (Intel VT-x, AMD-V, Apple’s Virtualization framework) to create a fake computer: virtual CPU, virtual memory, virtual disk. That fake computer boots its own kernel. Code inside the VM talks to its kernel, not yours. To reach your host, an attacker must find a bug in the hypervisor itself, which is a much smaller and much more heavily scrutinized surface.
11. A microVM keeps the strong part of a VM (separate kernel, hypervisor boundary) and throws away the heavy part. 
12. It emulates only the handful of devices a server workload needs, boots a minimal kernel, and starts in a fraction of the time. The same idea powers serverless platforms that run untrusted customer code side by side.
13. Docker Sandboxes is a tool from Docker that gives each AI coding agent its own disposable microVM, with its own filesystem, network and Docker daemon, so the agent can run unattended without touching your host.
14. Docker started the project to answer a simple question developers kept asking: how do I run Claude Code or Gemini CLI safely?
15. moved to one microVM per sandbox and to a standalone CLI called sbx. You no longer need Docker Desktop to use it.
16. sbx run claude
17. Installed packages, pulled images and agent history survive sbx stop and come back on the next sbx run. A sandbox is deleted only when you run sbx rm (or start it with --rm for a throwaway session).
18. This “start closed, open as needed” pattern is called an **allowlist**, and 
    1.  it is the same approach firewalls in production networks use. 
    2.  The benefit is that a surprise destination (for example a paste site or an unknown IP) shows up in the log as blocked instead of quietly succeeding.



## Prerequisites

The prerequisite that stops everyone: **Partner Network + a work email**.

Certification is available only to people at Claude Partner Network organizations. Registration requires a partner email address on a recognized company domain — personal email addresses will not work.

1. [Complete guide to Anthropic's Claude Certifications](https://medium.com/@roanmonteiro/the-complete-guide-to-anthropics-claude-certifications-the-4-exams-the-prerequisite-that-blocks-4d1f743bc5c4)
2. [Certification FAQ](https://anthropic-partners.skilljar.com/page/faq-certifications)
3. [Anthropic Partner Academy](https://anthropic-partners.skilljar.com/)

The Claude Certification program validates that people at partner organizations have the skills to do real work with Claude, across three roles: Associate, Developer, and Architect. Certification counts toward your firm's standing in the Claude Partner Network.

---

## Study Plan — 6 Weeks

1. **Weeks 1–2 — Baseline (any track):** AI Fluency, Claude 101, Claude Platform 101, Building with the Claude API.
2. **Weeks 3–4 — Primary sources:** "Building Effective AI Agents", the MCP spec, the Claude Code docs. Read, don't skim.
3. **Week 5 — Build, don't just read:**
   1. Ship a private repo with an MCP server returning the structured error envelope.
   2. A Claude Code project with a `CLAUDE.md`, one pre-commit hook, one slash command, one skill under `.claude/skills/`.
   3. Bonus: a raw-Python agent loop handling `tool_use → result → end_turn` with timeout retries.
   4. An extraction pipeline that reports segmented accuracy, not just aggregate.
4. **Week 6 — Mock:** Build 60 of your own questions per track, time-box to 120 minutes, grade ruthlessly. Every miss becomes one log line with the correct answer and the trap.

---

## Resources

1. [Tutorials Dojo – CCAR-P Study Guide](https://tutorialsdojo.com/ccar-p-claude-certified-architect-professional-study-guide/)
2. [Claude Cheat Sheets](https://tutorialsdojo.com/other-cheat-sheets/claude-cheat-sheets/)
3. [Claude Code Cheat Sheet](https://tutorialsdojo.com/claude-code/)
4. [Anthropic Courses](https://claude.com/resources/courses)
5. [Anthropic Skilljar](https://anthropic.skilljar.com/)
6. [Deploying Claude Enterprise with Confidence](https://anthropic-partners.skilljar.com/deploying-claude-enterprise-with-confidence-the-five-decisions-that-shape-your-rollout)
7. [Claude with Amazon Bedrock](https://academy.claude.com/courses/claude-with-amazon-bedrock)
8. [Claude with Google Cloud's Vertex AI](https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai)
9. [AI Fluency for Builders](https://academy.claude.com/courses/ai-fluency-for-builders)
10. [Build Frontier Agents on the Claude Platform](https://claude.com/platform/api)

---

## Claude Certified Architect – Professional (CCAR-P)

For experienced solution architects. Covers designing and leading enterprise-scale deployments, integration architecture, optimization at scale, and governance.

1. [CCA-P Official Home Page](https://anthropic-partners.skilljar.com/claude-certified-architect-professional-certification)
2. [CCA-P Exam Guide v1.0 – Effective July 2026 (PDF)](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542810%2FClaude+Certified+Architect+%E2%80%93+Professional+Exam+Guide.pdf)
3. [Certification: Architect Foundations](https://anthropic-partners.skilljar.com/claude-certified-architect-foundations-certification)

### Free Pre-Reads

1. [AI Fluency Framework – Foundations](https://anthropic-partners.skilljar.com/ai-fluency-framework-foundations)
2. [Claude with the Anthropic API](https://anthropic-partners.skilljar.com/claude-with-the-anthropic-api)
3. [Claude with Google Vertex](https://anthropic-partners.skilljar.com/claude-with-google-vertex)
4. [Claude 101](https://anthropic-partners.skilljar.com/claude-101)
5. [Claude in Amazon Bedrock](https://anthropic-partners.skilljar.com/claude-in-amazon-bedrock)
6. [Introduction to Model Context Protocol](https://anthropic-partners.skilljar.com/introduction-to-model-context-protocol)
7. ✅ [Claude Code in Action](https://anthropic-partners.skilljar.com/claude-code-in-action)

### Claude Model Family

1. Fable 5.1
2. Opus 5.5
3. Sonnet 5.5
4. Haiku 4.5

---

## CCAR-P Exam Domains

| # | Domain | Weight |
|---|--------|--------|
| 1 | Integration | 19% |
| 2 | Solution Design and Architecture | 17% |
| 3 | Evaluation, Testing, and Optimization | 16% |
| 4 | Governance, Safety, and Risk Management | 14% |
| 5 | Stakeholder Communication and Lifecycle Management | 14% |
| 6 | Claude Models, Prompting, and Context Engineering | 13% |
| 7 | Developer Productivity and Operational Enablement | 7% |

---

## Domain 1 – Integration (19%)

As the highest-weighted domain, this focuses on wiring Claude into complex, legacy enterprise environments securely and performantly.

1. **RAG Pipeline Architecture** — Designing production retrieval-augmented generation pipelines, selecting chunking and indexing strategies matched to enterprise data shapes and query patterns.
2. **Connection Protocols** — Evaluating integration mechanisms: Model Context Protocol (MCP), standard API/CLI access, and agent-to-agent protocols.
3. **Trade-Off Operations** — Balancing accuracy-latency trade-offs, managing system monitoring/observability at scale, and securing API keys, authentication, and authorization frameworks.

---

## Domain 2 – Solution Design & Architecture (17%)

Tests your ability to translate vague business problems into scalable, concrete Claude-powered system topologies.

1. **Architectural Pattern Selection** — Deciding when to use a strict workflow pattern (deterministic pipelines), an augmented LLM pattern (single call enriched with tools/retrieval), or a fully agentic pattern (autonomous looping and dynamic reasoning).
2. **Orchestration Strategies** — Building and managing complex multi-agent architectures and implementing problem decomposition techniques.
3. **Business Pillars** — Ensuring architecture aligns with enterprise SLAs, cost boundaries, efficiency goals, and production scaling demands.

### Architectural Patterns

| Pattern | Use When |
|---------|----------|
| **Workflow (Chained / Sequential)** | Steps are deterministic and sequential; each stage feeds directly into the next without branching loops |
| **Augmented LLM (RAG)** | Claude needs external factual grounding or up-to-date data retrieved dynamically before generating a response |
| **Agentic (Autonomous / Loop-based)** | Number of steps is unpredictable; Claude must dynamically decide and execute tool calls in a feedback loop |
| **Multi-Agent Systems** | Specialized roles (Coordinator, Researcher, Validator) must divide complex work; accept higher latency and failure surfaces |

### Exam Traps & Decision Rules

1. **The Complexity Trap** — Avoid choosing the "impressive" agentic pattern when a simple workflow or single-shot prompt suffices.
2. **The Fit Rule** — The correct answer is never which pattern is best in the abstract; it's always the one that balances capability against latency, cost, and reliability.
3. **Failure Surface** — Adding agents or autonomous loops increases error propagation and debugging overhead; justify every extra layer with a clear requirement.

### Workflow Pattern Deep Dive

**When to choose it:**
1. High reliability required, known steps in a known sequence
2. Minimize token cost, respond within tight SLA

**When NOT to choose it:**
1. Steps are unpredictable or require dynamic branching

**Example use cases:** Structured data extraction, content pipelines

### Mock Question 1

> An enterprise financial services company processes quarterly earnings report PDFs to generate compliance-checked executive summaries. The process has three fixed steps: extract financial metrics → draft summary in corporate tone → validate against regulatory compliance checklist. The engineering team must minimize token costs and ensure a fully auditable execution path.

**Answer: Workflow (Chained / Sequential)**

1. **Minimize token costs** → rules out Agentic Loop and Multi-Agent structures.
2. **Three distinct steps** → each prompt stays small, sharp, and focused on one task.
3. Break the chain: Step 1 extracts, Step 2 writes, Step 3 validates.

### Mock Question 2

> A global retailer uses Claude to review inbound freight quotes before selecting carriers. The system must: extract shipment costs and service terms → validate against procurement policies → generate a recommendation. Stages follow consistent rules and later stages depend on earlier output. The company needs a predictable and auditable pattern.

**Which architectural pattern best meets these requirements?**

| Option | Assessment |
|--------|------------|
| A. Fixed workflow with discrete, sequenced LLM calls for each stage | ✅ **Correct** — predictable, auditable, stages depend on prior output |
| B. Single monolithic prompt that autonomously decides additional processing | ❌ Not auditable; unpredictable execution path |
| C. Autonomous agent that dynamically creates its own processing plan | ❌ Overkill; steps are well-defined and consistent |
| D. Parallel LLM calls that independently extract, validate, and generate simultaneously | ❌ Validation cannot run before extraction completes |

---

## Domain 3 – Evaluation, Testing & Optimization (16%)

Covers methodologies to continuously prove that production systems work, avoid regression, and operate cost-efficiently.

1. **System Testing & Data** — Designing mixed-method evaluation frameworks and test datasets for continuous integration checks.
2. **Metrics Defensibility** — Tracking and defending metrics across five pillars: accuracy, latency, cost, safety, and security.
3. **Root Cause Diagnostics** — Identifying and resolving prompt failures, hallucinations, model mismatches, and token-bloat using enterprise observability tools.

---

## Domain 4 – Governance, Safety & Risk Management (14%)

Professional-exclusive domain focused on responsible AI deployment.

1. **Regulatory Compliance** — Architecting guardrails to meet GDPR, HIPAA, and FedRAMP.
2. **System Defences** — Designing enterprise-grade safety controls, context isolation, and prompt injection mitigation.
3. **Validation Loops** — Architecting optimal human-in-the-loop (HITL) checkpoints to handle edge cases safely without slowing operations.

---

## Domain 5 – Stakeholder Communication & Lifecycle Management (14%)

Tests an architect's ability to act as the primary interface between the technical team and business executives.

1. **Defending Decisions** — Articulating complex architectural trade-offs (e.g., context caching vs. fine-tuning, Sonnet vs. Opus for a specific workflow).
2. **Lifecycle Ownership** — Managing the full lifecycle from business discovery and requirement gathering through handoff, operations, and iterative updates.

---

## Domain 6 – Claude Models, Prompting & Context Engineering (13%)

Focuses on optimizing Claude's native capabilities to minimize latency and manage cost.

1. **Model Tier Optimization** — Correctly selecting across the Claude family (Haiku, Sonnet, Opus) based on computational and financial constraints.
2. **Context Window Engineering** — Managing large token footprints, prompt templates, system prompts, few-shot conditioning, and chain-of-thought.
3. **Token Reuse Strategies** — Implementing advanced caching, modular systems, and Anthropic Skills frameworks.

### Key Concepts

1. **Primacy effect** — LLMs tend to recall information placed at the beginning of the context.
2. **Recency effect** — LLMs also have good recall of information at the end of a prompt.
3. **Lost in the middle / attention dilution** — In large contexts, LLMs tend to miss, ignore, or poorly reason about information in the middle.
4. **U-shaped recall** — The combined result: strong recall at both ends, poor recall in the middle.

---

## Domain 7 – Developer Productivity & Operational Enablement (7%)

Tests your capacity to establish platform infrastructure that lets engineering teams build with Claude efficiently.

1. **Team Tooling** — Configuring standardized workspaces, environments, and AI-assisted tools like Claude Code for enterprise teams.
2. **Workflow Acceleration** — Driving debugging methodologies, deployment workflows, and operational incident resolution.

---

## Claude Code – Key Commands & Concepts

### CLAUDE.md Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Generated with `/init`; commit to git and share with the team |
| `CLAUDE.local.md` | Personal commands and notes; do not check in |
| `~/.claude/CLAUDE.md` | Machine-level instructions applied to all projects |

Every request to Claude Code includes the content of `CLAUDE.md`. Update it to shape Claude's behavior (e.g., add `# use comments sparingly`).

### Useful Commands

| Command / Key | What it does |
|---------------|-------------|
| `/init` | Read the codebase and write notes to `CLAUDE.md` |
| `Shift Tab` | Auto-accept all changes |
| `/plan` or `Shift Tab Shift Tab` | Enter plan mode (breadth-first research) |
| `Ctrl 0` | Show Claude's thinking process |
| `/effort` | Check how hard Claude is thinking |
| `/ultrathink` | Boost thinking depth |
| `/compact` | Summarize a long, useful context to save tokens |
| `/clear` | Clear conversation and start over |
| `Esc` | Interrupt a running task |
| `Esc Esc` | Rewind conversation (discard detour context) |
| `Ctrl V` | Paste an image into Claude Code (works on Mac too) |
| `>` prefix | Ask a question about the code (e.g., `> How does auth work?`) |

### Custom Commands

Add `.claude/commands/my-own-command.md` — an md file with a blueprint of what you want Claude to do.

### Hooks

Run code before or after a tool call (e.g., code formatter).

1. **`PreToolUse`** / **`PostToolUse`** — configured in `settings.local.json`
2. Use `PreToolUse` to inspect or block what Claude is about to do
3. Exit code `2` blocks the tool call; stderr is forwarded to Claude
4. Example: Block Claude from ever reading `.env` files containing secret keys

**Caveat:** You need to know which tools to block. Listing tools is a point-in-time snapshot — new tools added later won't be automatically covered.
