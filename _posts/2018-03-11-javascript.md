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
- Functions can be passed around like any other object.

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

- addition, subtraction, modulus (or remainder) arithmetic, 

```javascript
Math.sin(3.5);
var circumference = 2 * Math.PI * r;
parseInt('123', 10); // 123, 10 is the base. 
parseInt('010', 10); // 10
parseInt('010');  //  8
parseInt('0x10'); // 16
parseInt('11', 2); // 3, 2 is the base. 
// parseFloat() always uses base 10.
parseInt('hello', 10); // NaN
NaN + 5; // NaN
isNaN(NaN); // true
1 / 0; //  Infinity
-1 / 0; // -Infinity
isFinite(1 / 0); // false
isFinite(-Infinity); // false
isFinite(NaN); // false
```

## Strings 

```javascript
'hello'.length; // 5
'hello'.charAt(0); // "h"
'hello, world'.replace('hello', 'goodbye'); // "goodbye, world"
'hello'.toUpperCase(); // "HELLO"
'hello' + ' world'; // "hello world"
'3' + 4 + 5;  // "345", starts from left, moves to right. 
 3 + 4 + '5'; // "75"
```


## Two types of things that are not there. 
- null, a value that indicates a deliberate non-value 
- In JS you can declare a variable without assigning a value to it.
- It then becomes undefined. 
- undefined is actually a constant.
- undefined, which is a value of type undefined that indicates an uninitialized value

## And there there are the true and false. 
- false, 0, empty strings (""), NaN, null, and undefined all become false.
- All other values become true.
- The logical operators - && (logical and), || (logical or), and ! (logical not)

```javascript
Boolean('');  // false
Boolean(234); // true

// Equality *might* do implicit type changes. 
123 == '123'; // true
1 == true; // true

// If you did not want JS to be over smart 
123 === '123'; // false
1 === true;    // false
```

## Variables in JS 

- blocks do not have scope; only functions have a scope.
- starting with ECMAScript 2015, let and const declarations allow you to create block-scoped variables.

### let varaibles 

```javascript
let a;
let name = 'Simon';

// myLetVariable is *not* visible out here

for (let myLetVariable = 0; myLetVariable < 5; myLetVariable++) {
  // myLetVariable is only visible in here
}

// myLetVariable is *not* visible out here
```

### const variables 

```javascript
const Pi = 3.14; // variable Pi is set 
Pi = 1; // will throw an error because you cannot change a constant variable.
```

### var variables 

```javascript
var a; 
var name = 'Simon';

// myVarVariable *is* visible out here 

for (var myVarVariable = 0; myVarVariable < 5; myVarVariable++) { 
  // myVarVariable is visible to the whole function 
} 

// myVarVariable *is* visible out here

```

## Control structures 

### if else if else 

```javascript
var name = 'kittens';
if (name == 'puppies') {
  name += ' woof';
} else if (name == 'kittens') {
  name += ' meow';
} else {
  name += '!';
}
```

### while 

```javascript
while (true) {
  // an infinite loop!
}
```

### do while 

```javascript
var input;
do {
  input = get_input();
} while (inputIsNotValid(input));
```

### for 

```javascript
for (var i = 0; i < 5; i++) {
  // Will execute 5 times
}
```

### for of 

```javascript
for (let value of array) {
  // do something with value
}
```

### for in 

```javascript
for (let property in object) {
  // do something with object property
}
```

### switch case default 

```javascript
switch (action) {
  case 'draw':
    drawIt();
    break;
  case 'eat':
    eatIt();
    break;
  default:
    doNothing();
}
```


# Function 
# Object 
# Closure 
