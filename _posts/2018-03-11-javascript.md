---
layout:     post
title:      JavaScript
date:       2018-03-11 
summary:    JavaScript
categories: howto 
---



# [A re-introduction to JavaScript (JS tutorial)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

- History
  - JS created in 1995 by Brendan Eich while he was an engineer at Netscape.
  - JS was first released with Netscape 2 early in 1996.
  - Several months after that, Netscape submitted JavaScript to Ecma International, a European standards organization, which resulted in the first edition of the ECMAScript standard that year. 
  - Many parts of the fourth edition formed the basis for ECMAScript edition 5, published in December of 2009, and for the 6th major edition of the standard, published in June of 2015.
- Basics 
  - No concept of input or output. 
  - Supposed to be scripting language in a host environment, 
  - It is up to the host environment to provide mechanisms of i/p and o/p 
  - The possible host environments are 
    - Browser
    - Adobe Acrobat, Adobe Photoshop, 
    - SVG images, 
    - Yahoo's Widget engine, 
    - server-side environments such as Node.js, 
    - NoSQL databases like the open source Apache CouchDB, 
    - embedded computers, 
    - complete desktop environments like GNOME (one of the most popular GUIs for GNU/Linux operating systems)
    - and other 


## JavaScript supports OO programming and functional programming

- JavaScript supports object-oriented programming 
- JavaScript use object prototypes, instead of classes 
- see more about prototypical inheritance and ES2015 classes
- JavaScript also supports functional programming 
- functions are objects, 
- Functions have the capacity to hold executable code 
- Functiona can be passed around like any other object.

## JavaScript types 

- Number, String, Boolean 
- Symbol 
- Object : Function, Array, Date, RegExp 
- null, undefined  

## Number 

- Not an integer. If you are *java* or *C* person, please take care. 
- double-precision 64-bit format IEEE 754 values - if that makes any sense. 

- Huh ???? 

```javascript
0.1 + 0.2 == 0.30000000000000004;
```
