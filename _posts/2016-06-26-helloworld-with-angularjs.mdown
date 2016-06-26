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
