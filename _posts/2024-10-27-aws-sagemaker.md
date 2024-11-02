---
layout: post
title: AWS SageMaker 
categories: [AWS, SageMaker] 
---

1. https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45285053#notes
1. Service for ML, workflow in AWS. From before GenAI 
1. SageMaker helps with the entire **Machine Learning (ML) workflow**
    1. Fetch, clean and prepare data. Feature engineering. 
    1. Train model. Evaluate. Pick the best. 
    1. Deploy model in production for inference by other apps and users. 
    1. Monitor performance. Learn, if anything is to be picked from the production. 
    1. Feedback to the begining of the process. 

## [69 Data Prep on SageMaker](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45285065#notes)

1. Data could come from S3. 
    1. But could also be from Athena (database)
    1. EMR (distributed processing framework like Hadoop). Spark (distributed processing system)
    1. Redshift (Data warehouse)
    1. Amazon Keyspaces DB (??)

1. Data format could be many. RecordIO. ProtoBuf. 
    1. [RecordIO Data Format](https://mesos.apache.org/documentation/latest/recordio/)
        1. Binary data format. Data is broken into chunks, called records. 
        1. Each record is prepended by the length of the record. 
    1. [Protocol Buffers](https://protobuf.dev/)
        1. Google’s language-neutral, platform-neutral, extensible mechanism for serializing structured data
        1. e.g. XML, but smaller, faster, and simpler

1. You could work on data with popular framework / tools like Pandas, numpy, scikit_learn etc. 

1. Steps 
    1. Copy data from source (S3?)
    1. Spin up a processing container (SageMaker could do it for you or you could have your own)
    1. Output processed data (S3?)

1. Training on SageMaker
    1. You should already have data - S3 path 
    1. You should already have code to train the data on - ECR path - 
        1. Elastic Container Registry (ECR)
        1. ECR - store, share, and deploy your container software anywhere
    1. S3 bucket for output 
    1. ML compute - could be costly 
    1. For training algorithm, you have a wide variety of options 
        1. SageMaker built-in training algo 
        1. Algorithm purchased from AWS marketplace. 

## [77 SageMaker / Canvas](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45536591#notes)

1. For BA. No code ML. 
1. Upload CSV (just that, CSV please)
    1. Point out the column to predict. 
    1. Automatic data cleaning 
        1. Missing values (drop, imputation, imputation+ )
        1. Outliers (kya karna hota hai)
        1. Duplicates (kya karna hota hai ) 
    1. Can join datasets 
    1. Classification or regression 
    1. Share models and datasets with SageMaker studio 
        1. BA is done, give it to ML engineer. 
    1. Has support for GenAI via Bedrock or Jumpstart foundation models 

## [78 AWS glue (major one needs own page?)](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45285225#notes)

1. Serverless 
1. Glue is the **glue between unstructured data and the structured data** so you can query them together. 
1. Table definitions ?? Central meta data repository. 
    1. Extract structure from unstructured data
1. Glue allows you to discover table definitions + schema 
    1. S3 data lakes - unstructured data? No problem. 
    1. **Glue crawler** runs over S3 and creates the schema. 
    1. Doing so creates a **data catalog** that has only table definition. 
    1. The data is still in S3. 
1. AWS glue also Does ETL.
    1. Now that it knows the schema it could do ETL. 
    1. Trigger. Schedule. Demand. 
1. ETL uses Apache Spark for distributed data processing    

1. **Question** You are managing a big data project that requires periodic processing of large datasets stored in Amazon S3. Which service would you use to schedule and manage the execution of these data processing jobs?
1. AWS Glue is a managed ETL service that allows you to schedule and manage data processing jobs, making it ideal for periodic processing of large datasets.



## How does Glue crawler work. 

1. Depending on how the S3 buckets are organized, 
1. Glue crawler will extract partitions. 
1. How are you planning to query the **Data Lake in S3** 
1. Do you query by time ranges? Organize your S3 by YYYY/MM/DD/something 

## [79 AWS Glue Studio](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45285265#notes)

1. Visual job editor for ETL 
1. Visually 
    1. Create DAGs for complex workflows 
    1. Pick data from - S3, JDBC, Kinesis, Kafka 
    1. Work on the data - sample, join, transform etc. 
    1. Put data in - S3, Glue Data Catalog 
    1. ??? Support partitioning 
    1. Supportability - overview, status, run times. 

## [80 AWS Glue Data Quality](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45285281#notes)

1. Some check fails? Fail the job Or go ahead but log in CloudWatch. 
1. Have the rules made automatically, also. Apart from manually coding them. 
1. You want to write manually? Then use **Data Quality Definition Language(DQDL)**. 

## [81 AWS Glue DataBrew](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45285287#notes)

1. UI for pre-processing large dataset. 
1. Input (S3, database etc. ) - Output (S3 only)
1. 250 ready made transformations 
1. Join different transoformations to come up with your own **recipes** of transformation. 
1. The recipes can become **jobs** within a larger project. 

1. May define data quality rules. 
1. Custom SQL - Redshift , Snowflake. 

1. Security with Glue Data brew 
    1. IAM 
    1. SSL in transit 
    1. CloudWatch and CloudTrail 
    1. Can integrate with KMS (??) 

1. Cost - $1 per interactive session. As a job it is charged in node hour. 


## [PII in DataBrew](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45285349#notes)

1. Delete it. 
1. Mask it. 
1. Encrypt. 
    1. Detereministic. 
    1. Probabilistic. 
1. Hashing 
1. Replace with random 
1. Shuffle 




## SageMaker Training Jobs 

1. Question 
    1. Your team is building a recommendation system for an e-commerce platform. Which SageMaker feature would help you efficiently handle and scale the training of your machine learning model?
    1. SageMaker Training Jobs are designed to scale the training of machine learning models, making it the right choice for building a recommendation system.

## SageMaker Model Monitor 

1. A financial institution wants to detect anomalies in transaction data to identify potential fraud. Which AWS service could you use to deploy an outlier detection model, and monitor its performance over time?
1. SageMaker Model Monitor is designed to track model performance, detect anomalies, and ensure that the deployed models continue to perform as expected.

## SageMaker Clarify

1. Your company is developing a machine learning model to predict customer churn, but you’re concerned about potential bias in the model’s predictions. Which SageMaker feature helps detect and mitigate bias during model training?
1. SageMaker Clarify is specifically designed to detect, explain, and mitigate bias in machine learning models, making it the right choice for this scenario.

## SageMaker Neo 

1. You are tasked with deploying a machine learning model to edge devices in a factory. Which SageMaker feature would you use to optimize and deploy the model efficiently?
1. SageMaker Neo is designed for optimizing and deploying models on edge devices, making it the perfect choice for this task.

## SageMaker GroundTruth 

1. **Question** A healthcare company needs to label large amounts of medical images for training a diagnostic AI model. Which SageMaker service would streamline this process by managing the labeling tasks?
1. SageMaker Ground Truth is designed to manage and streamline the labeling of datasets, making it ideal for large-scale labeling tasks like this.

## SageMaker Studio 

1. **Question** A data scientist wants to experiment with different machine learning algorithms and compare their performance on a dataset. Which SageMaker feature provides an environment for such experimentation?
1. SageMaker Studio is an integrated environment where data scientists can experiment with different algorithms, track experiments, and compare their performance, making it the best choice for this task.

## imputation Techniques 

1. **Question** You are working with a dataset that contains several missing values in a column representing customer ages. The data is relatively small, and the distribution of ages is skewed by a few extreme outliers. Which imputation technique should you choose to fill in the missing values?
1. **Median replacement** is a better choice in this scenario as it is less affected by extreme outliers, providing a more accurate central tendency for imputation.
1. No. **Mean** will not work since there are some extreme numbers and the mean would be distorted. 
1. No. **drop** will not work since there are too less data anyway. 
1. No. **Dropping** rows might be considered if the missing data is minimal and the sample size is large enough, but it is not ideal for preserving data integrity.
1. No. **Mode** Mode replacement is generally used for categorical data, not continuous data like ages, so it wouldn’t be suitable here.



## Synthetic data / Synithetic Minority Over-sampling Technique (SMOTE) 

1. **Question** Your machine learning model is struggling to accurately predict a rare event, such as equipment failure, which occurs in less than 1% of your dataset. You want to generate synthetic samples to balance the dataset without simply duplicating existing data. Which technique should you use?
1. SMOTE generates synthetic samples by interpolating between existing minority class examples, helping to balance the dataset without duplication.


## AWS Managed AI services 

1. [85 Why AWS Managed AI services?](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356791#notes)

## What are the AWS managed AI services available? 
1. **Pre trained ML services. Ready to go**
    1. SageMaker Jumpstart - ?? 
    1. Amazon Bedrock - hugging face ?
    1. Amazon Q Business ? 
    1. Amazon Q Developer ? 
1. **text and documents** 
    1. Comprehend - ?? 
    1. Translate - ?? 
    1. Textract - 
1. **images** 
    1. Rekognition 
1. **search** 
    1. Kendra 
1. **speech** 
    1. Polly 
    1. Transcribe 
1. **chatbots** 
    1. Lex 
1. **recommendation** 
    1. Personalize 

## What is the benefit of using AWS Managed AI services? 

1. Redundancy and regional coverage - across multiple Availability Zones (AZ) and regions. 
1. Specialized hardware (CPU and GPUs) for specific use case 
1. Token based pricing. Pay as you go. 

## [86 Amazon Comprehend, fully managed serverless NLP](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356799#notes)

1. Natural Language Processing (NLP) tool and 
1. Text Analytics
1. Usage : sentiment analysis of emails. 
1. group customer emails based on categories - support request, billing request, etc. 
1. Training data > S3 > Comprehend > custom classifier 
    1. new document > cusomtom classifier > looks like a "complaint", "support request", "billing request" etc. 
    1. Can be both synchronous real time (single document) or async. 

1. **Named Entity Recognition (NER)**
1. **Custom Entity Recognition(CER)**

## [88 Amazon Translate](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356807#notes)

1. Language translation service
1. Handles languages and moods as well - can do formal or informal tone translate. 

## [90 Amazon Transcribe, speech to text](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356813#notes)

1. Deep learning process 
1. Automatic Speech Recognition (ASR) is used to do the transcribe. 
1. Remove PII by Redaction 
1. Speaking in multiple lanaguages? No problem. Automatic detection and handling. 
1. Usage 
    1. Transcribe customer calls 
    1. Automate close captioning / subtitling 
    




