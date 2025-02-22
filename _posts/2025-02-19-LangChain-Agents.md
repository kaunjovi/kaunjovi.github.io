---
layout: post
title: AI Agents with LangGraph
categories: [LangChain, SequentialChains, ai] 
---

1. https://campus.datacamp.com/courses/developing-llm-applications-with-langchain/chains-and-agents?ex=4

## What are agents? 

1. Agents use LLMs to get some job done. 
1. They use **tools** which are functions to get their biddng done. 

## Different types of Agents. 
1. ReAct Agent = Reasoning and Acting 

```Python 
from langgraph.prebuilt import create_react_agent 
from langchain_community.agent_toolkits.load_tools import load_tools 

llm = ChatOpenAI( model = xxx, api_key= xxx)
tools = load_tools( ["llm-math"], llm=llm )
agent = create_react_agent(llm, tools )

messages = agent.invoke( {"messages" : [("human": "what is the square root of 101)]}) 
``` 

```Python 
# Define the tools
tools = load_tools(["wikipedia"], llm=llm )

# Define the agent
agent = create_react_agent(llm, tools)

# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response['messages'][-1].content)
```

## Custom tools for agents 

1. https://campus.datacamp.com/courses/developing-llm-applications-with-langchain/chains-and-agents?ex=7

```Python 
# Define the tools
tools = load_tools(["wikipedia"], llm=llm )

# investigating the tools 
print ( tools[0].name ) # Calculator 
print ( tools[0].description ) # short description about calculator 

# agent uses the tools description to use the tool. 

print ( tools[0].rerturn_direct ) # agent should stop immediately after. 

```

1. Create a tool that the Agent can call. 

```Python 

from langchain_core.tools import tool 

@tool 
def hello_world( greeter_name:str, greety_name:str ) -> str: 
    """Geet a person, from another person"""

    greetings = f"Hello {geety}. Long time no see.\n"
    greetings = f"Hope you are doing well. Take care.\n"
    greetings = f"Thanks.\n"
    greetings = f"Thanks.\n"
    greetings = f"{greeter}.\n"

    return greetings  

print( hello_world.name )
print( hello_world.description )
print( hello_world.rerturn_direct )
print( hello_world.args )

``` 


```Python
from langgraph.prebuilt import create_react_agent 

# Create a LLM agent 
# What does temperature do ? 
llm = ChatOpenAI ( model = xxx, api_key = xxx, temperature = 0 )
agent = create_react_agent ( llm , [financial_report ])

# invoke the agent 
messages = agent.invoke( { "messages": ["human", "XYZ generated $10 million with $8 million cost. Generate a financial report please."]}) 
print (messages)
```

1. LLM will do wordsmithing. Dont worry. 

```Python 
# Define a function to retrieve customer info by-name
def retrieve_customer_info( name : str ) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Call the function on Peak Performance Co.
print(retrieve_customer_info("Peak Performance Co."))
```

```Python 
# Convert the retrieve_customer_info function into a tool
@tool 
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Print the tool's arguments
print(retrieve_customer_info.args)
```

```Python
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Create a ReAct agent
agent = create_react_agent ( llm, [retrieve_customer_info])

# Invoke the agent on the input
messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages["messages"][-1])
```

```Python
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Create a ReAct agent
agent = create_react_agent ( llm, [retrieve_customer_info])

# Invoke the agent on the input
messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages["messages"][-1].content)
```
