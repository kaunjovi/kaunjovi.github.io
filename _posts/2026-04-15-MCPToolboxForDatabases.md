---
layout: post
title: MCP Toolbox for Databases 
categories: [MCP Toolbox for Databases] 
---

## MCP Toolbox for Databases (v0.26.0+) 

1. Risk : No support for Snowflake ?? Really. Non starter then. Check. 

2. Ref : [MCP Toolbox for Databases in Action](https://www.youtube.com/watch?v=hVZbzd2sMic)

3. **MCP (Model Context Protocol)** : Standardized way for AI agents to communicate with tools. 
4. Helps your AiAgents utilize Enterprise Data. 

5. there is a client SDK and support for LangGraph(??) and LlamaIndex(??)

6. Supports a broad number of databases from the **Google cloud**. 

7. Some of the best practices for XXX 
   1. Connection pooling ( already done in MCP toolbox)
   2. Integrated authentication methods. 
   3. built in OpenTelemetry(??) support. 
   4. Tools(??) are in a centralized location ( lookup ) allowing to be reused. 
   
8. MCP clients - IDE, ADK (??)
9. Talks to MCP toolbox ( server for the defined db capabilities )
10. Talks to different databases. 

11. Example query **Forecast liquor sales**
12. agent needs to "understand" this "english" 
13. then figure out how to get the forecast 
14. Ther are tools in the toolbox ( where are the definition of the tools ? in a config file, tools.yml )

15. **ADK'S forecasting UI**
16. Type in the forecasting request 
17. The agent comes back and asks - in english - about constraints, like the time horizon
18. And then based on the response, runs the query and presents back - again in plain english - the findings. 





4. [Building Semantic Search into Your AI Agents](https://medium.com/google-cloud/building-semantic-search-into-your-ai-agents-d72349496340)

5. **What is semantic search?** Identifying information through text similarity rather than relying on exact keyword matches

6. MCP Toolbox for Databases (v0.26.0+) introduces **Embedded Parameters**
By integrating embedding models directly into the tool-calling workflow, MCP Toolbox can now automatically transform natural language into high-dimensional vectors, streamlining powerful similarity searches across your data

1. typical Retrieval-Augmented Generation (RAG) workflow
2. manually handle the text embedding step
   1. taking a user’s query, 
   2. sending it to an API like Gemini, 
   3. retrieving the resulting vector, and 
   4. finally incorporating that vector into a SQL query.

3. Do this automatedly using **Embedding Model resource**
4. Right now it supports only **Gemini embedding models**. Hence dropped for now. Come back later. 

