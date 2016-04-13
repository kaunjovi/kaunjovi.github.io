---
layout:     post
title:      Configuration
date:       2016-03-25
summary:    Notes on setting configurations of an application. 
categories: 
---

  - The application code should not bother whether a setting is coming in from configuration file or not. Or should it? 
  - Configuration should allow nesting. So it can't be a simple list of properties. Or could it? 
  - Configuration should only load at the bootup or should it load as soon as changed. 



### Use properties files. 
  - [Properties](http://docs.oracle.com/javase/tutorial/essential/environment/properties.html)
  - [Java Properties file examples](http://www.mkyong.com/java/java-properties-file-examples/)



```
// I can do this
Configuration.get("DBServerName") ; 
// But how do I get to this automagically?
Configuration.getDBServerName() ; 
```



Abstract Syntax Tree (AST)

Lombok annotation handler hijacks AST, and changes the code. 
Compiler generate code from the modified (and hacked) AST. 




### Custom Annotation with no element 
  - Marker Annotation 

### Custom Annotation with a single element 
  - the element has to be named value

### Annotation annotating itself 
  - meta-annotations 
  - @Target(ElementType.METHOD) - can only be applied to methods. 
  - @Target(ElementType.TYPE) - can be applied to interface, class and enum 
  - @Retention(RetentionPolicy.RUNTIME) - retain till runtime. Some reflection code will work on it. 
  - @Retention(RetentionPolicy.SOURCE) - The annotation is not needed at runtime e.g. if using the annotation to generate a method during compilation


### How to create a custom annotation 

  - public, static, or final - or your custom annotations. 
  - Annotations preced other modifiers. 
  - Annotation type declarations are similar to normal interface declarations. 
  - An at-sign (@) precedes the interface keyword. 
  - Each method declaration defines an element of the annotation type. 
  - Method declarations must not have any parameters or a throws clause. 
  - Return types are restricted to primitives, String, Class, enums, annotations, and arrays of the preceding types. 
  - Methods can have default values. 


CustomAnnotation.MarkerAnnotation 


http://docs.oracle.com/javase/1.5.0/docs/guide/language/annotations.html
http://www.mkyong.com/java/java-custom-annotations-example/



### SPI (Service Provider Interfaces)

use SPI (Service Provider Interfaces) to transparently invoke an annotation processor during compilation
Create a simple annotation. 


http://programmaticallyspeaking.com/playing-with-java-annotation-processing.html


Extending Lombok

Extending Lombok is a 3-step process:



Create the annotation. Since the annotation is used at compile-time, it can be safely be discarded afterwards so its retention policy can be left to its default value (namely RetentionPolicy.SOURCE)

Create the handler. A handler is a class that directly implements lombok.javac.JavacAnnotationHandler. Why directly? Because Lombok uses the ServiceProvider service and it’s one of its limitations

Reference the fully qualified class name of the handler in a file named lombok.javac.JavacAnnotationHandler under META-INF/services


The real coding takes place in step 2: the interface has a single method handle(AnnotationValues annotation, com.sun.tools.javac.tree.JCTree.JCAnnotation ast, JavacNode annotationNode). Notice the 2nd parameter package? It’s denotes Sun private implementation. It has some big drawbacks:



The documentation is sparse if not completely unavailable. You go into unknown territory here

Since the com.sun.tools.javac is not part of the public API, it can change at a moment’s notice. You can break your code with each update

Remember that previously, I talked about this being only good for Java? That’s still true. If you want this new annotation to work under Eclipse, that’s another handler to write
