---
layout: post
title: Rough Notes
categories: [notes] 
---

### Free AI courses 

1. https://academy.genai.works/free-courses-ai
2. Before you begin, ask any questions that you might need to have clarification on. 
3. 

### Free Claude course : Claude Code 101 

1. **Claude code is an Agentic coding assistant** 
2. https://academy.claude.com/courses/claude-code-101/what-is-claude-code
3. It can access the web - e.g. to look up on the latest documentation of an API (can it?? how to check??)

4. context memory - it can hold a lot but not infinite. 
   1. This is the agentic part - it does not hold the entire codebase in memory 
   2. 
```
/context 
```

1. **Free lesson : How Claude Code works**
2. https://academy.claude.com/courses/claude-code-101/how-claude-code-works
3. The Agentic Loop 
4. You prompt - it springs into action, does something, checks if it is done 
   1. If not done it does the thing all over again. 
   2. Through these iterations, it leaarns itself, and / or takes inputs from human operator 
5. Context window 
   1. The note book as it interacts with external world. 
   2. Once it is almost full it /compacts the conversation. 
6. Tools 
   1. Read file tool 
   2. Search web tool etc. 
7. Permissions 
   1. Plan mode - read only 
   2. Auto - write to files, but ask before running a shell command. 
   3. 


### full stack data and ai engineer 

A Full-Stack Data and AI Engineer builds, deploys, and maintains end-to-end intelligent systems, managing everything from raw data pipelines and machine learning models to user-facing applications.Core ResponsibilitiesData Engineering: Ingest, clean, store, and process structured and unstructured data using ETL/ELT pipelines, SQL, and vector databases.AI & Machine Learning: Develop, fine-tune, and integrate classical ML models or Large Language Models (LLMs), Retrieval-Augmented Generation (RAG) systems, and multi-agent workflows.Backend & MLOps: Serve models via scalable APIs (FastAPI, Flask) and manage production environments using containerization (Docker, Kubernetes) and CI/CD pipelines.Frontend & UX: Build AI-driven user interfaces or integration layers so end users can interact seamlessly with the underlying intelligence.Essential Tech StackLanguages: Python, advanced SQL, TypeScript/JavaScript.Data & Databases: Snowflake, Apache Airflow, PostgreSQL, and vector databases (Pinecone, Chroma, Milvus).AI Frameworks: LangChain, CrewAI, Vercel AI SDK, PyTorch, Hugging Face.DevOps & MLOps: Docker, Kubernetes, MLflow, Git, AWS/GCP/Azure.


### GPT-6 Astra just ended software.

1. https://michalmalewicz.medium.com/gpt-6-astra-just-ended-software-e6047997b667
2. OpenAI has released their latest Astra model.
3. AGI is finally here
4. Sol was OUR star. Astra is “all the stars”
5. The SaaS MRR model(???) is dying as more and more users look for one-time payment alternatives
6. Amazon has had 4 (Sev-1) outages in just one week between February and March of 2026. Their memos showed “AI-assisted” code changes as the primary culprit.
7. A six-hour outage cost them around $6.3M in orders lost. It was a deploy that went live with no approval or even documentation.
8. The 2024 Sonos app rewrite was utterly broken when it went live. Took a year of fixes and tens of millions of dollars. They even kicked out the CEO. Many disgruntled users never came back to the brand.
9. Vibe coding resulted in an 84% jump in new Apple App store submissions in a single quarter. It was the largest bump in a dacade.
10. AI coding is mesmerizing if you know software architecture. 
11. I installed Omarchy linux (???) on it and the laptop has gained a new life. It’s also “agentic” now, with AI deeply embedded into the OS.
12. 

### Databricks introduced a new database that could change everything
1. **May 2025**, Databricks **acquired Neon**, the company that provides serverless Postgres
2. **Databricks introduced Lakebase**, a serverless, Postgres-compatible transactional database architecture that separates compute from storage to enable low-latency applications and AI agents.
3. PostgreSQL is an **OLTP (Online Transaction Processing)** DB. 
4. **High Concurrency**: To support thousands of users and processes simultaneously reading and writing data without interfering with each other.
5. **High Throughput for Writes**: To quickly process a large volume of minor, frequent updates, inserts, and deletes.
6. most OLTP systems manage data in a row format (records are stored next to each other)
7. A database page is the I/O unit created and managed by the database software itself. 
8. A page contains metadata, actual data, or indexes, and it usually doesn’t include a mix of data types (e.g., a page for data only or a page for indexes only)
9. When the database needs to read data, it doesn’t fetch a single row from the disk; it reads the entire page containing that row into memory. 
10. Likewise, when it writes data, it writes the whole modified page back to disk.
11. **Problem with Write** / **Write Ahead Log (WAL)**
12. When you modify data, the affected page is brought into memory, changed there, and eventually flushed back to disk. 
13. But memory is volatile; if the machine crashes before that flush happens, the change is gone.
14. OLTP databases such as PostgreSQL use a Write-Ahead Log (WAL) to provide durability
15. WAL is a separate, append-only structure on disk
16. PostgreSQL acknowledges a commit as soon as the change is durably in the WAL; it doesn’t wait for the actual page to be written back to disk at all. 
17. **What is Databricks trying to achieve with Lakebase**
18. Has compute and storage separate.
    1.  The first one is to leverage object storage for the storage layer.
