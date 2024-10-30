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

