---
layout:     post
title:      Notes on Docker
date:       2016-04-24
summary:    Notes on Docker
categories: notes docker
---

Python
  
  Can Python be coded on Mac, using Xcode?
    https://hackercodex.com/guide/python-development-environment-on-mac-osx/
    http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/
    (too old)[https://jakevdp.github.io/blog/2013/02/02/setting-up-a-mac-for-python-development/]
    [too old](https://jakevdp.github.io/blog/2013/02/02/setting-up-a-mac-for-python-development/)

  Can Python be coded on Mac? 
    https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/

  Python with Sublime 3? 
    - https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/

  Can Python read Excel files? 
    http://stackoverflow.com/questions/22169325/read-excel-file-in-python
    https://automatetheboringstuff.com/chapter12/

The openpyxl module allows your Python programs to read and modify Excel spreadsheet files. 
  workbook 
  worksheet 
  active sheet 

```
import openpyxl
```




Read these 
http://martinfowler.com




http://www.completeitprofessional.com/7-things-that-should-be-on-your-linkedin-profile/?utm_content=buffer061bf&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer






https://www.thoughtworks.com/radar




### How much EMI do you have to pay? 
http://emicalculator.net
http://www.businesstoday.in/opinion/columns/arvind-jain-pride-group-on-closing-home-loan-early/story/205706.html
http://www.nitinbhatia.in/home-loan/prepay-home-loan/

18002085959 

9212 084 304

admin admin 
postpaid 

setting lan 


http://iconnect-ap.jpmchase.com
https://appsphere.jpmchase.com/vpn/appsphere.html


### Getting started with TS. 
https://cmatskas.com/getting-started-with-typescript-and-sublime-text/

```
$ node -v 
v4.2.3
$ npm -v 
2.14.7
```

```
sudo npm install -g typescript
npm list -g typescript 
```

Typescript plugin from Microsoft 
package control 


http://amanvirk.me/setting-up-typescript-for-sublime-text-on-mac/
https://blogs.msdn.microsoft.com/typescript/2015/06/05/developing-in-typescript-on-a-mac-with-sublime/



### Angular 2 

  - https://angular.io
  - same for mobile and desktop


### Rent vs Buy 

  - http://makaanvalue.com


### HBase 

  - [Home page.](https://hbase.apache.org)
  - [Bigtable](http://research.google.com/archive/bigtable.html)
  - [Installing on mac](https://github.com/hixiaoxi/hixiaoxi.github.io/wiki/Installing-HBase-on-Mac-OS-X-(10.8))
    + Install Hadoop 
    + Install HBase 
    + Install Phoenix 


# Install Hadoop on Mac 

  - [INSTALLING HADOOP ON MAC PART 1](https://amodernstory.com/2014/09/23/installing-hadoop-on-mac-osx-yosemite/)
  - Install HomeBrew 
  - Install Hadoop using HomeBrew 
  - [Configure Hadoop](https://dtflaneur.wordpress.com/2015/10/02/installing-hadoop-on-mac-osx-el-capitan/)


```bash

$ brew --version 
Homebrew 0.9.5 (git revision 92c6c; last commit 2015-09-22)

$ hadoop version 
Hadoop 2.7.1
Subversion https://git-wip-us.apache.org/repos/asf/hadoop.git -r 15ecc87ccf4a0228f35af08fc56de536e6ce657a
Compiled by jenkins on 2015-06-29T06:04Z
Compiled with protoc 2.5.0
From source with checksum fc0a1a23fc1868e4d5ee7fa2b28a58a
This command was run using /usr/local/Cellar/hadoop/2.7.1/libexec/share/hadoop/common/hadoop-common-2.7.1.jar
$ 


```

## take Hadoop for a spin

```
hstart /usr/local/Cellar/hadoop/2.7.1/libexec/etc/hadoop
hstop 

```



random, realtime read/write access to your Big Data
hosting of very large tables -- billions of rows X millions of columns -- atop clusters of commodity hardware



### Docker

  - Docker is a container manager.
  - Docker is an engine to package an individual application system to run in its own particular environment.
  - Docker is NOT a virtualization solution. 

### How is Docker useful for cloud computing enablers like Google cloud computing? 


Could not understand it well, but there was something interesting here. 
// TODO : Come back 
https://hub.docker.com/_/java/

### Installing Docker on OSX. 

  - You might need to install boot2docker. 
  - [How to install Docker on OSX](https://docs.docker.com/engine/installation/mac/#installation)


```

                        ##         .
                  ## ## ##        ==
               ## ## ## ## ##    ===
           /"""""""""""""""""\___/ ===
      ~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
           \______ o           __/
             \    \         __/
              \____\_______/


docker is configured to use the default machine with IP 192.168.99.100
For help getting started, check out the docs at https://docs.docker.com

$ 

```

### Verify that Docker got installed properly. 

docker run hello-world

### What is this yml file all about? 
TODO 





### Thanks to 

  - [Docker for Java Developers](http://zeroturnaround.com/rebellabs/docker-for-java-developers-how-to-sandbox-your-app-in-a-clean-environment/)