19. Stores data in an “open“ format to enable interoperability.
20. Has the ability to “branch out“
21. Reference 
    1.  https://blog.dataengineerthings.org/databricks-introduced-a-new-database-that-could-change-everything-99e24709846f
    2.  https://www.databricks.com/blog/object-storage-wal-lakebase-postgres-agentic-era
    3.  https://www.vldb.org/pvldb/vol19/p4385-pandis.pdf



### From Messy Data Models to Agentic Data Catalogs

1. [Building an AI Data Architect with OKF and Gemini](https://medium.com/google-cloud/from-messy-data-models-to-agentic-data-catalogs-building-an-ai-data-architect-with-okf-and-gemini-75a20caee9ed)
1. Can we do the same without using Gemini ??

## MCP is Dead 
1. Do not use MCP 
2. Use direct CLI + direct API call instead. 
3. (??) How to interact with Collibra w/out MCP server from Claude. 
4. https://uxplanet.org/mcp-is-dead-cf16b667ba6d





5.  https://jamwithai.substack.com/p/pre-rag-era-building-an-end-to-end


## GenAI / Links 

1. [Emerging Patterns in Building GenAI Products](https://martinfowler.com/articles/gen-ai-patterns/)

## GenAI / Courses 

1. [The Hugging Face AI Agents Course](https://huggingface.us17.list-manage.com/subscribe?u=7f57e683fa28b51bfc493d048&id=9ed45a3ef6)

## GenAI / basics 

1. What is Temperature? 
1. What is Max Tokens? 
1. What is Top P? 
1. Explain "!pip install ..". 



## GenAI / OpenAI / Getting started with OpenAI client library. 


## GenAI / Groq 

1. [Getting strated](https://console.groq.com/docs/overview)
1. [Welcome to the Groq Console - Getting Started](https://www.youtube.com/watch?v=Ig7esRBhFPY&t=7s)
1. What am I building ? 





1. Unity Catalog. Unified and open governance for data and AI. #databricks [link](https://www.databricks.com/product/unity-catalog)
1. Photon. The next generation engine for the Lakehouse. #databricks [link](https://www.databricks.com/product/photon)
1. mlflow. Build better models and generative AI apps on a unified, end-to-end, open source MLOps platform. #databricks [link](https://mlflow.org/#core-concepts)
1. Data Sharing. Open data sharing for data, analytics and AI. [link](https://www.databricks.com/product/delta-sharing)
1. Delta Live Tables. data pipelines. declarative ETL framework. #databricks. [link](https://www.databricks.com/product/delta-live-tables)

1. crewai [AI Agents reimagined for enterprises](https://www.linkedin.com/company/crewai-inc/) with 2-10 employees
1. [A No-Code Assistant to BUILD A Crew!](https://www.youtube.com/watch?v=0XX7cx0pk54)
1. Enhancing customer support with Claude at Coinbase [link](https://www.anthropic.com/customers/coinbase)
1. These tools are designed to run locally on your machine without requiring expensive GPU resources. They can also run offline, without any internet connection. [smol-tools](https://github.com/huggingface/smollm/tree/main/smol_tools#smol-tools)
1. What is the sate of AI agents. [link](https://www.langchain.com/stateofaiagents)
1. AI agents to help with UX. [link](https://uxdesign.cc/treating-ai-agents-as-personas-6ef0135bdcad)
1. Amazon Bedrock Agents. Tutorial by Amazon. [link](https://aws.amazon.com/blogs/machine-learning/deliver-personalized-marketing-with-amazon-bedrock-agents/)

## What are the most common LLMs. 

1. OpenAI’s GPT, Google Gemini, or Anthropic’s Claude.

## Agent vs. LLM 

1. The difference between an agent and a language model is that agents complete task autonomously.≈


## [Building effective agents](https://www.anthropic.com/research/building-effective-agents)

## AI agents 

1. [Building effective agents](https://www.anthropic.com/research/building-effective-agents)
1. [OpenAI has released a new open-source framework called "Swarm" on GitHub.](https://the-decoder.com/openai-introduces-experimental-multi-agent-framework-swarm/)


## MLflow 

1. AWS SageMaker introduced fully Managed MLflow 

## dbt 

1. https://www.getdbt.com/product/what-is-dbt
1. dbt is the industry standard for data transformation. 
1. Transform raw data into analysis-ready insights, and make data-driven decisions with confidence.
1. DataOps - ?? 
1. Trace lineage across domains 
1. [ebook - Guide to data mesh](https://8698602.fs1.hubspotusercontent-na1.net/hubfs/8698602/Guide%20to%20data%20mesh%20eBook%20V2.pdf)
1. [certification - dbt](https://www.getdbt.com/dbt-certification)


## courses 

1. Machine Learning in Production
1. https://www.deeplearning.ai/courses/machine-learning-in-production/
1. https://www.coursera.org/learn/introduction-to-machine-learning-in-production?specialization=machine-learning-engineering-for-production-mlops?utm_source=deeplearning-ai&utm_medium=institutions
1. https://www.coursera.org/learn/introduction-to-machine-learning-in-production/lecture/uoVS1/welcome 
1. 3K for certificate 


