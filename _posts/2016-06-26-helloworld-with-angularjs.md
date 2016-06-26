---
layout:     post
title:      Helloworld with Angularjs
date:       2016-06-26 
summary:    Getting started Angularjs. Just pure vanilla stuff. 
categories: howto angularjs
---


### Write a vanilla angularjs 
  * Create a HTML file
  * Add angularjs file to your HTML 
  * Declare an app
  * Inside the app, create a model 
  * Display the model. 

### Code snippets 


```
<!-- Add the magic. AngularJs that is.  -->
<script 
  type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.7/angular.min.js">
  </script>
```

```
<!-- It is not any old HTML now. It is an angular application  -->
<html ng-app>
```

```
<!-- Add some model -->
<input type="text" ng-model="hello-model"></input> 
<!-- And show that up -->
<h1>{{hello-model}}</h1>

```


### The first vanilla AngularJs page. 

```
<!DOCTYPE html> 

<!-- It is not any old HTML now. It is an angular application  -->
<html ng-app>

<head>
<meta charset="UTF-8">
<title>Learn Angular series.</title>
</head>

<body >
  <h1>Hello world from</h1>
  
  <!-- Add some model -->
  <input type="text" ng-model="hello"/> 
  <!-- And show that up -->
  <h1>{{hello}}</h1>

</body>

<!-- Add the magic. AngularJs that is.  -->
<script 
  type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.7/angular.min.js">
  </script>


</html>

<!-- https://egghead.io/lessons/first-step-adding-to-project -->
```
