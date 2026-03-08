---
layout: post
title: Running Notes 
categories: [Running Notes] 
---


## cybersecurity posture 
1. In cybersecurity, "posture" isn't how you sit—it's how your data is governed and protected. Just like physical posture, a small security "slouch" today can break your system tomorrow.
1. AppSec and AI Security
1. 𝗗𝗶𝘀𝗰𝗼𝘃𝗲𝗿𝘆 (𝗙𝗶𝗻𝗱 𝘁𝗵𝗲 𝗦𝗽𝗶𝗻𝗲): You cannot protect what you don't see. You must map out where your data lives—especially the data feeding your AI models.
1. 𝗖𝗹𝗮𝘀𝘀𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻 (𝗔𝘀𝘀𝗲𝘀𝘀 𝘁𝗵𝗲 𝗦𝘁𝗿𝗲𝘀𝘀): Is this public data, or is it the "backbone" of your company’s intellectual property?
1. 𝗥𝗲𝗺𝗲𝗱𝗶𝗮𝘁𝗶𝗼𝗻 (𝗥𝗲𝗮𝗹𝗶𝗴𝗻𝗺𝗲𝗻𝘁): This is where tools like n8n, Terraform, and Kubernetes come in to automate security guardrails and ensure your infrastructure stays upright.
1. 



## n8n - Flexible AI workflow automation for technical teams.
1. https://docs.n8n.io/try-it-out/tutorial-first-workflow/
2. Your first workflow
3. https://docs.n8n.io/try-it-out/tutorial-first-workflow/
   

## kapa.ai 
1. https://www.kapa.ai/
1. The answers are in your docs. Nobody can find them.
1. Kapa knows when it doesn't know. That's the difference. We tried other vendors and nothing came close.


## OpenClaw (formerly Clawdbot/Moltbot)
2. https://openclaw.ai/
3. Clears your inbox, sends emails, manages your calendar, checks you in for flights.
4. All from WhatsApp, Telegram, or any chat app you already use.
5. Future of personal AI assistant. 
6. OpenClaw runs a local gateway that connects messaging apps to a coding agent powered by Claude. 
7. You send messages through WhatsApp, Telegram, or the terminal, and the agent responds by running commands on your machine: searching files, executing scripts, and reading logs. 
8. Your text arrives through 
   1. WhatsApp (Baileys protocol), 
   2. Telegram (Bot API), 
   3. Discord, iMessage, or CLI.
