---
layout:     post
title:      Mac Dev Box 
date:       2022-06-22
summary:    Mac Dev Box 
---

## Reference 
- [Zero to Hero: Set Up Your Mac for Software Development](https://faun.pub/zero-to-hero-set-up-your-mac-for-software-development-919ede3df83b)
- [Development Environment on macOS 2022](https://dev.to/andrewbaisden/how-i-setup-my-development-environment-on-macos-2022-edition-5elf)
- [Beginner's Setup Guide for Ruby, Node.js, Git, Github, and other things on Mac OS X 10.9](http://burnedpixel.com/blog/beginners-setup-guide-for-ruby-node-git-github-on-your-mac/)

## Homebrew
- Homebrew, or simply Brew, is the “The Missing Package Manager for macOS.”
- /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

## Install Git 

```code
kaunjovi@devbook ~ % brew install git 
...........................
... git will be updated ...
...........................
kaunjovi@devbook ~ % git --version    
git version 2.36.1
```

## Pulling in an existing github project in Eclipse

- Create a project in github. Easier that way. Have it be initialized with README.md
- Eclipse. Import git project. 
- Add gradle nature. 
- Add a build.gradle. Add a couple of dependencies. 
- Check if they are getting downloaded fine. 
- Add a src/main/java, src/test/java and their corresponding resources folder. 
- Hit "refresh gradle project" to have Eclipse recognize these folders. 

## Checking in an existing Eclipse project in github XXX


parthabh /  S..1806

### Mac Eclipse Shortcuts 

  * [Keyboard shortcut for code completion in Eclipse on Mac OS X](http://stefaanlippens.net/code_completion_shortcut_eclipse_osx)

    