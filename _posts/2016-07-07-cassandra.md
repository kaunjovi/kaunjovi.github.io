---
layout:     post
title:      Cassandra
date:       2016-07-07 
summary:    Cassandra
categories: howto Cassandra
---

# Cassandra 
http://cassandra.apache.org
Scalable, Available, Performant 
Supports column indexes
Best replication across data centers. 


# What does Casssandra do?
Cassandra Scales linearly with massive write.
Cassandra's storage engine provides constant-time writes no matter how big your data set grows. 
Cassandra is an excellent choice for real-time analytic workloads
Cassandra can be integrated with Hadoop, Hive and Apache Spark for batch Processing
http://blogs.shephertz.com/2015/04/22/why-cassandra-excellent-choice-for-realtime-analytics-workload/
http://stackoverflow.com/questions/2892729/mongodb-vs-cassandra

# What is the use case for Cassandra? 
# Where is Cassandra not applicble? 

# When to use RDBMS instead of Cassandra? 
Cassandra is based on NoSQL database and does not provide ACID and relational data property. If you have strong requirement of ACID property (for example Financial data), Cassandra would not be a fit in that case. 
http://stackoverflow.com/questions/2634955/when-not-to-use-cassandra

# What are the competitors of Cassandra? And how do they measure up? 
  - Hazelcast
    - https://hazelcast.com/use-cases/nosql/apache-cassandra-replacement/
    - https://mpouttuclarke.wordpress.com/2013/12/12/titan-cassandra-vs-hazelcast-persistence-benchmark/
    - Hazelcast is ten times faster than Cassandra on reads and faster also on writes


# "Hello world" with Cassandra. 

# CQL (Cassandra Query Language)
# Use java to read from Cassandra. 
http://www.tutorialspoint.com/cassandra/cassandra_read_data.htm

