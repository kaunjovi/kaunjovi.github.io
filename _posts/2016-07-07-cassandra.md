---
layout:     post
title:      Cassandra
date:       2016-07-07 
summary:    Introduction to cassandra
categories: howto cassandra
---

### What is the most popular database? 
http://db-engines.com/en/ranking

### [Cassandra](http://cassandra.apache.org)

  - Scalable, Available, Performant 
  - Supports column indexes
  - Best replication across data centers. 


### Cassandra is good for. 

  - Cassandra Scales linearly with massive write.
  - Cassandra's storage engine provides constant-time writes no matter how big your data set grows. 
  - Cassandra is an excellent choice for real-time analytic workloads
  - Cassandra can be integrated with Hadoop, Hive and Apache Spark for batch Processing
  - http://blogs.shephertz.com/2015/04/22/why-cassandra-excellent-choice-for-realtime-analytics-workload/
  - http://stackoverflow.com/questions/2892729/mongodb-vs-cassandra

### What is the use case for Cassandra? 

### Where is Cassandra not applicble? 

### "Hello world" with Cassandra. 

### CQL (Cassandra Query Language)

### Use java to read from Cassandra. 
http://www.tutorialspoint.com/cassandra/cassandra_read_data.htm


### When to use RDBMS instead of Cassandra? 

  - Cassandra is based on NoSQL database and does not provide ACID and relational data property. If you have strong requirement of ACID property (for example Financial data), Cassandra would not be a fit in that case. 
  - http://stackoverflow.com/questions/2634955/when-not-to-use-cassandra

### What are the uses of different NoSQL databases? 

  - MongoDB is fit for usecases where your system demands schema-less document store. 
  - Redis is built to provide In-Memory search for varieties of data structures like tree, queue, link list etc and can be good fit for making real time leaderboard, pub-sub kind of system. 
  - Similarly there are other database in this category (Including Cassandra) which are fit for different problem statement.
  - Being a part of NoSQL family Cassandra offers solution for problem where your requirement is to have very heavy write system and you want to have quite responsive reporting system on top of that stored data.
  - http://stackoverflow.com/questions/2634955/when-not-to-use-cassandra

### Column oriented key-value store 

  - Cassandra 
  - HBase

### Hazelcast vs. Cassandra

  - https://hazelcast.com/use-cases/nosql/apache-cassandra-replacement/
  - https://mpouttuclarke.wordpress.com/2013/12/12/titan-cassandra-vs-hazelcast-persistence-benchmark/
  - Hazelcast is ten times faster than Cassandra on reads and faster also on writes

### HBase 

  - HBase, like Cassandra a column-oriented key-value store.
  - HBase might be fit for Search engines, Analysing log data, Any place where scanning huge, two-dimensional join-less tables are a requirement. 





