---
layout: post
title: Snowflake MCP Server
categories: [Snowflake-Managed MCP Server, Composio, LlamaIndex] 
--- 

## Snowflake-Managed MCP Server 
1. [Documentation of Snowflake-managed MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp)
1. Alternative to Google's MCP Toolbox for Databases
2. Native Tools: Directly exposes Snowflake-specific services such as 
   1. **Cortex Analyst** : for natural language to SQL. Using the Analyst tool, your client can generate SQL from natural language text. 
   2. **Cortex Search** : perform unstructured search (what-is-that??) on their data. 
   3. Cortex Agents 
3. Direct SQL Execution: Includes a SYSTEM_EXECUTE_SQL tool for running LLM-generated SQL statements.
   1. **SQL execution tool** : 
   2. read_only: When set to true, only read operations (SELECT queries) are allowed. Defaults to false.
   3. query_timeout: Maximum time in seconds for query execution.
   4. warehouse: The warehouse to use for query execution. If not specified, the default warehouse is used.
4. Managed Infrastructure: Hosted within Snowflake


## MCP url
 
1. https://<account_URl>/api/v2/databases/{database}/schemas/{schema}/mcp-servers/{name}


## Composio - https://composio.dev/toolkits/snowflake
1. Snowflake Integration for AI Agents
2. [Quickstart with Composio](https://docs.composio.dev/docs/quickstart)

## LlamaIndex is an AgentSDK like Claude Agents SDK


```
CREATE [ OR REPLACE ] MCP SERVER [ IF NOT EXISTS ] <server_name>
  FROM SPECIFICATION $$
    tools:
      - name: "product-search"
        type: "CORTEX_SEARCH_SERVICE_QUERY"
        identifier: "database1.schema1.Cortex_Search_Service1"
        description: "cortex search service for all products"
        title: "Product Search"

      - name: "revenue-semantic-view"
        type: "CORTEX_ANALYST_MESSAGE"
        identifier: "database1.schema1.Semantic_View_1"
        description: "Semantic view for all revenue tables"
        title: "Semantic view for revenue"

    - title: "SQL Execution Tool"
        name: "sql_exec_tool"
        type: "SYSTEM_EXECUTE_SQL"
        description: "A tool to execute SQL queries against the connected Snowflake database."
        config:
            read_only: false
            query_timeout: 600
            warehouse: "WAREHOUSE"

    - title: "Agent V2"
        name: "agent_1"
        type: "CORTEX_AGENT_RUN"
        identifier: "db.schema.agent"
        description: "agent that gives the ability to..."
  $$
```


```
SHOW MCP SERVERS IN DATABASE <database_name>;
SHOW MCP SERVERS IN SCHEMA <schema_name>;
SHOW MCP SERVERS IN ACCOUNT;
DESCRIBE MCP SERVER <server_name>;
DROP MCP SERVER <server_name>;
```


