---
layout:     post
title:      Hello world
date:       2016-02-14 
summary:    Getting started with the blogging like a hacker stuff. 
categories: howto 
---


# How to for AndroidStudio
  - Format file on save. 
  - 

# [Android Development for Beginners](https://www.udacity.com/course/android-development-for-beginners--ud837)


@ signifies a resource. 
@drawable is a image, for example. 
Kirill Grouchnikov. Google playstore guy. 


  - [Material colors](https://material.io/guidelines/style/color.html#color-color-palette)
  - https://developers.google.com/android/for-all/vocab-words/?utm_source=udacity&utm_medium=course&utm_campaign=android_basics
  - developer.android.com/index.html 

# [Lesson 2: Building layouts, Part 2](https://classroom.udacity.com/courses/ud834/lessons/4330701752/concepts/42372186530923)

  - ViewGroup 
    + Linear layout could be vertical or horizontal
    + Relative layout allows positioning of children in relation to parent and / or siblings.
  - @ signifies resource 
  - @+id/ is a new resource that you are creating on the spot . 
  - Padding inside. Margin outside. 

# [Lesson 3: Practise set: Building layouts]

  - Install JDK. You are looking for Mac OS x64 version. 
  - Install AndroidStudio
  - API 15 - 90% 
  - NFC - 
  - Create a new "empty activity"

https://docs.google.com/document/d/1w1Xn_hnSAODAAtdRDp7haYPBtEwX_l7Htpf8Wpgbu6w/pub?embedded=true


### Check for java on your mac 

```
$ java -version 
java version "1.8.0_31"
Java(TM) SE Runtime Environment (build 1.8.0_31-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.31-b07, mixed mode)
```

# [Installing app on phone](https://classroom.udacity.com/courses/ud837/lessons/4034888704/concepts/43534185630923)

- Configure your android phone in developer mode. 
-   Browse to Settings / About phone / Build Number and click it 7 times. What. Why. 
-   Now you should see Developer{} available on the phone. 
-   Turn on USB Debugging. 
- Connect phone to mac. 
- Run app from AndroidStudio. Chose to run on the attached phone and not on emulator. 






# Create a Android Hello World app from scratch, using AndroidStudio but none of the wizards. 

  - Create a github project. Choose to create a readme. 
  - Import as a general project in AndroidStudio. Ensure that AndroidStudio uses the standalone Gradle. 
  - Create the build.gradle.
  - Open the build.gradle file in AndroidStudio and it will wake up to the fact that this is a Gradle project. 
  - 


# Where should I create the tech blog. 
  
  - ??
  - Don't want to use the github io. 
  - It is best for notes. 
  - It does not show up nice in office. Most likely the same will happen in other orgs as well. 
  - Where are most of the android tech blogs at? 
  - Medium is looking good / stylo. 
    + https://medium.com/@rotxed/dex-skys-the-limit-no-65k-methods-is-28e6cb40cf71
    + 


# [Building Android Apps — 30 things that experience made me learn the hard way](https://medium.com/@cesarmcferreira/building-android-apps-30-things-that-experience-made-me-learn-the-hard-way-313680430bf9)

  - Dont add 
    + 3rd party libraries 
    + database 
    + unless you absolutely have to. 

  - There will be performance issues 
    + check for overdraw. [link](https://riggaroo.co.za/optimizing-layouts-in-android-reducing-overdraw/)
    + check for 65K method issue. [link](https://medium.com/@rotxed/dex-skys-the-limit-no-65k-methods-is-28e6cb40cf71)

  - Read the full thing. It has some pointers that seem promising but are advanced. 
  - https://medium.com/@cesarmcferreira/building-android-apps-30-things-that-experience-made-me-learn-the-hard-way-313680430bf9
  - 


# dashboard 
https://blackrockdigital.github.io/startbootstrap-sb-admin-2/pages/forms.html

# How to used Sublime for JS projects? 



# angularjs

  - When building out Angular projects, you should not add on the full jQuery library. jQlite is already included in Angular

## Can I share working demo of angularjs with the world. 

  - codepen? No can do. The free version supports only one project with only 10 files. 
  - anything else out there??
  - 


  - [AngularJS Tutorial — Learn AngularJS in 30 minutes](https://blog.revillweb.com/angularjs-tutorial-learn-angularjs-in-30-minutes-35b5eae52dc2)
  - [Building a Web App From Scratch in AngularJS](https://code.tutsplus.com/tutorials/building-a-web-app-from-scratch-in-angularjs--net-32944)





# angularjs, bootstrap 
[How to Correctly Use BootstrapJS and AngularJS Together](https://scotch.io/tutorials/how-to-correctly-use-bootstrapjs-and-angularjs-together)


# Rapid prototyping with SpringBoot and AngularJS

  - [Rapid prototyping with Spring Boot and AngularJS](https://g00glen00b.be/prototyping-spring-boot-angularjs/)


# Get a bare bones SpringBoot application up and running. 

  - Use maven to do the heavy lifting and bring everyone to the party. 
  - Write the main class and bind it with SpringBoot. 
  - Write a basic HTML in src/main/resources/static/index.html. 
  - Boot up the SpringBoot application using Maven. 
  - The log file should show your message. The http://localhost:8080 should show the HTML. 


```
mvn -e clean install spring-boot:run
```

## Add bootstrap with bower to the SpringBoot application. 

  - Ensure that you have npm and bower installed. 

```
$ npm --version 
3.10.10
$ bower --version 
1.8.0
```

  - Configure bower to use the static folder for downloading libraries. Create the .bowerrc file. 

```
bower init
bower install angular --save 
bower install bootstrap --save 
```

  - Configure .gitignore to ignore the libraries folder. 
  - Put bootstrap elements in the index.html.  

## Add AngularJS

```
bower install angular --save 
```



# myCircle
  - The 5 people that you would like to SOS in case something goes wrong 
  - Seek help for you, right where you are 
  - Seek help for someone you know, at some other point 
  - You are in a fix. Is there someone who knows someone who you know, and who is around and can help. 
  - Needs to connect with GPS. 
  - Someone asked for help from Malad. Is there someone I know who is in Malad at the moment? 





[Example questions for interview](https://www.glassdoor.co.in/Interview/hyderabad-amazon-interview-questions-SRCH_IL.0,9_IM1076_KE10,16_IP2.htm)
  - Design vending machine 
  - Desing IVR 
  - Design air ticket picker 


# Design a vending machine 

  - http://javarevisited.blogspot.in/2016/06/design-vending-machine-in-java.html


1994 - Jeff Bezos - D. E. Shaw & Co. - Cadabra to Amazon 
As of early 2017, Amazon had nearly 269,000 employees worldwide

Non-clustered and clustered index


# Amazon leadership principles

Customer Obsession
Leaders start with the customer and work backwards. They work vigorously to earn and keep customer trust. Although leaders pay attention to competitors, they obsess over customers.

Ownership
Leaders are owners. They think long term and don’t sacrifice long-term value for short-term results. They act on behalf of the entire company, beyond just their own team. They never say “that’s not my job". 

Invent and Simplify
Leaders expect and require innovation and invention from their teams and always find ways to simplify. They are externally aware, look for new ideas from everywhere, and are not limited by “not invented here". As we do new things, we accept that we may be misunderstood for long periods of time.

Are Right, A Lot
Leaders are right a lot. They have strong judgment and good instincts. They seek diverse perspectives and work to disconfirm their beliefs.

Learn and Be Curious
Leaders are never done learning and always seek to improve themselves. They are curious about new possibilities and act to explore them.

Hire and Develop the Best
Leaders raise the performance bar with every hire and promotion. They recognize exceptional talent, and willingly move them throughout the organization. Leaders develop leaders and take seriously their role in coaching others. We work on behalf of our people to invent mechanisms for development like Career Choice.

Insist on the Highest Standards
Leaders have relentlessly high standards - many people may think these standards are unreasonably high. Leaders are continually raising the bar and driving their teams to deliver high quality products, services and processes. Leaders ensure that defects do not get sent down the line and that problems are fixed so they stay fixed.

Think Big
Thinking small is a self-fulfilling prophecy. Leaders create and communicate a bold direction that inspires results. They think differently and look around corners for ways to serve customers.

Bias for Action
Speed matters in business. Many decisions and actions are reversible and do not need extensive study. We value calculated risk taking. 

## Frugality
  - Accomplish more with less. Constraints breed resourcefulness, self-sufficiency and invention. There are no extra points for growing headcount, budget size or fixed expense.
  - do more with less 
  - -----------------
  - save ops headcount. 
  - kill the tail. 
  - in case an application does not fit into the rest of the portfolio, give them away. 

## Earn Trust
  - Leaders listen attentively, speak candidly, and treat others respectfully. They are vocally self-critical, even when doing so is awkward or embarrassing. Leaders do not believe their or their team’s body odor smells of perfume. They benchmark themselves and their teams against the best.
  - At the end of the day, the team is the source of strength. 
  - It is important to know each member of the team accurately, know their strengths and weak spots. 
  - It is only possible when the leader connects with the team. This can only happen when the team is treated with humility, respectfully and with honesty. 
  - Communication plan
  - ------------------
  - Each product team meets once a month for all hands on where the report card is presented in details. 
  - With all leads and designated high performers there is a monthly one to one. documented next steps. 
  - With all teams there is a skip level meeting, at regular intervals. 
  - There is a monthly report card that is published by each team. 

## Dive Deep
  - Leaders operate at all levels, stay connected to the details, audit frequently, and are skeptical when metrics and anecdote   differ. No task is beneath them.
  - Urgent
  - ------ 
  - P1. Standing instruction to text for every case. In case of escalations, get in call as the AD lead. 
  - P1. All cases. Friday. Weekly call with all leads. 
  - P1. All cases. Monday morning call to provide sr. mgmt. 
  - Non urgent, Important 
  - ---------------------
  - Randomly join weekly / daily scrum meetings, to be in touch with the grassroot detals. 
  - Working towards sending critical stability, management metrics from prod over emails to AD, ProdSupport. 
  - Insists on access to codebase. Randomly pull code and review. 
  - Dev fridays. Critical dev, arch updates are shared. 
      

## Have Backbone; Disagree and Commit
  - Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable or exhausting. Leaders have conviction and are tenacious. They do not compromise for the sake of social cohesion. Once a decision is determined, they commit wholly.
  - Graphs are not required for the MVP in MyReports. 
    + Challanged on the basis of SME knowledge and understanding. Disagreed. 
    + Spawn off another thread to collect data about usage of graphs. In progress. 
    + Did a demo to sr. stakeholders from client. Most of the feedback was on the ease of creating new reports and formatting them. 
    + We agreed on a list of features for MVP. Clients chose not to put graphs on that. 
  - ??  


## Deliver Results
Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion. Despite setbacks, they rise to the occasion and never settle.






Decision with less data 
  vocally self critical 
  backbone - feature which is good for 
  technologies - 5  / 6 

Think big - vision 

Team - self motivated - 100 members

Leadership principles 

2 project detailed description - data, users, 

problem solving - 
  - telephonic machines - 
  - vending machine 
  - smallest path 
  - IPL dashboard 
  - one liner 
    + clear assumptions 
    + probe 
    + dealing with ambiguity 
    + user base / scale / 10X user base 
    + frugality 

AWS 
  - familiarity with cloud 





# [Spring Boot and AngularJS](https://examples.javacodegeeks.com/enterprise-java/spring/boot/spring-boot-and-angularjs-integration-tutorial/)


# When should we use bower and when npm? 
  - It seems we can download js using bower. We could add that to a spring-boot application. 
  

## Install bower

```bash 

$ npm --version 
3.10.10

$ npm install -g bower 
/usr/local/bin/bower -> /usr/local/lib/node_modules/bower/bin/bower
/usr/local/lib
└── bower@1.8.0 


Configure bower to install js in our folder. 

$ cat .bowerrc
{
  "directory": "src/main/resources/static/bower_components",
  "json": "bower.json"
}


// bower will not work due to permission issues to start with. fix that. 
sudo chown -R $(whoami) ~/.config
bower init
bower install --save jquery bootstrap 
bower install --save angular angular-route angular-resource angular-cookies angular-sanitize 
bower install --save bootstrap 

bower install --save angular-ui-grid


```

## Configure bower to download files in a provided folder. 

Add the .bowerrc file to the project folder. 
And then run bower init

```bash 


{
  "directory": "src/main/resources/static/bower_components",
  "json": "bower.json"
}

```

```
mvn clean install

mvn spring-boot:run

```


## spring-boot, angularjs tutorial 

  - [Part 1](http://rajandesai.com/blog/2014/03/08/getting-started-with-spring-boot-application-using-maven/)
  - [Part 2](http://rajandesai.com/blog/2014/03/10/web-application-development-using-spring-boot-and-maven-part-2-adding-angularjs-support/)
  - [Part 3](http://rajandesai.com/blog/2014/03/12/web-application-development-using-angularjs-spring-boot-and-maven-part-3-beautify-using-bootstrap/)
  - [Part 4](http://rajandesai.com/blog/2014/03/14/web-application-development-using-angularjs-spring-boot-and-maven-part-4-birdlog-application/)
  - [Part 5](http://rajandesai.com/blog/2014/03/18/part-5-web-application-development-using-angularjs-spring-boot-and-maven-using-ebird-apis-in-birdlog-application/)


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

