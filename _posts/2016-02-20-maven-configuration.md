---
layout:     post
title:      Maven Configuration
date:       2016-02-20
summary:    Maven Configuration. 
categories: howto 
---


### Maven configuration 

  * [Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
  * http://mvnrepository.com/artifact/ch.qos.logback/logback-classic/1.1.5

### Configure Maven to use java 8

```
<build>
    <plugins>
        <plugin>
            <!-- Configure the project to use java 8 version. -->
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.5.1</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
            </configuration>
        </plugin>
    </plugins>
</build>
```

