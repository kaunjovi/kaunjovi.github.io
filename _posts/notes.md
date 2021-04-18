
- [Logging in Python](https://realpython.com/python-logging/)

```python
import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logging.basicConfig(level=logging.DEBUG)

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')
# 18472-WARNING-This is a Warning

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')
# 2018-07-11 20:12:06,288 - Admin logged in

logging.error('%s raised an error', name)

logging.error(f'{name} raised an error')

# capture stack tracke
logging.error("Exception occurred", exc_info=True)

# capture stack tracke
logging.exception("Exception occurred")
```

# Python3, VSCodium, snippet for logging 

```json
"Log debug": {
  "prefix": "logd",
  "body": [
    "logging.debug(f'$0')"
  ],
  "description": "Log debug"
}
```


- Python3, Function, Variable number of arguments 

```python
def my_method(*args, **kwds):
    # Do something

# When you call the method
my_method(a1, a2, k1=a3, k2=a4)

# You get:
args = (a1, a2)
kwds = {'k1':a3, 'k2':a4}
```

- [no Function Overloading in Python?](https://www.codementor.io/@arpitbhayani/overload-functions-in-python-13e32ahzqt)


## [MOVETO - Python3 basics] Naming convention of Python 

- [Naming conventions in Python3](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

- _single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not import objects whose names start with an underscore.
- [TODO] check _variable name. Apparently import does not import this. 
- single_trailing_underscore_: used by convention to avoid conflicts with Python keyword

```
tkinter.Toplevel(master, class_='ClassName')
```
- Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability
- Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.
- Class names should normally use the CapWords convention.
- Function names should be lowercase, with words separated by underscores as necessary to improve readability.
- Variable names follow the same convention as function names.
- Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.

```
from typing import TypeVar
```

- Changing existing code ? 
  - Document what have been used. Get to an agreement. Use that. 
- Writing new code ? 
  - Try to follow these suggestions. 

### Constants
- TOTAL
- MAX_OVERFLOW 


# How to set up a dev toolchain for Python3 developement 

# Full stack web app with Python3 

- What is anvil ? 
- [Full stack web apps with nothing but Python](https://anvil.works)
- Full stack web app. Develop only in Python3
- Deploy for free 
- Looks good. Come back sometime. 
- At the moment. I am looking for creation and deploy on cloud. 







# [MOVETO - shares]ProCapital 

- https://www.youtube.com/watch?v=sFXZLCixT8A
- Respond to this one? This is the index 


# [MOVETO - VSCodium]How to switch on quick suggestions in VScode for MD files? 

- In "Configure Language Specific Settings" 
- [TODO] Move to VSCode configurations. 
- [TODO] Move to MD file based blogging. 

```json 
   "[markdown]": {
        
        "editor.quickSuggestions": {
            "comments": true, 
            "other": true , 
            "strings": true 
        }
    },
```



## [ MOVETO - python3 ] File handling in Python 

```python 
# 'a' is for append, or use
# 'w' to write with truncation
with open('somefile.txt', 'a') as the_file:
    the_file.write('Hello\n')
```

## [ MOVETO - python3 ] Regular expression in Python 

```python
def modifyDataLine ( rawLine , date ): 
    return re.sub(r"^[0-9]*,[0-9]*,", date + "," , rawLine )
```



## [MOVETO: Python3 basics] Module in Python3 

- <something>.py , <my_something>.py, <test_the_app>.py
- Modules should have short, all-lowercase names.
- Underscores can be used in the module name if it improves readability. 
- Inside the file, we can have definitions and implementations of classes, variables, or functions. 
- This differs from a package in that a package is a collection of modules in directories that give structure and hierarchy to the modules.

## [MOVETO: Python3 basics] Methods (or is it function) in Python3. Reuse across modules. 

```python
def my_function():
    print("Hello World")
```

```python
import hello
hello.my_function()
```

```python
from hello import my_function
my_function()
```


# How to write good code in python3

- [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/)
- seems good 
- [TODO] read in details 

## What are the questions to ask the chart for entry and exit points? 
[MOVETO] buying stocks 

- What books to read ? 
- Look for strategies ? 

# How to distribute a python code app  
[MOVETO] Getting started with Python 

- https://realpython.com/pyinstaller-python/#preparing-your-project 


# How to code the main() function in Python 
[MOVETO] Getting started with Python 

- https://realpython.com/python-main-function/#use-__name__-to-control-the-execution-of-your-code
- This code pattern is quite common in Python files that you want to be executed as a script and imported in another module.

```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```


# How to share methods across Python code. 
[MOVETO] Getting started with Python 

- https://stackoverflow.com/questions/38980899/sharing-code-between-python-files
- https://stackabuse.com/creating-and-importing-modules-in-python/
- https://stackabuse.com/creating-and-importing-modules-in-python/
- https://realpython.com/python-import/
- https://realpython.com/absolute-vs-relative-python-imports/



Python Development: pipenv

https://www.stuartellis.name/articles/mac-setup/#python-development-pipenv

## What is the current version of Python in my Mac ? 






Current versions of macOS include a copy of Python 3, but this will not be the latest version of Python. Use Homebrew to install the latest release of Python.

To maintain current and clean Python environments, you should also use pipenv. 
This builds on two features of Python: the virtual environments and the pip utility.

Enter this command to install Python 3 and pipenv using Homebrew:

```
brew install python3 pipenv
```

Use pipenv to manage your Python projects. The pipenv tool itself will automatically work with the copy of Python 3 from Homebrew.

To use the Python 3 interpreter outside of projects that are managed by pipenv, specify python3 on the command-line and in your scripts, rather than python:

python3 --version

If you need to run the pip utility, rather than setting up a development environment with pipenv, always use the command pip3:

pip3 --version

The Python Guide tutorial shows you how to work with pipenv.





Refactor agressively. As soon as any section is worth sharing, give it its own page. 

# React vs AngularJS
[React vs AngularJS – How the two Compare](https://www.codementor.io/reactjs/tutorial/react-vs-angularjs)
[Hello world with React](http://codepen.io/chrisharrington/pen/pvEYJv/)




# Online brand
We need a brand. Something collaborative. Positive. 
Should have face. People trust face. Not impersonal logos. 


# Spring boot 
[Spring MVC with Bootstrap and Thymeleaf](http://joaoduraes.github.io/2015/02/07/spring-bootstrap-thymeleaf-example.html)


# Nice looking github io blogs 
http://joaoduraes.github.io/2015/02/07/spring-bootstrap-thymeleaf-example.html





https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html





# Where to learn Angular from ?
http://www.learn-angular.org
http://www.w3schools.com/angular/angular_controllers.asp



# How do you show the tags in your github.io page? 
TODO 



## Why are js files added at the end of the HTML files? Why not at the header? 
TODO

##When would Angular be a poor choice to use as a framework? 
During writing games, because ... 

## Yeoman 
http://yeoman.io
THE WEB'S SCAFFOLDING TOOL FOR MODERN WEBAPPS
Get started and then find a generator
Yeoman can build (any of these for you)[http://yeoman.io/generators/]. 


```
$ node -v
v4.2.3

// npm is the package manager for Node.js and comes bundled with it.
$ npm -version 
2.14.7

// Install yo using npm
sudo npm install -g yo

// Install the needed generator(s)
sudo npm install -g generator-angular

// Go to your developer directory 
yo angular twentyfourtyeight

```

## Building the 2048 game in AngularJS

To build our app, we’ll create a basic app (we used the yeoman angular generator to generate the structure of our app, but it’s not necessary. We only use it as a starting point, but quickly diverge from its structure). We’ll create the app directory which will house the entire application. We’ll place the test/ directory as a sibling to the app/ directory.



http://www.ng-newsletter.com/posts/building-2048-in-angularjs.html


#Songs
[Biroho madhur holo aaji madhurate](https://www.youtube.com/watch?v=87pb_7EZ8Jg)



https://incometaxindiaefiling.gov.in
https://incometaxindiaefiling.gov.in/e-Filing/UserLogin/LoginHome.html
PAN 




# Fitness 

Get help. Pick the right kind of workout. Burn fat for 40+. 
Get rid of bellyfat. That brings down T. 

Enjoy it. Else there is no point really. 
Look good. In cheap shirts too. 

https://www.youtube.com/watch?v=ijsu8GFZBTg


Use grill. Lean meat. Fish. 
Correct type of snacks. 

multijoint excercise. 


[Smart Cardio For Full-Body Fat Loss: Functional Cardio Day](https://www.youtube.com/watch?v=pGdScp-Kn6w)
[What Men Over 40 Need To Eat In Order To Get Six Pack Abs](https://www.youtube.com/watch?v=kWSRFwwQjnU)
[3 Tips To Boost Your Testosterone -- For Men Over 40 Only](https://www.youtube.com/watch?v=i4aN-typhlo)
[Can I still TRANSFORM my body when OVER 40?](https://www.youtube.com/watch?v=6G222Kx4r40)




### Which version of Python to use now ###

  - Install Python 3 - if you are a showoff
  - Use Python 2, if you want to achieve something with it. 

### What all do we need in the editor? ### 
  
  - Git integration 
  - autocomplete - anaconda 


### References ###

  - [Python 3 & Python 2.7 dual install - the right way on OSX](https://www.youtube.com/watch?v=c9LlK2iu7OA)
  - [Learn Python Through Public Data Hacking](https://www.youtube.com/watch?v=RrPZza_vZ3w)
  - 



### How to setup Sublime 3 for Python development on Mac? 

  - [Sublime Text 3 for Python development](http://piotr.banaszkiewicz.org/blog/2013/08/24/sublime-text-3-for-python-development/)
  - [Setting Up Sublime Text 3 for Full Stack Python Development](https://realpython.com/blog/python/setting-up-sublime-text-3-for-full-stack-python-development/)
  - Add Package Control. This is the first thing to do and the only manual install to do. 
  - Add Git 
  - Add GitGutter 
  - Add some themes and colors. It does not hurt to be cool.
