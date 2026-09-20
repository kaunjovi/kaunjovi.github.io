## Assume 
1. Usage of Claude as VSCODE plugin. 
2. Assume usage of Snowflake-Managed MCP Server only. 
3. Assume dev environment is Windows and it is preferrable to leverage environment variables for storing sensitive informaiton like Environment Variables. 
4. 

## Question : 
When Claude calls the Snoflake managed MCP server, it is backed by a Cortex Agent. So, the call is first intercepted and worked up by the Cortex Agent and then further analysed by Cortex agent. This makes the process slow and costly. How do we handle something like this. 



## Set Windows Environment Variables
1. Press Win + R, type sysdm.cpl, and press Enter.
2. Go to the Advanced tab → Environment Variables.
3. Under User variables, click New.
4. Set Variable name to SNOWFLAKE_PAT and Variable value to your token.
5. Click OK and restart VSCode for the variable to take effect.



Create or edit .vscode/mcp.json in your project:


```json
{
  "mcpServers": {
    "snowflake-managed": {
      "type": "sse",  
      "url": "https://<account_url>/api/v2/databases/<database>/schemas/<schema>/mcp-servers/<server_name>",
      "headers": {
        "Authorization": "Bearer <YOUR_PAT_TOKEN>"
      }
    }
  }
}
```

## .vscode/mcp.json

```json 
{
  "servers": {
    "snowflake-managed": {
      "type": "http",
      "url": "https://<account_url>/api/v2/databases/<database>/schemas/<schema>/mcp-servers/<server_name>",
      "headers": {
        "Authorization": "Bearer ${env:SNOWFLAKE_PAT}"
      }
    }
  }

```


## Security & Auditing Best Practices

1. Use the Least-Privileged Role: When creating your PAT, bind it to a role with only the minimum permissions required (e.g., SELECT on specific views/tables). This prevents leaking a secret with access to a highly-privileged role.
2. Apply a Network Policy: Restrict PAT usage to specific IP addresses by applying a network policy to the user. For human users (TYPE=PERSON), they must be subject to a network policy to authenticate with the token.
3. Enforce Read-Only Access: If using a community server like @bossforce.ai/mcp-snowflake that cannot enforce read-only at the server level, ensure the database role bound to the PAT has only SELECT permissions.
4. Use Environment Variables: Store the PAT in environment variables (as shown above) rather than hardcoding it in the configuration file to reduce the risk of token leakage.
5. Avoid Recursive Loops: Prevent configurations where the MCP server could call itself or create circular dependencies, which can lead to runaway costs.
6.  Verify Third-Party Servers: Before using any community MCP server, review its code and the tools it exposes to avoid vulnerabilities like tool poisoning or tool shadowing.


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


