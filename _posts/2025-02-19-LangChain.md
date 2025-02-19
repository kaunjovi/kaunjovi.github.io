---
layout: post
title: LangChain
categories: [LangChain, ai] 
---

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

1. An example of PromptTemplate 

```Python 
# Create a prompt template from the template string
template = "You are an artificial intelligence assistant, answer the question. {question}"
prompt = PromptTemplate( template = template, input_variables = ["question"])

# Create a chain to integrate the prompt template and LLM
llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct', huggingfacehub_api_token=huggingfacehub_api_token)
llm_chain = prompt | llm 

question = "How does LangChain make LLM application development easier?"
print(llm_chain.invoke({"question": question}))
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

1. Another example. 

```Python
# Define an OpenAI chat model
llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')		

# Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Respond to question: {question}")
    ]
)

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm 
response = llm_chain.invoke({"question": "How can I retain learning?"})
print(response.content)
```

## Limitations of prompt templates 
1. PromptTemplate + ChatPromptTemplate 
1. Can't scale. 
1. Arrey scale karna kyon hai? 

## Few Shot Prompting | from langchain_core.prompts import FewShotPromptTemplate 


1. We have a few examples of question and answers. 

```
examples = [
    {
        "question" : "kyon?", 
        "answer" : "pata nahin"
    }, 
    ...

]
```

1. Change the DataFrame to list of dicts 

```
examples = df.to_dict( orient = "records")
```

```Python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate 

example_prompt = PromptTemplate.from_template ( "Question: {question}\n{answer}") 

prompt = example_prompt.invoke( {"question" : "ye kya hua?"
                                "answer" : "jo hua so hua" })

print( prompt.text )

```

1. Integration with OpenAI 

```Python 
llm = ChatOpenAI( ... )


## testing ?? 
example_prompt = PromptTemplate.from_template ( "Question: {question}\n{answer}") 
prompt = example_prompt.invoke( {"question" : "ye kya hua?"
                                "answer" : "jo hua so hua" })

print( prompt.text )



prompt_template = FewShotPromptTemplate (
    ## list of dicts 
    examples = examples, 
    ## template for formatting examples ?? 
    example_prompt = example_prompt, 
    suffix = "Question: {input}", 
    input_variables = ["input"]
)

## Lets check the prompt is correct ?? 
prompt = prompt_template.invoke ( {"input" : "Ye kya ho raha hai"} ) 
print (prompt)

llm_chain = prompt_template | llm 
response = llm_chain.invoke ( { "input": "Ye kya ho raha hai?" })
print ( response )
```

1. One more example. 

```Python

# Create the examples list of dicts
examples = [
    { "question" : "How many DataCamp courses has Jack completed?", 
    "answer" : "36"}, 
    { "question" : "How much XP does Jack have on DataCamp?", 
    "answer" : "284,320XP"}, 
    { "question" : "What technology does Jack learn about most on DataCamp?", 
    "answer" : "Python"}
]

# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# Create the few-shot prompt
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

# Invoke the prompt template
prompt = prompt_template.invoke({"input": "What is Jack's favorite technology on DataCamp?"})
print(prompt.text)


prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

# Create an OpenAI chat LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Create and invoke the chain
llm_chain = prompt_template | llm 
print(llm_chain.invoke({"input": "What is Jack's favorite technology on DataCamp?"}))
```




