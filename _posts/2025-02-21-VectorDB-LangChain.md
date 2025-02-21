---
layout: post
title: VectorDB with LangChain
categories: [VectorDB, LangChain, ai] 
---

1. https://campus.datacamp.com/courses/developing-llm-applications-with-langchain/retrieval-augmented-generation-rag?ex=9

## Embeddings 

1. **What are embeddings?**
1. **What are embedding models?**
1. **Why are embeddings required?** 
1. **Where should we store the Embeddings?** 

## VectorDB

1. Commercial db that also acts as a vector database 
    1. elasticsearch 
    1. redis 

1. Considerations while chosing a VectorDB
    1. Open source vs. Licensed (elasticsearch, redis)
1. Cloud vs on-premises
1. Lightweight and inmemory (ChromaDB) or powerful 


```Python 
from langchain_openai import OpenAIEmbeddings 
from langchain_chroma import Chroma 

open_api_key = "*******" 
embedding_model = "text-embedding-3-small" 
embedding = OpenAIEmbeddings( open_api_key = open_api_key, embedding_model = embedding_model)

vectorstore = Chroma.from_documents ( 
    docs, 
    embedding = embedding, 
    persist_director = "full path to directory" 
)

## Run a similiarity search and return top n most similar documents. 
n = 2 
retriever = vectorstore.as_retriever (
    search_type = "similiarity", 
    search_kwargs = {"k": n }
)

## Prompt template 
message = """ 
lorem ipsum. lorem ipsum. lorem ipsum. lorem ipsum. lorem ipsum.

Guidelines: 
{guidelines}

Copy: 
{copy}

Fixed Copy: 
"""

prompt_template = ChatPromptTemplate.from_messages([("human", message)]) 

from langchain_core.runnables import RunnablePassthrough 

rag_chain = ( {"guidelines": retriever, "copy": RunnablePassthrough() } | prompt_template | llm )

response = rag_chain.invoke("some ***")
print (response) 
```

1. A running example. 

```Python
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Split the document using RecursiveCharacterTextSplitter
chunk_size = 300
chunk_overlap = 50
splitter = RecursiveCharacterTextSplitter(
    ## separators = ["\n\n", "\n", " ", ""] , ## this is the default anyway. 
    chunk_size = chunk_size , 
    chunk_overlap = chunk_overlap
)
# docs = splitter.split_text(data[0]) 
docs = splitter.split_documents(data)
print(docs)

# Embed the documents in a persistent Chroma vector database
embedding_function = OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small')

vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_function,
    persist_directory=os.getcwd()
)

# Configure the vector store as a retriever
n = 3 
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": n }
)

# Add placeholders to the message string
message = """
Answer the following question using the context provided:

Context:
{context}

Question:
{question}

Answer:
"""

# Create a chat prompt template from the message string
prompt_template = ChatPromptTemplate.from_messages([("human", message)])

vectorstore = Chroma.from_documents(
    docs,
    embedding=OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small'),
    persist_directory=os.getcwd()
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create a chain to link retriever, prompt_template, and llm
rag_chain = ({"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | llm)

# Invoke the chain
response = rag_chain.invoke("Which popular LLMs were considered in the paper?")
print(response.content)

```

1. [LangChain Hub](https://smith.langchain.com/hub)
1. https://python.langchain.com/docs/introduction/
1. [LangChain Templates](https://templates.langchain.com/)
1. LangGraph 


