---
layout:     post
title:      Gradle project with AndroidStudio
date:       2017-04-16 
summary:    Create a gradle project in AndroidStudio. 
categories: howto 
---


# Create a gradle project in AndroidStudio. 

  - Create a github project. Choose to create a readme. 
  - Import as a general project in AndroidStudio. 
    + File / New / Import project from version control / GitHub
    + The integration is actually much more intuitive and easier than Ecliplse. +1 to AndroidStudio. 
    + Once the project shows up the Readme.md actually is not seen. -1 to AndroidStudio. 
    + Changing the view from Android to Project solves the problem. Not very intuitive. 
    + The md files have a preview available. Not half bad. +1 to AndroidStudio. 

  - Create a build.gradle file and add a task in it. 

```
task helloWorld {
  doLast {
   println 'Hello world from gradle.'    
  }
}
```

  - Open the build.gradle file in AndroidStudio and it will wake up to the fact that this is a Gradle project. 
    + AndroidStudio will realize that it is a gradle project. C'mon. There ought to be some button for that rather than this mumbo jumbo. -1 to AndroidStudio. 
    + AndroidStudio will also create a dozen files. Not cool man. 
    + Ensure that AndroidStudio uses the standalone Gradle and not the one that came packed with it. 
    + Run the task from AndroidStudio. You should get the "Hello world", in one of the views. Takes a bit of looking around.

```
12:40:13 AM: Executing external task 'helloWorld'...
:helloWorld
Hello world from gradle.

BUILD SUCCESSFUL

Total time: 0.023 secs
12:40:13 AM: External task execution finished 'helloWorld'.
```
    + Now, run the task from command prompt. It should do the same "Hello world" thing. 

```
$ pwd 
/Users/parthabhattacharjee/git/tutorialGradle001

$ gradle helloWorld
:helloWorld
Hello world from gradle.

BUILD SUCCESSFUL

Total time: 0.648 secs
```
    + Unexpected really. But AndroidStudio seems to be running Gradle much faster than command prompt. +1 to AndroidStudio. 
