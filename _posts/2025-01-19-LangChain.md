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

## Sequential Chains 

1. You ask something. AI responds back. You pick some options. AI responds back. Go back and forth a few times. And then you get to the itinerary. 


## Integrating document loaders

1. https://campus.datacamp.com/courses/developing-llm-applications-with-langchain/retrieval-augmented-generation-rag?ex=1
1. Pre trained LLM are closed. They have learned. Cant learn any more. 
    1. Dont have access to any more data. No external data access. 
    1. Understanding coming only from training data. 
1. What if? you need it to know about your company data. Or world events after the llm was released. 
1. Retrieval Augmented Generation (RAG)
    1. User query is embedded. 
    1. Used to query the most relevant dcoument from database 
    1. The document is then added to the model's prompt. 
    1. Now the model has extra context - new data - to derive answer over. 
1. RAG development steps 
    1. Loading the document (in vector database?)
    1. Split them in chunks. Vector db does not know documents. It knows chunks only. They are indexed. 
    1. Storage of the chunks for retrieval. 

1. https://python.langchain.com/docs/integrations/document_loaders

## LangChain / Document loaders 

1. https://campus.datacamp.com/courses/developing-llm-applications-with-langchain/retrieval-augmented-generation-rag?ex=1
1. Load document and cofigure. .csv. .pdf. .html. 
1. also - S3 files (which format?), notebooks (.ipynb), audio transcripts (.wav)

```Python 
## Needs the dependency pypdf 
from langchain_community.document_loaders import PyPDFLoader 
from langchain_community.document_loaders import UnstructuredHTMLLoader 
from langchain_community.csv_loader import CSVLoader 

loader = PyPDFLoader("path to the pdf you want to load")

## load the document into memory 
data = loader.load() 
print ( data[0])

```

1. an example of PyPDFLoader

```Python
# Import library
from langchain_community.document_loaders import PyPDFLoader 

# Create a document loader for rag_vs_fine_tuning.pdf
loader = PyPDFLoader( "rag_vs_fine_tuning.pdf" )

# Load the document
data = loader.load()
print(data[0])
```

1. an example of CSVLoader

```Python 
# Import library
from langchain_community.document_loaders.csv_loader import CSVLoader

# Create a document loader for fifa_countries_audience.csv
loader = CSVLoader("fifa_countries_audience.csv")

# Load the document
data = loader.load() 
print(data[0])
```

1. An examply of HTML loader 

```Python
from langchain_community.document_loaders import UnstructuredHTMLLoader

# Create a document loader for unstructured HTML
loader = UnstructuredHTMLLoader("white_house_executive_order_nov_2023.html") 

# Load the document
data = loader.load() 

# Print the first document
print(data[0])

# Print the first document's metadata
print(data[0].metadata)
```


## LinkedIn Certifications 

1. [Docker Foundations Professional Certificate](https://www.linkedin.com/learning/paths/docker-foundations-professional-certificate)
1. [Data Engineering Foundations Professional Certificate by Astronomer](https://www.linkedin.com/learning/paths/data-engineering-foundations-professional-certificate-by-astronomer)
1. [OpenEDG Python Institute: Programming with Python Professional Certificate](https://www.linkedin.com/learning/paths/openedg-python-institute-programming-with-python-professional-certificate)
1. [Anaconda Python for Data Science Professional Certificate](https://www.linkedin.com/learning/paths/anaconda-python-for-data-science-professional-certificate)
1. [Microservices Foundations Professional Certificate by Kong](https://www.linkedin.com/learning/paths/microservices-foundations-professional-certificate-by-kong)
1. [AWS Certified Machine Learning Engineer Associate: Hands On!](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356927#overview)



