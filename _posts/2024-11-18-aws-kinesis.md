---
layout: post
title: AWS Kinesis Data Streams 
categories: [AWS, Kinesis] 
---


1. **Kinesis Producers**
1. SDK
    1. 3rd parties can use this SDK to send data 
    1. Spark, Log4j, Kafka, Nifi etc. 
1. Kinesis Producer Library (KPL)
1. Kinesis Agents - programs running on servers, sending data such as logs etc. to Kinesis Data Streams. 

## Kinesis Producers / SDK
1. **PutRecord** 
1. **PutRecords** - use batching to increase througput. Less HTTP requests. 
1. Too many data being sent? **ProvisionedThroughputExceeded** 
    1. You are exceeding the MBPS ( 1 MBPS per shard)
    1. Or, exceeding the records ( 1000 messages per second per shard)
    1. Check for **hot shard** - did you somehow mess up with the partitionin keys that you created. 
        1. Is your partition key deviceid for example - and most of uers iphone users - 90% of your messages will go into the same shard. 
    1. Solution
        1. Fix your partition 
        1. Try - retries with backoff - retry after 2 seconds, then 4 seconds, then 8 seconds and so on. **exponential backoff**
        1. Increase the number of shards 

1. Use case 
    1. low througput, high latency 
    1. simple API, AWS lambda etc. 
1. AWS services that uses SDK behind the scenes 
    1. Kinesis Data Analytics 
    1. CloudWatch logs 
    1. AWS IoT 
     
## Kinesis Producers / Kinesis Producer Library (KPL)
1. https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356725#notes
1. C++/Java Library - high performance, long running producers - automated and configurable retry mechanism. 
1. Synchronous API - same as SDK 
1. Asynchronous API - better peroformance 
    1. submits metrics to CloudWatch 
1. NO compression out of the box though. 
1. The Record is stored - not in plain text. It needs to be decoded by KCL (??)
1. Batching 
    1. Collect Recoreds and write to different shards in the same PutRecords call 
    1. Wait and Aggregate - increased latency but decreased cost - bling bling 
        1. Put multiple records in one record - and hence you can bypass the 1000 records per second limit ) 
        1. Increased payload. Hit the 1MB/S more 
1. **How does batching work?**
1. KPL waits for **RecordMaxBufferedTime** to collect enough records so that the aggregation is almost 1 MB (which is the max size it can send)
1. Then it collects a few of these aggregated records and uses PutRecords to send all of them together. 
1. **When not to use KPL and use SDK instead**? 
1. We cant wait for the delay. Some real time use case. 
1. We dont mind the intermediate updates. Just want the lates and most relevant. E.g. if the IoT was offline and we want the latest data only when it comes online. 

## Kinesis Producers / Kinesis Agent 
1. Java based. Built on top of KPL. 
1. Installed in **Linux based servers** only to send log files (etc.) to Kinesis Data Streams. 
1. Benefits - it is built for the logs 
    1. Can write from multiple directories to multiple Streams
    1. handles log file roation (?), checkpointing (?), retry upon failures 
    1. pre-process log files - csv to json, log to json etc. 
    1. Emits metrics to CloudWatch for monitoring 
    1. You want aggregation of logs, in mass ? Use this.  

## How to scale up Kinesis? Increase throuhput.  

1. https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356743#notes
1. **Shard splitting** 
1. Just split the existing one. In the same space as the old one, you will get two (or can I get more??)
1. One shard - 1MB/s/shard. N shards = N MB/s. 
1. Is there a "hot shard" - all Records are going to that one ? 
    1. Just split the "hot shard". 
1. Once you "split" a shard - the old shard is closed and deleted once the data in it expires - and what is the new ?? 


## How to scale down Kinesis? Decrease throughput, probably to save some $$. 

1. Mrege two. same thing as above. The old one will be closed and deleted after data expiry. 

## In which scenario could you receive data out of sequence. Out-of-order records. 

