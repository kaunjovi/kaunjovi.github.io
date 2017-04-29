---
layout:     post
title:      proto to java
date:       2017-04-29 
summary:    Compile proto file to java using maven. 
categories: howto 
---


# How to compile .proto file into java using maven? 

  - Create a vanilla maven project. 
  - Add [protoc-jar-maven-plugin](https://github.com/os72/protoc-jar-maven-plugin)
  - Remember to add protbuf as well. Else the created java files will complain. 
  - Add a .proto file. 
  - Run ```-e clean install``` and you should have a java file created for you by protobuf. 
  - [The working maven project](https://github.com/kaunjovi/protobuf)

### protoc-jar-maven-plugin 

```
<!-- compile proto file into java files. -->
<plugin>
  <groupId>com.github.os72</groupId>
  <artifactId>protoc-jar-maven-plugin</artifactId>
  <version>3.2.0.1</version>
  <executions>
    <execution>
      <phase>generate-sources</phase>
      <goals>
        <goal>run</goal>
      </goals>
      <configuration>
        <!-- <includeDirectories> <include>src/main/protobuf</include> </includeDirectories> -->
        <inputDirectories>
          <include>src/main/protobuf</include>
        </inputDirectories>
        <!-- Create java files. And put them in the src/main/java directory. -->
        <outputTargets>
          <outputTarget>
            <type>java</type>
            <outputDirectory>src/main/java</outputDirectory>
          </outputTarget>
        </outputTargets>
      </configuration>
    </execution>
  </executions>
</plugin>
```

### protobuf 

```
<!-- protobuf -->
<dependency>
  <groupId>com.google.protobuf</groupId>
  <artifactId>protobuf-java</artifactId>
  <version>3.2.0</version>
</dependency>
```

### proto file

```
syntax = "proto2";

// This is the package where the java source code will be placed. 
option java_package = "le.arn";

// This is the name of the class. 
// If not provided, it will be created as <message name>OuterClass. 
option java_outer_classname = "GreetingProtos";

message Greeting {
  required string greeting = 1;
  
} 
```

