---
layout:     post
title:      Contact mishtusorous
date:       2016-02-15 
summary:    Talk to me. 
categories: howto 
---

  
### Create a new ssh key 

```
ssh-keygen -t rsa -b 4096 -C "mishtusorous@gmail.com"
pbcopy < ~/.ssh/id_rsa.pub
```

### Get the github.io 

```
  
$ mkdir mishtusorous.github.io
$ cd mishtusorous.github.io

$ git config --global user.name "mishtusorous"
$ git config --global user.email "mishtusorous@gmail.com"
$ git clone git@github.com:mishtusorous/mishtusorous.github.io.git .

$ git add --all && git commit -m "new version" && git push 

```
  
### Hello BigData 

  * [33 Brilliant And Free Data Sources For 2016](http://www.forbes.com/sites/bernardmarr/2016/02/12/big-data-35-brilliant-and-free-data-sources-for-2016/#88155ee67961)
  * 


### News 

  * [MIT News](http://news.mit.edu/2016/quantum-approach-big-data-0125?platform=hootsuite)

### ToRead 

  * [Proven practices for accelerating enterprise analytics adoption](http://public.dhe.ibm.com/common/ssi/ecm/im/en/imw14848usen/IMW14848USEN.PDF)
  * [20 Stupid Claims About Big Data](https://www.linkedin.com/pulse/20-stupid-claims-big-data-bernard-marr)

### Lambda architecture 

  * [Applying the Big Data Lambda Architecture](http://www.drdobbs.com/database/applying-the-big-data-lambda-architectur/240162604)
  * Twitter, Nathan Marz, Storm 
  * New data / batch layer / serving layer (batch view) / query 
  * New data / speed layer (real time view) / query 



### Lambda architecture provides 

  * Robust fault-tolerant system , both against hardware failures and human mistakes (how is that?)
  * Wide range of workloads and use cases, in which low-latency reads and updates are required. 
  * Should support ad-hoc queries.
  * throwing more machines at the problem will do the job.
  * The system should be extensible so that features can be added easily, and it should be easily debuggable and require minimal maintenance.
 
### Read more 

  * https://twitter.com/martinfowler
  * https://twitter.com/KentBeck
  * https://medium.com
  * http://dilbert.com



### Sublime shortcuts 

  * https://www.youtube.com/watch?v=0ZnVBVaQpWs


### Configure blog 


### Examples of blog 

  * https://spring.io/blog | Search 
  



















