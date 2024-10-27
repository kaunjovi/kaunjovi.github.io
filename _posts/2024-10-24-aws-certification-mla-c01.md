---
layout: post
title: AWS Certifications MLA C01
categories: [certifications] 
---

## AWS Certification MLA-C01

1. This one is for SageMaker. Is there any for Domnio??? What are the other alternatives??? 
1. What is the latest thinking about MLOps ???
1. [Udemy / Master MLA-C01](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45284683#overview)

## Data Ingestion and Storage 

1. Amazon Kinesis (think Kafka)
1. Amazon FSx 
1. Amazon S3 
1. Amazon Elastic 
    1. Block Store (EBS)
    1. File System (EFS)

## Data Types and Formats 

## Data Warehouse vs. Lakes vs. Lakehouse 

## Extract Transform and Load (ETL) pipelines and Orchestration 

## AWS services / storage 
## AWS services / streaming 

1. Elastic MapReduce (EMR) - running big parallel data processing jobs at scale. Hadoop. Spark. 


## Data / Missing. Unbalanced. Outlier. 

## Data / Transformation 

1. To Transform data to the format needed by the ML to work. 

## SageMaker / Data processing and analysis 

1. built in algorithms you can just use. XGBoost. LinearLearner. 


## AWS Glue / Data processing and Transformation. 

## Amazon Rekognition 

1. Image recognition. 

## Amazon Forecast 

1. Forecasting data. 

## Amazon Q 

1. For building chatbot 


## Model Training, Tuning and Evaluation. 

1. Deep learning fundamentals. How does Neural Network work. What is the meaning of Topology. 
1. Measuring Model Performance. 
1. Automatic Model Tuning in Sagemaker

## Generative AI. Transformer Architecture. 

1. Transformer Architecture. 
1. Self Attention. 
1. How GPT works. How Claude works. 
1. SageMaker Jumpstart. 

## Amazon Bedrock 

1. Built on top of Foundation models. 
1. Retrieval Augmented Generation (RAG) works - preventing hallucinations. injecting proprietary data. 
1. Knowledge Bases - store the external data 
1. Vector Stores 
1. Guardrails - prevent model from doing things that you dont want it to do. 
1. LLM agents - custom code to 
1. 

## ML operations (MLOps)

1. SageMaker 
1. Containerize (ECS, ECR)
1. Cloudformation 
1. CDK
1. CodeDeploy 
1. CodeBuild 
1. CodePipeline 
1. EventBridge 
1. Step Functions
1. Managed Workflows for Apache Airflow (MWAA)

## Security. Identity. Compliance. 

1. Securing Data . in SageMaker
1. AWS IAM 
1. KMS 
1. Macie 
1. Secrets Manager 
1. Website Application Firewall (WAF)
1. Shield 
1. Network isolation - VPC, Private Link 

## Management. Governance. 

1. CloudWatch. CloudFormation. Config. CloudTrail. 
1. Budgets. CostExplorer. 
1. New - TrustedAdvisor. X-Ray 

## [Data Engineering fundamentals](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45284653#overview)

## Three types of Data. 3 Musketeers

1. Structured data 
    1. We know the columns, the data types in them, and their relations with each other. 
    1. Easy to query. 
    1. There is a defined schema. 
    1. The data is cleaned and consistent. 
    1. examples - Database tables (Oracle, Redshift, MySQL, ...) , CSV files, XLS etc. 
1. Unstructured data 
    1. No defined structure or schema. 
    1. Can't query because there is no structure. 
    1. Video, audio, images, emails, word file, pdf files, text without a fixed format. 
1. Semi structured data 
    1. There is no strict schema or structure, but there is some tags, hierarchies, or other patterns. 
    1. XML, JSON, email headers, Log files of various formats. 

## Properties of data. 3 Vs. 

1. Volume - How much data. GB, PB, TB. 
    1. How much do we have in EDC and in UDS??? 
    1. How much data comes in per day? How much are we keeping? 
    1. How long for? How much in transactional storage? How much in backup?
1. Velocity - the speed at which new data is generated, collected and processed. 
    1. Batch vs. stream in real time and process continuously. 
    1. High velocity? Real time or near real time processing capability is required. 
    1. Real time vs. Near real time ???
    1. Kinesis data stream vs. Kinesis data firehose ???
    1. Sensor data from IOT - 
    1. High frequency trading system - 
1. Variety - Types of data  - structured, semi structured, Unstructured
    1. 
1. Veracity 

## [DataWarehouse vs. DataLakes](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45284683#overview)

1. DataWarehouse - legacy approach to data engineering. 
    1. Centrailized. Optimized for analysis. 
    1. Data collected from various sources. Arranged in structured format. 
    1. Optimized for analysis. Optimized for read heavy operations. 
    1. Star schema vs Snowflake schema. 
    1. Write vs Read heavy operations??
    1. Amazon Redshift, Google BigQuery, Azure SQL Data Warehouse (Amazon used Oracle - very expensive - before Redshift)
    1. Source1, Source2, Source3, ... -> DataWarehouse -> DataMart1, DataMart2, DataMart3, ... 

1. Data Lake 
    1. Holds raw data in native format. Could be structured, semi-structured, or Unstructured.  
        1. No replication is happening in any structured format. 
    1. Amazon S3, Hadoop Distributed File System (HDFS), Azure Data Lake Storage 
    1. S3 (keep raw data ) > Glue (extract meta data from the raw data ) > Athena (use the meta data to query the raw data)

1. DataWarehouse vs DataLake
    1. Schema on Write vs Schema on read 
        1. DataWarehouse has to write to a schema. Hence ETL. 
        1. DataLake used schema on write. Hence ELT. 
    1. Structured vs Semi/un structured 
        1. DataWarehouse is primarily used for structured data 
        1. DataLake are primarily suitable for Semi/un structured data. 
    1. Agility 
        1. DataWarehouse - less agile to ingest 
        1. DataLake - more agile to ingest 
    1. Cost 
        1. DataWarehouse - more 
        1. DataLake - less 

1. When to choose which one? 
    1. DataWarehouse 
        1. Structured data sources 
        1. BI and analytics is the primary use 
        1. Need fast query. complex query 
            1. Know the schema. Know the indices. Can optimize. 
        1. Know the data from different sources. Data integration is done. 
            1. Data is kept in a read optimized way. 
    1. DataLake
        1. You have variety of data ./semi/un structured data. 
        1. Storing data in a cost effective way is the primary objective. 
        1. You are unsure about what needs to be done with the data later and want to be flexible about it. 
        1. Data discovery, Advanced Analytics, ML are the probable use cases. 

1. [DataLakehouse](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45284683#notes)
    1. Databricks concept 
    1. Supports all 3 varieties of data. 
    1. Support 2 varieties of schema on write and on ready
    1. Supports both families of use case Analytics and BI  and data discovery, AI/ML 
    1. S3 > Delta Lake - brings ACID to big data. 
    1. AWS Lake Formation - with S3 and Redshift Spectrum (to query that data)
    1. Delta Lake - opensource storage layer, brings ACDI transactions to Apache Spark and big data 

1. [Data Mesh](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45337673#notes)
    1. Coined in 2019 by who ?? 
    1. More about governance and organization of data within an enterprise. 
    1. Domain based Data Management 
    1. Central standards. Federated governance.
        1. Can AWS Glue be the centralized catalog for all the data products for users to discover???
    1. Self service tooling and infr for data owners to leverage to create and expose data products. 

1. [ETL pipelines](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45284695#notes)
    1. Real time or batches
    1. Database, files, APIs, message queues etc. 
    1. Data integrity
        1. What if api fails on call 
        1. Do you retry it. How often. How many times. 
    1. Velocity - in real time, in near real time (in a few minutes), batch fashion (overnight)

1. Transform 
    1. Transform the raw data into a suitable forrmat for the target data warehouse 
    1. Cleanse the data - duplicate data, fixing errors 
    1. Correct the format - incorrect format 
    1. Enrich - add additional data / reference data to the raw data 
    1. Aggregation or computations - totals, sums, averages, means etc. 
    1. Encoding / decoding - zipped data needs to be unzipped, some data needs to be encrypted 
    1. Handling missing values - drop rows with missing values ? 

1. Load 
    1. Batch vs realtime 
    1. reliable. if something goes wrong we need to know about it and be able to do something about it. 

1. Managing ETL pipelines 
    1. Automated. Reliable way. 
    1. AWS glue can do the job 
    1. Orchestration 
        1. Glue Workflows
        1. EventBridge
        1. Managed Workflows for Apache Airflow (MWAA)
        1. AWS step functions 
        1. Lambda 

## Data Sources 

1. JDBC - Platform independent. Java dependent. 
1. ODBC - Not in Java? No problem. Use ODBC. Platform dependent. You will need Platform specific drivers. 
1. Raw files 
1. APIs 
1. Streams (Kafka, Kinesis) 

## Data Formats 

1. CSV - Text based. Human readable. Small to medium sized datasets only please. Not very efficient about storage. 
1. Javascript Object Notation (JSON) - Structured or semi-structured data, between backend services and front end. 
    1. Light weight. Text based. Human Readable. 
    1. Based on key value pairs. 
    1. Main diffrence - it can be semi-structured. Flexible schema. Nested structures. 
    1. Good for Configurations and settings 
    1. Used in : NoSQL databases e.g. MongoDB. RESTful APIs. 
1. Avro - Binary format. Both data and schema. Machines can read, without knowing the origination. 
    1. Not human readable / writable. 
    1. Schema is there in the file. So if the schema was changing in the source, distribution system, that is no problem. 
    1. Adding schema to data everytime means some extra space. But gives the flexibility of handling changing schema. 
    1. efficient serialization for data transport. 
    1. Usage : Apache Kafka, Sparc, Flink and Hadoop ecosystem
1. Parquet - Columnar storage. Optimized for analytics. You might be looking for only some columns, not all, for analytics. 
    1. Storage optimization. You can put entire set of columns in a different server. How does that help ??? 
    1. Usage : Redshift Spectrum, Hadoop, Apache Spark / Hive / Impala


## Investigate Further ??? 

1. Redishift Spectrum ??? 

