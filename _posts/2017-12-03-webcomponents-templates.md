---
layout:     post
title:      WebComponents Templates
date:       2017-12-03 
summary:    Getting started with WebComponents.Templates
categories: howto 
---


## Templates before WebComponents and their problems. 

- http://www.dotnetcurry.com/html5/1079/html5-web-components-tutorial
- The first option 
  - use a block element that would be hidden initially and displayed later when some web page interaction occurred. 
  - The problem with this option is that you fetch resources from the server, for example images, even though they might not be shown to the user.
- The second option 
  - Create a script tag with an id and give it the text/template type. 
  - In that script tag, you would plant your DOM code. 
  - In this option the web page won’t load unnecessary resources but in order to use the template, you need to fetch the script tag element and extract its HTML. That might lead to cross-site scripting vulnerability. We can do better than that.

```html
<script id="myTemplate" type="text/template">
  <div>
    …
  </div>
</script>
```

## Templates in WebComponents

- http://www.dotnetcurry.com/html5/1079/html5-web-components-tutorial
- [The official doc. Read once you know your way around](https://www.w3.org/TR/html5/scripting-1.html#the-template-element)
- Wrap HTML content including script and style tags inside a template element
- Fetch the template using javascript and clone. 
- Once the clone is appended, 
  - script tags or style tags, they will be executed. 
  - Resources such as images or videos, they will be retrieved from the server.


```html 
<template id='myTemplate'>
  <div>
    …
  </div>
</template>
```

```javascript
var template = document.querySelector('#myTemplate');
var clone = document.importNode(template.content, true);
```

## Templates in WebComponents dont do 

- it doesn’t support data binding.
