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
1. Batching 
    1. Collect Recoreds and write to different shards in the same PutRecords call 
    1. Wait and Aggregate - increased latency but decreased cost - bling bling 
        1. Put multiple records in one record - and hence you can bypass the 1000 records per second limit ) 
        1. Increased payload. Hit the 1MB/S more 
1. NO compression out of the box though. 
1. The Record is stored - not in plain text. It needs to be decoded by KCL (??)




1. **Resources** 
1. [Kinesis Data Streams](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45356719#notes)
