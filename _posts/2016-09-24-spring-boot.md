---
layout:     post
title:      Spring Boot
date:       2016-09-24
summary:    Notes on Spring Boot
categories: notes Spring Boot
---

[Link to self](http://kaunjovi.github.io/notes/spring/boot/2016/09/24/spring-boot/)

### Reference 
  - [Nice writeup. Why Spring Boot?](https://dzone.com/articles/why-springboot)
  - [For when you have time. Spring Boot Reference Guide](http://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle/)
  - [For when you have time. Source code. And good documentation.](https://github.com/spring-projects/spring-boot)
  - [Learn Spring Boot](https://github.com/kaunjovi/learnSpringBoot)


### [Building an Application with Spring Boot](https://spring.io/guides/gs/spring-boot/)
  - Create src/main/java/hello 
  - In pom.xml
    + Add Spring Boot Maven plugin 
      * Builds a single uber jar. Should this be more cloud friendly then? 
  - Create a controller class which is ```@RestController```
  - Create a method. Mark it as ```@RequestMapping("/")```
  - Create a ```MyApplication``` class. Mark it ```@SpringBootApplication```. It contains. 
    + Add a few ...
    + ```SpringApplication.run()``` launches the current class as application. 
  - Compile and run 
    + ```mvn package && java -jar target/gs-spring-boot-0.1.0.jar```
  - Unit test the stuff 
    + You need this one ```spring-boot-starter-test```
    + read more ... 
  - Integration tests 
    + This is also interesting. //TODO: read and make notes. 
  - ```-e clean install exec:java -Dexec.mainClass="fun.and.games.MyApplication"```