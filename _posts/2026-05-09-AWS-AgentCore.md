

## [Observe your Agentic Applications with Amazon Bedrock AgentCore Observability](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/jMMtv2vJFrgaLJCEvDcKIoMxR9EU3KOU)



## [Amazon Bedrock AgentCore Observability](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/Qja9YaoUqTRgL2flvLCmB6q1agn_KVd3)

1. They are supposed to act autonomously. So, you have to deeply understand what they are doing in prod, step by step 
1. Full tracing 
1. telemetry (??) and 
1. Metrics 
1. Monitor, debug and understan what is going on 
1. If you turn on observability - it emits run time metrics 
1. See them in Amazon CloudWatch

1. Each user has a session. That is tracked from start to finish. 
1. Within session - traces and spans - 
2. Please turn on CloudWatch transaction search 
3. **AWS Distro for Open Telemetry (ADOT) SDK**


## [Using Amazon Bedrock AgentCore Built-in Tools with the Strands Agents SDK](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/72p-Xb4G0H4GW0NAPJhZ0oqsTBtwUMCO)

1. Let LLM answer. And then write a code, run it, to confirm that the answer was correct. 
   1. Why not do the latter to begin with ? 
   2. What is the largest prime number under 100 
2. Or, might be there is a need for a basic prototyping? You could do this here. 
3. **bedrock_agentcore.tools.code_interpretor_client**


## [Amazon Bedrock AgentCore Built-in Tools](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/66A0zdrYFrMZyzt4fv3YGz3D9JELc_lN)

1. Tool #1 : **Code interpretor**
2. Secure, Sandboxed environment, where the Agent could write and run code on demand 
   1. Python, javascript and typescript
   2. csv, xls and json
3. Run custom logic, interpret data etc. 
   1. Pull large dataset from S3 - GB scale 
4. Code execution - upto 15 minutes, extendable to 8 hours 
5. Fully managed - done have to provide infra, manage dependencies etc. 
6. Files and data created during session is available throughout the session lifetime. 
7. Tool #2 : **Browser Tool**
8. Testing webapplications, scraping information, 
9. Agent could take screenshot of the website and try to understand that as well 
10. Supports 
    1.  **Live view**. So you can see what the agent is doing on the browser in real time. 
    2.  **Replay** : So you can see what had happened. 
    3.  


## [Amazon Bedrock AgentCore Identity Basics](https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/RG1RmAO7xxjYtTh9OAz_skGLjgXjo9_P)


1. **Workload Identity**
2. Way for agents to prove who they are w/out hardcoding credentials anywhere 
3. Workload Identity gives each identity a secure portable identity
4. They can be used across trust domains (what is ??)
5. **Agent Identity**
6. Specialized Workload Identity. 
7. Have agent specific metadata 
   1. uniqueId, name, arn, OAuth settings, and policy attributes 
8. Agent identfy as themselves and not on behlf of the user 

1. **Inbound Authentication**
2. Who is allowed to invoke your agent ? 
   1. Supports AWS SigV4. IAM-based permissions to restrict access. 
   2. Is external usrs accessing the agent ? Can use JWT based / ...
      1. When the user send request they send a token from a registered Id provider 
      2. Runtime automatically checks for validity of the token 
      3. 

1. **Outbound Authentication**
2. How does the 

