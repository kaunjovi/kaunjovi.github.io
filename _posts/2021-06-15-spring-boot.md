---
layout:     post
title:      Spring Boot
date:       2021-06-15
summary:    Notes on Spring Boot
categories: notes Spring Boot
---

## Spring Boot 2.5.1

- [Home page of Spring Boot, latest version 2.5.1](https://spring.io/projects/spring-boot)
- [Spring Quickstart Guide](https://spring.io/quickstart)

## Install Open JDK

- https://adoptopenjdk.net
- Install Open JDK - OpenJDK 11 (LTS) - HotSpot
- /Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk
- What is the story with AdoptOpenJDK? https://adoptopenjdk.net

```
/Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk
```

```
kaunjovi@devbook ~ % java --version 
openjdk 11.0.11 2021-04-20
OpenJDK Runtime Environment AdoptOpenJDK-11.0.11+9 (build 11.0.11+9)
OpenJDK 64-Bit Server VM AdoptOpenJDK-11.0.11+9 (build 11.0.11+9, mixed mode)
```

## Integrate Open JDK with Visual Studio 

- Install "Language Support for Java(TM) by Red Hat"
- Add back 

```
gradle clean build bootRun
```


## Read more 

- What is the story with AdoptOpenJDK? https://adoptopenjdk.net
- Investigate Undertow. Some sort of a web / app server ? 
- Investigate Kotlin. 
- Investigate Groovy. 


## Move to market 

- Defensive sectors ? IT, FMCG 
- [NIFTY FMCG Index](https://www1.nseindia.com/content/indices/ind_nifty_FMCG.pdf)
- FMCGs (Fast Moving Consumer Goods)
- non-durable, mass consumption products and available off the shelf

- FMCG) sector is the fourth largest sector in the Indian economy with Household and Personal Care accounting for 50% of FMCG sales in India
- FMCG sector is defensive in nature with less impact of the economic situations on the revenues
- FMCG is outlook for growth in household incomes.
- [Nifty FMCG Index by moneyworks4me](https://www.moneyworks4me.com/nse-index/top-nse-fmcg-companies-list/)

    - Hindustan Unilever Ltd. 27.59
    - ITC Ltd. 25.00
    - Nestle India Ltd. 8.34
    - Britannia Industries Ltd. 5.70
    - Tata Consumer Products Ltd. 5.57
    - Godrej Consumer Products Ltd. 4.54
    - Dabur India Ltd. 4.28
    - Marico Ltd. 3.44
    - Jubilant Foodworks Ltd. 3.33
    - Colgate Palmolive (India) Ltd. 3.21
    - As of May 31, 2021


# MOVETO [Python](https://www.geeksforgeeks.org/python-programming-language/)

- [Python Programming Language in geek for geeks](https://www.geeksforgeeks.org/python-programming-language/)


## Functions in Python

- [Functions in Python](https://www.geeksforgeeks.org/functions-in-python/)

- What is a good name of a function? 

- Define a function 
- Call a function 
- Provide documentation to a function 
- Print out the documentation of a function

```python
def hello_world() : 
    """
    This is the ubiquitious
    hello world code in python
    """
    print ('Hello world.')

hello_world() 
print (hello_world.__doc__) 
```

### default values in Python

```python
def hello ( name = 'Partha') :
    """
    Function with default arguments
    """
    print(f'Hello {name}')


if __name__ == "__main__":
    hello() 
    hello('buddy')
```

## Functions in Python pass by ref only 

- in Python every variable name is a reference. 
- When we pass a variable to a function, a new reference to the object is created. 
- Parameter passing in Python is the same as reference passing in Java.

- Within function 
    - modify the parameter passed, 
        - the change shall go back to the caller as well 
        - var was ref. You used the var to modify the actual data 
        - hence the actual data got changed and it will show the change 
        - even if you ref with another var e.g in the calling function
        - e.g. a = a + 1 
        - e.g. some_list[0] = 10 

    - change the parameter
        - you are the changing the ref. Now it is pointing to something else. 
        - now whatever changes you are doing, that is not going out. 
        - i.e. a = 10 
        - i.e. some_list = [1,2,3]

Python caches integers in the range [-5, 256]
Why ? 

## Variables in Python

- [Facts and myths about Python names and values](https://nedbatchelder.com/text/names.html)
Names refer to values
Many names can refer to one value.
Names are reassigned independently of other names
Values live until nothing references them.
Python keeps track of how many references each value has, and automatically cleans up values that have none. This is called “garbage collection,” and means that you don’t have to get rid of values, they go away by themselves when they are no longer needed.
Assignment never copies data.

Changes in a value are visible through all of its names. (Mutable Presto-Chango)

Values fall into two categories : mutable or immutable. 
Immutable values include numbers, strings, and tuples. 
Almost everything else is mutable, including lists, dicts, and user-defined objects. 

Mutable means that the value has methods that can change the value in-place. 

Immutable means that the value can never change, instead when you think you are changing the value, you are really making new values from old ones.

- [Visualize execution of code](http://pythontutor.com/visualize.html#mode=edit)

- Java passes by value 
    - [Does Java pass by reference or pass by value?](https://www.infoworld.com/article/3512039/does-java-pass-by-reference-or-pass-by-value.html)
    - [Java is Strictly Pass by Value!](https://www.geeksforgeeks.org/g-fact-31-java-is-strictly-pass-by-value/)
    - Like C/C++, Java creates a copy of the variable being passed in the method
    - 

- https://nedbatchelder.com/. Ned Batchelder. Coverage.py author. 







# MOVETO 
- Wendy Harrington 
- Raja Doddala 
- Nuveen Labs 
- Snowflake 
- Correlation one, Datascience for one 
- Ransomeware examples 
- Michael Normandy 

