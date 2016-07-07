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
  - Cassandra descends from both Bigtable and Amazon's Dynamo
  - Cassandra has implemented CQL (Cassandra Query Language), the syntax of which is obviously modeled after SQL.
  - [Cassandra Stays Ahead Of The NoSQL Pack](http://www.networkworld.com/article/2222246/opensource-subnet/cassandra-stays-ahead-of-the-nosql-pack.html)


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

### HBase vs. Cassandra

  - HBase, like Cassandra a column-oriented key-value store.
  - HBase might be fit for Search engines, Analysing log data, Any place where scanning huge, two-dimensional join-less tables are a requirement. 
  - HBase describes itself as an "open source Bigtable implementation."
  - [Big data showdown: Cassandra vs. HBase](http://www.infoworld.com/article/2610656/database/big-data-showdown--cassandra-vs--hbase.html)

### Column oriented database 

  - Data is apparently arranged initially by row, and a table's primary key is the row key. 
  - However, unlike a relational database, no two rows in a column-oriented database need have the same columns. 
  - You can add columns to a row on the fly (after the table has been created). 


### Working of column oriented db e.g. Cassandra, HBase etc 

  - Write paths begin with logging write operations to a log file to ensure durability. 
  - Even if the remainder of the write fails, the operation saved in the log can be replayed. 
  - Next, the data is written to a memory cache. 
  - Then finally to disk via a large, sequential write (essentially a copy of the memory cache). 
  - The overall memory-and-disk data structure used by both Cassandra and HBase is more or less a log-structured merge tree. 
  - The disk component in Cassandra is the SSTable; in HBase it is the HFile.

### NoSQL comparison

  - [A vendor-independent comparison of NoSQL databases: Cassandra, HBase, MongoDB, Riak](http://www.networkworld.com/article/2160905/tech-primers/a-vendor-independent-comparison-of-nosql-databases--cassandra--hbase--mongodb--riak.html)
  - Column family store 
    - HBase
    - Cassandra
  - Document-oriented database 
    - MongoDB 
  - Key-value store
    - Riak

### Internal working of Cassandra 

  - https://academy.datastax.com/resources/brief-introduction-apache-cassandra
  - In Cassandra, all nodes play an identical role; there is no concept of a master node. 
  - With all nodes communicating with each other via a distributed, scalable protocol called "gossip."
  - Cassandra’s built-for-scale architecture means that it is capable of handling large amounts of data and thousands of concurrent users or operations per second—​even across multiple data centers—​as easily as it can manage much smaller amounts of data and user traffic. 
  - To add more capacity, you simply add new nodes to an existing cluster without having to take it down first.
  - Cassandra’s architecture also means that, unlike other master-slave or sharded systems, it has no single point of failure and therefore is capable of offering true continuous availability and uptime.

### Writing data on a Cassandra node. 

  - Data written to a Cassandra node is first recorded in an on-disk commit log
  - then written to a memory-based structure called a memtable. 
  - When a memtable’s size exceeds a configurable threshold, the data is written to an immutable file on disk called an SSTable. 
  - Buffering writes in memory in this way allows writes always to be a fully sequential operation, with many megabytes of disk I/O happening at the same time, rather than one at a time over a long period. 
  - Because of the way Cassandra writes data, many SSTables can exist for a single Cassandra logical data table. A process called compaction occurs on a periodic basis, coalescesing multiple SSTables into one for faster read access.
  - https://academy.datastax.com/resources/brief-introduction-apache-cassandra

### Reading data from Cassandra node. 

  - Cassandra consults an in-memory data structure called a Bloom filter that checks the probability of an SSTable having the needed data. 
  - The Bloom filter can tell very quickly whether the file probably has the needed data, or certainly does not have it. If answer is a tenative yes, Cassandra consults another layer of in-memory caches, then fetches the compressed data on disk. 
  - If the answer is no, Cassandra doesn’t trouble with reading that SSTable at all, and moves on to the next.
  - https://academy.datastax.com/resources/brief-introduction-apache-cassandra





