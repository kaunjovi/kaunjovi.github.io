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
  - ```mvn -e clean install exec:java -Dexec.mainClass="fun.and.games.MyApplication"```


### Spring Boot, REST and H2. 


<parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>1.3.6.RELEASE</version>
    </parent>

<artifactId>spring-boot-starter-data-rest</artifactId>
<artifactId>spring-boot-starter-data-jpa</artifactId>


<artifactId>h2</artifactId>


<artifactId>spring-boot-maven-plugin</artifactId>


@SpringBootApplication
public class Application {
 
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

mvn spring-boot:run 

curl localhost:8080



@Entity
public class Person {
 
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;



@Entity
public class Person {
 
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;



## Links
  - [The daily WTF](http://thedailywtf.com)
  - [Dilbert](http://dilbert.com)
  - [Twitter](https://twitter.com)    
  - [Stack overflow](http://stackoverflow.com)
  - [Gists](https://gist.github.com/kaunjovi)
  - [Java revisited](http://javarevisited.blogspot.in)
  - [pinterest](https://in.pinterest.com)
  - Slant 
  - 

## Todo 
  - How to get a patent? 
  - 

We need a way to safeguard identity online? 

What the heck is Tor? 


Function