9. [OpenClaw (Clawdbot) Tutorial: Control Your PC from WhatsApp](https://www.datacamp.com/tutorial/moltbot-clawdbot-tutorial)


## https://nixos.org/


## Semantic first 

1. Semantic Layers: dbt Semantic Layer, AtScale, and Cube.
1. Graph Databases: Neo4j and Amazon Neptune.
1. BI Platforms: Power BI, Tableau Semantics, and Looker.

1. [Semantic data](https://www.thoughtworks.com/en-in/insights/decoder/s/semantic-data)
2. Semantic data is an important step in AI-readiness, 
   1. but it also bridges the gap between abstract data and day-to-day organizational language.
3. Semantic data powers knowledge graphs, AI systems and search. It enables smarter, more context-aware applications.
4. Semantic data is data structured and organized in a way that adds meaning. 
   1. This enables machines (and, by extension, humans too) to understand context and relationships across a data set.


1. **Semantic data can improve data-driven decision making.**
1. Many businesses struggle with fragmented data spread across different departments and systems (e.g., "customer" in sales might be "client" in logistics and "counterparty" in finance). 
1. With semantic layers across — a core feature of semantic data — you have an intermediary that can translate disparate definitions into a unified, consistent view.

1. **It can simplify data access for non-technical users.**
1. Semantic data abstracts the complexity of underlying data structures. This means non-technical users won’t need to write complex SQL queries or understand intricate data schemas — they can access and analyze data using more familiar business terms.

1. **It can improve search (internal and external tools) by better connecting fragmented information.**
1. Semantic data helps to connect scattered information, such as customer feedback across support tickets, social media and reviews, to form a comprehensive understanding of customer sentiment and identify patterns.
1. 
1. **Semantic data can also power AI, and is particularly important in an age of increasing unstructured data and generative AI.**
1. With additional contextual information, semantic data can support conversational interfaces and applications.
1. 
1. **It also has compliance and governance benefits too**
1. explicitly defining data semantics can help ensure consistency and accuracy as well providing transparency on data lineage and provenance.

1. Financial Information Business Ontology (FIBO) 
2. Enterprise Data Management (EDM) Council, FIBO
   


## [Design-First Collaboration](https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html)

1. When I pair program with a colleague on something complex, 
1. we don't start at the keyboard. 
1. We go to the whiteboard. We sketch components, debate data flow, argue about boundaries. 
1. We align on what the system needs to do before discussing how to build it. 
1. Only after this alignment — sometimes quick, sometimes extended — do we sit down and write code. 
1. The whiteboarding is not overhead. 
1. It is where the real thinking happens, and it is what makes the subsequent code right. 
1. The principle is simple: whiteboard before keyboard.
1. 
1. With AI coding assistants, this principle vanishes entirely. 
1. The speed is seductive: describe a feature, receive hundreds of lines of implementation in seconds. 
1. The AI may understand the requirement perfectly well — an email notification service with retry logic, say. 
1. But understanding what to build and collaborating on how to build it are two different activities, and AI collapses them into one. 
1. It does not pause to discuss which components to create, whether to use existing infrastructure or introduce new abstractions, what the interfaces should look like. 
1. It jumps from requirement to implementation, making every technical design decision silently along the way.
1. 
1. I have come to think of this as the “Implementation Trap.” 
1. The AI produces tangible output so quickly that the natural checkpoint between thinking about design and writing code disappears. 
1. The result is not just misaligned code. 
1. It is the cognitive burden of untangling design decisions I was never consulted on, bundled inside an implementation I now have to review line by line.

1. The Implementation Trap is not simply that AI skips design. 
1. In a meaningful sense, the AI does make design decisions when it generates code — about scope, component boundaries, data flow, interfaces, error handling. 
1. But those decisions arrive silently, embedded in the implementation. 
1. There is no moment where I can say “wait, we already have a queue system” or “that interface won't work with our existing services.” 
1. The first time I see the AI's design thinking is when I am reading code, which is the most expensive and cognitively demanding place to discover a disagreement.
1. 
1. This, is why reviewing AI-generated code feels so much more exhausting than reviewing a colleague's work. 
1. When a human pair submits code after a whiteboarding session, I am reviewing implementation against a design I already understand and agreed to. 
1. When AI generates code from a single prompt, I am simultaneously evaluating 
   1. scope (did it build what I needed?), 
   2. architecture (are the component boundaries right?), 
   3. integration (does it fit our existing infrastructure?), 
   4. contracts (are the interfaces correct?), and 
   5. code quality (is the implementation clean?) — all at once, all entangled.











## dbt Semantic Layer



## [Colrows](https://www.colrows.com/)
1. Constrain LLMs with governed semantics, examples, and rules to ensure deterministic, explainable answers in production.
1. Dashboards That Build Themselves
2. At the core of Colrows is an open, searchable, and fully autonomous Semantic Layer—
3. the invisible infrastructure that powers 
4. AI agents, copilots, and intelligent workflows across the enterprise. 
5. Continuously learning from data, metadata, and business context, 
6. it becomes the single source of truth that bridges human intent and enterprise systems. 
7. This foundation accelerates AI adoption by making organizational knowledge instantly accessible and actionable. 
8. Built on the same semantic core, Colrows introduces two specialized AI agents—
   1. the AI Data Analyst, who transforms natural language into insights and visualizations, and 
   2.  the AI Data Engineer, who automates data transformations and pipeline design. 
9. Together, they enable enterprises to operate with a self-evolving data intelligence layer that fuels every AI-driven initiative.
10. [Knowledge Drift and Semantic Decay: The New Technical Debt](https://blog.colrows.com/knowledge-drift-and-semantic-decay-the-new-technical-debt-11b25224d408)
11. Semantic decay happens when systems continue to store data faithfully but lose track of what that data is supposed to represent and unlike broken pipelines, semantic decay doesn’t announce itself.
12. [Agents That Maintain Your Data Systems](https://blog.colrows.com/agents-that-maintain-your-data-systems-b649576fb954)
    






## Data 3.0 

1. From Data 2.0: the modern data stack to Data 3.0: the autonomous data stack.
2. Data 2.0 : dashboards and human analysts 
3. Data 3.0 : agents, and humans
4. AI agents, copilots, and applications that must discover, reason about, and act on data autonomously.


There are six foundational shifts to Data 3.0:

🔹 Structure : Domain-oriented, semantic-first So agents can build context-aware ground truth.

🔹 Modality : Multi-format, multimodal use. So AI protocols like RAG and MCP and new ones can operate natively.

🔹 Discovery 
Manual discovery → API-first automatic discoverability 
So agents can find and use data by intent.

🔹 Orchestration 
Pipelines → Self-orchestrated sensing systems 
So data moves faster from signal to action.

🔹 Observability 
Bolted-on lineage → Built-in lineage 
So agents can reason about provenance and trust.

🔹 Governance 
After-the-fact governance → Continuous computational governance 
So data is instantly safe for agents.

At Nextdata we enable these shifts through autonomous data products, data and its processing that behaves like autonomous applications centered around business domains, business semantic and business context first (not schemas and tables).

Join us for the demonstration of the first shift: the structural shift, from storage-centric and schema-first to domain-centric and semantic-first data processing.

📅 March 24, 2026 | Online
👉 Reserve your seat: https://luma.com/mxjn7mks


## Context Engineering

1. [Context Engineering for Coding Agents](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)
2. [Harness Engineering](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)
3. [Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/)
4. 



## Your Master Prompt Template
Role & Context
You are acting as my expert social media consultant. My background: a tenured IT leader with 25+ years of global experience delivering platforms for top banks and financial institutions. My target audience on LinkedIn is senior IT peers, enterprise architects, and decision-makers in financial services and other regulated industries. The goal of my content is to establish thought leadership by sharing insights that blend emerging tech trends with hard-won, practical enterprise experience.

Task
Please review the LinkedIn post draft I have provided below.

Your Review Should Include:

A clear rating out of 10, with a brief explanation.

Strengths: What is working well (e.g., hook, evidence, targeting).

Areas for Improvement: Specific, actionable suggestions on elements like:

The hook and opening lines.

Structure and logical flow.

Credibility and use of evidence/data.

Targeting and relevance to my niche (finance/enterprise IT).

The call-to-action (CTA) and engagement potential.

Clarity, conciseness, and word choice.

A Polished Rewrite (Optional): If the changes are minor, provide a "clean" version of the post incorporating the feedback, so I can see the final product.

Formatting Tips: Any suggestions for line breaks, emojis (use sparingly and professionally), or visual formatting to improve readability on LinkedIn.

My Post Draft:
[Paste your draft LinkedIn post here]



1. The Coming of Agentic Process Outsourcing 


1. 

AI models are fast becoming the new commodity, and not the differentiator.

The real moat? Your data. And the enterprise-grade fundamentals we've valued for decades: security, stability, scalability,  and observability. 

This is playing out in the real world. A new report from Azul (cited by The New Stack) shows that 62% of enterprises are now using Java for production AI workloads—up from 50% last year.

Why? Because while Python dominates prototyping, Java's robust ecosystem is what scales AI in the high-stakes, mission-critical environments we operate in, especially in finance.

The gold rush on models is plateauing out. The hard work of building reliable, secure systems on top of them has just begun.

What enterprise IT "old guard" principles do you think are becoming more important in the AI era? Repost if you agree that fundamentals still matter.

https://thenewstack.io/2026-java-ai-apps/



## FastMCP 

1. Jeremiah Lowin https://www.linkedin.com/in/jlowin/
1. Washington, District of Columbia, United States


## LLM fast 

https://www.seangoedecke.com/fast-llm-inference/?utm_source=perplexity



## secure data 

- FastAPI (via Pydantic) has a SecretStr


## Webmcp 

1. Agentic for web 
1. https://github.com/webmachinelearning/webmcp



## Context Engineering: A Guide With Examples


## What Is Context Engineering?

1. Context engineering is the practice of designing systems that decide what information an AI model sees before it generates a response.
1. the principles behind context engineering have existed for quite a while. 
1. This new abstraction allows us to reason about the most and ever-present issue of designing the information flow that goes in and out of AI systems.
1. Instead of writing perfect prompts for individual requests, 
1. you create systems that gather relevant details from multiple sources and 
1. organize them within the model’s context window. 
1. This means your system pulls together conversation history, user data, external documents, and available tools, then formats them so the model can work with them.
1. How ???
1. but as the conversation goes on, your chatbot often forgets the earliest and most important pieces of your instructions, 
1. your code assistant loses track of project architecture, and 
1. your RAG tool can’t connect information across complex documents and domains.
1. writing a clever prompt is just one small part of a much larger challenge: context engineering.

## how it works, 
## when to use it 

## [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)

1. with a large enough window, 
1. you can simply throw everything into a prompt you might need – tools, documents, instructions, and more – and let the model take care of the rest.
1. 
1. Long contexts kneecapped RAG enthusiasm (no need to find the best doc when you can fit it all in the prompt!), 
1. enabled MCP hype (connect to every tool and models can do any job!), and fueled enthusiasm for agents2.
1. 
1. But in reality, longer contexts do not generate better responses. 
1. Overloading your context can cause your agents and applications to fail in suprising ways. 
1. Contexts can become poisoned, distracting, confusing, or conflicting. 
1. This is especially problematic for agents, which rely on context to gather information, synthesize findings, and coordinate actions.
1. 
1. Let’s run through the ways contexts can get out of hand, then review methods to mitigate or entirely avoid context fails.








## Certification 

## MCP Certification from Huggingface 

1. https://huggingface.co/learn/mcp-course/en/unit0/introduction
1. https://huggingface.co/mcp-course
1. [Hugging Face MCP Course](https://huggingface.co/mcp-course?joined=true)
1. [Introduction to Model Context Protocol (MCP)](https://huggingface.co/learn/mcp-course/unit1/introduction#introduction-to-model-context-protocol-mcp)
1. [Key Concepts and Terminology](https://huggingface.co/learn/mcp-course/unit1/key-concepts)
1. [Architectural Components of MCP](https://huggingface.co/learn/mcp-course/unit1/architectural-components)
1. [MCP SDK](https://huggingface.co/learn/mcp-course/unit1/sdk)




## MCP resources 
1. What are the MCP resources. 
1. How to use them. 
1. Tools are designed to be model-controlled. Model is supposed to look them up and use them. 
1. Resources are designed to be application-driven
1. [Example Clients - A list of applications that support MCP integrations](https://modelcontextprotocol.io/clients)
1. [MCP Resources explained (and how they differ from MCP Tools)](https://medium.com/@laurentkubaski/mcp-resources-explained-and-how-they-differ-from-mcp-tools-096f9d15f767)


## [Visual Studio Code - The open source AI code editor](https://code.visualstudio.com/)

## Ollama 

1. Lama 2. We should be able to run it. 

```bash 
ollama run llama2 
ollama run mistral 
ollama run deepseek-r1:8b # find out more about it.

ollama pull mxbai-embed-larg # embedding model 

ollama serve # run the http service. 11434 

>>> /bye # for exit 
```


1. [MCP meets Ollama: Build a 100% local MCP client](https://www.youtube.com/watch?v=C64rVY1eN8k)
1. [Learn Ollama in 15 Minutes - Run LLM Models Locally for FREE](https://www.youtube.com/watch?v=UtSSMs6ObqY)

## LMStudio 

1. Local LLM ? 
1. Local AI, on Your Computer.
1. [How to Use LM Studio: A Step-by-Step Guide](https://www.youtube.com/watch?v=9zbFzVXSywg)
1. Install. Download model. Chat. 
1. Now which model to use for checking out MCP server. 
1. How to set up the Open AI like API. 

## [MCP + LM Studio: Local LLM Free Web Search Agent](https://www.youtube.com/watch?v=Y9O9bNSOfXM)


## [Notes : My hands-on experiments with Model Context Protocol (MCP): Bridging AI and a Lakehouse](https://medium.com/everyday-ai/my-hands-on-experiments-with-model-context-protocol-mcp-bridging-ai-and-a-lakehouse-6eac25c19c13)

1. Connect with Iceberg using MCP. 
1. [iceberg-mcp-server](https://github.com/cloudera/iceberg-mcp-server)


```bash 
API_KEY="<your API token>"
MODEL_NAME="<your model name>"
BASE_URL="<your Cloudera AI Inference endpoint>"
```



## **DeepEval**
1. the open-source LLM evaluation framework
1. Getting started with DeepEval : https://deepeval.com/docs/getting-started

## **Evidently AI** 
1. You can’t trust what you don’t test. Make sure your AI is safe, reliable and ready — on every update.
1. Quick start : https://docs.evidentlyai.com/quickstart_llm


## LLM-as-a-Judge Approach

1. Open-Source Frameworks: 
    1. Libraries like **DeepEval** allow you to implement both single-output and pairwise LLM judges in just a few lines of code. 
    1. **Evidently AI** is another open-source option focused on evaluating and monitoring ML models.
1. Application Development Platforms: 
    1. **LangSmith** and **Langfuse** provide built-in functionality 
    1. to define and run LLM-as-a-Judge evaluators directly on your application traces and datasets, often with no-code solutions.
1. Cloud Services: 
    1. Amazon Bedrock offers a fully managed "LLM-as-a-judge" feature. 
    1. It provides pre-selected judge models and optimized prompts, requiring you only to prepare your dataset in the required format.


## Data, that is ready for AI 

Is your data architecture ready for agents that don’t wait for humans? 
Agentic AI depends on deep, real-time access to machine data, 
not just nicely structured tables, 
but messy logs, traces, and security events. 

We must make a powerful case for a federated data fabric that stitches these sources together 
into a single, governed view so autonomous systems can act fast without flying blind. 




## LangGraph

1. Dictionary 


1. **Typed Dictionary**
1. code the type of the data in the Dictionary as well. 
1. from typing import TypedDict

1. **Union** 
1. from typing import Union 
1. when x can be both int and float 
1. x: Union[int, float]

1. **Optional**
1. You could give it a value or it will be None
1. def some_function ( name : Optional[str]): 
1. Now name can be a string e.g. "Partha" or None. 
1. But it can't be 1, or some other data type. 

1. from typing import **Any**
1. If it can take any value then how is it different from what we already have ?? 

1. square = **lambda** x: x*x
1. shortcut to write small functions. 

1. Different **Elements** in LangGraph
1. **State**
1. The notebook, whiteboard for the Agents?? / Participants / Nodes. 

1. **Nodes**
1. Anything that can receive a state. 
1. Individual functions etc. that does one very specific function in the graph. 
1. They receive input and give output 
1. Often the input, output is updated State.
1. They can use specialized functions call **Tools**
1. **Tool Nodes** are specialized nodes. 
1. They call the Tools and write output back in State. 


1. **Start Node** : Does not do anything itself, but gets started. 
1. **End Node**

1. **Graph**
1. The workflow of the connection of Nodes. 
1. They work on the some common task and update the State. 

1. **Edge** and **Conditional Edge** (traffic light)


1. **State Graph** : Builds and compiles graph 

1. **Runnable** : Anything that can Run. 

1. **Messages** 5 types 
    1. Human 
    1. AI 
    1. System : Set the persona. You are a helpful ... 
    1. Tool : System message but specific to Tool ?? 
    1. Function : Represens the result of a function call 
















1. **Reference**
1. https://docs.langchain.com/oss/python/langgraph/overview
1. [LangGraph Complete Course for Beginners – Complex AI Agents with Python](https://www.youtube.com/watch?v=jGg_1h0qzaM)



## XGBoost (eXtreme Gradient Boosting)

1. It is an optimized implementation of **Gradient Boosting** 
1. and is a type of **ensemble learning method** that **combines multiple weak models to form a stronger model**.
1. builds decision trees sequentially with each tree attempting to correct the mistakes made by the previous one
1. XGBoost uses **decision trees** as its base learners 
    1. combines them sequentially to improve the model’s performance. 
    1. Each new tree is trained to correct the errors made by the previous tree and 
    1. this process is called **boosting**.
1. parallel processing to train models on large datasets quickly






1. **Reference**
1. [Implementation of XGBoost (eXtreme Gradient Boosting)](https://www.geeksforgeeks.org/machine-learning/implementation-of-xgboost-extreme-gradient-boosting/)
1. https://www.geeksforgeeks.org/machine-learning/xgboost/
1. https://www.linkedin.com/posts/swatee-singh-phd-b237916_ai-agenticai-datascience-activity-7394064479321288704-755g?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACOR8UB3zqZApJHm3jXnrFZcfmFgwNtOq4
1. 


## What is ? 
1. similar to ZoomInfo, Uplead


## TOON vs JSON 

1. TOON - Token-Oriented Object Notation.
1. ? Do you have pure tabular data ? CSV would be more efficient. 
    1. So, why are we hearing that Coli. export is CSV is not helping. 
1. the TOON encoder can be used in Node.js or Python environments for batch conversions without performance loss

1. ** Who made TOON and why? ** 
1. At Scalevise, we handle thousands of API requests daily across ChatGPT, Claude, and other large language model platforms. 
1. Every token counts because it costs money.
1. A large portion of our API spend wasn’t tied to actual content but to data structure overhead
1. JSON, the web’s default data format, has brackets, commas, and quotes may seem trivial, but at scale, they add up quickly.
1. That’s when we decided to build our own optimized structure: TOON.

1. **Reference :**
1. https://medium.com/data-science-in-your-pocket/toon-bye-bye-json-for-llms-91e4fe521b14
1. https://youtu.be/oCWfB1lnvLA

## Konnect 
1. Konnect is the fastest way to deploy and manage API and AI gateways.
1. The unified platform for APIs and AI
1. https://cloud.konghq.com/in/welcome
1. 30 day trial - to what ?? 
1. ??? 

## Konnect AI Gateway 

1. Route, secure, and govern AI traffic across any provider.
1. Loved by developers. Trusted by enterprises.
1. ??? 

## Konnect AI Gateway providers
1. https://developer.konghq.com/ai-gateway/ai-providers/
1. ???

## Service Mesh - what is ??? 

## The Fundamentals of Quantum Computing

Learn quantum computing, starting with qubits and quantum mechanics. 
Discover quantum gates, circuits, and algorithms as Grover’s search and Shor’s factoring. 
Explore potential applications.

https://www.educative.io/courses/fundamentals-quantum-computing/what-is-quantum-computing?openHLOPage=true

1. **Qubits** : quantum computing posits a quantum bit (or qubit for short) as the centerpiece and most basic computation unit. Qubits are conceptually very similar to the bits. But unlike bits that can exist in a state of either 0 or 1 at any given time, a qubit has a larger state space. This essentially means that a qubit has more possible states to choose from beyond 0 and 1, and can therefore encode a lot more information compared to a classical bit.
1. quantum computers can use the quantum mechanical properties of **superposition** and **entanglement** of the qubits 

1. Powered by multiple qubits that have superposition and entanglement up their sleeve, 
1. quantum computers represent a new model of computation. 
1. Researchers have used quantum computers to solve and propose solutions to NP-hard problems 
1. (e.g. Protein Folding and the Traveling Salesman Problem) and produced 
1. quantum analogs of classical algorithms. 
1. In most cases, quantum computers and algorithms exhibit polynomial and sometimes exponential time speedup over their classical counterparts.
1. 

1. **NP-hard problems** - ??? 
1. **Traveling Salesman Problem** - ??? 

1. Big tech companies are adopting and investing heavily in quantum computing. 
1. Most quantum computers today are ensconced in expensive refrigerated laboratories, 
1. but these companies have connected their quantum computers to the cloud. 
1. These computers are now free for anyone to access and use. 
1. In the last few years, there has also been an active shift to recognize the power of quantum computers in industrial and commercial use cases. 
1. In short, 2021 is a fun time to be learning quantum computing.
1. Let us first turn our attention back to qubits and how they revolutionize the world of computation.

## The classical bit

1. The bit is the most basic unit of information. 
1. It either represents a 1 or a 0. 
1. It as analogous to a switch being on or off. 
1. A bit’s current status, either 1 or 0, is known as its state.

1. The transistor
1. The value of the bit being 1 or 0 are just abstractions. 
1. it is just a transistor, the building block of all modern computers. 
1. When the transistor allows the passage of current through it we consider this event to represent the 1 and 
1. when the transistor blocks the passage of current we consider this event to represent the 0.

## The quantum bit

1. The quantum bit can represent 0, 1, or both simultaneously. Kaise ??? 
1. This phenomenon is called superposition. 
1. For now, we just need to accept that it’s possible to be 0 and 1 at once.

1. A qubit can be built using any two-level quantum system. An example could be a phosphorus atom within a silicon superconductor.
1. Tangle Lake, Intel's 49-qubit chip.
1. The first takeaway here is that the superposition of 0 and 1 is not some third possible state of a bit. It is a special state that we cannot describe by using a classical bit.
1. 


Think of a slider moving between the values from 0 to 1. 
A superposition of 0 and 1 means our current state is somewhere on the slider, 
it could be a little more towards the 0 side, or it could be a little more towards the 1 side. 
We see from this slider analogy that there are infinitely many possible states 
that we can call “being both 0 and 1 at the same time”.

An equal superposition state would mean 50% of the qubit is a 0 and the other 50% of it is a 1. 

An equal superposition state would mean 50% of the qubit is a 0 and the other 50% of it is a 1. Using this way, we can think of the 
|0> state to be 100% 0 and 0% 1. 
Similarly, we can say the 
|1> state is 0% 0 and 100% 1.


One of the key differences is that all these operations have to be reversible.


## Quantum Computing Fundamentals 

Barron Stone (https://www.linkedin.com/in/barronstone/)  
Olivia Chiu Stone

1. Steps to understand Quantum
    1. How to represent quantum information
    1. Operations on a single quantum bit 
    1. Operations on a multiple quantum bit 
    1. entanglement
    1. Real quantum hardware 
    1. Quantum algorithms



## Volcano for AI 
1. https://volcano.dev/docs#installation



1. https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/
1. Willow quantum chip
1. first-ever algorithm
1. quantum computer can successfully run a verifiable algorithm on hardware, surpassing even the fastest classical supercomputers (13,000x faster)
1. 2019 - Back in 2019, we demonstrated that a quantum computer could solve a problem that would take the fastest classical supercomputer thousands of years.
1. 2024 - Late last year (2024), our new Willow quantum chip showed how to dramatically suppress errors, solving a major issue that challenged scientists for nearly 30 years


1. Introducing Microsoft Agent Framework
1. https://azure.microsoft.com/en-us/blog/introducing-microsoft-agent-framework/



## Decade of agents - it is still years away. 
Andrej Karpathy — AGI is still a decade away
https://www.dwarkesh.com/p/andrej-karpathy

Human limits are features 
Our forgetfulness helps us see patterns and stay creative. AI remembers everything — and often gets trapped in repetition instead of abstraction.


## Of course! Here is a longer story, set in Pune, written from the perspective of an 8-year-old.




## My Super Dooper Big Moon Adventure!**

**Chapter 1: My Didi and the Sky Full of Stars**

Hellow! My name is Abhro. I am eight years old and I live in Pune. I like it here. We have big mountains and nice weather, except in summer when it gets so hot I think I will melt like an ice-cream. My most favrit thing is space. I think about it all the time. The sun is a giant, I mean a GIANT ball of fire. If you put one million Earths inside it, it will just go *poof*! And a supernova is when a star gets so old it goes boom! It’s the biggest boom in the whole universe.

Every summer, when school is closed, we have the best time. All the kids from our society go to the big garden in the evening. And there, under the biggest tree you ever saw, sits Didi. She is not my real grandma, but she is every kid's grandma in our whole society. She tells us stories. She told us one about a monkey who built a bridge to Lanka. Another one about a boy who had a moon on his forehead! That one was my favrit.

My best frends are always there with me. There’s Reyansh. He is amazing. He can hear a song one time and then sing it perfectly. He even knows the old songs my dad listens to in the car. Then there is Arshita. She is the tallest in our class. She plays basketball and she runs so fast, she looks like a rocket! And Akshara. She is so pretty. She always has two nice braids with colourful ribbons and she stands like she is always ready for a photo. But she is also very kind and shares her tiffin with me.

**Chapter 2: The Big News from the Newspaper**

One Tuesday morning, I was eating my poha. My Papa was reading the newspaper. Suddenly, he made a loud noise. "WAH!" I got such a fright I spilled my milk. I thought I was in big trouble.

But Papa was smiling! His eyes were all wide. "Abhro! Listen to this! ISRO... you know, our space people... they have done it! They are making a special, one-time-only, 'Chandrayaan Kids Mission'! They will choose five children from all over India to go to the moon for one whole day!"

I think my heart stopped. For a real second. GO TO THE MOON? The actual moon?

I didn't even finish my poha. I ran out of the house. I ran to Reyansh's house first. I banged on his door. "REYANSH! WE CAN GO TO THE MOON!" He was practizing a song on his little keyboard. He stopped and said, "Really? I will compose a moon song! I will sing it for the Earth from up there!"

Then we ran to Arshita's house. She was bouncing a ball in her driveway. When we told her, she got so excited she threw the ball super high and it got stuck on their roof. She said, "I will take my basketball! I bet I can bounce it from one crater to another!"

Lastly, we found Akshara. She was helping her mom water the plants. She heard the news and got a very serious face. She said, "I will need a very good space suit. One that looks nice in pictures. And I will take a pink flag."

We all decided we had to apply.

**Chapter 3: The Application and The Long, Long Wait**

Applying was hard. We had to write an essay. The question was: "Why do you want to go to the moon?"

I thought and thought. Then I wrote: "I want to go to the moon becos it is our closest neighbour in space. I want to see if the marks on it are really holes or just shadows. I want to jump in low gravity and see if I can touch the Earth from there (just kidding). I will bring back a moon rock for my Didi so she can put it next to her tulsi plant. Also, I want to see if there is any cheese, just for checking."

Reyansh wrote that he wants to sing where there is no sound, to see what true silence feels like before a song. Arshita wrote that she wants to test how high she can really jump. Akshara wrote that she wants to show every girl in India that they can be beautiful and smart and an astronaut all at the same time.

We sent our applications. Then the waiting started. It felt like one billion, trillion years. Every day I would ask my mom, "Did ISRO call? Did they send an email?" She would just laugh and say, "No, beta, not today."

I even told Didi about it. She smiled her crinkly-eyed smile and said, "The moon is very patient, Abhro. It has been waiting for us for a long, long time. It can wait a little more for you."

**Chapter 4: The Big Surprise at School**

One normal day, we were in class learning about fractions. I don't like fractions. They are confusing. Suddenly, our principal, Ma'am, came on the loudspeaker. Her voice was all shaky and excited.

"Would students Abhro, Reyansh, Arshita, and Akshara from Class 3B please come to the principal's office immediately. Thank you."

My stomach did a flip. Oh no. What did we do? Did Reyansh sing too loud in the library? Did Arshita bounce a ball in the hallway? Did Akshara and I talk too much during lunch?

We all walked to the office, feeling very scared. But when we opened the door, we saw two people in cool blue ISRO uniforms! And they were smiling! One uncle had a big camera.

The ISRO aunty knelt down and said, "Are you Abhro?"

I could only nod. My voice was gone.

She said, "On behalf of India and ISRO, I would like to tell you that you have been selected for the Chandrayaan Kids Mission. You are going to the moon."

I think I screamed a little bit. Then Reyansh started singing a happy song right there! Arshita jumped so high she almost hit the ceiling! Akshara was crying happy tears and fixing her ribbons. It was the most amazing, crazy, best moment of my whole entire life. Our whole gang was going to the moon!

**Chapter 5: Getting Ready to be Astronauts**

The next few weeks were a super fun blur. We had to go to special training. Not in Pune, but in a big city. We got to wear puffy white astronaut suits. They made a *swish-swish* noise when we walked. Akshara said, "This fabric is not very flattering," but she still looked cool.

We learned about G-forces. They put us in a big machine that spins around super fast. It felt like a giant was squishing my face! It was weird but fun. Arshita loved it and said "AGAIN!" when it stopped.

We learned about zero gravity in a special plane. It goes up and down and for a few minutes, you float! It was the best feeling in the world. I did three somersaults. Reyansh tried to sing but his voice wobbled all over the place. We laughed so hard. Arshita tried to dribble her basketball, but it just floated away and hit an engineer on the head! We said sorry lots of times.

The food was funny. It was all in packets and tubes. You squeeze it into your mouth. I had mashed potato tube. It was okay. Reyansh got mango pulp and he was very happy.

**Chapter 6: Blast Off!**

The big day came. We went to the big ISRO place in Sriharikota. The rocket was there. It was so, so, so big. It was white and orange and it looked like it could punch a hole in the sky. My mom and dad were there. Mom was crying and taking photos. Dad was trying not to cry but his eyes were red.

We waved to everyone. We saw Didi in the crowd! She waved a white hanky. I felt so brave.

We climbed up the tall tower and got into our seats in the rocket. The seats were like big comfy chairs that hugged us very tight.

The countdown started. A loud voice said: "10... 9... 8..." I held Reyansh's hand. "7... 6... 5..." I heard Arshita whisper, "Goodbye, gravity!" "4... 3... 2... 1... IGNITION! MAIN ENGINE START! LIFT OFF!"

There was a ROAR. The whole rocket shook like our old mixer-grinder when mom makes chutney. I was pushed back into my seat. It felt like an elephant was sitting on my chest. It was scary for a minute, but then I saw the blue sky outside the window get darker and darker.

Then, suddenly, the shaking stopped. The roar stopped. It was very quiet. We were in space!

**Chapter 7: Hello, Zero Gravity!**

The first thing that happened was my pencil floated away from my pocket! It just floated in the air. Then I realised I wasn't sitting in my seat anymore. I was floating! The belt was holding me down, but the rest of me was floating.

"WE'RE FLOATING!" I shouted.

Everyone unbuckled. We became like superman! We flew around the cabin. It was so much fun. Arshita did a perfect somersault. Akshara's hair floated all around her head like a halo. She looked like an angel, but she was worried about her ribbons. Reyansh closed his eyes and said, "This is what music feels like inside my head before I sing it."

We looked out the window. The Earth was below us. It was a giant, beautiful blue and white and green marble. I could see India! I think I saw Pune, but it was very small. It made me feel very small, but also very special. We all live on that one beautiful marble.

**Chapter 8: One Small Step for Kids**

After what felt like a short time, the captain said, "Prepare for lunar landing." The moon got bigger and bigger. It was all grey and covered in circles and mountains. It looked like a giant, dusty playground.

We put on our big helmets and big gloves. We looked like real astronauts from TV.

The landing was a soft *thump*. The door opened. I was chosen to go first because my essay said I would. My heart was beating like a drum.

I carefully climbed down the ladder. The ground was soft and dusty. I took the last step.

"One small step for a kid," I said, my voice all shaky, "one giant... jump for kid-kind!" Then I jumped. I JUMPED! I flew up, like, three meters high! It was easy! I landed softly in the dust.

My friends came down next. Arshita immediately took out her basketball. She bounced it. It bounced so high we almost lost it! It went whoosh! She laughed and said, "I am the moon basketball champion!"

Akshara planted the Indian flag. It had a little pink ribbon tied to it, just for her. She posed next to it, and the camera on the rover took her photo. She looked like a movie star.

Reyansh said, "This is my concert." He turned on his microphone inside his helmet and started singing "Saare Jahan Se Achha". We couldn't hear it outside, but we could hear it in our helmets. It was the most beautiful song ever.

I collected rocks. I got a big grey one for Didi and a small white one for my mom.

We looked up. The Earth was in the black sky. It was a bright blue circle. It looked so peaceful and quiet. There were no borders. It was just... home.

**Chapter 9: The Return Home and The Best Story Ever**

Going back was faster. We blasted off from the moon and landed in the sea near India. A big ship came and picked us up.

When we got back to Pune, it was crazy! There was a big parade! People were throwing flowers and shouting our names. We felt like heroes.

The next day, we went straight to the garden. Didi was waiting under the tree. All the other kids were there too, looking at us with big, round eyes.

We walked up to her. I took out the moon rock. "This is for you, Didi. From the moon."

She took it in her wrinkly hands. She didn't say anything for a long time. She just looked at it and smiled. Then she looked at us. Her eyes were shiny.

"In all my years," she said, her voice soft like old paper, "I have told many stories about magic and gods and heroes. But today, the greatest story is not from me. It is from you. You, my children, are the new storytellers."

She made us sit down. "Now," she said, "Abhro, you tell us. Tell us the story of the boy who went to the moon."

So I did. I told them everything. About the scary blast-off, and the funny floating food, and about Arshita's bouncing ball, and Reyansh's silent concert, and Akshara's flag with the pink ribbon. My friends added parts too.

It was the best story we ever told under that tree.

And now, when we sit there, sometimes Didi tells her old stories, and sometimes we tell our new one. And I look up at the moon at night, and I smile. I know a secret. It's not made of cheese. It's made of memories. And I left a little piece of my heart there, right next to my footprint.

The End.

(P.S. My teacher said this story is too long. But I had lots to say. Going to the moon is a big thing you know.)