

Stop Reading About Ontology. Start Building One.
https://medium.com/@cloudpankaj/building-your-first-ontology-a-hands-on-tutorial-2cdd08bc2e02

owl-portability-layer
https://github.com/cloudbadal007/owl-portability-layer

The Enterprise AI Ontology Roadmap: 30+ Articles, 4 Learning Tracks, and Where to Start
https://medium.com/@cloudpankaj/the-enterprise-ai-ontology-roadmap-30-articles-4-learning-tracks-and-where-to-start-22efc17bb026

OntoGuard: I Built an Ontology Firewall for AI Agents in 48 Hours Using Cursor AI
https://pub.towardsai.net/ontoguard-i-built-an-ontology-firewall-for-ai-agents-in-48-hours-using-cursor-ai-be4208c405e7

Visualize your ontology: Try WebVOWL — upload your .owl file and see your ontology as an interactive graph
http://www.visualdataweb.de/webvowl/


IRI (Internationalized Resource Identifier)
RDF (Resource Description Framework) 



Learn SPARQL: The query language for knowledge graphs. It’s like SQL for ontologies and incredibly powerful.
Connect to a triple store: Load your ontology into Apache Jena or GraphDB Free Edition to query it programmatically.
Build a simple app: Create a basic web interface that queries your ontology and displays results.

1. **SPARQL** (pronounced "sparkle") is the standard W3C-endorsed query language used to retrieve and manipulate data stored in RDF (Resource Description Framework) format. 
SQL for graph databases and Semantic Web technologies
SPARQL operates on RDF data structured as "triples": Subject, Predicate, and Object. (e.g., “Tim Berners-Lee — created — the World Wide Web”). 
Variables are used as wildcards (e.g., ?person created ?invention) 
SELECT: Retrieves values from the database, returning them in a tabular, row-and-column format.
ASK: Checks if a certain pattern exists in the data, returning a simple true or false.

1. **Use cases of SPARQL**
   1. Knowledge Graphs: Querying highly interconnected datasets (e.g., querying data from Wikidata Query Service).
   2. Linked Data: Navigating and joining distributed datasets across the web.
   3. Semantic layer ??? 

1. **Implementation**
   1. Apache Jena (a free, open-source Java framework)GraphDB (by Graphwise/Ontotext)OpenLink Virtuoso

SPARQL 1.1 Query Language
W3C Recommendation 21 March 2013




Scan the schema registy - weekly ? 
capture the versions 
messages my have a older version of the schema registry (??)

schema id - can change 

1. Ontology vs. Knowledge Graph vs. Taxonomy — clearing up the confusion once and for all
2. Integrating your ontology with Python — making it part of real applications
3. Advanced reasoning techniques — property chains, disjointness, cardinality restrictions

Connect to a triple store: Load your ontology into Apache Jena or GraphDB Free Edition to query it programmatically.

**Apache Jena** A free and open source **Java framework** for building Semantic Web and Linked Data applications.

**GraphDB Free Edition** A powerful RDF database that allows you to store and query your ontologies with SPARQL.


https://kiran-pothina.medium.com/i-built-an-agentic-ai-platform-for-snowflake-heres-every-architectural-decision-and-why-d97aae25b5a8


LangGraph · pgvector · dbt semantic layer · Claude Sonnet ·
query fingerprinting · warehouse cost optimisation · Docker Compose

**SnowSense** an AI agent that answers natural language questions about Snowflake data, understands business semantics through dbt, and automatically routes queries to the optimal warehouse to minimise cost.

**LangGraph vs. a while true loop** 

multi-turn conversation continuity with zero extra code. ( what is multi-turn conversation ?? )


ChromaDB is a pure vector database. 
pgvector is a PostgreSQL extension — which means your embeddings live in a relational database and can be joined with other tables in a single query.
pgvector is fully free and open-source (PostgreSQL licence). It runs in Docker via pgvector/pgvector:pg16. No managed service, no API cost.


SOR - ingesting - kafka topic 
RLV - row level validation 

SOR file based 
DB based 
Kafka / file based - 

Schema Registry kafka - meta data   
scan the kafka 


https://kiran-pothina.medium.com/i-built-an-agentic-ai-platform-for-snowflake-heres-every-architectural-decision-and-why-d97aae25b5a8

1. Why dbt instead of native text2sql feature implemented in Cortex Analyst with native semantic models purposely built for SQL? 
2. Why pgvector instead of native vector data type in Snowflake? You can build RAG natively and evaluate it as well using **trulens**.
3. Why all-MiniLM-L6-v2 instead of native **Arctic model** for embedding?
4. Why docker-compose instead of hosting everything in **spcs**?
5. **Checkpointing** can be built natively via Snowflake tables, as well as Streamlit app.
6. No container restart needed if agent works in **spsc**, just to refresh oauth token after wake-up.
7. I like the idea with dynamic query routing, but how it fits with **native adaptive warehouse feature** which is currently in preview? 
8. Instead of routing queries across WHs, it automatically adjusts compute for a given query.
9. If everything would run in Snowflake you can get logging ootb, in worst case wrap you langgraph calls with otel sdk, or even build using **native snowflake agents** (no langgraph), you can achieve basically the same react loop with reasoning with all telemetry natively stored in snowflake tables with ootb observability dashboards. 
10. You can also build a custom skill for cortex code right in Snowflake and the cortex code UI will work exactly like your Streamlit app, so no need for Streamlit app at all.


[Microsoft Just Shipped Two Semantic Layers. One of Them Is Quietly More Powerful Than Fabric IQ](https://medium.com/@cloudpankaj/microsoft-just-shipped-two-semantic-layers-one-of-them-is-quietly-more-powerful-than-fabric-iq-92e2c630a0ef)

1. Microsoft enterprise semantic layer - Fabric IQ 
1. Ontology Items. 
1. Semantic contracts. 
1. Permitted actions. 
1. DirectLake bindings.

Dataverse as an Agent Data Platform
**Dataverse Search** is now enriched with an intelligent semantic layer that 
understands the business data schema and adds true business data understanding for agents to operate.
It is useful for very organization running Dynamics 365, Power Apps, Power Platform, Microsoft 365 Copilot — which is essentially every Microsoft enterprise customer.
Dataverse adds a **managed vector index** and **semantic search**


If your data isn’t in OneLake in DirectLake format, you’re not using Fabric IQ’s semantic layer.


## TruLens 

1. **TruLens** is an open-source library for evaluating and tracing LLM and RAG applications.
2. Measures quality, compares models, and logs metrics
3. Collects metrics, traces, and evaluations for transparency and benchmarking
4. Surfaces problems like bias, hallucinations, and latency
5. Follows modern standards such as **OpenTelemetry**
6. Snowflake acquired core TruEra, the creators of TruLens, in May 2024
7. [AI Observability with TruLens and Snowflake](https://sarathi-data-ml-cloud.medium.com/ai-observability-with-trulens-and-snowflake-5d1968a9e7a0)
8. [github : AI-Observability-TruLens-Snowflake](https://github.com/sarathi-aiml/AI-Observability-TruLens-Snowflake)