1. After resharding - if the consumer starts reading from the new shard before all the records are read from the parent shard - consumer may get out-of-order records. 
1. KCL has the logic built in - it finishes reading all the messages from parent shard before reading from the new ones. 
1. If you are building your own consumer using SDK, please handle it yourself. 
1. [click here](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356743#notes)

## Can you scale up or down the number of Kinesis shards automatically? 

1. There is no inherent feature. You will have to make and API call to **UpdateShardCount**. 
1. Might be - use AWS labda to do something like that. 
1. [depreccated : Auto scaling Amazon Kinesis Data Streams using Amazon CloudWatch and AWS Lambda](https://aws.amazon.com/blogs/big-data/auto-scaling-amazon-kinesis-data-streams-using-amazon-cloudwatch-and-aws-lambda/)
1. [Amazon Kinesis Data Streams On-Demand](https://aws.amazon.com/blogs/aws/amazon-kinesis-data-streams-on-demand-stream-data-at-scale-without-managing-capacity/)
1. [Amazon Kinesis Data Streams | Easily stream data at any scale](https://aws.amazon.com/kinesis/data-streams/)
1. **Limitations of resharding / scaling of Kinesis data streams**
1. Resharding has to be done one at a time and it takes a few seconds to do it. 
1. So, to double 1000 shards, it might take 30X1000 seconds = 8.3 hours. So, plan in advance. 


1. **Is it possible to have duplicate data in Kinesis Data Streams?**
1. **How might a Kinesis Data Stream end up having duplicate data?**
1. **What is the definition of duplicate data in Kinesis Data Streams?** 


1. **What are the scenarios that consumer side can read same data multiple times from Kinesis?** 
1. There are 4 cases 
    1. Application deploye - so worker added  
    1. worker added or deleted.
    1. a worker terminates unexpectedly - so worker deleted 
    1. sharding has happened 
1. **How to solve for duplicate reads from Kinesis?** 
1. De-duplicate in the consumer please. Kinesis cant handle. 
1. Make it idempotent - or do whatever it takes, Kinesis cant handle. 
1. [AWS | Handle duplicate records](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-duplicates.html)
1. [Udemy | click here](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356747#notes)

1. **What sort of security mechanisms are available to ensure that usage of Kinesis does not add any security hole in the architecture**? 
1. IAM - access and authorization 
1. HTTPS - Encryption in transit 
1. KMS (??) - Encryption at rest 
1. Client side - buddy, now you are pushing it. Do it yourself. 
1. VPC endpoints - for usage from your own private network i.e., VPC 
1. [click here](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356749#notes)

## Kinesis Data Firehose (KDF)
1. Write data into something. Load data into **Redshift, S3, Splunk, OpenSearch**
1. Fully managed. Lot of $$ ? 
1. Near real time. 
1. Automatic scaling. 
1. Many data formats. Data conversion from JSON to Parquet / ORC (only for S3)
1. More data conversion? Use Lambda. CSV to JSON. 
1. **watch out** Spark, KCL, cant read from KDF. 

## Kinesis Data Firehose (KDF) / buffer sizing 
1. Get data. Put in a buffer. Flush the buffer only if - time rule - size rule. 
    1. Buffer size - 32 MB - reached? flush 
    1. Buffer time - 2 mins - done waiting? flush - min time that can be set is 1 min 
    1. Can automatically increase buffer size to increase throughput. 
1. [Udemy | click here](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356757#notes)

## Kinesis Data Streams (KDS) vs. Kinesis Data Firehose (KDF)

1. Streams 
    1. Producer (need to be written) - streams - Consumer (need to be written)
    1. Data transmission is real time (200ms for classic. 70ms for enhanced fan-out)
    1. Data available for 1 to 365 days. Replay. Multi consumer. 
    1. No autoscaling. Shard splitting. Shard merging. 
1. KDF 
    1. Fully managed. Auto scaling. Send data to S3, Redshift, Splunk, OpenSearch 
    1. **Near** real time - NOT real time. 
    1. No data storage. 
    1. Need code transformation ? Use lambda. 
1. [Udemy | click here](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356757#notes)

## Kinesis Data Streams (KDS) | issuues and solutions
## Kinesis Data Streams (KDS) | issuues and solutions

1. Writing too slow. 
    1. Hot shard? Select partition key to distribute load evenly. 
    1. Are you pobably hitting the capacity? Check for **ProvisionedThroughputExceeded** 
    1. What is slow? There are stream level limits as well. CreateStream, Describ
1. 500 or 503 error 
    1. implement retry mechanism
1. Connection errors between Flink and Kinesis 
    1. Not enough resource on Flink 
    1. network issue. 
    1. VPC misconfiguration 


## Kinesis Data Streams (KDS) | issuues and solutions | Consumer 

1. [Udemy | click here](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45284803#notes) 


https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45284803#notes

1. [click here](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356757#notes)



1. **Resources** 
1. [Kinesis Data Streams](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356719#notes)
