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
        1. Try - retries with backoff - retry after 2 seconds, then 4 seconds, then 8 seconds and so on. 
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





1. **Resources** 
1. [Kinesis Data Streams](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356719#notes)
