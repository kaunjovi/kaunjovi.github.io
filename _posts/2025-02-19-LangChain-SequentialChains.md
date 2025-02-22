---
layout: post
title: LangChain | Sequential chains 
categories: [LangChain, SequentialChains, ai] 
---

1. https://campus.datacamp.com/courses/developing-llm-applications-with-langchain/chains-and-agents?ex=1

1. **What is a Sequential Problem?**
1. Create itinerary 
    1. human : going x. what to do. 
    1. ai : here is a list 
    1. human : only for the days 1 and 2 
    1. ai : oh then you can do only a, b 
    1. human : create itinerary for day 1 and 2, with a , b 
    1. ai : here you go, o free thinker. 
1. IMHO, this is a **conversational problem**.

1. The output from one will be input to the next step. 

```Python 

prompt_1 = PromptTemplate( input_variables = ["destination"], template = "Suggest activies for {destination}") 

prompt_2 = PromptTemplate ( input_variables = ["activities"]), template = "For one day travel, pick top 3 activities from {activities}" )

llm = ChatOpenAI( model = xxx, api_key = xxx )

seq_chain = ( { "activities": prompt_1 | llm | StrOutputParser() }
    | prompt_2 
    | llm 
    | StrOutputParser() ) 

print( seq_chain.invoke("destination" : "Rome") ) # All roads lead to Rome. 

``` 

1. A working example 

```Python
# Create a prompt template that takes an input activity
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# Create a prompt template that places a time constraint on the output
time_prompt = PromptTemplate(
    input_variables = ["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

# Invoke the learning_prompt with an activity
print(learning_prompt.invoke({"activity": "play golf"}))

```




