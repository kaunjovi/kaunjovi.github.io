---
layout: post
title: Streamlit, FrontEnd for python script. 
categories: [Steamlit, python] 
---

# AWS components - MoveToOwnPage
1. S3 
1. EC2 
1. Elastic IP 
1. Route XX 
1. Lambda 
1. RDS - Relational DB servcies 
1. Domino - No SQL 
1. Availability zones 
1. Queue Service 
1. 




## Liquid Neural Networks(LNN) - MoveToOwnPage 

1. Problem : How to have good acuracy, good robustness, without having a huge number of parameters.
1. Huge # of parameters = carbon footprint issue. Accountability goes for a toss. 
1. LNN - can stay adaptable, even after training. 
1. Perturbing the signal - add noise to the signal - make the video grainy 
1. LNN uses a relatively tiny number of parameters / neurons and shows far superior autonomously gleaning context of the task, from a very tiny amount of test data. 

1. [2023/01 Liquid Neural Networks | Ramin Hasani | TEDxMIT](https://www.youtube.com/watch?v=RI35E5ewBuI&t=472s)
1. [Ramin Hasani, CEO @ Liquid AI](https://www.linkedin.com/in/raminhasani/)
1. [2024 Adaptable Aviators: future of autonomous navigation Liquid networks](https://www.youtube.com/watch?v=2BoxhZUi01Y)
1. [Liquid Time-constant Networks by Cornell](https://arxiv.org/abs/2006.04439#)







1. Streamlit, was a startup launched in 2018, 
1. It was the brainchild of some former GoogleX and Zoox employees 
1. looking to build an open source project to make it easier to build custom applications to interact with data.
1. Streamlit launched in 2019 and raised $62 million.

1. Snowflake launched in 2012 and raised $1.4 billion before going public in September 2020.

## Get started with Streamlit 

1. [Get started with Streamlit](https://docs.streamlit.io/get-started?_fsi=NirxPvYO)


## Streamlit on Snowflake

1. Mar 2022 News [Democratizing Data Apps — Snowflake to Acquire Streamlit](https://www.snowflake.com/en/blog/snowflake-to-acquire-streamlit/)
1. [Snowflake acquires Streamlit for $800M](https://techcrunch.com/2022/03/02/snowflake-acquires-streamlit-for-800m-to-help-customers-build-data-based-apps/)
1. Founders - Adrien, Thiago, and Amanda, the founders of Streamlit,
1. Benoît Dageville, co-founder and president of products at Snowflake

```python 
import streamlit as st
import pandas as pd
import snowflake.connector

# Open a connection to Snowflake, using Streamlit's secrets management
# In real life, we’d use @st.cache or @st.experimental_memo to add caching
conn = snowflake.connector.connect(**st.secrets["snowflake"])

# Get a list of available counties from the State of California Covid Dataset
# Data set is available free here: https://app.snowflake.com/marketplace/listing/GZ1MBZAUJF
# More info on the data set: https://snowflakecloud.wpenginepowered.com/datasets/state-of-california-california-covid-19-datasets/
counties = pd.read_sql("SELECT distinct area from open_data.vw_cases ORDER BY area asc;", conn)

# Ask the user to select a county
option = st.selectbox('Select an area:', counties)

# Query the data set to get the case counts for the last 30 days for the chosen county
cases = pd.read_sql(f"SELECT date day, SUM(cases) CASES FROM open_data.vw_cases WHERE date > dateadd('days', -30, current_date()) AND area = %(option)s GROUP BY day ORDER BY day asc;", conn, params={"option":option})
cases = cases.set_index(['DAY'])

# Render a line chart showing the cases
f"Daily Cases in {option} over the last 30 days"
st.line_chart(cases)
```



1. Nice to show demo. Is it nice for prod? 
1. What was the conda activate for? 
1. Write in github repo. 
1. Deploy in 
    1. Streamlit Community Cloud 
    1. HF spaces. Allows you to deploy your code. Free ?? 
1. **alternatives to Streamlit**
    1. Gradio, Shiny, NiceGUI 
    1. stlite 
    1. Plotly Dash 
    1. Solara 
    1. Reflex 
    1. H2O wave 
    1. Or ... why dont you just do it the proper way, via. an HTML --- ahhhhh. Voldemort. 

## What are good backend servers to Streamlit
1. Tornado 

## Hosting LLMs in standalone machine 

1. LMstudio 
1. Ollama

## Reference
1. [Streamlit Crash Course: From Zero to Data App](https://youtu.be/d7fnzDQ5qM8?si=Xu9Q_HCzTCx_oRSS)
1. [He is good - 5 Things I Wish I Knew Before Learning Streamlit](https://www.youtube.com/watch?v=IOYHVPPbZII)



1. Service Account 
1. Policy per table / explicity for specific tables 
1. Unmasking policy - at field level / column level. 
1. Use policy (has to be done by SF admin) / call to_decrypt function 
1. SSN - string 
1. md5# - use the plain text - encryption. rowhaskey 


## [Claude 4](https://www.anthropic.com/news/claude-4)
1. Claude Opus - coding model, with sustained performance on complex, long-running tasks and agent workflows. 
    1. Opus 4 at $15/$75 per million tokens (input/output) and 
    1. SWE-bench (72.5%) and Terminal-bench (43.2%).
1. Claude Sonnet 4 - coding and reasoning while responding more precisely to your instructions.
    1. Sonnet 4 also available to free users.
    1. Sonnet 4 at $3/$15.
1. Claude Code - embeds Claude Opus 4
    1. supports background tasks via GitHub Actions and 
    1. native integrations with VS Code and JetBrains, displaying edits directly in your files for seamless pair programming.
    1. [Claude Code](https://www.anthropic.com/claude-code)
    1. Command-line AI, from concept to commit
    1. Claude Code embeds Claude Opus 4—the same model our researchers and engineers use—right in your terminal.

# [Build with Claude](https://www.anthropic.com/learn/build-with-claude)


# [Early Days of Agile Development & Is Design Dead? • Martin Fowler & James Lewis • GOTO 2024](https://www.youtube.com/watch?v=xsMUuOwv7IA&list=PLEx5khR4g7PIEQ3L-GI-DF5e6pIm1alq7)

Martin Fowler 
James Lewis ?? 



bagita 

Fret modeling 
Stride model 

Art of doing agile by Jim Shaw 

# [2020, The Art of Agile Development, Second Edition, by James Shore](https://www.youtube.com/watch?v=Ifxb8Bm4BlA)
1. 2007 - first edition. 
1. https://www.jamesshore.com/v2/projects/lunch-and-learn/art-of-agile-development


# [Scott W. Ambler & Pramod Sadalage • Refactoring Databases](https://amzn.to/3HgdLJ3)
1. ?? sounds intersesting. Refactoring db, schema and data, as we progress through the dev cycle. Check out. 
1. Why is it not more famous ? 

