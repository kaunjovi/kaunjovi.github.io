---
layout:     post
title:      proto serialize
date:       2017-04-29 
summary:    Serialize and De-Serialize java object from file using protobuf. 
categories: howto 
---

# Protobuf for serialization and de-serialization of Java objects.  

  - You need to have the java created by protobuf from proto file. [code here.](https://github.com/kaunjovi/protobuf)
  - Use protobuf builder to create the java. 
  - Use inbuilt ```writeTo(...)``` to save the flattened object in a file. 
  - Use inbuilt ```parserFrom(...)``` to recreate the object from a file. 
  - [The working maven project](https://github.com/kaunjovi/protobuf001)


### Create the java object. 

```java
// 1 : Create a Greeting object using the Protobuf builder.
Builder greetingBuilder = GreetingProtos.Greeting.newBuilder();
greetingBuilder.setGreeting(HELLO_WORLD);
Greeting greeting = greetingBuilder.build();
```

### Serialize the object 

```java 
// 2 : Write the message into a file. Serialize the object.
FileOutputStream output = new FileOutputStream(SER_FILE);
greeting.writeTo(output);
output.close();
```

### De Serialise the object

```java 
// 3 : Deserialize the object from the file.
Greeting greetingFromFile = Greeting.parseFrom(new FileInputStream(
    SER_FILE));
logger.debug("We read this from the file {}", greetingFromFile);

```



