---
layout: post
title: MCP Toolbox for Databases 
categories: [MCP Toolbox for Databases] 
---

## Move to own page : MCP Toolbox for Databases (v0.26.0+) - we need a deep dive in this one. 

1. [Building Semantic Search into Your AI Agents](https://medium.com/google-cloud/building-semantic-search-into-your-ai-agents-d72349496340)

1. **What is semantic search?** Identifying information through text similarity rather than relying on exact keyword matches

2. MCP Toolbox for Databases (v0.26.0+) introduces **Embedded Parameters**
By integrating embedding models directly into the tool-calling workflow, MCP Toolbox can now automatically transform natural language into high-dimensional vectors, streamlining powerful similarity searches across your data

1. typical Retrieval-Augmented Generation (RAG) workflow
2. manually handle the text embedding step
   1. taking a user’s query, 
   2. sending it to an API like Gemini, 
   3. retrieving the resulting vector, and 
   4. finally incorporating that vector into a SQL query.

3. Do this automatedly using **Embedding Model resource**
4. Right now it supports only **Gemini embedding models**. Hence dropped for now. Come back later. 

