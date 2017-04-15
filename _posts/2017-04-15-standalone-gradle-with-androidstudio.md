---
layout:     post
title:      Standalone Gradle with AndroidStudio
date:       2017-04-15 
summary:    Setting AndroidStudio to use the standalone gradle. 
categories: howto 
---


# Make AndroidStudio use the standalone Gradle of the machine. 

  - Ensure that you have gradle installed. I have Gradle 3.4.1. 

```
$ gradle -version 

------------------------------------------------------------
Gradle 3.4.1
------------------------------------------------------------

Build time:   2017-03-03 19:45:41 UTC
Revision:     9eb76efdd3d034dc506c719dac2955efb5ff9a93

Groovy:       2.4.7
Ant:          Apache Ant(TM) version 1.9.6 compiled on June 29 2015
JVM:          1.8.0_31 (Oracle Corporation 25.31-b07)
OS:           Mac OS X 10.11.6 x86_64
```

  - Find where is this gradle installed. Mine is at /usr/local/Cellar/gradle/3.4.1/bin/gradle

```
$ which gradle 
/usr/local/bin/gradle
$ ls -l /usr/local/bin/gradle
lrwxr-xr-x  1 parthabhattacharjee  admin  41 Apr 10 20:42 /usr/local/bin/gradle -> /usr/local/Cellar/gradle/3.4.1/bin/gradle
```

  - Configure AndroidStudio to use this gradle. Command+,. Then search for gradle in the window and set it to be the gradle you are running. 
