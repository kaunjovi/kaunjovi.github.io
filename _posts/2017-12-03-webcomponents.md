---
layout:     post
title:      webcomponents
date:       2017-12-03 
summary:    Getting started with webcomponents
categories: howto 
---


## Web Components

- Custom Elements, HTML Imports, Templates and Shadow DOM.
- https://www.webcomponents.org/
- CUSTOM ELEMENTS: This specification describes the method for enabling the author to define and use new types of DOM elements in a document.
- HTML IMPORTS: HTML Imports are a way to include and reuse HTML documents in other HTML documents.
- TEMPLATES: This specification describes a method for declaring inert DOM subtrees in HTML and manipulating them to instantiate document fragments with identical contents.
- SHADOW DOM: This specification describes a method of establishing and maintaining functional boundaries between DOM trees and how these trees interact with each other within a document, thus enabling better functional encapsulation within the DOM.
- http://www.dotnetcurry.com/html5/1079/html5-web-components-tutorial
- Create HTML reusable components. 


## Templates in WebComponents 

- http://www.dotnetcurry.com/html5/1079/html5-web-components-tutorial
- The first option 
  - use a block element that would be hidden initially and displayed later when some web page interaction occurred. 
  - The problem with this option is that you fetch resources from the server, for example images, even though they might not be shown to the user.
- The second option 
  - Create a script tag with an id and give it the text/template type. 
  - In that script tag, you would plant your DOM code. 
  - In this option the web page won’t load unnecessary resources but in order to use the template, you need to fetch the script tag element and extract its HTML. That might lead to cross-site scripting vulnerability. We can do better than that.

```javascript
<script id=""myTemplate"" type=""text/template"">
  <div>
    …
  </div>
</script>
```

## What are the libraries for building web components

- Bosonic is a collection of components designed to meet the everyday needs of web developers.
- Polymer provides a set of features for creating custom elements.
- SkateJS is a JavaScript library for writing web components with a small footprint.
- Slim.js is an opensource lightweight web component library that provides data-binding and extended capabilities for components, using es6 native class inheritance.
- Stencil is an opensource compiler that generates standards-compliant web components.
- X-Tag is an open source JavaScript library that provides an interface for component development.
- https://www.webcomponents.org/introduction
- 


## Polymer 

- https://jcrowther.io/2015/07/13/linking-polymer-model-updates-to-angularjs-digest-cycle/
- https://jcrowther.io/2015/05/26/using-polymer-webcomponents-with-angular-js/
- [Will Polymer kill AngularJS?](http://ng-learn.org/2014/12/Polymer/)
- The Polymer core provides a thin layer of API on top of web components.
- There are other players in market 
  + X-Tag, a small JavaScript library, created and supported by Mozilla. 
  + Bosonic is another one out there
- Polymer team - part of google - works really closely with Chrome’s team.
- If you know Angular, a directive is a complex API to create custom components. With web components and polymer things get much more simple when creating custom elements.
- Rob Dodson - part of the Polymer team - has been recording some polycasts. 


## angular-polymer 

- https://www.npmjs.com/package/angular-polymer
- 
