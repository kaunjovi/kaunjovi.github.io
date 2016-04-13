---
layout:     post
title:      Angularjs
date:       2016-03-06 
summary:    Getting started Angularjs. Just pure vanilla stuff. 
categories: howto angularjs
---

AngularJS is a very powerful JavaScript Framework. It is used in Single Page Application (SPA) projects.

### Write a vanilla angularjs 
  * Create a HTML file
  * Add angularjs file to your HTML 
  * Declare an app
  * Inside the app, create a model 
  * Display the model. 


The total code 

```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Playing with Angular.js</title>
<script
    src="http://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js"></script>
</head>
<body>

<h1>Hello world.</h1>

<div ng-app="">
<input type="text" ng-model="name">
Hello {{name}}.   
</div>

</body>
</html>
```

You can initialize models. 

```
<div ng-app="" ng-init="firstName='John'">
```

### Expressions
  * You could run maths 
  * AngularJS expressions do not support conditionals, loops, and exceptions, while JavaScript expressions do.
  * AngularJS expressions support filters, while JavaScript expressions do not.

```
<p>My first expression: {{ 5 + 5 }}</p>
```

### Application (or as they call it, Module)
  * You could name your app and put a controller to home the js code. 

```
<div ng-app="myApp" ng-controller="myCtrl">
```

And put some code in the app and controller. 

```
<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.firstName= "John";
    $scope.lastName= "Doe";
});
</script>
```

