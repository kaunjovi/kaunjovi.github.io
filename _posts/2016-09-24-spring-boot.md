---
layout:     post
title:      Spring Boot
date:       2016-09-24
summary:    Notes on Spring Boot
categories: notes Spring Boot
---

### [Building an Application with Spring Boot](https://spring.io/guides/gs/spring-boot/)
  - Create src/main/java/hello 
  - In pom.xml
    + Add Spring Boot Maven plugin 
      * Builds a single uber jar. Should this be more cloud friendly then? 
  - Create a controller class which is ```@RestController```
  - Create a method. Mark it as ```@RequestMapping("/")```