---
layout:     post
title:      Adding first Angular controller
date:       2016-06-26 
summary:    Getting started Angularjs. Just pure vanilla stuff. 
categories: howto angularjs
---

# How do you go about it? 
  - Write your simple HTML 
  - Include a js file
  - In that js file, write a AngularJs module, controller and something useful e.g. a message in the controller. 
  - Stitch up the module as the application, controller as the controller and the message as the model in your HTML 

# The js file. 

```
angular.module('MyModule', [])
  .controller("MyController", ["$scope", function($scope){
    $scope.HelloWorldMessage = "Hello master." ; 
  }]) ;
```

# The HTML file 

```
<!DOCTYPE html> 

<!-- 
It is not any old HTML now. It is an angular application. 
-->
<html >

<head>
<meta charset="UTF-8">
<title>Learn Angular series.</title>

<!-- Add the magic. AngularJs that is. And a bit of your js.  -->
<script 
  type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.7/angular.min.js">
  </script>
<script src="LearnAngular00020.js"></script>

</head>

<!-- 
The app is your module. 
The controller is your controller. 
The message in the js in the model to Angular. 
 -->
<body ng-app="MyModule" ng-controller="MyController">
  <h1>Hello world from a controller.</h1>
  <h1  ng-bind="HelloWorldMessage"></h1>

</body>

</html>

```
