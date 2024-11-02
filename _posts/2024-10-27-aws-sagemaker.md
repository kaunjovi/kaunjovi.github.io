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










## Find own space [Exam Guide](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45320497#notes)

1. Exam about details of the components. Not about designing and architecting. We will need to get to that as well. Soon. 
1. Question types 
    1. Multi choice - one out of 4. 
    1. Multi response - many out of 5 or more.  
    1. Ordering - 3 to 5 correct. and correct ordering. 
    1. Matching - 3 to 7. 
    1. Case study - one case study. multiple questions based on that. 
    1. No negative marking - guess please. Prep so you dont have to. 
1. 1000 - 720 passing marks 
1. Domains 
    1. Data preperation - 28% 
    1. ML model dev - 26% 
    1. Deployment and orch - 22% 
    1. monitoring, maintenance, security - 24% 
1. Take p/o of the course, and those that we need twitter update for. 

1. **more material** if you have time
1. [SageMaker Developer guide](https://docs.aws.amazon.com/sagemaker/) 
    1. [pdf](https://gmoein.github.io/files/Amazon%20SageMaker.pdf)

1. 3 hours. 65 questions (85 during beta)
1. flag the ones that you want to come back and recheck 




