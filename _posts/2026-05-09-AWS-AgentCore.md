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

1. Jupyter can help have a interactive demo running. Wow. 
1. Sample git : https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway



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

