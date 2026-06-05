




## [6/5 - vscode extnsion list]
1. Markdown All in One - Zhang 


## [6/1 - Replacing RAG in 2026 - for code, not for data](https://buzzgrewal.medium.com/ai-agents-dont-need-vector-search-anymore-inside-the-agentic-search-stack-replacing-rag-in-2026-58efcabe4f6f)

1. May 2025 - Anthropic took out vector search from Claude code. 
2. Claude Code's creator Boris Cherny
3. Cursor hired Boris Cherny and Cat Wu, the leads behind Claude Code’s agentic search, directly from Anthropic in July 2025
4. September 2025 engineering post “Effective context engineering for AI agents
5. rather than pre-processing all relevant data, agents maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime using tools.
6. they expose retrieval as a set of tools, and let the LLM decide what to call, when, and how often
7. agent-as-retriever, agentic search, vectorless RAG, just-in-time context loading, or simply tool-use retrieval
8. start with agentic search and only add semantic search if you need it
9. Amazon Science published “Keyword search is all you need” (AAAI 2026, arXiv:2602.23368) 


## [6/1 - FAQ on Metadata, Semantics, Taxonomy, Ontology, Knowledge Graphs, and Context](https://sanjmo.medium.com/faq-on-metadata-semantics-taxonomy-ontology-knowledge-graphs-and-context-c4a53bfda395)

1. First, people take the well-known techniques of semantics, call them context, and declare the whole topic brand new, as if AI agents had just unleashed it on us. 
1. Second, experts explain metadata, semantics, taxonomy, ontology, knowledge graphs, and context without a single example, which leaves the audience more confused than when the conversation began.

1. Physical data + Metadata (base)
1. Ontology + Taxonomy 
1. Knowledge graph 
1. Semantic Layer 
1. Context Layer (top)

1. https://sanjmo.medium.com/faq-on-metadata-semantics-taxonomy-ontology-knowledge-graphs-and-context-c4a53bfda395


## [6/1 - What “AI-Ready Data” Actually Means (And Why Most Teams Get It Wrong)](https://medium.com/predict/what-ai-ready-data-actually-means-and-why-most-teams-get-it-wrong-fd0fe7a0b649)

## [6/1 - Ontology and Graph Databases: Enterprise AI From Theory to Production Reality (Part II)](https://medium.com/@nebulagraph/ontology-and-graph-databases-enterprise-ai-from-theory-to-production-reality-part-ii-6b72415eb2b3)


1. Clean data - is not equal to - AI ready data. 
2. Missing piece is **context**
3. More data - is not equal to - AI ready data. 
4. AI does not need more, it needs **right things**, clearly defined. 
5. When is Data, AI ready ? 
6. Data - more, clean - is not enough. 
7. Semantic organization is required to make it AI ready. This is done by **Ontology layer**
8. Business semantics - needs to be **queryable**, **enforceable**
9. **Graph database** are natural fit to implement
1. The hidden tax of unorganized data 
1. Data w/out semantics is just noise. 
   1. raw data 
   2. Ontology layer - creates semantic organization - entities, relationships, rules. 
   3. AI layer 
2. **How Ontology layer does it.** 
3. Naming things inconsistently 
4. Define relations explicitly - the relationships are typed, directed and constrained. 
   1. typed 
   2. directed 
   3. constrained : Order must have at least one lineitem 
5. Inheritance and classification 
   1. Inheritance 
   2. classification 


**Graph Models - good fit - Ontology layer**

1. **Graph databases** are a natural fit for the ontology layer because they natively support:
1. Each Node has a lable - Customer, Product, etc. 
   1. Each Node has a property - what is required and what is optional 
2. Each edge has a type - purchased, shipped-to etc. 
3. Relationship - Customer can place and Order. A Supplier can not place an Order. 


1. Customer_marketing - anyone with an email 
1. Customer_finance - someone who has at least on paid transaction 
1. Ontology fixes this 