### Directives 

  * [List of directives in Angularjs](http://www.w3schools.com/angular/angular_ref_directives.asp)
  * That is not the official one. Find that and share here. //TODO: 

### AngularJS Services

  * http://www.w3schools.com/angular/angular_services.asp
  * a service is a function, or object
  * $location - 
  * $http is an AngularJS service for reading data from remote servers.

### Arrays in AngularJs

```
points=[1,15,19,2,40]

{{ points[2] }}

names=['Jani','Hege','Kai']

<li ng-repeat="x in names">

/* Let's handle some arrays.  */
$scope.arrayOfNames = ['mishtu', 'sorous'] ;


<!-- Let's handle some arrays.  -->
<h3>Names from an array</h3>
<ul>
<li ng-repeat="name in arrayOfNames">{{name}}</li>
</ul>


```

//TODO: Autocomplete of AngularJs. Eclipse is not quite good. 



### Ref
  * http://www.w3schools.com/angular/
  * http://www.w3schools.com/angular/angular_intro.asp
  * http://www.w3schools.com/angular/angular_expressions.asp
  * http://www.tutorialspoint.com/angularjs/



[Hosted js libraries with Google](https://developers.google.com/speed/libraries/#libraries)

Add AngularJs to HTML

```
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.9/angular.min.js"></script>
```

Create an app. 

```
<body ng-app = "myapp">
</body>
```

Create a view 

```
<div ng-controller = "HelloController" >
   <h2>Welcome {{helloTo.title}} to the world of Tutorialspoint!</h2>
</div>
```

Create a controller and model 

```
<script>
   angular.module("myapp", [])
   
   .controller("HelloController", function($scope) {
      $scope.helloTo = {};
      $scope.helloTo.title = "AngularJS";
   });
</script>
```

//TODO: Ng+Leaflet Application

//TODO: Ng+D3 Application 
http://www.ng-newsletter.com/posts/d3-on-angular.html
Scalable Vector Graphics (SVG)

Reference 
[Nice. But there should be a easier way to marry D3 with Angular](http://briantford.com/blog/angular-d3)
[Nice. But too complicated](http://www.sitepoint.com/creating-charting-directives-using-angularjs-d3-js/)


[Nice way to show the list of blogs.Simple and effective. Like the fact that he could show up the blogs that were shown somewhere else as well.](http://briantford.com/blog/)


<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.9/angular.min.js"></script>

[d3](https://d3js.org)


AngularJs is not all good 
http://tutorials.jenkov.com/angularjs/critique.html

[Things I Wish I Were Told About Angular.js](http://ruoyusun.com/2013/05/25/things-i-wish-i-were-told-about-angular-js.html)

[There is something called Rickshaw. And no, integrating d3 is not going to be very easy](http://tagtree.tv/d3-with-rickshaw-and-angular)

Contact me 
https://www.codeschool.com with github account 



### Get some songs. 
https://www.youtube.com/watch?v=d59zN-ZwX2k
https://www.youtube.com/watch?v=1VV2P71NstI


### Javascript 

http://javascript-roadtrip.codeschool.com/levels/1/challenges/1

Numbers 
Plus, Minus, Multiplication, Division and Modulo 
PEMDAS 
>, <, ==, !=, >=, <= 

Strings 
+, ==, != 
"abra".length
"ca".charAt(1)


Variables 
++, --

JS file 

```
<script src="application.js"></script>
```

JS while loop 
```
while(true){...}
```

JS for loop 
```
for(var counter = 10 ; counter >= 1 ; counter--){
  console.log(counter) ; 
}
```

```
var numSheep = 4;
var monthsToPrint = 12;
for (var monthNumber = 1 ; monthNumber <= monthsToPrint ; monthNumber++){
  numSheep = numSheep * 4;
  console.log("There will be " + numSheep + " sheep after " + monthNumber + " month(s)!");
}
```


```
var currentGen = 1;
var totalGen = 19;
var totalMW = 0;
while(currentGen<=4) {
  totalMW += 62 ; 
  console.log("Generator #"+currentGen+" is on, adding 62 MW, for a total of "+totalMW+" MW!"); 
  currentGen++; 
}
for(;currentGen<=totalGen;currentGen++){
  totalMW += 124 ; 
  console.log("Generator #"+currentGen+" is on, adding 124 MW, for a total of "+totalMW+" MW!");   
}
```



### Find home for the following 

Software engg have it tough. Or do they? https://m.signalvnoise.com/writing-software-is-easy-bcb77aa6bea1#.wkozqpohb

We all know these meetings, and we all hate them, but they still are there. Why? http://thehiggsweldon.com/thinking-inside-the-bubble/

Mr. Arkle? Teaching english writing. ?? 

To be happy, to have purpose, you must create. https://medium.com/life-learning/haters-gonna-hate-creators-gonna-create-5a6d9a701f21#.721dzz1tf

Well done, yo millennial. https://medium.com/slackjaw/good-job-millennials-56494aad19f8#.8xy09idkz

What is your street cred? https://medium.com/@kim617/yes-i-want-to-help-you-get-hired-beab89326192#.p80bov57o


TechCrunch articles. 


LinkedIn. Does it have a dev api that I can use? 

  LinkedIn Javascript API
  https://www.youtube.com/watch?v=bbu8JhqiOZA

  Linked In API Java Tutorial Part 1
  https://www.youtube.com/watch?v=eWgTg4ONEHU

  http://postimg.org/image/c23ds2wvx/


We want more than money :) 
https://medium.com/life-learning/what-we-want-more-than-money-b69801829e89#.7nb9yvckj

Yet another Spring Boot Application (Part 1)
https://medium.com/java-user-group-malta/yet-another-spring-boot-application-part-1-a6a26d7c036d#.rfjtimoht

Spring Boot: REST + TDD from scratch
https://medium.com/@krebs.bruno/spring-boot-rest-tdd-from-scratch-15f13ed799e0#.mg44l0lor



ScribeJava

<dependency>
  <groupId>com.github.scribejava</groupId>
  <artifactId>scribejava-apis</artifactId>
  <version>2.2.2</version> // please use always the latest version
</dependency>


Setting up Spring Boot
pom.xml file

https://medium.com/@krebs.bruno/spring-boot-rest-tdd-from-scratch-15f13ed799e0#.mg44l0lor

lin benjamin 
niraj gilja 
iasello, anthony p 
tolani, rajesh 

herman,
nirav 
sandeep and neelam 










