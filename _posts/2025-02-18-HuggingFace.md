---
layout: post
title: Hugging Face 
categories: [HuggingFace, ai] 
---


## Investigate 

1. HF spaces. Allows you to deploy your code. Free ?? 


## How to start and go about Vibe Coding 

1. https://www.reddit.com/r/OutOfTheLoop/comments/1jfwxxw/whats_up_with_vibe_coding/
1. https://www.reddit.com/r/ChatGPTCoding/comments/1jfacpu/if_you_are_vibe_coding_read_this_it_might_save_you/

my IDE (usually Lovable)

Wouldn't it be great if Claude laid this all out automatically, or asked if you'd like to?
Can you expand a little on Loveable & your course? 
Is it an alternative to Cursor? 
Is Loveable for web development only or apps too? 
Why did you pick it over alternatives? 
Is it worth watching your course if I’m planning on using Cursor? 


Sure, Lovable is the best first step into building web apps for non coders. 
I tested 11 other apps recently and they simply have the best UX and path to finished project that's ready for deployment.

If you are technical enough to use Cursor, 
the only reason why you should watch it is to learn how to create project documentation which you can then load and reference in Cursor and use Lovable just to set the project and set the context.
Cursor and Windsurf are both more technical but also more likely to give you good code quality. 
Lovable is great for those just starting off.


I do this all the time. You don’t have to “pass it through”. 
Try installing Cursor, ask it to review your changes. It will use git to see changes.

I use prompts like “does this xxx match the usual patterns used in this project?”. 
I also tell it to get rid of changes that it thinks it is not required “without changing the tests”, because AI usually generates a lot of noise. Also things like “what possible feedback will I get?”.

I also keep a markdown document with previous conversations and issues in PRs. 
Like if a colleague write “you should use X instead of Y”, I’ll put that in the document. 
Then I will add that document to the conversation as a set of rules it should follow. That document is over a 1000 lines by now.

I know many people consider “vibe coding” a joke but the reality is that, for me, 
it is incredibly effective and I have had multiple PRs merged that were completely written by AI. 
While I’m working, I’m also constantly improving my prompts, documenting them, and 
I intent to create some kind of workflow that consists of multiple AI agents, all with a different role, so I have to babysit it even less.

AI / vibe coding allows me to push more PRs faster. 

Oh, and you know who loves that I use so much AI? Management. 
I’ve made it no secret that I use AI extensively. I even have made guides for the company how I use it. 
The majority of devs in the company shrugs it off, like it’s the next 3D TV. 
I think it is a huge mistake, because I have been demoing the effectiveness of these tools to higher-ups and they love it.


```prompt
Please review for production readiness: check for common vulnerabilities, secure headers, forms, input validation, authentication, error handling, debug statements, dependency security, and ensure adherence to industry best practices.
```

1. [R2R (Reason to Retrieve)](https://github.com/SciPhi-AI/R2R?rdt_cid=5446329927798575344)
1. [The Prompt Index](https://www.thepromptindex.com/)
    1. https://chromewebstore.google.com/detail/the-prompt-index/ofaehlaoggbboahmpogkfhedgdeekekk


1. [Vibe Coding AI-Assisted Coding for Non-Developers](https://medium.com/@niall.mcnulty/vibe-coding-b79a6d3f0caa)

1. [Beer + GenAI = a whole useful app in an evening](https://vas3k.com/notes/vibe_coding/#:~:text=For%20example%2C%20I%20started%20with,this%20prompt)

Cursor Composer with Sonnet 
Talk to Composer with SuperWhisper 

1. [Move faster with intuitive React UI tools](https://mui.com/?srsltid=AfmBOooNuPR-wt16rmbcyQVOI6QLKhtARFFXlcoqb1a5rfFniRIAU634)






## [Working with Hugging Face](https://app.datacamp.com/learn/courses/working-with-hugging-face)



## [Developing LLM Applications with LangChain](https://app.datacamp.com/learn/courses/developing-llm-applications-with-langchain)


## [Designing Agentic Systems with LangChain](https://app.datacamp.com/learn/courses/designing-agentic-systems-with-langchain)
## [Retrieval Augmented Generation (RAG) with LangChain](https://app.datacamp.com/learn/courses/retrieval-augmented-generation-rag-with-langchain)

## [Introduction to LLMs in Python](https://app.datacamp.com/learn/courses/introduction-to-llms-in-python)


## [Huggingface]

1. [Huggingface Endpoints](https://python.langchain.com/docs/integrations/llms/huggingface_endpoint/)




## [Tutorial : Groq LPU Inference Engine Tutorial]

1. [Groq LPU Inference Engine Tutorial](https://www.datacamp.com/tutorial/groq-lpu-inference)



## [Course : Databricks](https://app.datacamp.com/learn/courses?technologies=22)

## Introduction to Databricks

1. https://app.datacamp.com/learn/courses/introduction-to-databricks

1. [Evolution to the Data Lakehouse](https://www.databricks.com/blog/2021/05/19/evolution-to-the-data-lakehouse.html)

1. **Options for enterprise data** 
1. Data Warehouse 
    1. structured data. Does not change too much. 
1. Data Lake 



1. [Databricks blog](https://www.databricks.com/blog)

1. [What is a Delta table in Databricks?](https://medium.com/event-driven-utopia/what-is-delta-table-in-databricks-b660b80ecc5a)

1. Delta tables are a new type of table in Databricks 
1. They are optimized for fast, read-intensive, large-scale data processing and are 
1. ideal for use cases such as data lakes.
1. A Delta table is essentially a **versioned version** of a data lake table 
1. that is stored as a collection of small data files in a **hierarchical file system**, 
1. Not as a single monolithic file. 
1. This allows for fast, incremental processing and 
1. enables you to keep track of changes to the data over time.

1. **Benefits of Delta Tables** 
1. 