[Diagram for ontology layer](https://medium.com/@nebulagraph/ontology-and-graph-databases-enterprise-ai-from-theory-to-production-reality-part-ii-6b72415eb2b3)

How to 
1. Select one business domain 
1. Identify - core entitites - and their relationships 
   1. Elimiate - synonyms and homonyms 
      1. Ploysemy - one word multiple meanings 
      2. synonyms - multiple word same meanings 
   
## [6/1 - Graph Algorithms](https://nebula-graph.io/posts/graph-algorithms-and-how-can-they-solve-real-business-problems) 

1. 
Nodes / Vertices : Entities. Customer, Product etc. 
1. Edges : Relationships. Purchased, shipped to etc.

**What is Ontology?**
1. 2,000-year-old branch of philosophy
2. Aristotle's formulation, ontology was "first philosophy"
   1. What is an entity? 
   2. What classes do entities belong to? 
   3. What properties define them? And crucially, 
   4. how do entities relate to one another? 

3. **Objects / Classes / Nouns / Nodes / Vertices**  
4. What categories of things exist in this domain. 
5. These are the nouns in the machine's world. 
6. Examples: Person, Company, City.
7. **Entity Instances / Hmm, this one might not be for us**
8. Specific individuals within those categories. 
9. Under "Person," you might have "John Smith"; under "City," "San Francisco."
10. **Properties / This one is also going to be different. These would be prop for Objects**  
11. Attributes that characterize each entity. 
12. Examples: "John Smith's age is 35," "San Francisco's population is 873,000."
13. **Links (Relationships)**
14. How entities connect to one another. Examples: "John Smith works at Company X," "Company X is headquartered in San Francisco."
15. How do you do that in Data world? 
16. **Constraints**
17. Logical boundaries that prevent errors. 
18. For instance, "A person cannot be employed by two mutually exclusive employers at the same time" or "A company's founding date must precede its dissolution date."
19. How do you do that in Data world? 
20. 

1. **Why is Ontology important all of a sudden?** 
1. the explosion of enterprise data, 
1. the limitations of large language models, and 
1. the acute need for deterministic AI in production environments.
2. https://nebula-graph.io/posts/ontology-and-graph-databases-the-missing-link-in-enterprise-ai




## Tutorials 

1. [Youtube Claude channel](https://www.youtube.com/@claude/videos)



## [Vibe Coding in Production: How Anthropic Uses AI to Write Code](https://www.youtube.com/watch?v=78EYLieMpvc)



## Universal Semantic Layer 

1. https://thedatagovernanceplaybook.substack.com/p/semantic-layer-vs-data-catalog-why
2. https://www.strategy.com/software/strategyone/product-tour

## Sridhar Vembu at Zoho



## TOREAD : https://moderndata101.substack.com/p/the-semantic-medallion

1. Graph of data at enterprise layer, in four lines ? 
2. Book : SHACL for the Practitioner
3. **SHACL (Shapes Constraint Language)** is a W3C standard for validating and describing data in Resource Description Framework (RDF) knowledge graphs.
4. Unlike **OWL (Web Ontology Language)**, which is used for logical reasoning and inferencing, SHACL is strictly focused on validation and defining data quality. 

## TODO : Have a open source, openai compatible, local LLM running on the laptop. 



## TODO: Collect Bagde : Upskill on AI agents in 90 minutes
https://www.databricks.com/learn/training/level-your-ai-agent-skills#data-video
kaunjovi+databricks@gmail.com 

AI agents fundamentals 
Introduction to ai agents 

## What is an AI agent? 
1. A **intelligent** tool, that uses 
2. an AI model, and 
3. other tools, to 
4. iteratively plan and execute sequence of actions 
5. to complete a complex task  

1. Complex task - examples - summarizing a document, write a piece of code etc. 

2. **Prompt engineering - zero shot** 
3. one question - one answer 
4. when was ACME founded ? ACME was founded in 1919. 

5. **Prompt engineering - multi shot** 
6. One question, augmented with an example - one answer. 
7. Learning by example. Show what is the correct answer to another example question. 
8. When was ACME found? E.g. When was FOOBAR found? 1945 - now the answer is just the year - 1919 

9. **Prompt engineering - chain of thought** 
10. The problem needs some reasoning, breaking the problem down to steps and then solving the steps correctly to arrive at an answer. 
11. Ask the Model to think out loud
12. Ability to Reason + Ability to Act = ReAct (Reason + Action) example  
13. Act = when to go and use a tool e.g. retreieve meta data from the Enterprise Data Governance platform 
14. **Common themes of Agents across the enterprises.** 
15. Document processing - retrieve data from documents such as contracts, images etc. , at scale (Naah). Categorize, index, make that available (hmmm, might be )
16. Knowledge base + Search - RAG + AI model 
17. Machine Learning + AI - (naah ). speech to text ( reverse ), image generation 
18. **Examples in Databricks world**
19. Databricks assistant - chatbot, ask questions about the platform. Help us writing scripts 
20. Customer support - 
21. Sales agent - internal tooling 
22. **Powering agents with Databricks Mosaic AI**

23. LLM - input text - output text 
24. I can speak in english to the LLM and it can communicate back in english 
25. My input - **prompt**
26. 
27. **Prompt engineering** : the engineering involved in forming precise prompts so the GenAI model does the required task effectively.
28. Some examples : providing examples. asking the LLM to think out loud. 
29. Different models went to different schools and hence there is a difference in what they are good at and how they respond to the same questions. 
30. **Mosaic AI** : Same chat interface that we all know 
    1.  but you can choose which LLM to talk to
    2.  you can compare side by side 
31. Prompt engineering : Chain of Thought : AI playground 
32. UI / Sidebar menu / AI submenu / Palyground 
    1.  Parameters 
    2.  Temperature 
    3.  Top P 
    4.  Top K 
    5.  Max Tokens  
33. Once you start conversation - apart from the response show 
   1. How long did it take
   2. How many tokens 
   3. How many $$s 
   4. Some parameters like - is the prompt well written, was it safe etc. 
   5. And finally, based on the answer 
      1. What are some follow up questions 
34. Allow the user to add System Prompt over the prompt. 
35. **Data Intelligence** 
36. 


33. **What are some of the LLM models, open source available?**
    1.  Llama 3.2 (Meta) - run with Ollama - Meta’s model cards, Ollama’s GitHub, etc. 
    2.  Phi-3 Mini / Phi-3.5 Mini (Microsoft)
    3.  Gemma 2 (Google)
    4.  Mistral 7B (Mistral AI)
    5.  Qwen2.5 (Alibaba)


## TODO : Put a test in place that the AgentDa is not commenting on anything irrelevant like that on politics, religion etc.? 
1. How - to put the guardrail + to test that it is happening? 

## TODO : Have some examples, news paper clips, about AI leading to embarassing failures for the firms? 
1. **Examples of failure of GenAI** 
1. AirCanda - refund policy - chatbot made up 
2. Chevrolet chatbot identifying Ford as the best choice. 

1. **What are Agentic AI systems?**
2. Non-Agentic / static workflow : Hardcoded prompt-response system. 
3. Agentic (dynamic, iterative) workflow : Planning by AI, Tool calling by AI, Execution by AI. Iterative. 

1. TODO : Find the source of the quote : 90% of GenAI projects do not go to production. 
2. TODO : How do. you measure if the response is good ? 
3. **AI playground**: Prototype and test an Agent. No code (How??)
4. **Mosaic AI agent framework** : Know Python ? Code agent. Author and deploy. Build agents from scratch. 
5. **Agent Bricks (beta)** : Build domain specific AI agent. You focus on data, system will build the agent. 
   1. production ready agents for your enterprise data - 
   2. Extract key information from your document 
   3. Turn your docs into an expert Agent chatbot


1. Information Extraction / Next generation of OCR 
   1. Legal document, contracts etc. extract key informaton from the document. 
2. Custom LLM 
   1. Summarize a document etc. 
   2. Generate a report 
3. Knowledge assistnace 
   1. Ingestion of document (??)
   2. Leverage them to create a chatbot 
4. Multiple Agent Supervisor 








## 5/18 

## Introduction to MCP (Model Context Protocol)

1. https://anthropic.skilljar.com/introduction-to-model-context-protocol/303756
2. https://modelcontextprotocol.io/docs/getting-started/intro
3. 



```
kaunjovi@devbook ~ % uv --version 
uv 0.11.14 (3fdfdc7d4 2026-05-12 aarch64-apple-darwin)
```



### What - what is the problem that MCP solves ? 

1. Provide context and tools to LLM without the developer of the tools to have to do the plumbing everytime. 
1. MCP Client can talk to multiple MCP servers which has 
   1. Tools 
   2. Resources 
   3. Prompts 

**ListToolsRequest** - give me a list of tools available. Response is **ListToolsResult**
**CallToolsRequest** - run a particular tools with all arguments. Response is **CallToolsResult**

1. User > Server > MCP client > MCP Server > 
1. User - asks some question to the server e.g. "What are the DP available?"
1. The server asks the MCP client, "List all the tools available." 
1. MCP client - receives the question, and sends **ListToolsRequest** to MCP server. Gets **ListToolsResult** is response. 
1. Client then sends the list to the Server
1. The server sends it directly to LLM to make sense of it. 
1. LLM understands it and tells exactly what tool to call and with what parameters. 
1. Servers sends that the MCP client. 
1. MCP client sends a **CallToolsRequest** to the MCP server. 
1. MCP server sends it to the services available in the background, and the service will do its job and send the response. 
1. The response is wrapped in **CallToolsResult** and send back to the MCP client. 
1. The server hands the **toolResul** to the LLM. 
1. LLM now has all the informaiton to stitch together a final response and sends it back to the user. 






## 5/17

## AI / ML certifications 

### Anthropic Academy (Free Courses with Certificates)

https://anthropic.skilljar.com/

Anthropic Academy is the company's dedicated learning platform, offering a library of self-paced, hands-on video courses—completely free. The curriculum is structured into three main tracks:

AI Fluency: Foundational courses like "Claude 101" for beginners, as well as specialized modules for educators and students.
Product Training: Focuses on applying Claude in everyday tasks, including enterprise deployment guidance for AWS and Google Cloud.
Developer Deep-Dives: Technical tracks covering the Claude API, Model Context Protocol (MCP), and Claude Code for building applications.

You can access these courses through the Anthropic Academy portal hosted on Skilljar, or find them on Coursera. 
Upon completing the video modules, exercises, and integrated quizzes, you will receive a free digital certificate that can be downloaded or shared on professional networks like LinkedIn. 
This is an excellent way to get structured, official recognition for your practical skills with Claude.

### 🌱 Foundation & Career Certifications

*   **IBM AI Engineering Professional Certificate (Coursera)**: Covers machine learning, deep learning, generative AI, and AI engineering best practices. It's designed to build a portfolio that demonstrates real-world proficiency to employers.
*   **Google AI Professional Certificate (Coursera)**: A great entry point for beginners, focusing on the fundamental concepts and practical applications of AI and machine learning.
*   **DeepLearning.AI TensorFlow Developer Professional Certificate**: A hands-on program focusing specifically on building and training powerful models using TensorFlow, one of the industry's leading frameworks.
*   **AI CERTs AI+ Engineer™**: A vendor-neutral certification that provides end-to-end expertise in building, deploying, and scaling intelligent systems. It covers everything from neural networks and NLP to deployment architecture.
*   **MIT xPRO Certificate Programs**: Options like "Designing and Building AI Products" offer a prestigious, university-backed credential. These programs often blend technical knowledge with strategic thinking, ideal for product leaders.

### ☁️ Cloud Platform Certifications
AI is deeply integrated with the cloud. These certifications from major providers are some of the most sought-after for developers and engineers.

*   **Amazon Web Services (AWS)**
    *   **AWS Certified AI Practitioner**: A foundational certification for those new to AI/ML on AWS. Great for non-technical roles too.
    *   **AWS Certified Generative AI Developer – Professional**: A newer, advanced certification focused on integrating foundation models, RAG, and agents into business workflows.
*   **Microsoft Azure**
    *   **Azure AI Fundamentals (AI-900)**: The perfect starting point for understanding core AI concepts on the Azure platform.
    *   **Azure AI Engineer Associate (AI-102)**: The gold standard for enterprise AI roles, this is a highly hands-on cert covering Azure OpenAI Service, RAG, and Prompt Flow.
*   **Google Cloud**
    *   **Professional Machine Learning Engineer**: An advanced certification with a strong focus on MLOps, scalable pipelines, and deploying models using Vertex AI and other Google Cloud tools.

### 🧠 Deep Learning & AI Engineering Specializations
For those who want to build the underlying models and systems, these certifications offer deep technical validation.

*   **DeepLearning.AI LLM Engineering Specialization (Coursera)**: Co-created with OpenAI, this is a highly practical and up-to-date program for mastering LLM-powered applications.
*   **NVIDIA Deep Learning Institute (DLI)**: Offers a range of instructor-led workshops and self-paced courses where you can earn certifications that prove your ability to develop applications using NVIDIA-accelerated computing.

### ✨ Generative AI & LLM Certifications
Specialize in the most cutting-edge area of AI with certifications from the companies leading the charge.

*   **NVIDIA-Certified Associate Generative AI Multimodal (NCA-GENM)**: An entry-level cert validating skills in building AI systems that work across text, image, and audio.
*   **NVIDIA-Certified Professional Generative AI LLMs**: An intermediate-level credential for professionals with 2-3 years of experience in designing, training, and fine-tuning LLMs.
*   **ISTQB® Certified Tester – Testing with Generative AI (CT-GenAI)**: A unique specialist certification for QA professionals on using generative AI for software testing, including prompt engineering and risk management.

### 🛡️ Ethics, Governance & Security
As AI becomes more widespread, proving you can build and manage it responsibly is a massive differentiator.

*   **ISACA Advanced in AI Security Management (AAISM)**: Designed for security managers to implement enterprise AI solutions while identifying and mitigating AI-specific security risks.
*   **CompTIA SecAI+**: A vendor-neutral professional certification focusing on both the security of AI systems and the application of AI in cybersecurity.
*   **Various Ethics Certifications**: Credentials like the **Certified Ethical Emerging Technologist (CEET)** or **Certified Responsible AI and Governance Specialist (CRAIGS)** validate expertise in applied technology ethics and governance frameworks.

### 🏢 Vendor-Specific Hardware & Software
Some certifications are specifically designed for professionals working within a particular technology ecosystem.

*   **Cisco AI Technical Practitioner (AITECH)**: Validated expertise in automating workflows, analyzing data, and designing AI-powered solutions on Cisco infrastructure. The exam was available starting December 18, 2025.
*   **Databricks Machine Learning Professional**: A "hottest hands-on cert" for data engineers focused on building and deploying ML pipelines in production using the Databricks platform.
*   **Alibaba Cloud Generative AI Engineer**: Best for engineers building solutions on the Alibaba Cloud platform.

### 🔬 Quality Assurance & Testing
A unique specialization that merges AI skills with software testing methodologies.

*   **ISTQB® CT-GenAI**: As mentioned above, this is the leading specialist certification for applying generative AI to software testing. It covers prompt engineering for test design, risk mitigation for AI-specific issues like hallucinations, and integrating AI into the testing infrastructure.

### 💡 How to Choose the Right AI Certification
To pick the best credential, consider your experience level, your career goals, and which technology ecosystem you work in (or want to work in).

*   **Define Your Career Goal**: If you want to be an engineer building and deploying models, look at cloud or vendor-specific certifications. If you're a business leader, a foundational or strategy-focused program might be a better fit.
*   **Align with Your Technology Stack**: If your company uses Microsoft Azure, the **AI-102** is a strategic choice. For AWS-centric companies, the **AWS Generative AI Developer** cert is ideal. Choosing a certification aligned with your current tools provides immediate, practical value.
*   **Consider Your Experience Level**: Beginners should start with **AI-900 (Azure)** or the **AWS Certified AI Practitioner**. Experienced ML engineers can jump to the **Google Professional ML Engineer** or **NVIDIA's professional-level certs**.
*   **Factor in Cost and Time**: Free options from Google or self-paced courses on Coursera offer flexibility. University programs from Stanford or MIT provide prestige but have a higher price tag.

Given the rapid pace of change, it is always best to verify the most current details directly on the official certification providers' websites.

I hope this comprehensive guide helps you find the right path to showcase your expertise. Do any of these roles or ecosystems particularly resonate with your career goals?

## [The Best RAG Architectures for AI Agents Every Developer Must Know](https://medium.com/@pankaj_pandey/the-best-rag-architectures-for-ai-agents-every-developer-must-know-434c97cf1645)


## [9 RAG Architectures Every AI Engineer Should Actually Understand]

What is RAG (in plain terms)?
User Query → Retrieve Data → Feed to LLM → Generate Answer

how you retrieve
what you retrieve
how you validate
and how the model reasons

## Standard RAG (The Starting Point)
This is what 90% of tutorials show.
Embed documents
Store in vector DB
Retrieve top-k chunks
Send to LLM
👉 Works well for:

FAQs
internal docs
basic search

**Conversational RAG**
Add memory 

**Corrective RAG (CRAG)**
Flow becomes:
Retrieve documents
Evaluate their quality
Fix or re-retrieve if needed

**Adaptive RAG**
Adaptive RAG decides:

how many sources to retrieve
how deep to search
whether to use multiple strategies
A smart backend router for queries.

**Self-RAG**
The model:

generates an answer
critiques itself
improves the response

**Fusion RAG**
Instead of asking one query, it asks multiple.
User asks:

“How to scale Node.js app?”

System generates:

“Node.js scaling techniques”
“horizontal scaling node”
“load balancing node apps”

**HyDE (Hypothetical Document Embedding)**

**Agentic RAG**
where RAG meets agents.
planning
tool usage
multi-step reasoning
User asks:

“Analyze sales drop and suggest strategy”

Agent might:

Fetch data
Run analysis
Retrieve docs
Generate insights

**GraphRAG**
Traditional RAG uses chunks.

GraphRAG uses:
👉 relationships

Works best for:

enterprise knowledge
research
connected data

## [Vectorless Agentic RAG](https://ai.plainenglish.io/vectorless-agentic-rag-is-quietly-replacing-traditional-rag-architectures-472c35a108f2)

Embeddings → Vector Database → Retrieval → LLM

Convert documents into embeddings
2. Store embeddings in vector DB
3. Convert user query into embeddings
4. Retrieve “similar” chunks
5. Send chunks to LLM
6. 


## [SDD Writing Specifications for AI: BDD as the Missing Link — Spec-Driven Development](https://medium.com/@wasowski.jarek/sdd-writing-specifications-for-ai-bdd-as-the-missing-link-spec-driven-development-ad1b540b7f75)

1. A specification is a **execution contract**. It is not a document to archive or audit. 
1. What should be the content of the **SDD (Spec Driven Development)**
   1. GitHub shipped Spec Kit, 
   2. AWS shipped Kiro, 
2. **Software 3.0** - description of intent in natural language 
3. **The New Code** : Sean Grove of OpenAI made the sharpest case in his widely discussed talk “The New Code” 

1. **A quick recap of the Traditional Engineering Documentation**
   1. **BRS (Business Requirements Specification)** — a business document describing requirements from the organization’s perspective, a precursor to the SRS. 
   2. **SRS (Software Requirements Specification)** — a classic engineering document describing functional and non-functional requirements, typically 50–200 pages of prose. 
   3. **HLD (High-Level Design)** — an architectural document describing system components and their interactions. 
   4. **LLD (Low-Level Design)** — a detailed document describing the internal structure of modules: classes, methods, and call sequences.

2. In practice — if / when it worked — it worked mainly because the developer filled in the gaps. 
3. All four formats were supposed to be unambiguous, and all four always had holes. 
4. Those holes were patched with **domain memor**y and a dense network of **informal hallway conversations**. 
5. AI doesn’t have that network, doesn’t walk the hallways, and doesn’t pretend to know what it doesn’t know.

## BDD (Behavior-Driven Development) - developed in 2003, before the consumer arrived. 

1. On Christmas Eve 2003, **Dan North** registered the domain jbehave.org and 
1. wrote the first lines of a tool meant to replace JUnit. He wasn’t doing it to invent a new form of testing — he was solving a pedagogical problem: 
1. the developers he was teaching TDD kept getting stuck on the word “test.” 
1. North swapped the word “test” for the word “behavior” — and suddenly an entire category of questions about what to test disappeared. Writing behavior is natural. Writing tests isn’t.
1. BDD (Behavior-Driven Development) — a methodology for describing system behavior in natural language, readable by the business and executable by machines, 
1. using **Given/When/Then scenarios**. 
1. Over two decades BDD traced a spectacular arc: peak popularity in 2015, 
1. a long decline 2018–2024 (when SmartBear handed off Cucumber and Tricentis killed SpecFlow), 
1. then an unexpected renaissance in the AI era. 
1. That renaissance isn’t coincidental — and it’s not because BDD suddenly “works better.” 
1. It’s because the reader BDD was designed for from the beginning finally appeared.

1. **Gherkin** — the DSL used in .feature files to write BDD scenarios

1. BDD framework (Cucumber, Reqnroll, Behave)
2. **Aslak Hellesøy**, Cucumber’s creator, once said provocatively: “BDD is not test automation — it’s collaborative requirements analysis combined with TDD.”

```
Feature: ATM cash withdrawal
Scenario: Sufficient balance
  Given the account balance is $100
    And the card is active
  When the customer requests a $20 withdrawal
  Then the ATM dispenses $20
    And the account balance is $80
```


6. [How We Built an AI Second Brain for 60K Knowledge Workers](https://medium.com/@AnalyticsAtMeta/how-we-built-an-ai-second-brain-for-60k-knowledge-workers-78c507dd795b)
7. ??

## [5/17 - We Build AI for a Living. Half Our Company Does Not Want to Use It.](https://ai.gopubby.com/we-build-ai-for-a-living-half-our-company-does-not-want-to-use-it-cf7e3d716c07) 

## [5/17 - Three Companies Tried Replacing Data Analysts With AI. Six Months Later, Here’s What Actually Changed.](https://pub.towardsai.net/three-companies-tried-replacing-data-analysts-with-ai-f9930095ae17)

## [5/17 - The Stanford AI Index 2026: What the Data Actually Says](https://ivopbernardo.medium.com/the-stanford-ai-index-2026-what-the-data-actually-says-57cb928e93d9)




## [5/18 - We Build AI for a Living. Half Our Company Does Not Want to Use It.](https://www.weeai.dev/blogs/developer-divide-ai-coding-tools)

We called a townhall last month to talk about AI coding tools. 
Not a casual Slack poll. A planned, company-wide session. 
The AI Solutions team — my team — had been using Claude Code, Cursor, and custom agent workflows for months. 
The Software Engineering team, the one building the core product, had not. 
Same company. Same office. Two completely different relationships with the tools we sell.
I walked in expecting a conversation about which tools to standardize. 
What I got was a lesson in the technology adoption curve that I should have seen coming.
The divide is not about tools.
The divide is not about whether AI coding tools work. 
Everyone agrees they produce code. 
The divide is about whether you trust what they produce, and whether you think the speed is worth the risk.
Here is the moment that made me take the “**almost right**” problem seriously.
We had a spec. Frontend and backend teams had agreed on the API contract. 
Route names, request bodies, response shapes. All documented. 
An engineer used an AI coding tool to generate the backend endpoint. The code was clean. It compiled. 
The endpoint responded correctly when tested in isolation.
The frontend got a 404.
**The confidence is the dangerous part**
The code looked correct. It passed linting. It returned the right data shape. 
If you tested the endpoint by itself, everything worked. 
The bug only appeared when frontend and backend talked to each other. 
That is not a hallucination. It is a misunderstanding. 
And it is the kind of bug that slips through code review if you are not looking for it.

METR, one of the few organizations running rigorous randomized studies on AI coding productivity, found that developers using AI tools were 19% slower on average. But the developers themselves estimated they were 20% faster. 
The perception gap is not small. It is a full 39 percentage points in the wrong direction.
https://metr.org/blog/2026-02-24-uplift-update/
https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/




https://medium.com/data-science-collective/i-spent-6-months-tuning-claude-code-heres-the-exact-setup-that-finally-worked-b41c67628478
https://ai.plainenglish.io/if-ai-can-code-why-are-big-tech-founders-coding-again-6791526cde51
https://medium.com/@pabhishek192/how-i-built-a-metadata-driven-data-pipeline-framework-using-databricks-04fed5b8a271
https://medium.com/@AnalyticsAtMeta/how-we-built-an-ai-second-brain-for-60k-knowledge-workers-78c507dd795b
https://ai.gopubby.com/we-build-ai-for-a-living-half-our-company-does-not-want-to-use-it-cf7e3d716c07
https://pub.towardsai.net/three-companies-tried-replacing-data-analysts-with-ai-f9930095ae17https://pub.towardsai.net/three-companies-tried-replacing-data-analysts-with-ai-f9930095ae17
https://ivopbernardo.medium.com/the-stanford-ai-index-2026-what-the-data-actually-says-57cb928e93d9
https://medium.com/@wasowski.jarek/sdd-writing-specifications-for-ai-bdd-as-the-missing-link-spec-driven-development-ad1b540b7f75
https://medium.com/@reliabledataengineering/the-last-generation-of-data-engineers-e095cd5437b2

1. **Deep dive into context engineering for AI agents**
2. https://code.likeagirl.io/deep-dive-into-context-engineering-for-ai-agents-584bf3e578df
3. **Context engineering**. 
4. Still evolving. Nobody knows for sure. 
5. Talking points 
6. Treat context as a resource - constrained and has associated cost. 
7. Context **retrieval** - pull only what is required and when it is required 
   1. Context **pollution** - too much informaiton. conflicting information. 
8. Context **offloading** - offload info to some external source 
9. Context **isolation** - one subtask should not contaminate others. 
10. Context reduction - once in a while, reduce. 
11. Context **rot** - even when the context window has not filled up, if it is too full, degradation sets in. 
   1. Information at the start and the end is more reliably recalled than things in the middle.
   2. Enterprise data is effectively unbounded and frequently updated that even if the model could ingest everything, 
   3. that would not mean it could maintain a coherent understanding over it.
12. Context **compaction** - counter the rot 
13. Context **folding** - new concept 
    1.  https://openreview.net/forum?id=JaLXQnA2wi
    2.  a framework that empowers agents to actively manage their working context
    3.  An agent can procedurally branch into a sub-trajectory to handle a subtask and then fold it upon completion, 
    4.  collapsing the intermediate steps while retaining a concise summary of the outcome


14. [What the Heck is Apache Iggy?](https://progrockrec.medium.com/what-the-heck-is-apache-iggy-6f7f5ab312f7)
15. Why are people moving to Rust? 
16. Apache Kafka has been the 800-pound gorilla since LinkedIn open-sourced it back in 2011
17. Piotr Gankiewicz back in April 2023
18. persistent message streaming platform (Kafka), not a message broker (RabbitMQ).


[AI makes you way less productive unless](https://michalmalewicz.medium.com/this-ai-game-undermines-all-you-do-28c9acaec440)


## FDE - Forward Deployed Engineer
1. A Forward Deployed Engineer (FDE) is a hybrid technical role where 
2. engineers embed directly with customers to solve complex technical problems, customize software, and own technical success. 
3. Pioneered by firms like Palantir, 
4. these engineers build production systems directly within a client's environment, bridging the gap between abstract tech capabilities and operational reality. 
5. **Core Responsibilities**
6. **Customer Integration**: Sitting side-by-side with clients (often on-site) to ensure products fit their specific infrastructure and real-world workflows.
7. **Custom Development**: Writing production code and adapting software to solve immediate customer pain points rather than generic product roadmaps.
8. **Feedback Loop**: Acting as the bridge between the customer and their own product engineering team, feeding operational insights back to the core team.
9. **AI & System Deployment**: Specializing in deploying complex technologies—like AI models, RAG pipelines, and data integration platforms—into legacy enterprise systems. 
10. [What is Forward Deployed Engineering? A guide to the role, benefits, and real enterprise examples](https://invisibletech.ai/blog/what-is-forward-deployed-engineering)
11. 

Claude code - free vouchers 
claude co-work - ?? - 
Partners ?? 
.claudeignore 

Harness over claude code 

## [How I Built a Metadata-Driven Data Pipeline Framework Using Databricks.](https://medium.com/@pabhishek192/how-i-built-a-metadata-driven-data-pipeline-framework-using-databricks-04fed5b8a271)
1. metadata-driven data pipeline framework using **Databricks**
2. pipeline behavior is controlled using configuration files (metadata) instead of hardcoded logic
3. Metadata (YAML-Based Pipeline Configuration)
   1. Source details
   1. File formats
   1. Target tables
   1. Transformations
   1. Validation rules


```yaml 
pipeline_name: customer_ingestion

source:
type: csv
path: /mnt/raw/customers/

target:
catalog: demo
schema: bronze
table: customers

load_type: incremental

primary_key:
— customer_id
```

1. Databricks Workflows to orchestrate the pipelines
   1. notebook execution
   2. dependency management
   3. retries
   4. scheduling

1. Further reading about Databricks : Medallion Architecture Using Databricks — Part 2



## [5/16 - Data Engineering Trends in 2026](https://medium.com/towards-data-engineering/data-engineering-trends-in-2026-adapt-or-become-a-ticket-taker-a45de072b10d)

## [5/16 - The Best RAG Architectures for AI Agents Every Developer Must Know](https://medium.com/@pankaj_pandey/the-best-rag-architectures-for-ai-agents-every-developer-must-know-434c97cf1645)

Some recent research and papers formalized this into three principles: 
autonomous strategy, iterative execution, and interleaved tool use.

https://weaviate.io/
One foundation for search, RAG, agents, and everything that comes next

```
# Pure vector search
response = collection.query.near_vector(
    near_vector=[0.1, 0.1, 0.1],
    limit=5
)

# Semantic search
response = collection.query.near_text(
    query="login issues after OS upgrade",
    limit=5
)

# Hybrid search (vector + keyword)
response = collection.query.hybrid(
    query="login issues after OS upgrade",
    alpha=0.75,
    limit=5
)
```

1. The alpha parameter controls the blend. 
1. For legal, compliance, and medical domains where exact terminology matters, we push alpha toward 0.5. 
1. For conversational queries, closer to 0.8.


## Self-correcting RAG with LangGraph 
1. Corrective RAG (CRAG), implemented as a state machine in LangGraph
1. Instead of blindly trusting retrieval results, an LLM grades them for relevance before generating an answer. 
1. If the documents are weak, it rewrites the query and falls back to web search.


## Semantic caching cuts the bill 
Before any of these hits the LLM, add a semantic cache. 
Identical and near-identical queries get served from cache instead of burning tokens.
Redis makes this straightforward with RedisVL

[Semantic Caching for LLMs using RedisVL](https://docs.redisvl.com/en/0.4.1/user_guide/03_llmcache.html)

## Ragas (Retrieval-Augmented Generation Assessment Suite)

[RAGAS](https://www.geeksforgeeks.org/artificial-intelligence/ragas/)

RAGAS (Retrieval-Augmented Generation Assessment Suite) is an 
open-source evaluation framework developed by Hugging Face 
to quantitatively assess the quality of RAG systems. 
It measures how well a system retrieves and utilises external context 
to generate accurate, faithful and relevant responses. 
Unlike traditional metrics that only compare text similarity, 
RAGAS evaluates the entire RAG pipeline i.e 
from context retrieval to answer generation hence helping developers to identify performance bottlenecks across the workflow.

1. **Answer Relevancy**: Measures how closely the generated response matches the user’s query intent.
1. **Faithfulness**: Evaluates whether the response stays true to the retrieved evidence.
1. **Context Precision**: Assesses how relevant the retrieved chunks are to the query.
1. **Context Recall**: Determines whether all necessary information was retrieved.
1. **Evaluation Dataset**: Represents the structured input including questions, contexts, responses and reference answers used for metric computation.

## How to regression test Data chatbot

RAGAS – built‑in metrics for faithfulness, answer correctness, etc.

DeepEval – unit‑testing style for LLMs, with Pytest integration.

LangSmith – if you’re using LangChain, its evaluation and tracing suite is a natural fit.

RAG (handbooks) and 
MCP tools (data-product metadata)

Golden Test Set (and Keep It Alive)

Create a file of test cases that represent the most frequent and high-risk user requests. Each case should include:

user_query (possibly multi-turn)

expected_tool_calls (which tools, with what arguments)

expected_retrieved_documents (IDs or key phrases)

expected_answer_facts (specific pieces of information that must appear)

must_not_contain (hallucinated or deprecated mentions)

1. **Organise by category:**
   1. Pure RAG – handbook questions like “What are the ACID guarantees in Delta Lake?”
   2. Pure MCP – “List all data products tagged ‘finance’.”
   3. Hybrid – “Which data product should I use for streaming ingestion according to the handbook?”
   4. Edge cases – vague queries, empty history, safety boundaries.




## [5/16 - Stanford’s AI Report 2026](https://medium.com/@usabilitycounts/stanfords-ai-report-2026-ai-isn-t-going-anywhere-neither-are-you-if-you-pay-attention-c27729b07f5b)
??

## [5/16 - Artificial Intelligence Index Report](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)

1. [Book : Crossing the Chasm, by 	Geoffrey A. Moore](https://en.wikipedia.org/wiki/Crossing_the_Chasm)
1. That chasm is where careers will quietly bend.
1. People who treat AI as a serious instrument — not a toy, not a threat — will be the ones writing the playbook everyone else eventually copies.
1. The opportunity isn’t the tool. The opportunity is being early enough to define what good use of it looks like for everyone else.
1. Quality is contextual. 


## [Bikash Debnath - spec driven coding ]
??




## [5/13 - The Ontology Stack: Grounding AI in Domain Knowledge](https://medium.com/@jingwang.physics/the-ontology-stack-grounding-ai-in-domain-knowledge-644ef1087c24)


**What Is an Ontology?**

An ontology is a formal framework of rules, relationships, and agreed vocabulary that makes domain knowledge machine-readable. 
The difference between an ontology and a taxonomy is the difference between a map and a rulebook. 
A taxonomy only classifies *what things are*. 
An ontology captures four dimensions of meaning simultaneously, which is what enables a system to reason rather than just store.

take the concept “Poodle.” 
A taxonomy tells you it is a Dog, which is a Mammal, which is an Animal. 
An ontology goes further. 
It records what a poodle is like — `weight: 5kg`, `lifespan: 14yr`, `hypoallergenic: true`. 
It records how it relates — *owned by* a Person, *can develop* a Disease, *bred for* Companionship. 
And it records what rules apply — 
it cannot be a Cat; 
if `age < 1yr` it is a Puppy. 


Those four dimensions together are what let a system compare (“find small dogs with a lifespan over 14 years that are hypoallergenic”), combine data from a vet and a breeder without confusion, and reason — inferring a lease violation without being told explicitly.

The core components of an ontology are controlled vocabulary, relationships, and constraints. Controlled vocabulary means precise, agreed definitions for every key term, with synonyms explicitly mapped. Relationships are verbs that link concepts: a disease *causes* symptoms, a treatment *is associated with* a disease. These enable inference — new knowledge derived from existing facts. Constraints are both hard rules (“never recommend a financial product to under-18s”) and soft guidelines (“prefer cheaper tests unless reliability is compromised”).

The two foundational standards are 
**OWL (Web Ontology Language)** : which handles complex class hierarchies, reasoning, and inference, and 
**RDF (Resource Description Framework)** : which is the underlying data model OWL builds on. 

Together they form the backbone of the semantic web — which links data across sources so “car” on one site and “automobile” on another are understood as the same concept.

## The Knowledge Stack


1. The **ontology layer** sits at the top as the governance layer. 
   1. It defines the controlled vocabulary, constraints, and semantic relationships that act as guardrails for everything below it.
   2. Building it requires expert consensus, and it is the layer that prevents hallucination and drift at the source.
2. Below it is the **knowledge graph**: entities as nodes, relationships as edges. 
   1. This is the layer that enables structured reasoning, data lineage, and explainability. 
   2. It takes the categories defined in the ontology and populates them with real-world instances. 
   3. The same pattern underpins Google Search, supply chain management, and clinical diagnostics.
3. Below that is **RAG (Retrieval-Augmented Generation)** 
   4. which combines semantic and keyword search across both structured and unstructured data. 
   5. RAG is where the model gains access to information beyond its training data, 
   6. but it needs the knowledge graph and ontology above it to do more than fuzzy similarity matching.
4. At the bottom is the **AI agen**t itself: 
   1. the layer that interprets tasks and generates responses through natural language. Without grounding from the layers above, it hallucinates and drifts. With those guardrails in place, it becomes domain-aware.





## [5/13 - Agentic Mesh Your Enterprise Agents Are Missing](https://pub.towardsai.net/mcp-a2a-owl-ontology-i-built-the-agentic-mesh-your-enterprise-agents-are-missing-84ec0487ddd4)

**Agentic Mesh** — a production pattern that wires together three protocols your enterprise already has access to:
**MCP (Model Context Protocol)** — the tool-access layer
**A2A (Agent2Agent Protocol)** — the agent communication layer
**OWL Ontology + SHACL** — the shared semantic contract that prevents both layers from lying to each other

[Agentic Mesh Blueprint](https://github.com/cloudbadal007/agentic-mesh-blueprint)

Agentic Mesh isn’t a product. It’s a pattern

AGENT COMMUNICATION (A2A)             │
│  Agent Cards • Task Lifecycle • SSE Streaming    │
├─────────────────────────────────────────────────┤
│          SEMANTIC CONTRACT (OWL + SHACL)         │
│  Shared Classes • Constraints • Reasoner         │
├─────────────────────────────────────────────────┤
│              TOOL ACCESS (MCP)                    │
│  MCP Servers • Resources • JSON-RPC 2.0     



**SHACL (Shapes Constraint Language)** 
It defines rules about your ontology classes — what’s required, what’s forbidden, what shape the data must take before it’s allowed to propagate through the mesh.
formal, machine-readable rules that say “a ComplianceHold cannot be released without Legal sign-off.” 
This isn’t a business rule buried in code. 
It’s a semantic guardrail that every agent in the mesh can reason over



Agents discover each other via Agent Cards, negotiate task delegation, and exchange results through Google’s Agent2Agent protocol. But crucially, every A2A message carries ontology-annotated payloads — not raw JSON. 
This means that when an agent receives a request, it can validate it against the shared OWL ontology and SHACL constraints before taking action.



## [5/13 - I Tried to Migrate a Palantir Foundry Ontology to Fabric IQ — the OWL Exit Ramp](https://medium.com/@cloudpankaj/i-tried-to-migrate-a-palantir-foundry-ontology-to-fabric-iq-heres-what-broke-what-it-cost-and-f5e6c554aa44)

1. [OWL portability layer](https://github.com/cloudbadal007/owl-portability-layer)

your business rules live in OWL/SHACL, not in either vendor’s proprietary format


## [5/13 - Microsoft vs Palantir: Two Paths to Enterprise Ontology](https://pub.towardsai.net/microsoft-vs-palantir-two-paths-to-enterprise-ontology-and-why-microsofts-bet-on-semantic-6e72265dce21)

1. Palantir built ontology for intelligence work (graph data + human reasoning). 
1. Microsoft built it for agentic systems (semantic contracts + autonomous action). 

Layer 1: The Ontology Item (The Foundation)
This isn’t metadata about your data. 
This is a formal semantic model that defines

**Entity Types** — Not just table schemas, but business concepts:

Customer
  ├─ Properties: CustomerID, Tier, RiskScore, LifetimeValue
  ├─ Constraints: RiskScore must be 0-100
  └─ Relationships: has_many Orders, belongs_to Region

**Typed Relationships** — Not just foreign keys, but semantic links

Shipment --[belongs_to]--> Customer
Shipment --[contains]--> LineItem
Shipment --[monitored_by]--> IoTSensor
Shipment --[governed_by]--> ComplianceRule

**Business Rules** — Executable logic that defines valid states

Rule: "High-Risk Shipment Alert"
  IF: Shipment.RiskScore > 80 
  AND: Shipment.Status = "In Transit"
  AND: IoTSensor.Temperature > Threshold
  THEN: Trigger_Action(Notify_Customer, Escalate_to_Operations)

**Permitted Actions** — What agents are allowed to do

Action: Reroute_Shipment
  ├─ Requires: Operations_Manager_Role OR System_Emergency_Override
  ├─ Validates: Destination must be valid Warehouse
  └─ Triggers: Update_Shipment_Status, Log_Audit_Trail

**semantic bindings**
The ontology becomes a semantic abstraction layer over your physical data
When an AI agent asks “Who are our high-risk enterprise customers?”, it’s reasoning at the ontology level, not writing SQL

Entity: Customer
  ├─ Ontology Definition: [Business concept of who a customer is]
  ├─ Data Binding: customers_table in OneLake
  ├─ Mapping:
      Customer.CustomerID → customers.customer_id
      Customer.Tier → CASE WHEN annual_revenue > 1M THEN 'Enterprise'...
      Customer.RiskScore → ml_models.risk_predictions.score

**What does the agent know?**
1. What these entities mean (from ontology definitions)
1. How they relate (from relationship graph)
1. What’s valid (from business rules)
1. What it can do (from permitted actions)
1. No prompt engineering about data schemas. No RAG pipeline wiring. The semantic contract IS the grounding.




## [5/13 - Google vs Microsoft vs Palantir: The Enterprise Ontology Race](https://medium.com/@cloudpankaj/google-vs-microsoft-vs-palantir-the-enterprise-ontology-race-and-the-layer-all-three-are-missing-e965b2d635d9)

1. [OWL Portability Layer](https://github.com/cloudbadal007/owl-portability-layer)
2. OWL - ?? 
3. Ontology first: Domain classes and properties live in ontologies/*.ttl as the single semantic source of truth.
4. SHACL as policy: Constraints (including SPARQL-based rules) enforce approvals and thresholds without scattering logic in adapters.
5. Dict → RDF: Payloads are lifted to RDF for validation, then passed unchanged to adapters when validation passes.
6. Pluggable targets: Register PalantirFoundryAdapter, FabricIQAdapter, or MCPAdapter under short keys; swap target_platform only.

7. semantic layer that grounds enterprise AI agents in meaning rather than just data
8. Microsoft entered it with Fabric IQ. 
9. Palantir has been running it for a decade with Foundry. 
10. Google has entered with the Knowledge Catalog and Enterprise Knowledge Graph


11. **Knowledge Catalog** 
12. formerly Dataplex Universal Catalog
13. Google - Knowledge Catalog (formerly Dataplex Universal Catalog)
14. The core shift: from a passive metadata registry to an active, AI-powered context graph.
15. Automatically extracts semantics from structured and unstructured data using Gemini
16. Exposes context to AI agents via MCP tools, Context APIs, and pre-verified “golden queries”

17. **Enterprise Knowledge Graph** : This is the entity resolution and reconciliation layer
18. Uses schema.org as its common ontology foundation
19. Converts relational BigQuery data into RDF triples via the Entity Reconciliation API


20. **Agentic Data Cloud** by Google 


## 5/9 

AgentCore Identity: Secure Agent Authentication

1. What are the different services of AWS Amazon Bedrock AgentCore
2. Production ready agents 
3. Strands Agents SDK 
4. AWS SDK boto3 
5. Bedrock as the model provider 

What do you need to scale up a POC for real users ? 
Application Hosting 
Memory 
Observability and more. 

1. **Center AgentCore Runtime** - agent runs in it. Fully managed. Serverless environment. 
2. Sessions upto 8 hours 
3. Payloads upto 100 megabytes 
4. Each sessions runs in its own micro VM (??) - dedicated CPU, memory, filesystem, and auto clean up 
5. Choose your model - claude, gemini, whatever 
6. Choose your framework - crewai, langgraph etc. 
7. MCP compatible. 

8.  **AgentCore Gateway**
9.  Actis as a MCP server and exposes targets like API, lamda functions, 
10. Connections to Salesforce, JIRA, 
11. Agent can discover and call anything it needs to integrate with 

12. **AgentCore Memory**
13. Short Term - what is happening in session. E.g. a coding assistant refactoring code. 
14. Long Term - User preferences. Store insights. Generate session summaries. etc. 

15. **Built in tools**
16. Code interpreter - run python, typescript or javascript, inside a secure (Bedrock) managed environment. 
17. Browser tool - let agents interact with live web pages
18. Both tools are integrated with IAM (secure)

19. **AgentCore Observability service**
20. Every step is there - reasoning, tool calls and outcome 
21. telemetry flows into CloudWatch by default - latency, token usage, session count, error rates (??)

22. **AgentCore Identity** : Every request is verified. 
23. Even if it comes from previously trusted sources. 
24. Each agent has a unique identity
25. And fine grain permissions 
26. Amazon Cognito built for Agent 
27. Both inbound and outbound authentication mechanisms
28. inbound - OAuth 2.0 flows - use an identify provider 
29. outbound - use the SDK - use annotiations - @requireaccesstokens 
   1. supports token refresh etc. 
   2. machine to machine and delegated access. 
30. **Secure Token Vault** - for storing credentials - OAuth token, client keys, etc. 


## [AgentCore Runtime Basics](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/xQjTIMMzTfzhWan9bjG9oNQwCKsybVIJ)

1.  **Center AgentCore Runtime** - agent runs in it. Fully managed. Serverless environment. 
2.  Sessions upto 8 hours 
    1.  stops after 15 minutes of inactivity 
3.  Payloads upto 100 megabytes 
4.  Each sessions runs in its own micro VM (??) - dedicated CPU, memory, filesystem, and auto clean up 
5.  Choose your model - claude, gemini, whatever 
6.  Choose your framework - crewai, langgraph etc. 
7.  MCP compatible. 

1. Start an agent ? **InvokeAgentRuntime**
1. **runtimeSessionId** - a client calling in? Must provide runtimeSessionId. AgentCore uses that to isolate the conversation. 
1. protocols supported 
   1. HTTP - simple request / response patter 
   2. MCP - agnet to tool interaction 

2. **AgentCore Runtime Service Contract** 
3. How to code your agent, so it can communicte with the (managed) hosting layer. 
4. What endpoints you must expose
5. AgentCore will sping it up, manage it and route traffic to it 
6. The agents have to created in a specific way 
7. That is the contract. 
8. Want to run on **HTTP** ? 
   1. Host must be 0.0.0.0 
   2. Port must be 8080
   3. Container must be ARM64 (??)
   4. Must have two endpoints 
      1. /invocations - get some job done. Should accept a HTTP POST. Can return JSON or SSE 
      2. /ping - HTTP GET. Health and status checks (JSON)
1. Want to run a **MCP**? Your agent is reaching out to a tools server that talks MCP 
   1. Host must be 0.0.0.0 
   2. Port must be 8000
   3. Container must be ARM64 (??)
   4. Must have two endpoints 
      1. stateless streamable HTTP for transport. MCP can be accessed remotely. 
      2. no stdio please. 


1. **Authentication**
1. SigV4 (Signature version 4) - the default version - similar to other AWS APIs or 
1. OAuth supported if you insist 
   1. User sends in a JWT with the request. AgentCore Identity validates it. 
   1. If pass, then only the agent code sees the request. 


1. **AgentCore Runtime**
1. Agent launched - get a unique identity and is versioned. It is immutable and a snapshot of the agent code / configuration. 
1. the app runs like a mini container 
1. Where do you send the requests ? Endpoints 
1. Endpoints can be for dev, stage, prod etc. 
1. and there is a default alias that always points to the latest version 
2. **AgentCore Runtime / sessions** - each users instance isolated 
3. They are the same session, across multiple interaction, in the same session. 

1. [AgentCore Sample tutorial](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime) 

## AWS Bedrock AgentCore Gateway / Discovery powered with Semantic search 

1. How do agents discover tools with Gateway ? 
2. Agent - user MCP to ineract with Gateway 
   1. Gateway - dynamic discovery at runtime ( semantic search )
   2. 

## AWS Bedrock AgentCore Gateway / Sample code 

Jupyter can help have a interactive demo running
Sample git : https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway



## AWS Bedrock AgentCore Gateway / Security 

1. Inbound ? OAuth mandatory 
2. It can validate the identity of the incoming requests 
3. Who is calling my tools. 
4. Outbound ? IAM for resources like Lambda. OAuth for others 
   1. Does you tool interact with external resource (an example please??) Gateway can manage token storage + credential exchange. 
   2. 


## [Strands Agents SDK](https://strandsagents.com/docs/user-guide/quickstart/overview/)
1. Can support Python (fuller support, use this) and typescript






## AWS AgentCore Gateway  

1. Building on AgentCore’s quality loop—the validation architecture is where this gets genuinely exciting.
2. Two validation paths work in parallel. 
3. Batch evaluation runs proposed changes against curated test datasets before anything touches production—catching regressions on cases you already know matter. 
4. Wire it into your CI/CD pipeline and no configuration change ships without passing known-good benchmarks.
5. Then A/B testing takes it live. 
6. **AgentCore Gateway** splits production traffic between current and candidate versions at configurable percentages. 
7. Online evaluations score every session. 
8. Results include **confidence intervals** and **p-values**—statistical rigor, not gut feel.
9. 
10. The key insight: configurations ship as immutable versioned bundles. Swapping a prompt or model becomes a configuration change, not a code change. Rollback is instant.
11. The flywheel compounds—each winning configuration becomes the baseline for the next cycle.
12. 
13. Is your team still shipping agent improvements blind, or building systematic validation into the loop?


[Context Data Products as real differentiators in the AI era.](https://medium.com/@arrufus/context-data-products-as-real-differentiators-in-the-ai-era-1664c951bac3)

Did you realise that the data products you’ve dedicated two years to building are mostly invisible to AI agents? 
After doing the hard work of having the domain teams build and own their own pipelines, 
making data discoverable in the catalogue, and 
federating governance and stewardship, 
your AI agents still cannot answer business questions using your data products. 
And it’s not because the data is wrong, but because data products were designed for human analysts, not autonomous systems.

The Context Gap
Traditional data products bundle raw data with basic metadata: 
schema descriptions, 
ownership tags, and 
quality scores. 

That worked when humans were the primary consumers: 
a data analyst could look at a table, r
ead the documentation and work out how to use it. 

AI agents operate differently. They need:
Semantic context. What does this field mean in business terms?
Temporal context — when was this relevant?
Usage context — how have others successfully used this data?
confidence context — how reliable is this for decision-making?

Without this layered understanding, 
even the most sophisticated AI model is pattern-matching in the dark. 
Knowledge graphs are a critical enabler for generative AI, 
precisely because they provide structured, 
relationship-aware context that flat metadata catalogues cannot.


Context data products are an evolution of traditional data products. They bundle data with rich contextual intelligence: structured through ontologies, semantic layers, and knowledge graphs — so that both humans and AI agents can reason over it.

A traditional data product says: “Here’s the customer transaction table.” 

A context data product says: “Here’s customer transaction data, filtered for active segments, enriched with lifetime value calculations, with an ontology defining what ‘active’ means in this domain, 
lineage showing how that definition was derived, and 
examples of analyses that used this successfully.”

It is machine-readable, meaning it is semantically structured so that an agent can navigate relationships, resolve ambiguity, and take autonomous action.


Ontology-Driven Domain Modelling
An ontology formally defines what entities exist in your business, how they relate and what rules govern them. Palantir’s Foundry platform demonstrates this at scale: its Ontology layer maps datasets to real-world counterparts, i.e. physical assets, customer orders, and financial transactions, creating a digital twin with semantic and operational capabilities. Defence, finance, and healthcare organisations use this to connect AI reasoning directly to governed data.

## [Open Data Product Specification - ODPS](https://opendataproducts.org/)

1. enabling scalable governance, monetization, and AI-native integration — all through a modular, machine-readable YAML specification. 
1. Product Strategy linking data product KPIs to shared business objectives. Together with in-spec referencing for SLAs, Data Quality, Access, and Pricing Plans, it enables measurable, outcome-driven governance and consistent, reusable metadata across large-scale data ecosystems.

## [MLG of ODPS](https://github.com/Open-Data-Product-Initiative/odps-knowledge-base/blob/main/resources/Minimum%20Lovable%20Governance%20for%20Data%20Products%20Whitepaper.pdf)

Minimum Lovable Governance (MLG) is designed to be adopted incrementally. 
Organizations can start with a single data product, define minimal governance, and reuse components as adoption grows.
Over time, automation and AI assistants can be layered on top. 
Governance maturity increases without disruptive transformation programs. 
MLG rewards progress rather than perfection.
Minimum Lovable Governance scales by repetition, not transformation.

1. Start with one data product
2. Select a product that is already shared or business-critical.
3. Define minimum governance once
4. Set ownership, access rules, and quality expectations for that product.
5. Extract reusable components
6. Turn access, quality, SLA, and usage rules into reusable definitions.
7. Apply components to the next product
8. Reuse the same governance blocks instead of redefining them.
9. Automate enforcement
10. Let platforms enforce rules, not people.
11. Repeat and refine
12. Governance improves through reuse, not redesign.

1. Jarkko Moilanen (Ph.D.) - Agentic AI Adoption in Data Exchange. Open (Source) Data Product Specification
2. https://www.linkedin.com/in/jarkkomoilanen/


## 5/2 

## What is the market already doing in terms of semantic graphs 
Microsoft Fabric IQ creates a persistent semantic graph that maps datasets to real‑world entities, relationships, and operational rules. 
Collibra’s Model Context Protocol (MCP) server delivers governed business terms, lineage, and quality signals directly into any copilot or chatbot. 
Starburst’s AIDA assistant reasons across federated data with a 3× accuracy lift when a governed semantic layer is present. 

## suman - something about AI registry 
## john - something about moonshot - Moonshot AI’s Kimi K2.6 j

## 8 is the one 


## [How to Develop An Open Source Ontology & AI Pipeline](https://dhirajpatra.medium.com/how-to-develop-an-open-source-ontology-ai-pipeline-20b31aecb2da)

In Palantir (specifically the Foundry platform), 
the Ontology is the “digital twin” of an organization. 
It is a semantic layer that sits on top of raw data and transforms technical tables into real-world business concepts.
instead of a data scientist looking for TABLE_CX_892 and a business user looking for "Customer 123," 
both go to the Ontology to find the "Customer" object.

The Ontology maps fragmented data into three core components:
**Objects**: The “nouns” (e.g., Aircraft, Employee, Invoice).
**Links**: The “verbs” or relationships (e.g., an Employee belongs to a Department, an Aircraft is assigned to a Flight).
**Actions**: The “kinetics” or changes (e.g., “Cancel Flight” or “Update Salary”). When a user performs an action in a Foundry app, it writes back to the underlying data.

The Pipeline: How it Works
The journey from raw data to the Ontology follows a specific flow:
Data Integration: Raw data is ingested from various sources (ERPs, CRMs, S3 buckets, SQL databases).
Transformation (The “Pipeline”): Data engineers use tools like Code Repositories (Python/Spark) or Pipeline Builder (no-code) to clean and join data into “backing datasets.”
Indexing: These backing datasets are mapped to the Ontology. For example, a row in your cleaned_flight_data table becomes a unique Flight Object.
Application Layer: Once indexed, the data is available in user-friendly apps like Workshop (app builder) or Quiver (analysis tool) without needing to write any more SQL or code.


## How to build an “Open Ontology”

1. **Step 1: Data Integration (The Foundation)**
2. Instead of Palantir’s “Data Connection,” use tools that move data from your sources into a central Data Lakehouse.
3. Tools: Airbyte or Fivetran (Ingestion), combined with dbt (data build tool) for cleaning.
4. Action: Create “Bronze” (raw), “Silver” (cleaned), and “Gold” (business-ready) tables.
5. **Step 2: Define the “Noun” (Object Modeling)**
6. In Palantir, you create an “Object.” 
7. In an open stack, you define a Semantic Model.
8. Tools: Cube.js, dbt Semantic Layer, or AtScale.
9. Action: Instead of just a table orders, you define a "Sales" entity in a YAML file. 
10. You tell the system that "Revenue" is SUM(price) and that every "Sale" is linked to a "Customer ID."
11. **Step 3: Map the “Verbs” (Relationship Graph)**
12. Palantir’s “Links” are simply joins that are pre-defined so users don’t have to write them.
13. Tools: Graph Databases (Neo4j) or Semantic Knowledge Graphs (using RDF/OWL standards).
14. Action: Use a tool like Stardog or simply well-documented foreign key relationships in your Semantic Layer (Cube.js) to define how “Aircaft” relates to “Maintenance Log.”
15. **Step 4: The “Kinetics” (Action Framework)**
16. Palantir’s “Actions” allow you to “write back” to the database (e.g., clicking a button to “Approve Invoice”).
17. Tools: Retool, Appsmith, or Streamlit.
18. Action: Build a small front-end app. When a user clicks “Approve,” the app triggers a Python script or a SQL command that updates your database and logs the change.
19. **Step 5: AI/ML Integration**
20. This is where you, as a Data Scientist, have an advantage.
21. Tools: MLflow or BentoML.
22. Action: Wrap your ML model in an API. Connect this API to your Semantic Layer so that “Predicted Churn” becomes just another property of the “Customer” object, updated every 24 hours.


## What is an enterprise context layer?

1. the **governed infrastructure** between your data stack and AI systems. 
1. It encodes what data means — 
   1. business definitions, 
   2. relationships, 
   3. operational rules, 
   4. lineage, and 
   5. policies
2. so AI agents reason correctly at inference time rather than guess from raw records. 
3. Unlike a semantic layer, it also captures 
   1. decision history, 
   2. authority attribution, and 
   3. policy applicability: 
4. the properties that make context AI-grade. 
5. Without it, 95% of GenAI pilots (MIT, 2025) fail to reach production.


## Semantic knowledge graphs (KGs)

1. Semantic knowledge graphs (KGs) use standardized formats like RDF and OWL 
2. to create a machine-readable "semantic layer" that turns raw data into interconnected knowledge. 
3. Unlike standard databases, these graphs focus on the meaning (semantics) and logical relationships between data points. 
5. **RDF (Resource Description Framework)**: 
6. The foundation that models data as "triples" (Subject > Predicate > Object). 
7. For example: . It uses URIs (unique web identifiers) to ensure every entity and relationship can be linked globally across different systems. 
8. RDF is a data model for representing information as triples and graphs. 
9. It is concerned with identifiers, edges, and values.
10. **OWL (Web Ontology Language)**: 
11. A rich modeling language built on top of RDF that adds logic and constraints. 
12. It allows you to define complex hierarchies, property characteristics (like "inverse" or "transitive"), and class equivalencies. 
13. OWL is an ontology language built on RDF. 
14. It specifies classes, properties, and logical relationships that interpret and constrain what the RDF data means.

[Ontology Reasoning in Knowledge Graphs, 2024](https://medium.com/data-science/ontology-reasoning-in-knowledge-graphs-7e563cc5b62a)
[You Don’t Need a PhD to Build an Ontology](https://medium.com/@irregularbi/you-dont-need-a-phd-to-build-an-ontology-f50ff00b6db9)
**OrionBelt Ontology Builder** is a browser-based ontology editor built with Streamlit and rdflib.

[Cube.js, the Open Source Dashboard Framework](https://medium.com/cube-dev/cube-js-the-open-source-dashboard-framework-ultimate-guide-af38bc9955a1)
[Implementing a Semantic Layer with dbt: A Hands-On Guide](https://www.datacamp.com/tutorial/semantic-layer-with-dbt)
[#dbt / Understanding the Semantic Layer](https://medium.com/data-driven-diaries/understanding-the-semantic-layer-c98c88c50e5e)
[#dbt /  Getting started with data lineage / might be only useful if you have used dbt for transformation.](https://www.getdbt.com/blog/getting-started-with-data-lineage)

[A CTO’s field guide to building, governing, and scaling meaning across data, retrieval, knowledge graphs, and agents](https://gauravagg2016.medium.com/ontology-engineering-as-the-semantic-operating-system-of-the-ai-first-enterprise-e8db15bc0957)

## Ontology engineering precondition for safe autonomous action at enterprise scale

1. Every major cloud provider has released agent runtime infrastructure (Google Agent Builder, AWS Bedrock Agents, Azure AI Foundry) that is designed for enterprise-scale autonomous action.
1. The regulatory environment for AI systems is tightening: the EU AI Act’s requirements for traceable, auditable AI decision-making are structurally aligned with what a semantic control plane provides
1. the competitive differentiation window is open but closing: the enterprises that build their semantic operating systems in 2025–2026 will have identity graphs, SHACL conformance histories, and domain ontology depth that are expensive and slow to replicate from zero.

## Meaning. Enterprise wide. Centralized. Owned. Understood by humans and agents alike. 

1. The same business word means different things in different systems, teams, and agent workflows.
   1. Is a customer the same as an account?
   2. Is a product the same as an offer?
   3. Is a subscriber the same as a payer?
   4. Is a diagnosis term equivalent to a billing code?
   5. Is a service outage a network event, a customer-impact event, or both?
2. 
3. In a human-mediated enterprise, that drift created friction and meeting time. 
4. In an AI-mediated enterprise, it creates compounding failures at machine speed.


## What are the various layers ( arranged in the order of value ) meta-data for enterprise data ? 

1. https://gauravagg2016.medium.com/ontology-engineering-as-the-semantic-operating-system-of-the-ai-first-enterprise-e8db15bc0957
   
2. **Business Glossary** 
3. Definitions. Provided by business. Human readable. 
4. As is the case of any free text, is open to interpretation. 
5. Not - in a formal definition. ( What is the formal definiton ?? )
6. Cannot - be queried by reasoner. ( What does that mean ?? )

7. **Database schema**
8. You can get it from the database, e.g. Iceberg, Starburst etc. 
9. Tables, columns, data types, relationships.
10. Cannot - tell what is the meaning of that data. (Give an example?? )

1. **(BI) Semantic Layer**
1. Definitions of business metrics, joins etc. 
1. These are used in query time by BI tools e.g. ??, ?? 
1. Cannot - be used by AI agents. ( Why ?? )

1. **Taxonomy (SKOS)**
1. Hierarchical classification ( why do we need them?? )
1. Synonym relationships ( what are they?? what is the use ?? )
1. No - properties, constraints, and instance level facts ( which one had instance level facts ?? )

1. **Knowledge Graph / Property Graph** 
1. Connections allowing graph traversals. 
1. Not - a web of meanings, but a web of links. 

1. **Ontology**
2. RDF / OWL / SHACL 
3. Classes (data products??), 
4. Properties ( column level details ?? )
5. axioms ( ?? )
6. equivalences (??)
7. constraints ( foreign keys etc.?? )
8. inference rules (??)
9. Supports machine reasoning and runtime validation (??)


5. **RDF (Resource Description Framework)**: 
6. The foundation that models data as "triples" (Subject > Predicate > Object). 
7. For example: . It uses URIs (unique web identifiers) to ensure every entity and relationship can be linked globally across different systems. 
8. RDF is a data model for representing information as triples and graphs. 
9. It is concerned with identifiers, edges, and values.


10. **OWL (Web Ontology Language)**: 
11. A rich modeling language built on top of RDF that adds logic and constraints. 
12. It allows you to define complex hierarchies, property characteristics (like "inverse" or "transitive"), and class equivalencies. 
13. OWL is an ontology language built on RDF. 
14. It specifies classes, properties, and logical relationships that interpret and constrain what the RDF data means.





Key Features and Benefits 

1. **Automated Reasoning**
2. By using OWL's formal logic, systems can infer new facts that aren't explicitly written down. 
3. If the graph knows "A is the father of B" and "father" is a sub-property of "parent," 
4. it automatically infers "A is the parent of B". 
5. **Open-World Assumption**
6. Unlike traditional databases, OWL assumes that if information is missing, it is simply unknown rather than false. 
7. This makes it ideal for the "messy" reality of the web where data is often incomplete. 
8. **Interoperability**
9. Because they follow W3C Semantic Web Standards, these graphs can integrate data from diverse, siloed sources by mapping them to a common vocabulary or ontology. 
10. **Data Validation**
11. While OWL handles logic, SHACL (Shapes Constraint Language) is often used alongside it to validate the actual structure and quality of the RDF data against specific shapes or schemas. 

12. To build and query these graphs, developers typically use: 
   1. **SPARQL**: The standard query language for RDF, similar to SQL but designed for graph pattern matching. 
   2. **Triple Stores**: Specialized databases like GraphDB or Apache Jena that are optimized for storing and reasoning over RDF/OWL data. 
   3. **Protégé**: A widely used open-source editor for designing OWL ontologies. 

AI responses may include mistakes.

[2] https://atlan.com/know/rdf-vs-owl/
[3] https://rushdb.com/blog/knowledge-graphs-semantic-reasoning-meets-graph-architecture
[4] https://milvus.io/ai-quick-reference/what-is-the-purpose-of-semantic-web-in-the-context-of-knowledge-graphs
[5] https://www.youtube.com/watch?v=4fKm-NXZamI
[6] https://www.youtube.com/watch?v=kcRggv2e7-o
[7] https://www.w3.org/RDF/
[8] https://en.wikipedia.org/wiki/Resource_Description_Framework
[9] https://www.w3.org/OWL/
[10] https://www.youtube.com/watch?v=WIflwx2EC54
[11] https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-knowledge-graph/
[12] https://medium.com/vaticle/knowledge-graph-representation-grakn-ai-or-owl-506065bd3f24
[13] https://bryon.io/from-facts-to-knowledge-the-layer-cake-of-rdfs-and-owl-e84819d8075d
[14] https://www.linkedin.com/pulse/great-graph-divide-deep-dive-rdfowl-property-graphs-geraci-wh73c
[15] https://graphdb.ontotext.com/documentation/11.3/introduction-to-semantic-web.html
[16] https://enterprise-knowledge.com/cutting-through-the-noise-an-introduction-to-rdf-lpg-graphs/
[17] https://link.springer.com/book/9798868818226







## Books 

1. [12 AI Books Worth Reading in 2026 — If You Actually Build Things](https://medium.com/data-science-collective/12-ai-books-worth-reading-in-2026-if-you-actually-build-things-3de8e3dfd8a8)



## What is AI-Ready Data?**

1. [AI-Ready Data vs. Analytics-Ready Data](https://medium.com/@community_md101/ai-ready-data-vs-analytics-ready-data-f67ef0804341)
1. **Who consumes AI-Ready Data**
1. AI-ready data is built for a very different kind of consumer. The consumer here is not a human analyst, but a model: LLMs, machine learning systems, and increasingly, autonomous agents.
1. **How is AI-Ready Data Consumed**
1. These systems do not read dashboards or interpret charts. They consume data as tokens, embeddings, features, and context windows, and they reason statistically rather than intuitively.
1. **What does “good” look like for AI-Ready Data?**
1. Because models consume data differently, “good” means something fundamentally different.
1. 
1. **Context**: There is no way for models to experience the world, they must always infer it. 
1. Without sufficient surrounding context, like historical state, user intent, environmental conditions, and system constraints, models are forced to guess (popularly known as “hallucinate”). 
1. And when models guess, they do so confidently.
1. **Completeness**: Unlike humans, models cannot pause and ask for clarification or fill in gaps with judgment. 
1. Missing data is not interpreted as uncertainty but treated as absence. This leads to brittle outputs that appear coherent but are logically incomplete. Complete data gives models the full boundary of the problem space they are expected to operate within.
1. **Timeliness**: An AI system trained or prompted on stale data is reasoning about a world that no longer exists. In dynamic systems, yesterday’s truth becomes today’s liability. Fresh data anchors model behaviour to current reality, reducing drift between what the model believes and what is actually happening.
1. **Semantically rich**: Models do not understand meaning unless meaning is explicitly encoded. Relationships, hierarchies, intent, and constraints must be expressed in the data itself. Semantic richness is what allows models to distinguish between similar-looking signals and reason correctly across domains, rather than hallucinating connections that were never there.
1. 
1. Together, these properties reflect how AI systems are NOT intuitive. They are literal, probabilistic, and unforgiving. AI-ready data is not about making data elegant but about making reality legible to a machine in machine language.
1. 




[SDLC That Ships Features End-to-End](https://medium.com/@brettluelling/how-we-built-a-16-agent-sdlc-that-ships-features-end-to-end-2a3621fc9e64)

https://github.com/garrytan/gstack


## Corporate Chanakya (CC)

1. Your work speaks for itself : Name what you delivered. Every time.
2. You speak up in every meeting equally : Pick the one room where it counts most. Watch VM 
3. You wait for results to get noticed : Decision makers need context, not proof. Hmm.. what to do of this ? 
4. You build relationships when you need them : Start before you need anything from anyone. Who are you meeting this week ? 
5. You communicate how hard you worked : Talk about what changed because of you. What is the message? 
6. Your best work happens behind closed doors : Find one way to make the output visible.
7. You make yourself easier to manage : Being liked keeps you comfortable. Being visible gets you promoted. Where are you visible ? 
8. You stay loyal to people who cannot advocate for you : Know whose voice actually reaches the room. Damn. D cant speak. SS is woman scorned (?). V is insipid. 
9. You perform competence under pressure : Trust lands harder than polish every time.
10. You assume visibility feels like self-promotion : Presence is clarity. Start there. Are you present in the right discussions? 


## CUDA (Compute Unified Device Architecture)

1. Speaker(??) - leather jacket with chains hanging from zips (??). All black and frankly not too high quality looking either. But very meticulously done hairline. Age : 65 ? 

1. CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model developed by NVIDIA 
1. that allows software to use GPUs for general-purpose processing (GPGPU). 
1. It enables developers to use C++ and other languages to 
1. speed up data-intensive applications—like AI, scientific simulation, and image processing—
1. by harnessing thousands of GPU cores simultaneously.
1. **NVIDIA Ecosystem**: It is a proprietary technology requiring NVIDIA GPUs and includes the CUDA Toolkit, libraries (like cuDNN, cuBLAS), compilers, and tools.
2. CUDA acts as a bridge, allowing the host (CPU) to send tasks to the device (GPU) via kernels—functions executed in parallel by many threads
1. **Usage** : deep learning, high-performance computing (HPC), finance, and computer graphics

All GPUs are architecturally compatible (??). Ok. Why?? 

journey started 20 years ago. GeForce RTX 5090. 
Programmable what? pixel shader. 
make an accelerator programmable. 

fusion of 3d graphics and artificial intelligence. DLSS 5 

Federated - if others are not able to build their success stories on your platforma, it is not going far. 
Controllable - if it is not controllable, it is not your, you might as well not  feed it much at all. 

**Structured Data is the foundation of Trustworthy AI**

cudaX libraries - algorithm company. 70 libraries + 40 models 
cuDNN - Deep Neural Networks. 
cuDF - for structured data. Data frames. 
cuVS - for vector stores. reading data at enterprise scale ? 

multi modality perception and understanding - ai to read a PDF 

Semantic data. Unstructured data. AI data. 

IBM inventor of SQL - domain specific language 
IBM watsonx.data 
system 360 - general purpose computing 

Data for the era of AI 

Accelerate Data Processing // On cloud // and on Prem 

Dell 
Google, BigQuery 

Amazon were the first cloud partners of NVIDIA 
Amazon Bedrock 
Amazon SageMaker AI
OpenAI to AWS 

Confidential computing - even the operators can't touch your data or model. 

**CoreWeave** - worlds first AI native cloud. 

**Palantir** ontology platform. Working with Dell. 

Vertically integrated and horizontally open (?? )

25 companies building next Quntum GPU hybrid system

AI natives 

miniCUDA (??)
ampere (??)

You need install base. You need developers / users using it to create new things. 

inference inflection has arrived 

[NVIDIA GTC Keynote 2026](https://www.youtube.com/live/jw_o0xr8MWU?si=tIyyOkYKOP6Q2mAf)


How do you make sure that the answers are correct 
spyder 
birt 
feedback 

Enterprise Context Layer ( Data Context Layer )
Ontology 
Taxonomy 
Business Rules 
Glossary Definitions 
Synonyms 

Semantic Layer 
Data definition 
Column description 
Metrics (?)
Logic (?)


[From Dashboards to AI Decisions: Rethinking Enterprise Intelligence](https://starburstdata.ondemand.goldcast.io/on-demand/b2f3950e-1530-4344-9ad2-64a8dd5b0b5c?__hstc=81614408.f9a947593140bfd97ebcb97600ef34c0.1777691441068.1777691441068.1777691441068.1&__hssc=81614408.2.1777691441068&__hsfp=2084a4d51d5540dadca31207244bc581&submissionGuid=fba61f69-09d0-4412-ab84-eb0befd799ab)

## Logical layers 

1. Agents 
1. Agentic Control Plane 
1. Business Control Layer 
1. Analytics Engine 


## AI Data Assistant (AIDA) by Starburst 

AIDA leverages a ReAct (reason–act–observe) framework to move beyond query generation into true analytical reasoning, combining live data sampling and metadata analysis to reach a well-grounded answer. The result is an assistant that reasons through problems like an analyst, not just a text-to-query translator. 
1. AIDA tailors responses based on user role, 
   1. delivering detailed technical explanations for data practitioners and 
   2. concise, decision-ready summaries for business leaders.

1. Ask questions across all your data ( and not only the centralized one )
   1. Show insights 
   2. Make decisions and 
   3. Take actions 

Shared Enterprise Context ?? 

AI driven decisions 
Context 
Data Layer 



Starburst announced AIDA (AI Data Assistant), an AI assistant designed to reason across distributed enterprise data sources without requiring data movement or centralization[1]
business-user-facing tool, not a developer platform
AIDA’s thesis is that the dominant pattern of centralizing data before applying AI is architecturally wrong for most enterprises.
OpenAI leads adoption at 64%, followed by Azure OpenAI at 62% and Google Gemini at 54%, according to Futurum Group’s 1H 2026 
AI Platforms Decision Maker Survey (n=820)

The Semantic Layer is Finally Code, Not Just a Concept,’ March 2026

The global Data Intelligence, Analytics, & Infrastructure (DIAI) market is projected to grow at a 16.9% CAGR to surpass US$1.2 trillion by 2031, according to Futurum’s 1H 2026 Data Intelligence, Analytics, & Infrastructure Market Sizing & Five-Year Forecast. 

Perhaps the most forward-looking aspect of this news is the introduction of the agentic layer and the support for the Model Context Protocol (MCP). The industry is rapidly moving away from simple chatbots toward agentic AI workflows where AI can take actions.

This bring your own model (BYOM) philosophy is essential. During demonstrations, Starburst used Claude 4.6 Sonnet to analyze complex Formula 1 and financial datasets. However, the platform remains model-agnostic, allowing businesses to optimize for cost, performance, or accuracy based on their specific needs.

This transition from conversational intelligence to intelligent action, facilitated by an Agent Gateway, is the next frontier of enterprise productivity.

Does Starburst partner with semantic layer vendors such as AtScale or dbt

Ref : https://futurumgroup.com/insights/can-starbursts-aida-crack-the-enterprise-ai-data-access-problem/
Ref : https://www.starburst.io/press-releases/starburst-announces-its-ai-data-assistant-to-bring-ai-to-the-business-user/


## 5/1 

1. [TODO] Must have a lint to go through all the notes. Things should belong to their own pages. Other pages must refer to that page rather than repeating the information. 


## 4/28 

Build your own LLM Wiki from scratch                                                                                    
Today: working code. No framework needed.

You need three things: an LLM API, a folder of markdown files, and git.

Step 1: Write your schema
schema.md defines page types, naming conventions, extraction rules, and cross-reference policy. 
This is the single most important file. Start simple. Refine after a few ingestions.

Step 2: Seed with empty index.md and log.md
The LLM populates these during the first ingestion.

Step 3: Ingest your first source
Drop a document into sources/. The ingestion script:
Reads source + schema + current index
Asks the LLM to generate wiki pages per the schema
For existing pages, merges new info into existing content
Updates index.md and log.md
git commit

Expect 4-8 pages from a single paper or article.

Step 4: Query
The query script:
- Reads index.md to find relevant pages
- Loads 3-8 wiki pages + follows one level of [[wikilinks]]
- Synthesizes an answer with citations back to wiki pages
- With --save flag, writes the answer as a new wiki page

Step 5: Lint periodically
The lint script reads all pages and checks for:
- Contradictions between pages
- Orphan pages with no incoming links
- Stale pages not updated despite newer sources
- Missing pages referenced in links but not yet created
- Claims without source attribution

 Report gets appended to log.md.

 —

 Existing Implementations

 If you want to skip the build:

1. [LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki)
   1. [click here](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
2. [mcptube-vision](https://github.com/0xchamin/mcptube)
   1. mcptube-vision (v2) is an open-source tool designed to turn YouTube videos into an AI-queryable, persistent knowledge base, inspired by Andrej Karpathy's "LLM Wiki" concept. 
   2. It operates as both a Command Line Interface (CLI) and a Model Context Protocol (MCP) server, allowing AI agents to "watch" and analyze video content for deep insights. 
3. [Memoriki](https://github.com/AyanbekDos/memoriki)
   1. Personal knowledge base with real memory.
   2. Wiki gives structure. MemPalace gives memory.
4. [mempalace](https://github.com/MemPalace/mempalace)
   1. Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.
   

 - llmwiki.app — Claude via MCP with a web UI. Closest to Karpathy's canonical description.
 - llm-wiki-compiler — Two-phase pipeline with SHA-256 change tracking and paragraph-level source attribution.
 - mcptube-vision — YouTube-focused variant. Processes video frames + transcripts.
 - Memoriki — Combines semantic search with temporal knowledge graphs.

 —
 Three days, one pattern.
 Day 1: the flow — 3 operations, 18 steps.
 Day 2: the architecture — concurrency, scale, when to use it.
 Day 3: the code — directory structure, scripts, ship it.
#GenerativeAI #AI #LLM #RAG


## 4/26 

[Data Products: The Essential Context for Enterprise AI](https://moderndata101.substack.com/p/data-products-the-essential-context)

What are the six deliberate layers - in OpenAI ?? 

Two engineers, three months, a production system used daily by roughly 4,000 people across the company. 
The headline wasn’t the output; it was the architecture.

1. The agent was built on **six deliberate layers** of context grounding every query: 
   1. schema metadata (that is ok) and lineage (where do we get that for??), 
   2. curated expert descriptions (that is fine) 
   3. historical query patterns (from where? and what do i do with that?)
   4. code-derived definitions from pipelines, ( what will we do of that)
   5. institutional knowledge pulled from Slack and docs, (dont need that - just yet) 
   6. persistent memory of past corrections (what of that??)
2. Separately, the agent could issue live queries to inspect schemas when context was missing or stale (not right now. wait.)


transformational rise of the modern data stack with Tristan Handy from dbt in the past and 
in our own reference architectures. 
The general evolution over the past decade has transformed data architectures across ingestion, transformation, warehousing, and 
storage to centralize data and make it quickly and easily accessible. 
The idea is then with cleanly organized data, 
teams could simply write SQL to derive data from their data warehouses, 
power charts/dashboards, and 
enable business intelligence across an entire organization.

**The agent frenzy**
In 2024 moving into 2025 as LLM capabilities increased, 
essentially every single organization wanted to build and deploy agents on top of their existing data stacks. 
We’ve previously discussed how we define agents, 
but from an organizational point of view the natural allure of more work being done with greater efficiency and less time naturally led to the gravitation towards agentic workflows. 
Companies attempted to build “chat with your data” chatbots, 
support agents, etc. 
The frenzy was both bottoms-up and tops-down – developers wanted to make use of the newest, 
shiniest LLM capability and leadership applied AI adoption pressure to increase automation and reduce costs.


**Hitting the wall**
1. Despite the initial optimism, 
2. it quickly became clear that most of these efforts failed. 
3. Organizations tried to deploy their agents but ran into a wall. 
4. MIT famously published their **“State of AI in Business 2025”** report which stated that with AI deployments, 
5. “most fail due to brittle workflows, lack of contextual learning, and misalignment with day-to-day operations.”


as evidenced through SQL benchmarks like **Spider 2.0** and **Bird Bench**

Our query comes in. “What was revenue growth last quarter?” 
that is typically easily answered by a quick glance at a **Looker** or **Tableau** dashboard

head of the data platform steps in and says – 
“we’ve built semantic layers to solve this exact problem. 
We capture our revenue definition there.” 

challenge #2 – where are the right data sources? Which ones are the right sources of truth?
data agents need access to a repository of up-to-date business definitions and data sources to overcome these problems.

**Context layer, context OS, context engine, contextual data layer, ontology**
there needs to be up-to-date and maintained context that 
not only understands how an enterprise works and 
how the data systems are structured, but 
also maintains the tribal knowledge to tie everything together.

**Context Layer vs. Semantic Layer**
A traditional semantic layer in the context of BI is great for specific metric definitions (like revenue, churn, ARPU). However, they are usually hand constructed by data teams using very specific syntax through a dedicated layer like LookML and are connected directly to a BI tool like Looker.

**Data Context Layer as a superset of Semantic Layer**
1. data context layer should essentially become a superset of what a semantic layer would traditionally cover. 
2. Sure, specific metric definitions can be hard-coded, but a modern context layer should include more to ensure agent autonomy – 
3. canonical entities, 
4. identity resolution, 
5. specific instructions to dissect tribal knowledge, 
6. proper governance guidance, and more.

7. **Accessing the right data**: ensuring all the right data is accessible. 
8. This is table stakes. 
9. Ideally an organization would be implementing some form of the modern data stack with some degree of unification through a lakehouse architecture. 
10. Even then, we’d want to ensure the agent has access to all the data it needs, 
11. which may extend beyond just what’s available in warehouses and operational apps. 
12. This includes tribal knowledge captured in internal systems, GDrive/Slack, etc.

13. **Automated context construction**
15. Dats is accessible? If yes, then the next step is starting the construction of the context layer. 
16. The benefit of using LLMs is that a lot of the initial context gathering can be done in an automated way. 
17. An emphasis of focus should be on high signal context – 
18. for example, looking through past query history can be high signal in determining the most referenced tables and most common joins, and data modeling solutions like dbt or LookML can provide clear definitions for business metrics.
19. 

1. **Agents** 
1. once the context layer is properly constructed, 
1. it just needs to be exposed to agents and accessible real-time. This can typically be done through API or MCP

1. **Keep it updated**
1. While the initial system has been set up correctly, 
2. data systems are never static and as a result the context layer shouldn’t be either. 
3. Data sources and formats can change upstream and 
4. individuals may have custom instructions they’ll want to add and modify based on changing business requirements. 
5. In the case a data agent provides incorrect data and requires accuracy refinement, 
6. that should of course be incorporated back into the context layer. 
7. In this way the context layer becomes a living and constantly evolving corpus.
   

1. Context Layer 
   1. Natural Language : context.md - 
      1. For CRM data, do this ... 
      2. For XYZ data, do that ... 
2. LookML syntax : orders.view.lkml 
3. Metrics SQL
   1. revenue.sql 

Palantir has a long history of constructing ontologies for organizations 
that provide clear context from messy data, and have built a big business doing so.



1. A Data Product is context packaged as a first-class asset.
1. A **Data Product** is a managed unit of data 
2. that is treated like a product (what does that mean??)
3. rather than as a byproduct of some operational system.
   1. It has an owner.
   2. It has a contract describing what it guarantees and what it doesn’t.
   3. It has a named consumer in mind.
   4. It has a lifecycle: versioned changes, deprecation windows, sunset.
   5. It is discoverable in a catalog,
   6. It is addressable through a stable interface, and 
   7. accompanied by its own semantics, lineage, and quality signals.



Schema metadata and lineage: a Data Product carries its schema and its upstream lineage as part of its specification.
Historical query patterns: usage telemetry is a natural byproduct of a Data Product served through a governed interface.
Curated expert descriptions: the Data Product’s owner writes these as part of its contract.
Code-derived definitions: the transformation logic that produces the product is its definition, and it’s already versioned.
Institutional knowledge: the product’s semantic layer captures the decisions that tribal knowledge otherwise preserves.
Memory of past corrections: a governed product that reviews and incorporates feedback accumulates this automatically.





Making it work is not primarily a model problem.
The industry spent 2025 discovering this, and the consensus across OpenAI, a16z, MIT, Palantir, and others is that the missing piece is context infrastructure: durable, managed, versioned, available to agents.

The right shape for that context is the Data Product.
This is not a new idea, but the AI era has made it load-bearing. 
A Data Product is what an enterprise builds once, and agents consume forever, 
in contrast to the status quo of agents assembling context per query.

1. **The architectural choice of where the Data Product exists**
1. …determines whether this strategy is portable across the enterprise or 
1. locked into a single compute platform. 
1. The data gravity platforms (Databricks, Snowflake, Palantir) are building strong context surfaces tied to their compute. 
1. DataOS is building for the enterprise whose data is in more than one place, and intends to keep it that way.

The missing layer for enterprise AI is the Data Product, and the right way to build Data Products is above the engine, not inside it.




## [Inside OpenAI’s in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/)






## [Your Data Agents Need Context](https://a16z.com/your-data-agents-need-context/)

Recently in the world of data and AI agents, 
context layers and graphs have emerged as an interesting topic of discussion. 
In fact, it’s difficult today to have a conversation with an organization working with data and AI and not have the topic of context come up.

And for good reason. Over the past year, the market has realized that data and analytics agents are essentially useless without the right context – they aren’t able to tease apart vague questions, decipher business definitions, and reason across disparate data effectively.

It’s not their fault, of course. The modern data stack has undergone a decade+ transition from disparate data sources to consolidated data and cleaned definitions (which is good), but even then the consolidation is never perfect and a lot of messiness is introduced. The general market evolution has been as follows:


## [20260129 -Inside OpenAI’s in-house data agent](https://openai.com/index/inside-our-in-house-data-agent/)

1. agent is powered by ?? GPT‑5.2 and 
2. designed to reason over OpenAI’s data platform. 
3. It’s available wherever employees already work: 
   1. as a Slack agent, 
   2. through a web interface, 
   3. inside IDEs, in the Codex CLI via MCP⁠(opens in a new window), and 
   4. directly in OpenAI’s internal ChatGPT app through a MCP connector⁠(opens in a new window).

4. User interface ( ....)
5. UI Agent API 
6. Supported by pre-processed offline - internal data KB, company context 

## How it reasons through problems. 
1. Rather than following a fixed script, the agent evaluates its own progress. 
2. If an intermediate result looks wrong (e.g., if it has zero rows due to an incorrect join or filter), 
3. the agent investigates what went wrong, adjusts its approach, and tries again. 
4. Throughout this process, it retains full context, and carries learnings forward between steps. 
5. This **closed-loop, self-learning** process shifts iteration from the user into the agent itself, 
6. enabling faster results and consistently higher-quality analyses than manual workflows.






## 4/24 

## 𝗛𝗼𝘄 𝗟𝗟𝗠𝘀 𝘀𝗵𝗼𝘂𝗹𝗱 𝗺𝗮𝗻𝗮𝗴𝗲 𝗸𝗻𝗼𝘄𝗹𝗲𝗱𝗴𝗲

https://www.linkedin.com/feed/update/urn:li:activity:7451634712130920448/

**Old way** : chunk documents, embed them, search at query time, hope the right fragments surface.

**𝗔𝗻𝗱𝗿𝗲𝗷 𝗞𝗮𝗿𝗽𝗮𝘁𝗵𝘆** - link ?? 
𝗛𝗲𝗿𝗲'𝘀 𝘁𝗵𝗲 𝗰𝗼𝗿𝗲 𝗶𝗱𝗲𝗮: 𝘀𝘁𝗼𝗽 𝘁𝗿𝗲𝗮𝘁𝗶𝗻𝗴 𝘁𝗵𝗲 𝗟𝗟𝗠 𝗮𝘀 𝗮 𝘀𝗲𝗮𝗿𝗰𝗵 𝗲𝗻𝗴𝗶𝗻𝗲. 𝗧𝗿𝗲𝗮𝘁 𝗶𝘁 𝗮𝘀 𝗮 𝗰𝗼𝗺𝗽𝗶𝗹𝗲𝗿.

## Operation 1 : Ingest

1. **The key architectural point**: Ingest is write-heavy (single-writer model), 
2. Read the full source document
3. Read schema (extraction rules for the source type)
4. Read index.md to identify existing pages and prevent duplicates
5. Create source-{title}.md with key content from this document
6. Create or update entity pages (people, companies, tools)
7. Create or update concept pages (technical ideas, methods)
8. Update topic pages with new synthesis reflecting the source
9. Add [[wikilinks]] between all touched pages
10. Update index.md and append to log.md

## Operation 2 : Query

1. **The key architectural point**: Query is read-only (concurrent-safe), 
1. Read index.md to identify relevant pages
2. Pull 3-8 pre-synthesized wiki pages
3. Follow cross-references (like Wikipedia browsing)
4. Compose answer with citations to wiki pages (which cite original sources)
5. (Optional) Save the answer as a new wiki page (query --save pattern)

## Operation 3 : Lint

1. **The key architectural point**: Lint is a maintenance sweep. 
2. Contradiction scan: flag pages with conflicting claims
3. Orphan detection: find pages with no incoming links
4. Staleness check: flag pages not updated despite newer relevant sources
5. Gap analysis: identify referenced topics that lack their own page

Each ingestion is committed as a git snapshot, giving full rollback capability.

(𝗗𝗮𝘆 𝟮): 𝗧𝗵𝗲 𝗮𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁'𝘀 𝘃𝗶𝗲𝘄 — 𝗰𝗼𝗻𝗰𝘂𝗿𝗿𝗲𝗻𝗰𝘆 𝗺𝗼𝗱𝗲𝗹, 𝘀𝗰𝗮𝗹𝗲 𝗯𝗼𝘂𝗻𝗱𝗮𝗿𝗶𝗲𝘀, 𝗮𝗻𝗱 𝘄𝗵𝗲𝗻 𝘁𝗼 𝘂𝘀𝗲 𝗪𝗶𝗸𝗶 𝘃𝘀 𝗥𝗔𝗚 𝘃𝘀 𝗛𝘆𝗯𝗿𝗶𝗱.

What's your current approach when your documents exceed the context window?
#LLMWiki #RAG #KnowledgeManagement #AI

𝐃𝐚𝐲 𝟐 𝐨𝐟 𝟑: 𝐋𝐋𝐌 𝐖𝐢𝐤𝐢 𝐚𝐫𝐜𝐡𝐢𝐭𝐞𝐜𝐭𝐮𝐫𝐞

 Yesterday: the 18-step flow behind Karpathy's LLM Wiki pattern.
 Today: the engineering decisions underneath it.
 ---
 THE DEVELOPER ANALOGY

 RAG is like running grep across your codebase every time someone asks "how does auth work?" Raw match


 RAG is like running grep across your codebase every time someone asks "how does auth work?" Raw match



## 4/18 Saturday 
1. **data load tool (dlt): load data anywhere**
   1. https://dlthub.com/product/dlt
   2. https://www.datacamp.com/tutorial/python-dlt

1. **Cobrix**
   1. https://github.com/AbsaOSS/cobrix
   2. 

## 4/13 

1. [Data Architecture Patterns for Enterprise-Scale AI Adoption](https://medium.com/@uchit86/data-architecture-patterns-for-enterprise-scale-ai-adoption-69547f51f520)
2. [Deep Agents, code and check](https://pub.towardsai.net/langchain-just-released-deep-agents-and-it-changes-how-you-build-ai-systems-cc2371b04714)
3. [Claude / ClaudeCode / Skills](https://medium.com/@tort_mario/skills-for-claude-code-the-ultimate-guide-from-an-anthropic-engineer-bcd66faaa2d6)
4. [Claude / Claude managed agents][https://reliable-data-engineering.netlify.app/posts/article_claude_managed_agents/]
5. [AI PM](https://medium.com/agileinsider/ai-pms-at-netflix-dont-write-prds-here-s-what-they-actually-do-536e4e1f2ef0)
6. [Sam Altman / OpenAI](https://medium.com/predict/you-have-no-idea-how-screwed-sam-altman-really-is-7a66baaa5a5d)
7. [Read more : Causal Inference Methods](https://medium.com/@uvstharun183/%C3%A9-causal-inference-methods-every-data-scientist-should-know-72ea6d84ecc1)
8. [Anthropic / Mythos drama](https://dinmaybrahma.medium.com/opus-has-been-dethroned-meet-the-ai-that-even-anthropic-is-afraid-to-release-76803c6893f4)
9. [CDAIO / How to pick your data team](https://medium.com/@reliabledataengineering/building-a-data-team-from-0-to-10-what-wed-do-differently-2267292821e3)
10. [DataGeek / Research papers - data - 2026](https://medium.com/data-science-collective/6-research-papers-every-data-scientist-should-read-in-2026-eeb660fd2db1)
11. [DataWorkers / SQL Monkey to AI Architect](https://medium.com/predict/how-ai-is-reshaping-the-data-engineering-role-6081da17a28e)
12. [AIAgent / How to test - Google ADK](https://pub.towardsai.net/how-to-test-your-ai-agent-with-google-adk-so-it-doesnt-embarrass-you-in-production-096f5f6bb290)
13. [Enterprise + AI Data Platform](https://medium.com/@community_md101/ai-data-platform-for-enterprise-how-businesses-benefit-from-enterprise-ai-322a7c124dd2)
14. [AiDeveloper / 4 Observability Layers](https://pub.towardsai.net/4-observability-layers-every-developer-needs-for-production-ai-agents-a-complete-guide-24db9cbcb83c)
15. [AI Code Assistants for Data Engineering](https://medium.com/@reliabledataengineering/ai-code-assistants-for-data-engineering-i-tested-6-tools-for-sql-and-python-e20183f3154e)
16. [Can something be done with our code ? 10 GenAI Use Cases in ETL You Can Implement Today](https://medium.com/@Rohan_Dutt/10-genai-use-cases-in-etl-you-can-implement-today-0a5ba84dfc75)
17. [AI-powered-Enterprise-Data / Semantic layer - Data Ontology](https://pub.towardsai.net/ontology-the-hidden-layer-that-makes-ai-actually-work-875c3079fd55)
18. [AI-powered-Enterprise-Data / Context Engineering](https://medium.com/@reliabledataengineering/context-engineering-is-now-the-most-critical-data-engineering-skill-and-90-of-engineers-dont-166ac340beef)
    


## [Read Medium](https://medium.com/)
1. [Stop building dashboards](https://medium.com/dashboards-suck/stop-building-dashboards-what-high-impact-data-teams-do-instead-c36290240461)
2. [The Expert Way to Decide the Data Model for Any Data Engineering Problem](https://medium.com/@anchitgupt/the-expert-way-to-decide-the-data-model-for-any-data-engineering-problem-5ff383ba8bca)
3. [Why Parquet Is Not Enough Anymore](https://medium.com/@elalaouisara/why-parquet-is-not-enough-anymore-11ac121aa166)
4. [SQL Is Quietly Taking Over Data Engineering—Again](https://medium.com/towards-data-engineering/sql-is-quietly-taking-over-data-engineering-again-1dec44ca2c7d)
5. [Failed Uber’s System Design](https://medium.com/@emilyhustlenyc/i-failed-ubers-system-design-interview-last-month-here-s-every-question-they-asked-bdaf1bd6e64b)
6. [Anthropic Says Engineers Won’t Exist in a Year. It’s Also Paying Them $570K Today.](https://medium.com/@kanishks772/anthropic-says-engineers-wont-exist-in-a-year-it-s-also-paying-them-570k-today-5ee2a673f1ef)
7. [AI Is Reshaping Data Engineering in 2026](https://medium.com/expocomputing/how-ai-is-reshaping-data-engineering-in-2026-12291d2d1b76)
8. [7 Data & AI Predictions for 2026](https://medium.com/@salmabakouk/7-data-ai-predictions-for-2026-00d4211c62d8)
9. [Agile Is Dead. AI Killed It.](https://medium.com/@brian_carpizo/agile-is-dead-ai-killed-it-welcome-back-waterfall-e41bfabdd408)


## [Vanderbilt University]()
1. [AI Agents and Agentic AI Architecture in Python](https://www.coursera.org/learn/ai-agents-architecture-python#outcomes)
2. https://www.coursera.org/learn/ai-agents-architecture-python#outcomes


## [Ontology, Taxonomy, Data Model, Context Graph & Friends](https://medium.com/response42/ontology-taxonomy-data-model-context-graph-friends-56a605e14355)

1. We need an ontology-driven semantic layer feeding a context graph for the agent.
2. ontology is the meaning system: concepts + relationships + constraints

```
Customer: "A person or organization that can place orders"
Order: "A commercial transaction created by one Customer"
Product: "An item or service that can be purchased"

Rules:
 - "Order has exactly one Customer"
 - "Order contains at least one Product"
 - "ActiveCustomer = Customer with Order in last 90 days"
```

Ontology answers questions such as:
What counts as a Customer?
Can an Order exist alone? (No.)
What makes someone an Active Customer?
Use it for:

defining what things mean in your domain (Customer vs Prospect vs Active Customer)
documenting business rules
machine reasoning




3. Teams, Slack, Zendesk - Meet users team where they work
4. Agent Orchestration Platform - why do we need it? How does this work with A2A?  
5. Building the foundations for agentic AI at scale
   1. https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale

## Publish queue 

1. https://levelup.gitconnected.com/claude-code-just-released-a-feature-that-genuinely-scares-me-and-i-use-ai-every-day-4f23cd3051c0
1. Agentic addiction is a thing now. Too early 



## Columnar Formats (Parquet & Arrow)
Parquet for “Cold” disk storage
Apache Arrow for “Hot” in-memory processing
https://medium.com/@Rohan_Dutt/10-system-design-topics-every-data-engineer-is-expected-to-know-in-2026-interviews-d74dc4e3b1bb

Vectorized Execution: Modern CPUs can process an entire “vector” of values (e.g., 1024 integers) in a single instruction (SIMD). 

## Message Queues (Kafka vs. RabbitMQ vs. SQS Serverless Queue )

1. the choice usually sits between the Smart Pipe (RabbitMQ or SQS) and the Dumb Pipe, Smart Consumer (Kafka).
2. In Kafka, you can “rewind” your consumer to last Tuesday to re-calculate a metric. You cannot do this in RabbitMQ or SQS.
3. RabbitMQ excels when you need complex logic (e.g., “Send messages with header X to Queue Y”). Kafka expects the consumer to do the filtering.

## Consensus (Raft vs. Paxos)

1. Paxos was the original mathematical proof, 
2. Raft is the 2026 industry standard because it is easier to understand and implement.
   1. Embedded Consensus: Databases like CockroachDB and TiDB build Raft into their storage layer. 
3. In giant systems, the biggest risk is the **Split-Brain scenario** where two nodes both think they are the leader and make conflicting changes. 
4. Consensus algorithms prevent this by requiring a Quorum (a majority) for every decision. 
5. This is how Kubernetes maintains cluster state and how Amazon Aurora handles fast failovers.
6. The industry has moved away from using external consensus tools like Zookeeper.
7. KRaft (Kafka Raft): Kafka 3.x+ removed Zookeeper. It moved consensus logic inside the Kafka brokers. 
8. Embedded Consensus: Databases like CockroachDB and TiDB build Raft into their storage layer. 
9. Byzantine Fault Tolerance (BFT): Standard Raft assumes nodes are honest but might fail. 2026 interviews for high security or Web3 platforms often ask about BFT. This is a tougher type of consensus that handles nodes that are actively malicious or lying.

1. https://medium.com/@Rohan_Dutt/10-system-design-topics-every-data-engineer-is-expected-to-know-in-2026-interviews-d74dc4e3b1bb


## Idempotency & Exactly-Once Processing

1. https://medium.com/@Rohan_Dutt/10-system-design-topics-every-data-engineer-is-expected-to-know-in-2026-interviews-d74dc4e3b1bb
2. Idempotency ensures that performing an operation multiple times has the same effect as performing it once.
3. As we move toward event-driven architectures in 2026, the ability to handle retries gracefully via **Exactly-Once Semantics (EoS)** is what separates a junior script-writer from a senior systems architect.
4. This example demonstrates an idempotent “Sink” that uses a Hash-based Deduplication Store (simulated here with a set)

1. Upsert Logic: Using INSERT ... ON CONFLICT (SQL) or merge() (Delta Lake/Hudi) to ensure that late-arriving duplicates simply update existing records rather than creating new ones.
2. Stateful Processing: How **Apache Flink uses “Checkpoints”** to roll back the entire system state to a consistent point in time if a failure occurs.


## Data Contracts & Schema Evolution

1. https://medium.com/@Rohan_Dutt/10-system-design-topics-every-data-engineer-is-expected-to-know-in-2026-interviews-d74dc4e3b1bb

1. In 2026, “Data Contracts” have replaced manual QA and “broken pipeline” Slack alerts. 
2. A Data Contract is a formal agreement between a data provider and a consumer that defines the structure, quality, and semantics of the data being exchanged.
3. The biggest bottleneck in modern data platforms is “upstream drift” — when a backend engineer changes a database schema and unintentionally breaks a downstream dashboard. 
4. Data Contracts turn this “silent failure” into a “build failure,” preventing bad data from ever entering the warehouse.
   
5. **Pydantic-Based Contract Enforcement**
6. **Schema Registries**: Using **Confluent Schema Registry** or **AWS Glue** to enforce Avro/Protobuf schemas at the message-bus level.
7. **Contract-as-Code**: Storing contracts in **YAML or JSON within a Git repo** that both producers and consumers reference.
8. **Governance via CI/CD**: Running “Contract Compatibility” checks during a Pull Request to prevent merging breaking changes.

1. Observability-Driven Failover: Using Prometheus or OpenTelemetry signals to automatically trigger traffic redirection via Service Mesh (like Istio)
   

## Qwen 

1. https://medium.com/@stawils/qwen-just-quietly-became-the-most-dangerous-open-source-ai-model-b5bcf7b2743c
   

## SDLC pipeline 

1. https://medium.com/@brettluelling/sdlc-for-agentic-ai-engineering-5813abfdbc12


## If You Understand These 5 AI Terms, You’re Ahead of 90% of People

1. https://pub.towardsai.net/if-you-understand-these-5-ai-terms-youre-ahead-of-90-of-people-c7622d353319
   

## Semantic Layer in an Open-Source Architecture

1. https://medium.com/@grom_65116/semantic-layer-in-an-open-source-architecture-98fbbb0d0df3


## AI-ready data will be the biggest topic of 2026

1. https://barrmoses.medium.com/10-data-ai-predictions-for-2026-adf2750cccba
2. [I Spent 20 Years Building Data Warehouses. Here’s Why GenAI Just Changed Our Playbook.](https://medium.com/towards-data-engineering/i-spent-20-years-building-data-warehouses-heres-why-genai-just-changed-our-playbook-01fc14431881)




## Claude Code Channels

1. https://levelup.gitconnected.com/claude-code-just-released-a-feature-that-genuinely-scares-me-and-i-use-ai-every-day-4f23cd3051c0
2. Agentic addiction is a thing now. Too early 



## Semantic Layer, Ontologies, Knowledge Graph, Data Product

1. https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale
2. The semantic layer turns data into knowledge. 
3. It sits between raw data and AI applications and 
4. codifies the business meaning of data into a machine-readable form that humans can understand. 
5. Rather than treating data as disconnected tables or files, the semantic layer defines 
6. what things are, how they relate, and what rules govern them.
7. In practice, this layer is most often implemented through ontologies and knowledge graphs. 
8. Ontologies define how the attributes and relationships between data add up to business reality. 
9. Knowledge graphs operationalize this vocabulary by linking real-world data across systems into a connected network of entities. 
10. Without this shared semantic foundation, agents may act on incomplete or conflicting interpretations of the same data, increasing error rates and operational risk as scale grows.
11. Data products turn curated data into reusable, business-ready assets. 
12. They package data with **clear ownership**, **quality standards**, **semantics**, and **interfaces for consumption**. 
13. Through a product mindset, ( what is this ? )
14. companies treat data as a performance asset that can be reused across multiple use cases and domains. 
15. Reusable data products allow agents to draw on trustworthy predictive and generative insights at scale, 
   1. while observability records how agents use data, 
   2. creating the traceability needed for oversight and enabling feedback loops that improve upstream data and models.

## How to use Claude Code ? What can be done for Kiro ?  

1. Claude Code is an **Agent Orchestration Platform** in Disguise
1. After diving into the architecture, it’s clear: 
    1. this isn’t just an interface; 
    1. it’s developer infrastructure. 
    1. If you want to move from "chatting" to "automating," you need to understand the underlying engine.

1. **CLAUDE.md is your "System Prompt" on steroids**
    1. It’s loaded on every single turn, not just at session start. 
    1. With a 40K character budget, you should be using it for more than just style guides.
    1. The Hierarchy: Global → Project → Modular Rules → Local Notes.
    1. The Play: Use it to enforce architectural "never-do-this" rules and file conventions.

2. Parallel Agents are (virtually) free
    1. Because forked sub-agents share a **prompt cache via byte-identical context**, 
    1. running 5 agents costs roughly the same as 1. 
    1. The system is purpose-built for parallel workflows (fork/teammate/worktree).

3. Stop clicking "Allow"
    1. Stop the friction. There is a five-level permission cascade (policy > flag > local > project > user).
    1. Pro Tip: Configure your settings.json once. The system even uses an LLM classifier to decide if an action is safe in "Auto" mode.
    1. 

4. Master the 5 Compaction Strategies
1. Context pressure is the silent productivity killer. Claude Code uses five tiers of thinning: 
    1. Microcompact, 
    1. context collapse, 
    1. session memory, 
    1. full compact, and 
    1. PTL truncation.
1. The Play: Use /compact proactively as a "save point" before starting a new sub-task.

5. **Hooks**: The "Hidden" Extension API
   1. There are 25+ lifecycle events (PreToolUse, SessionStart, etc.).
   2. Automation: Use hooks to auto-inject test outputs, git diffs, or fresh documentation into every prompt without typing a word.


6. Sessions are Persistent JSONL
   1. Never start a "clean" session unless you have to. Use --continue.
   2. The session memory extracts task specs, errors, and learnings over time. 
   3. Starting fresh is like closing your IDE every hour you're throwing away your mental model.


7. Smart Tool Batching
The engine handles concurrent reads (parallel) vs. serial mutations (conflict-safe) automatically. Plus, MCP servers are loaded deferred—they cost zero tokens until the moment they are invoked.

8. Interruption is Free
Thanks to async generators, there is zero penalty for redirecting the model mid-stream. If you see it hallucinating, kill it immediately and pivot.

9. Built for Unsupervised Execution
With 10-tier exponential backoff, OAuth auto-refresh, and a 90s watchdog timer, this is designed to run in the background while you grab coffee.

The Takeaway: The 10x developers aren't better "prompters" they are better configurators. 
Claude Code is infrastructure, not just an interface. Stop chatting with it and start orchestrating it.


## Onyx - AI chat 
1. https://onyx.app/integrations
1. Summarize a thread at Teams. 
1. 
1. Claude only runs Claude models.
1. Onyx works with any LLM (Claude, GPT, Gemini, local models).
2. But does it have Cowork, Skills, Projects etc?
3. 
4. https://deepresearch-bench.github.io/
5. DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents
6. https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard


## Multi-Agent Architecture in AI: A Quick Read

In contrast to a single monolithic AI agent, a **multi-agent architecture** consists of multiple autonomous agents that interact, collaborate, or compete(??) to solve complex tasks. 
Each agent typically has a specialized role, local knowledge, and limited capabilities, yet together they achieve goals beyond any individual’s reach.

### How It Works
- Agents communicate via message passing, shared memory, or environmental signals.
- Coordination mechanisms include:
  - **Centralized** (one controller delegates tasks)
  - **Decentralized** (agents negotiate or use market-based protocols)
  - **Hierarchical** (higher-level agents manage lower-level ones)

### Key Benefits
- **Scalability & Robustness** – Add agents without redesign; failure of one doesn’t collapse the system.
- **Specialization** – Each agent excels at a narrow task (e.g., perception, planning, execution).
- **Resilience** – No single point of failure; agents can compensate for others’ errors.
- **Parallelism** – Agents act simultaneously, speeding up large workflows.

### Real-World Examples
- **Autonomous vehicles** – Lane-keeping, obstacle avoidance, and navigation agents working together.
- **Robotic swarms** – Search-and-rescue drones dividing areas and sharing discoveries.
- **Software development** – One agent writes code, another reviews, a third runs tests.
- **Trading systems** – Multiple agents tracking different markets and executing strategies.

### Common Challenges
- **Coordination overhead** – Communication and consensus can become expensive.
- **Emergent behavior** – Unpredictable outcomes from simple agent rules (may be good or bad).
- **Security & trust** – Malicious agents can disrupt the system; requires authentication and reputation mechanisms.
- **Debugging complexity** – Harder to trace failures across interacting agents.

### Popular Frameworks
- **LangGraph** – Graph‑based multi‑agent workflows.
- **AutoGen** (Microsoft) – Conversational agents for code, planning, and tool use.
- **CrewAI** – Role‑based agent collaboration with orchestration.
- **JADE** – FIPA‑compliant Java framework for classical multi‑agent systems.

### When to Use It
Multi‑agent architecture shines when tasks are **modular**, require **diverse expertise**, or need **geographic distribution**. 

### When NOT to Use It
For simpler, tightly coupled problems, a single agent may be more efficient.



## Link
1. https://www.linkedin.com/feed/update/urn:li:activity:7443846488708759553/?utm_source=share&utm_medium=member_desktop&rcm1. =ACoAAACOR8UB3zqZApJHm3jXnrFZcfmFgwNtOq4
1. What problems are you not solving today because you think they're unsolvable?
1. https://www.linkedin.com/posts/suman-biswas-63a3b262_autonomousai-aiagents-openclaw-share-7439355018161545216-8T-n?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACOR8UB3zqZApJHm3jXnrFZcfmFgwNtOq4
2. 𝐈𝐭'𝐬 𝐧𝐨𝐭 𝐭𝐡𝐞 𝐀𝐠𝐞𝐧𝐭𝐢𝐜 𝐞𝐫𝐚 𝐚𝐧𝐲𝐦𝐨𝐫𝐞. 𝐈𝐭'𝐬 𝐭𝐡𝐞 𝐀𝐮𝐭𝐨𝐧𝐨𝐦𝐨𝐮𝐬 𝐞𝐫𝐚.

## [OpenClaw](https://openclaw.ai/)



I think each of us is observing a major effort in shifting from #OpenAgents → #Guardrails → #TrustedAgenticAI. 

AI agents that can act across systems is becoming the new normal—but how do we define what “safe” means?

Solutions like NVIDIA NemoClaw introduce sandboxing, policy enforcement, and runtime controls— which I consider a critical step toward securing agent execution.

What are agent guardrails?
They define what agents can access and execute, enforcing boundaries across data, tools, and environments.

Where is the real challenge?
Guardrails control how agents act—but not fully why or whether they should:
• Who defines the right policies?
• How are they validated as conditions change?
• Who owns the outcome when agents make decisions?

Why it matters?
As agents move from automation → autonomy, security alone isn’t enough. The real challenge is governance, accountability, and continuous validation at scale.

The shift is clear: from “controlling agents” → “trusting and governing agent-driven decisions”, but is the governance catching up?


optimal architecture is no longer a single platform, 
but a composable, data-fabric-like layer built on three pillars: Open Formats, Semantic Context, and Agentic Interfaces.


1. **Open Table Formats (OTF):**
2. Apache Iceberg is the undisputed winner here. 
3. The current thinking is that proprietary storage formats (like those in legacy warehouses) are a liability for AI. 
4. AI models and engines (Pandas, Spark, Flink, TensorFlow) need direct access to data without vendor-imposed API bottlenecks. 
5. Iceberg provides the "universal connector."

6. **Separation of Storage & Compute:** 
7. This is no longer just about cost savings; it’s about elasticity for AI workloads. 
8. Training a large model requires bursting to thousands of GPUs for a short period. 
9. The platform must allow compute clusters to spin up, access petabytes of data via Iceberg, and spin down without locking storage.

10. **Unified Batch & Streaming:**
11. Current thinking holds that if your data platform isn't real-time (via Kafka, Pulsar, or Flink) but treats streaming as a separate silo, it will fail for AI. 
12. AI agents require "freshness" (context from the last 5 seconds), not just batch historical data.


**The Semantic Layer: The "Killer Component" for AI**
1. The biggest lesson learned from early AI adopters is that feeding raw data to AI models fails. 
1. Raw data lacks business context. 
1. The current thinking prioritizes the Semantic Layer as the central architectural component.

In the AI era, the Semantic Layer (implemented via tools like dbt, Cube, or embedded in platforms like Databricks or Snowflake) serves two critical functions:


**For Retrieval-Augmented Generation (RAG):** 
1. You cannot just dump a data lake into a vector database. 
1. The current best practice is to use the semantic layer to define units of knowledge. 
1. Instead of retrieving a row of a table, the platform retrieves a "business entity" (e.g., "Customer 404’s lifetime value, including churn risk calculated by our ML model").

**For Text-to-SQL/Agents:**
1. LLMs are terrible at guessing database schemas. 
1. The platform must expose a curated, well-documented semantic layer (a "knowledge graph") that tells the AI what columns mean, how tables join, and what the business definitions are.


**Governance: The "Agentic" Shift**
Governance used to be about preventing data breaches (RBAC). 
In the AI era, governance is about orchestrating machine identity.

Current thinking introduces **Agentic Governance**:

**Data Products:**
1. The "Data Mesh" concept (domains owning their data) has matured. 
1. The current best practice is that domains don’t just produce tables; 
1. they produce data products with SLAs, schemas, and
1. crucially—pre-approved AI endpoints. 
1. A marketing domain doesn't just give access to a table; 
2. they expose a "Marketing Insights API" that the central AI agent can call.

**Vector Database Governance:**
1. A major headache currently is the proliferation of "shadow vector databases" where engineers embed proprietary data into vectors and lose lineage. 
1. The current thinking mandates that vector stores (Pinecone, Milvus, or native platform features) must be integrated into the central data platform’s governance framework to prevent "AI data sprawl."
   

**The Platform Engineering Layer**
For the last decade, enterprises built "self-service" platforms for data analysts (SQL). 
For the AI era, the platform must serve three distinct personas equally well, which requires a new level of sophistication:

1. **The Data Engineer**: Needs Git-like workflows, 
   1. CI/CD for data (Dagster, Airflow, or Prefect), and 
   2. declarative infrastructure (Infrastructure as Code).
2. **The Data Scientist/ML Engineer**: 
   1. Needs native access to GPUs, 
   2. feature stores (Feast or Tecton) to prevent training/serving skew, and 
   3. model registries. 
   4. The feature store must be inside the data platform, not a separate tool, to ensure the features used in training are the same ones served in real-time inference.
3. **The Application Developer (The New King)**: In the AI era, data platforms are no longer just for BI dashboards. 
   1. They are backend infrastructure for production applications. 
   2. Therefore, the platform must expose APIs first. 
   3. The current best practice is to treat the data platform as a "backend for AI agents," 
   4. providing low-latency APIs (gRPC or REST) for vector search, real-time features, and semantic lookup.

**The "Unstructured" Mandate**
1. Traditional platforms focused on structured (rows/columns) and semi-structured (JSON) data. 
1. AI is fueled by unstructured data (PDFs, videos, audio, code).
1. Unify Structured and Unstructured: It cannot be a data warehouse and a separate document store. The best modern platforms (Databricks, Snowflake, Google BigQuery) now treat unstructured data as a first-class citizen, allowing you to store blobs and run inference (via built-in AI functions) directly on them without moving the data.
1. Built-in Embedding Generation: The platform must handle the vectorization pipeline. The current preference is for platforms that can take a PDF, chunk it, call an embedding model (hosted or local), and store the vector inside the governed platform rather than exporting data to an external vector database.


## Summary of Best Practices AI ready Data Platform for 2025-2026

1. Storage: Adopt Apache Iceberg as the single standard for all tabular data. Insist on open formats to avoid vendor lock-in for AI workloads.
1. Compute: Implement a multi-engine architecture. Use Spark for ETL, Trino for federated queries, and GPU clusters for training, all reading from the same Iceberg tables.
2. Semantics: Invest heavily in a semantic layer (dbt + a metric store) before deploying AI agents. If your AI agents don’t have a glossary, they will hallucinate business logic.
3. Vectors: Do not create a separate "AI database." Use vector search capabilities within your primary data platform or a tool that integrates tightly with your Iceberg catalog to maintain lineage and governance.
4. Agents: Shift from building dashboards to building APIs. Your data platform’s success in the AI era will be measured by how many production applications (powered by AI agents) are calling its APIs, not by how many Tableau reports are running on it.

In short: the best enterprise data platform for the AI era is no longer a database; it is an operating system for data that manages the lifecycle from raw blob to semantic API, with open formats as its kernel and governance as its security model.

**The Vendor Landscape (The "Bifurcation")**

1. **The Open Ecosystem (Databricks)**: The prevailing wisdom for mature tech companies or those with strong engineering teams is to build on Databricks using Apache Iceberg (via their acquisition of Tabular) and Unity Catalog. 
1. The logic is control, open formats, and best-in-class MLflow for the AI lifecycle.

**The Managed Polaris (Snowflake):** For enterprises with less engineering bandwidth or those heavily invested in SQL, 
1. Snowflake is the current choice. 
1. Their strategy revolves around Snowpark (for Python/ML) and Cortex (AI functions). 
1. The current critique is that while Snowflake is easier to manage, the "openness" of Iceberg interoperability is still evolving compared to the Databricks stack.


**Why This Architecture Works for Financial Institutions**
1. No vendor lock‑in – Iceberg + Polaris means you can switch from Snowflake to Databricks to Trino without rewriting pipelines. Regulators require long‑term data retention; open formats guarantee you are not trapped.
1. AI‑native from the start – The vector store, feature store, and LLM serving all read the same Iceberg tables. No exporting data to “AI silos.”
1. Strong governance – The unified catalog enforces policies across all engines, including GPU clusters. Auditors see a single source of truth for both data and AI artifacts.
1. Legacy integration – CDC captures mainframe changes into Iceberg without stopping core banking systems.
1. Real‑time + batch unified – Flink writes streaming results to Iceberg tables, which are immediately available for Spark or Trino. No lambda architecture duplication.


## Plumery introduces AI Fabric for AI-ready core banking

1. https://ibsintelligence.com/ibsi-news/plumery-introduces-ai-fabric-for-ai-ready-core-banking/
2. 

## GoodData Brings AI-Native Data Intelligence to Financial Services

1. https://www.gooddata.com/press-releases/gooddata-brings-ai-native-data-intelligence-to-financial-services/
2. 

## Building Agentic GraphOS: The 16-Layer Architecture Behind Production-Ready Knowledge Graphs

1. https://medium.com/@aiwithakashgoyal/building-agentic-graphos-the-16-layer-architecture-behind-production-ready-knowledge-graphs-9ca632bc74c5

## Build time-aware knowledge graphs with Temporal Agents 

1. https://medium.com/@aiwithakashgoyal/temporal-agents-in-graphos-building-time-aware-knowledge-graphs-with-multi-level-ingestion-ee448441929c
2. 



## Spec-Driven-Development 

1. [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)
2. 


## Context Engineering

1. [Context Engineering: The Next Evolution in Prompt Design](https://medium.com/@tahasamavati/context-engineering-the-next-evolution-in-prompt-design-3bf68d1de841)

A few years ago, many predicted that prompt engineering would quickly become obsolete. 
Instead, it evolved and grew more essential, giving rise to context engineering 
Context engineering — a broader, richer discipline that optimizes not just prompts, but the entire context an AI model sees: instructions, inputs, tools, memory, and relevant history. 
Context engineering is about systematically architecting this environment so models deliver reliable, useful results — on the first try.

Prompt engineering isn’t merely “asking questions.” 
It’s the practice of carefully designing, structuring, and refining instructions to shape how AI responds. 
Context engineering expands on this by architecting all relevant context — tool definitions, schemas, temporal grounding, memory, and application state — so the model has exactly what it needs, in the form it needs it.


**What Exactly Is Context Engineering?**

1. Context engineering is the iterative process of 
1. crafting, optimizing, and testing the inputs provided to AI systems, 
1. ensuring they have precisely the information they need, 
1. structured in the right way, at the right time, to perform their tasks effectively. 

1. This includes:
   1. Structuring inputs and outputs (e.g., JSON Schema, Pydantic/dataclasses)
   2. Managing dynamic elements (user inputs, dates, locales, feature flags)
   3. Utilizing Retrieval‑Augmented Generation (RAG) and long‑term memory
   4. Tool integration (function calling) with schema‑validated inputs and constrained outputs
   5. Handling historical context and application state, plus evaluation signals
   6. Essentially, you’re not just writing prompts; you’re designing the operating environment your model works in.


1. [Context Engineering for Agents Jun 23, 2025](https://rlancemartin.github.io/2025/06/23/context_engineering/)
3. LLMs are like a new kind of operating system. 
4. The LLM is like the CPU and its context window is like the RAM, 
   1. serving as the model’s working memory. 
5. Just like RAM, the LLM context window has limited capacity to handle various sources of context. 
6. And just as an operating system curates what fits into a CPU’s RAM, “context engineering” plays a similar role. 
8. What are the types of context that we need to manage when building LLM applications? 
9. Context engineering is an umbrella that applies across a few different context types:
   1. Instructions – prompts, memories, few‑shot examples, tool descriptions, etc
   2. Knowledge – facts, memories, etc
   3. Tools – feedback from tool calls









**Context engineering is curating what the model sees so that you get a better result.**

Context engineering is the systematic, iterative process of designing, managing, and optimizing the information (data, instructions, tools) provided within an LLM's context window to improve task performance. Often considered an evolution of prompt engineering for AI agents, it ensures the model receives precise, relevant data to avoid context rot and enhance reliability. 

1. https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
2. Context Engineering for Coding Agents
3. How about context engineering for chatbots with specialized domains. 





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