---
layout: post
title: RAG with LangChain
categories: [RAG, LangChain, ai] 
---

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

## LangChain / RAG / Splitting 

1. https://campus.datacamp.com/courses/developing-llm-applications-with-langchain/retrieval-augmented-generation-rag?ex=5
1. LLM has only a so much wide context window. You cant load the whole world in the context window. 
1. So, you must chunk up the document and load only the ones that you need. 
1. The chunk could be each line, each paragraph, each page or whatever works for you. 
1. **chunk overlap** 
1. Every chunk in isolation, has less information than what it has if it has a bit of overlap with it's neighbours. 


1. CharacterTextSplitter

```Python
from langchain_text_splitter import CharacterTextSplitter 

ct_splitter = CharacterTextSplitter(
    separator = '.', 
    chunk_size = , 
    chunk_overlap = .. 
)

docs = ct_splitter.split_text ("aldfajkskldjfjasf" )
print ( docs )
```

```Python
# Import the character splitter
from langchain_text_splitters import CharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = CharacterTextSplitter (
    separator = "\n", 
    chunk_size = chunk_size, 
    chunk_overlap = chunk_overlap
)

# Split the string and print the chunks
docs = splitter.split_text(quote) 
print(docs)
print([len(doc) for doc in docs])
```


1. RecursiveCharacterTextSplitter

```Python
from langchain_text_splitter import RecursiveCharacterTextSplitter 

rc_splitter = RecursiveCharacterTextSplitter(
    separator = ["\n\n", "\n", " "],  
    chunk_size = , 
    chunk_overlap = .. 
)

docs = rc_splitter.split_text ("aldfajkskldjfjasf" )
print ( docs )
```

```Python
# Import the recursive character splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = RecursiveCharacterTextSplitter(
    separators = ["\n\n", "\n", " ", ""] , 
    chunk_size = chunk_size , 
    chunk_overlap = chunk_overlap
)

# Split the document and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])
```
