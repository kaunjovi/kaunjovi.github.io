---
layout: post
title: Streamlit, FrontEnd for python script. 
categories: [Steamlit, python] 
---

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
