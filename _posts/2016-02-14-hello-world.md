---
layout:     post
title:      Hello world
date:       2016-02-14 
summary:    Getting started with the blogging like a hacker stuff. 
categories: howto 
---


# [Spring Boot and AngularJS](https://examples.javacodegeeks.com/enterprise-java/spring/boot/spring-boot-and-angularjs-integration-tutorial/)



# References for Android developement 
  - [Android Development](http://www.vogella.com/tutorials/android.html)
  - 


# Android 7.0 Nougat!
  - https://developer.android.com/index.html
  - Get Android Studio

# Android Studio
  - Download. It is about 500Mb
  - Configure. https://developer.android.com/studio/install.html
  - http://www.vogella.com/tutorials/Android/article.html

# Is there TDD for android? TODO




# What is using all the space on my mac? TODO. 

# Should I develop for iOS or Android? TODO 

# How to develop for both iOS and Android? 
  - [10 tools](http://thinkapps.com/blog/development/develop-for-ios-v-android-cross-platform-tools/)


# How to monetize? 
  - [FbStart](https://developers.facebook.com/fbstart/?utm_source=Twitter&utm_campaign=fbs)
    - Launched an app on Google Play or iOS. 
    - ...
  - Android / iPhone. Which app is more likely to be monetized? 
  - 

# What are the features of a good tech blog? 
  - [It is a simple, beautiful Jekyll theme that's mobile first.](https://github.com/johnotander/pixyll)
  - Manage content in a no fuss way. On Sublime. And push from it. 
  - Multiple ways to share code. From the blog. From github. Etc. 
  - Free text search. Preferrably autocomplete. 
  - Multiple ways to find content. E.g. free text search, tags, date wise archive etc.  
  - Push content to social media. Twitter. Google etc. 
  - Search engine optimization. 
  - Optimized for mobile. 

# What can we make the pixyll do for your blog? 
  - [Notes from the link.](https://github.com/johnotander/pixyll)
  - If you don't want the header to link back to the root url
  - Add Contact Form from https://formspree.io
  - What is Disqus for? 
  - Change colors etc by changing _sass/_variables.scss
  - You can add some rudimentary animation by animated: true to your _config.yml
  - Add deep anchor links. AnchorJS
  - You can measure visits to your website either by using Google Analytics tracking embed or the more advanced Google Tag Manager container.
  - In order to get more information about your website's status in search engines, you can register it in Google Search Console and/or Bing Webmaster Tools.
  - What is this https://moz.com/blog/i-cant-drive-155-meta-descriptions-in-2015??
  - Add tags like 
    - [numbered and links shown.](http://zdf615328619.github.io/tags/)
    - [minimal and with count.](http://themes.gohugo.io/theme/pixyll/tags)
    - [or like so.](http://zpbappi.com/tags/)
  - Add contact [like so.](http://zpbappi.com/contact/)
    - Add archive [like so.](http://zpbappi.com/archive/). Or [like so.](http://zdf615328619.github.io/archive/)
    - Add the ribbon [like so.](http://ramonaharrison.github.io)
    - Add the search [like how?]
  - Add search 
    - [Search and archive together](http://www.repleatur.net/search/)
    - [type and search hits show up](http://www.perfectlyrandom.org/search/)
    - [loved the search on it](http://adrian-philipp.com)
  - Good design 
    + [clean and minimal and not too big](http://markibrahim.me//musings/)




# Build Apps for Free on Heroku

https://www.heroku.com/free
Heroku Postgres
  What is Postgres used for ?? 

Heroku Redis 
  What is Redis used for ?? 

Is it free? 
  [This is a free dyno concept. Is that good enough?](https://blog.heroku.com/heroku-free-dynos)

What is good about Heroku??
  Good according to http://www.toptenreviews.com/services/web-hosting/best-cloud-hosting/heroku-review/

What is bad about Heroku? 
  [Someone got locked out](http://augustin-riedinger.fr/en/resources/the-day-i-stopped-using-heroku/)

What are the alternatives to Heroku? 
  AWS 
  Nodejitsu


# How to deploy a node.js app in Heroku? 

## Installations and setups 

  - You should have a Heroku account. A free one is good enough for now. kaunjovi@gmail.com. 
  - You need the following on your local box. 

```bash

$ node --version 
v6.9.5
$ npm --version 
3.10.10
$ git --version 
git version 2.7.4 (Apple Git-66)
$ heroku --version 
heroku-cli/5.6.17-bee0f80 (darwin-amd64) go1.7.5

```




```bash 
$ heroku login 
Enter your Heroku credentials.
Email: kaunjovi@gmail.com
Password (typing will be hidden): 
Logged in as kaunjovi@gmail.com
```







# Follow https://tests4geeks.com/oauth2-javascript-tutorial/
  - Login with google and then logout 
  - You have to register your application with OAuth provider e.g. ??who are the different OAuth provider?? 
  - Go to API manager / Dashboard and enable Google+ API.  



```html
<script src="static/hello.all.js"></script>
<script>
  hello.init({
    google: "Client-ID-From-Google-Dev-Console"     // not real id
  });
</script>
```

```html 
<button onclick="hello('google').login()">google</button>
<button onclick="hello('google').logout()">logout</button>
```


# How to create a single page website using Node.js? 

  - http://www.clock.co.uk/blog/a-simple-website-in-node-js-2016-edition
  - https://shapeshed.com/creating-a-basic-site-with-node-and-express/

```bash 
$ node -v
v4.2.3
$ npm -v 
2.14.7

mkdir simple-website && cd simple-website
npm init


npm i --save express morgan nodemon hellojs 

npm i --save express@4 morgan@1
npm i --save nodemon@1.9
npm i --save hellojs

{
  "build-css": "stylus source/stylesheets/index.styl -o static/css",
  "watch-css": "stylus source/stylesheets/index.styl -o static/css -w",
  "clean": "rm -rf static/css && mkdir -p static/css",
  "build": "npm run clean && npm run build-css",
  "watch": "npm run clean && npm run watch-css & nodemon server -e js,jade",
  "start": "node server"
 }

```


server.js 

```javascript
var express = require('express')
  , logger = require('morgan')
  , app = express()
  , template = require('jade').compileFile(__dirname + '/source/templates/homepage.jade')

app.use(logger('dev'))
app.use(express.static(__dirname + '/static'))

app.get('/', function (req, res, next) {
  try {
    var html = template({ title: 'Home' })
    res.send(html)
  } catch (e) {
    next(e)
  }
})

app.listen(process.env.PORT || 3000, function () {
  console.log('Listening on http://localhost:' + (process.env.PORT || 3000))
})
```


# How to configure Google Credentials For OAuth with our App
  - Navigate to the Google Developer Console and select Credentials in the API Manager.
    + https://console.developers.google.com/projectselector/apis/credentials
    + Project name : loginLogoff 
    + click Create Credentials/OAuth Client Id.
    + Put the origin and redirect as http://localhost:5000
    + clientId : 528837191694-lr65jsi83hmsl1dti2jakh3mo586f1nb.apps.googleusercontent.com
    + clientSecret : PfmplOVEr96Vm8yRsK_5Yp7B


# What should software developers concentrate on in 2017? 

  - https://techbeacon.com/6-code-framework-trends-you-should-follow-2017
  - Progressive web apps (PWAs) emerged as a major new paradigm in mobile web development
  - [Google Go or Node.js for web development? Which is better?](https://www.topcoder.com/blog/google-go-or-node-js-for-web-development-which-is-better/)
  - Is Go better for web development than Node.js and JavaScript ?? 


# How to mine LinkedIn data using code? 
  - ?? 
  - LinkedIn relies on the industry standard OAuth 2.0 protocol for granting access
  - interacting with LinkedIn's REST APIs. 
  - if you are developing a front-end JavaScript LinkedIn provide SDKs to handle the authentication process for you. 

  - Using the JavaScript SDK requires you to have an application registered with LinkedIn.  
  - If you have not already done so, create an application. 
  - If you have an existing application, select it to modify its settings.

  - Create an application
  - Register that with LinkedIn
  - 

# Twitter for developers. 
  - https://dev.twitter.com
  - [Twitter Developer Documentation](https://dev.twitter.com/overview/api)
  - [Twitter Libraries in different technologies](https://dev.twitter.com/resources/twitter-libraries)
  - Twitter APIs in Java 
    - [The simple OAuth client Java lib](https://github.com/scribejava/scribejava)
    - [A Java HTTP client for consuming Twitter's Streaming API](https://github.com/twitter/hbc)
    - http://twitter4j.org/en/index.html
  - Python 
    - [Example app using Python to get Twitter data.](https://github.com/x0rz/tweets_analyzer/blob/master/secrets.py)
  

# What is wrong with Javascript? 

  - https://whydoesitsuck.com/why-does-javascript-suck/ ?? 
  - 
  - 

# [Go, or the Golang](https://golang.org)

  - Create a web app using Go 
  - Apparently Go is as good as or better than Node.js 
  - Host it on Heroku. 

## Go vs Node.js 

  - [Node.js vs Golang: Battle of the Next-Gen Languages](http://www.hostingadvice.com/blog/nodejs-vs-golang/)

## Why should I bother about learning Go? 

  - https://whydoesitsuck.com/why-does-javascript-suck/ ?? 
  - 


## Resources on Go

  - [Home page](https://golang.org)
  - [Building Go Web Apps](https://www.topcoder.com/blog/building-go-web-apps/)
  - [An Introduction to Programming in Go](http://www.golang-book.com/books/intro)
  - [Learning Go - a free PDF for learning the Go language.](https://github.com/miekg/gobook)
  - [Go Bootcamp](http://www.golangbootcamp.com/book/)
  - [Learn X in Y minutes](https://learnxinyminutes.com/docs/go/)
  - 


# What is Progressive web apps (PWAs)? 
  - ??



# [Eloquent JavaScript](http://eloquentjavascript.net)
  
  - TOREAD

# [Learning JavaScript Design Patterns](https://addyosmani.com/resources/essentialjsdesignpatterns/book/)

  - TOREAD 


# Javascript 

  - [This looks very detailed and interesting](http://eloquentjavascript.net)
  - https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
  - [codingame with Javascript](https://www.codingame.com/ide/66095220104dcab34ebde2a460a63bdf3348eb0)

```javascript
    var enemy1 = readline(); // name of enemy 1
    var dist1 = parseInt(readline()); // distance to enemy 1
    var enemy2 = readline(); // name of enemy 2
    var dist2 = parseInt(readline()); // distance to enemy 2
```
  - ternary operator 


```javascript
print(dist1 < dist2 ? enemy1 : enemy2);
```


```javascript
while (true) {
  // your logic here. 
}
```


# Where is Java installed on my mac? 

```bash
$ /usr/libexec/java_home
/Library/Java/JavaVirtualMachines/jdk1.8.0_31.jdk/Contents/Home
```

# How to use sublime for java based developement? 
  - Start with Sublime. Move as soon as it becomes too big. Too much effort.


# [Building "Hello World" in Angular 2](https://thinkster.io/tutorials/angular-2-hello-world)

  - There has to be an entry point to each application. This will do the bootstrapping. File name : main.ts. 
  - To bootstrap, there needs to be a component called "AppComponent". File name : app/app.component.ts
  - You could have a HTML template. It is not mandatory. 

main.ts



```javascript


import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/index';

platformBrowserDynamic().bootstrapModule(AppModule) 
```

app/app.module.ts

```javascript 

import { NgModule } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'

import { AppComponent } from './app.component';

@NgModule({
  imports: [ BrowserModule ],
  declarations: [ AppComponent ],
  bootstrap: [ AppComponent ]
})
export class AppModule {}

```

### app/app.component.html

```html 
<div>
  <h2>Hello {{name}}</h2>
</div>
```

  - @Anything is a decorator. Allows you to extend a class. 
  - @NgModule is a decorator in Angular2. It does ???
  - [How to autocomplete in sublime?](http://stackoverflow.com/questions/12656448/sublime-text-2-auto-completion-popup-does-not-work-properly)
  - 

# Read 

## Bookamark 
  - [Hackernoon, #hacker, #leisure](https://hackernoon.com)

## Come back 
  - [What is the big deal with mirrors?](https://hackernoon.com/i-made-myself-a-smart-mirror-50e56966c478#.buuvucryz) 
  - [What is this about robots taking away jobs?](https://hackernoon.com/the-robots-are-coming-9fbe73a0ec40#.wxyi1gpfz)

## Learn 
  - [The Tour of Heroes tutorial](https://angular.io/docs/ts/latest/tutorial/)
  - [Seems to be the latest on Angular2. Is it any good?](https://thinkster.io/tutorials/learn-angular-2)

## Good tech blog design 
  - http://blog.mgechev.com/2016/06/26/tree-shaking-angular2-production-build-rollup-javascript/
  - 
  
# Sublime


## Sublime, git 
  - C,S,P + quick
  - Highlight changed lines 
    - https://github.com/gornostal/Modific
    - https://github.com/jisaacks/GitGutter
    - 

## Sublime, typescript
  - https://github.com/Microsoft/TypeScript-Sublime-Plugin 
  - 

### Which all packages are installed in my Sublime installation? 
  - TBD 

## Sublime | shortcuts 
  - S+tab - collapse / uncollapse.  
  - A+cmd+enter - open the url in the chrome. 

# TypeScript
  - It seems to be js the way it should have been. Best to spend time only on the bits that gets something done. E.g. the bits that make Angular2 tick. 
  - So, no more in depth reading for now. 
  - [Learn TypeScript in 30 Minutes](http://tutorialzine.com/2016/07/learn-typescript-in-30-minutes/)
  - [If you just want to write ts and press play](http://www.typescriptlang.org/play/)
  - [If only js forced you to declar var type, we would not need a new language?](https://blogs.msdn.microsoft.com/somasegar/2012/10/01/typescript-javascript-development-at-application-scale/)
  - [TS seems to be getting popular over time. But why?](https://www.google.com/trends/explore?date=all&q=typescript)
  - [Babylon guys moved to ts](https://www.eternalcoding.com/?p=103)
  - [Why does TypeScript have to be the answer to anything?](http://www.hanselman.com/blog/WhyDoesTypeScriptHaveToBeTheAnswerToAnything.aspx)

## How to install
  - How to check if typescript has been installed correctly? TBD

```json 
sudo npm install -verbose -g typescript
npm list -g --depth=0 

$ tsc -v 
Version 2.1.4

tsc *.ts 
tsc helloworld.ts andsomemore.ts 

tsc helloworld.ts --watch
```


# Generics @ TypeScript  
  - http://tutorialzine.com/2016/07/learn-typescript-in-30-minutes/

# Modules @ TypeScript 
  - http://tutorialzine.com/2016/07/learn-typescript-in-30-minutes/






### Thanks to

  * https://help.github.com/articles/set-up-git/
  * https://help.github.com/articles/generating-a-new-ssh-key/
  * https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
  * https://help.github.com/articles/set-up-git/
  * https://help.github.com/articles/caching-your-github-password-in-git/
  * [Pushing to GitHub with HTTPS and 2-Factor Authentication](https://www.youtube.com/watch?v=hJLaXNMz8zw)


### How to setup git command line to connect with github account? 

```

git config --global user.name "kaunjovi"
git config --global user.email "kaunjovi@gmail.com"

// Where is this git from? 
git remote -v 

// How many files are there to be checked in? 
git status 

// What are the changes
git diff 

// Add the file in  
git add filename
git commit -m "blah"
git push 

```






### A pedantic way to push changes to git. 
```
git add --all && git commit -m "new version" && git push 
```
It is a bit pedestrian but, it is guaranteed not to eat too much system resource. And it will not run without me knowing. 

There was the other one. But, one, I could not get it to work. Second, I could not get it to work. Third, it is a little too clever script for me. I could not make head or tail out of it. Or how is it supposed to work. 

