---
layout: post
title: Hugging Face 
categories: [HuggingFace, ai] 
---

## [Working with Hugging Face](https://app.datacamp.com/learn/courses/working-with-hugging-face)



## [Developing LLM Applications with LangChain](https://app.datacamp.com/learn/courses/developing-llm-applications-with-langchain)

1. Connect - LLM, Data, Other functionality - under a common unified syntax. 
1. Prompts, Chains, Retrievers, Agents. 
1. LLMs - accessing those on HuggingFace is free. Falcon-7b ( 7 billion parameter)
1. langchain 0.3.13


```Python
from langchain_huggingface import HuggingFaceEndpoint

# Set your Hugging Face API token 
huggingfacehub_api_token = '---'

# Define the LLM
llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)

# Predict the words following the text in question
question = 'Whatever you do, take care of your shoes'
output = llm.invoke(question)

print(output)
```

```Python
# Define the LLM
llm = OpenAI(model="gpt-3.5-turbo-instruct", api_key="<OPENAI_API_TOKEN>")

# Predict the words following the text in question
question = 'Whatever you do, take care of your shoes'
output = llm.invoke(question)

print(output)
```



```Python
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate 

llm = HuggingFaceEndpoint( repo_id = "", huggingfacehub_api_token = "")

template = "You are an XXX. Answer the question. <some question>"

template = "You are an XXX. Answer the question. {question}"
prompt_template = PromptTemplate( template, input_variables=["question"])

print( prompt_template.invoke({"question" : "What is abc?"}) )

llm_chain = prompt_template | llm 
print( llm_chain.invoke({"question" : "What is abc?"}) )


```

## from langchain_core.prompts import PromptTemplate

1. Template for generating prompts. 
1. Context. Question. Response. 

```Python
from langchain_core.prompts import PromptTemplate
template = "You are bewakoof. Answer the question. {question}" 
prompt_template = PromptTemplate ( template = template, input_variables = ["question"])
print ( prompt_template.invoke({"question" : "What is the meaning of it all?"}))
```

```Python
from langchain_huggingface import HuggingFaceEndpoint 

llm = HuggingFaceEndpoint( repo_id = "tiiuae/falcon-7b-instruct", huggingfacehub_api_token = "")
llm_chain = prompt_template | llm 

llm_chain.invoke( {"question" : "aapko itni fakiri kaise aayi?"} )


```

## LangChain Expression Language (LCEL)




## from langchain_core.prompts import ChatPromptTemplate 

```Python
from langchain_core.prompts import ChatPromptTemplate 

prompt_template = ChatPromptTemplate.from_messages (
    [
        ## Define the model behaviour 
        ("system", "You are Amrish Puri"), 
        ## Human to provide inputs, instructions
        ("human", "Don't be afraid" ), 
        ## ai role to define outputs. These are additional examples for the model. 
        ("ai", "When you are afraid, shout."), 
        ("human", "Respond to the question : {question}")
    ]
)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI( model = "gpt-4o-mini", api_key = xxxx)
llm_chain = prompt_template | llm 

question = "Kab aaoge haveli main?" 

response = llm_chain.invoke ( { "question" : question } ) 

```




## [Designing Agentic Systems with LangChain](https://app.datacamp.com/learn/courses/designing-agentic-systems-with-langchain)
## [Retrieval Augmented Generation (RAG) with LangChain](https://app.datacamp.com/learn/courses/retrieval-augmented-generation-rag-with-langchain)

## [Introduction to LLMs in Python](https://app.datacamp.com/learn/courses/introduction-to-llms-in-python)



## [Course : Databricks](https://app.datacamp.com/learn/courses?technologies=22)

