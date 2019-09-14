---
layout:     post
title:      Logging in Java
date:       2019-09-14 
summary:    Making logging effective and effortless
categories: howto 
---

## Logging in Java using SLF4J and log4j, in Eclipse. 

### Add gradle dependency

```code
testCompile group: 'org.slf4j', name: 'slf4j-log4j12', version: '1.7.28'
```

### Add log4j.properties

- src/test/resources/log4j.properties

```code 

log4j.rootLogger=DEBUG,stdout

log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.Target=System.out
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n

And to see log in file  , set log4j.properties 

log4j.appender.file=org.apache.log4j.RollingFileAppender
log4j.appender.file.File=./logs/logging.log
log4j.appender.file.MaxFileSize=10MB
log4j.appender.file.MaxBackupIndex=10
log4j.appender.file.layout=org.apache.log4j.PatternLayout
log4j.appender.file.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n
```

### Add code template in Eclipse to add loggers  

```code
${:import(org.slf4j.Logger,org.slf4j.LoggerFactory)}
private static final Logger LOG = LoggerFactory.getLogger(${enclosing_type}.class);
```

### Finally, you are free to log 

```java
logger.debug("Hello world.");
logger.info("Example log from {}", Example.class.getSimpleName());
```