[Github : AgentCore samples](https://github.com/awslabs/agentcore-samples/tree/main/01-tutorials/03-AgentCore-identity) 




## Adding Memory to Agents with Amazon Bedrock AgentCore Memory

1. Lesson 8 of 15
1. https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/RIYzpTyKOucys_Pza4ctdPtGbWqpNHBK
2. [Git AgentCore Memory toosl from Strands](https://github.com/strands-agents/tools/blob/main/src/strands_tools/agent_core_memory.py)
3. MemoryClient from boto3 
4. /summaries/{actorId}/{sessionId}
5. We can let the agent decide when to store memories. That might not be reliable. 
6. We can advise that in the system prompt and still there is not guarantee
7. Another way is to have hooks (Strands)
   1. on_agent_initialized()
8. 


## Amazon Bedrock AgentCore Memory Basics

1. https://html.cdn.contentraven.com/crcloud/uploads/aws_partners_11276/encryptedfile/693416/v1.0/index.html#/lessons/JA6nNXaFRKx-H7T7vHU-_7QqQpdS1Nd3

1. **How does it work?** 
1. Configure / set up memory, calling up memory space, memory strategy etc. 
1. Interact during sessions 
1. Store events. Retrieve them. During the session. 
1. Improve quality of interactions with historical context from long term memory

17. What is session (identified by sessionID )? 
    1.  One conversation, inclduing multiple back and forth. 
18. **Short Term** - what is happening in session. E.g. a coding assistant refactoring code. 
    1.  Running history of what has happened so far in the current conversation / session. 
    2.  Stores raw **events**. 
        1.  User messages. Agent responses.
        2.  Tool calls and the results that came back. 
        3.  System events ?? 
        4.  State changes ?? 
    3.  It is a chronological record of activities that happened during a specific session / conversation. 
    4.  You have to **create** the memory resources. **Programmatically** store and retrieve events. 
    5.  
19. **Event** 
    1.  memoryid - id of the memory resource created to store events 
    2.  sessionid, 
    3.  actorid - entity associated with the event. Is it the end user / the agent 
    4.  payload 
        1.  multiple possible 
        2.  conversational payload for messages 
        3.  blob for images / files 
    5.  Retreiver a single event ? **GetEvent** API. 
    6.  Retrieve list of events ? **ListEvents** API. Give it memoryId, actorId and sessionId
    7.  You can manually delete via **DeleteEvent** API. 
    8.  Or you can set expiration event. Auto expiration and deleted. 
    9.  
20. **Long Term** - User preferences. Store insights. Generate session summaries. etc. 
    1.  Do not store all events. Store summaries. 
    2.  Assuming a customer says he likes a particular brand, keep that in the long term. 
        1.  You dont have to manually store it. 
        2.  A process goes on in the background, finds the relevant stuff, and puts it in Long Term membory. 
21. **Memory Strategy** is created when the memory resource is created. 
   1. Strategies include 
   2. summarization : 
   3. semantic memory : 
   4. user preference : 
   5. Or custome strategy : 
22. **RetreieveMemoryRecords** 
    1.  memoryId
    2.  namespace 
    3.  searchCriteria : Semantic query 
23. **ListMemoryRecords** - list all, w/out search. 
24. **DeleteMemoryRecord** - delete long term memory. 

25. **Center AgentCore Runtime** - agent runs in it. Fully managed. Serverless environment. 
26. Sessions upto 8 hours 
27. Payloads upto 100 megabytes 
28. Each sessions runs in its own micro VM (??) - dedicated CPU, memory, filesystem, and auto clean up 
29. Choose your model - claude, gemini, whatever 
30. Choose your framework - crewai, langgraph etc. 
31. MCP compatible. 

32. **AgentCore Gateway**
33. Actis as a MCP server and exposes targets like API, lamda functions, 
34. Connections to Salesforce, JIRA, 
35. Agent can discover and call anything it needs to integrate with 

36. **AgentCore Memory**
37. Short Term - what is happening in session. E.g. a coding assistant refactoring code. 
38. Long Term - User preferences. Store insights. Generate session summaries. etc. 

39. **Built in tools**
40. Code interpreter - run python, typescript or javascript, inside a secure (Bedrock) managed environment. 
41. Browser tool - let agents interact with live web pages
42. Both tools are integrated with IAM (secure)

43. **AgentCore Observability service**
44. Every step is there - reasoning, tool calls and outcome 
45. telemetry flows into CloudWatch by default - latency, token usage, session count, error rates (??)

46. **AgentCore Identity** : Every request is verified. 
47. Even if it comes from previously trusted sources. 
48. Each agent has a unique identity
49. And fine grain permissions 
50. Amazon Cognito built for Agent 
51. Both inbound and outbound authentication mechanisms
52. inbound - OAuth 2.0 flows - use an identify provider 
53. outbound - use the SDK - use annotiations - @requireaccesstokens 
   1. supports token refresh etc. 
   2. machine to machine and delegated access. 
54. **Secure Token Vault** - for storing credentials - OAuth token, client keys, etc. 


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

