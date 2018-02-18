---
layout:     post
title:      Hello world
date:       2016-02-14 
summary:    Getting started with the blogging like a hacker stuff. 
categories: howto 
---



# Blockchain

- https://www.youtube.com/watch?v=SSo_EIwHSd4 
- What is the hash ? 
- What is the proof of work ? 
- Everyone in the network gets a full copy of the blockchain 
  + How does that work? 
  + Would I not need a lot of space on my computer
  + What is a smart contract? 
  + 
- https://www.youtube.com/watch?v=5BGCKkgW8CU 
- How many intermediaries come into play when I pay for something that I paid on Amazon? 
- How do I join the blockchain network? 
- How do I create a network of blockchain nodes? 
- Can I have my own private little blockchain network? 
- You have to take over more than 50% of the network and change the truth. 

- https://www.youtube.com/watch?v=bBC-nXj3Ng4
- public ledger 
- Partha says Partha pays XX too ABC and then sign it. Digital signature. 
- Digital signature. The proof that she has seen it and approves of it. 
- Nobody else should be able to forge that digital signature. 
- What if Tom just copies Alice's signature? Whatever the number might be. 
- You have a secret key that you dont share. 
- Take the message that you want to sign on. 
- The signature is a function of your secret key and the message. 
- Changing the message will change the signature and hence. 
- The signature is generally 256 bits. 
- You also have a public key 
- Verify (message, digital sign on the message, your public key ) = Either True / False 
- Ok, I get it. I cant copy just the signature. What if I copy the message and the signature? 
- So, for the message to be secured by signing, there needs to be a unique number there. Datetime? 
- Ok. So what if the maths is alright but Alice is a crook and she pulls a modi. 
- Keep a running check. Nobody can spend what she does not own. 
- LD (Ledger Dollars)
- History of transactions *is the currency*
- Alice adds a transaction in her ledger and broadcasts. Tom is listening. But how could he trust. 
- The hash function. SHA256( "Humpty dumpty sat on a wall."), creates a *hash* or a *digest* of a fixed length, say 256 bits. 
- SHA256 
  + Is a cryptographic hash function 
  + The hash is one way i.e. you can't create or guess the message from the digest. 
  + 
- Proof of work 
  + Add a number at the end of the ledger. 
  + This number will cause the combined SHA256 to start with 30 zeroes. 
  + You will have to spend the time guessing and running checks to come to the number. 
  + I can quickly check if the number indeed generates a SHA with 30 zeroes. 
  + Proof of work - hard to put in the work - easy to check that the work was put in. 
- How the block is created 
  + All listen to transactions being broadcasted. 
  + Collect them into a block. 
  + Each block is limited to about 2400 transactions. 
  + Prepend with the previous hash. 
  + Append with a proof of work. 
  + Add a small fee to the block and hope to be accepted. 
  + This money does not come from anyone and is called mining. 
  + Now there are nodes that are not listening for transactions. 
  + They are looking for blocks. 
  + They get the block and add them to their personal ledger. 
  + In case of conflict pick the one with the longest block chain. 
  + So, dont believe the new kid in the block chain. 
  + Wait till the chain has grown a bit 
  + And you have not heard a conflicting chain of blocks.
- How much work is required to put in the proof of work 
  + The intent is to require about 10 minutes to do the work. 
  + The work is to find the number that when hashed with the rest of the message 
  + creates a hash that is zeros for the first N numbers 
  + The N is generally changed periodically to keep the time taken to approx 10 minutes


- [Home page of blockchain](http://blockchain.info)
- [Check out the first transaction](https://blockexplorer.com/block/000000006a625f06636b8bb6ac7b960a8d03705d1ace08b1a19da3fdcc99ddbd)
- [protocol labs]()
- [Mining Bitcoin with pencil and paper](https://www.youtube.com/watch?v=y3dqhixzGVo)

- Secure Hashing Algorithm (SHA1)
  + NSA created SHA1 in 1990s 

## Ethereum

- https://www.youtube.com/watch?v=-SMliFtoPn8
- HashBash
- How does the hashing work? 
- A hash gives a string of a XX length for any input. 
- With a small change in the input the hash changes by a lot. 
- Who get to add the next block. 
  + A whole group of people racing to get to be the next one to add a block 
  + 

## Merkel Trees 

- Git uses Merkel Tree 
- 




# How to uninstall Java 9 from Mac? 
[How to uninstall Java 9 from Mac](https://gist.github.com/schnell18/bcb9833f725be22f6acd01f94b486392)


# What is the latest version of Java? 
- Version 8 Update 161 for mac. 
- Release date January 16, 2018 

# What is the version of Java on my mac? 
```
$ java -version 
java version "1.8.0_162"
Java(TM) SE Runtime Environment (build 1.8.0_162-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.162-b12, mixed mode)
```

# Where is Java stored in my mac? 

```
$ pwd 
/Library/Java/JavaVirtualMachines
$ ls -lart 
total 0
drwxr-xr-x  3 root  wheel  102 Feb  8 00:37 jdk1.8.0_162.jdk
drwxrwxr-x  4 root  wheel  136 Feb  8 00:37 ..
drwxr-xr-x  3 root  wheel  102 Feb  8 00:37 .
```

# What is the version of Gradle on my mac? 

```
$ gradle -version 

------------------------------------------------------------
Gradle 4.4.1
------------------------------------------------------------

Build time:   2017-12-20 15:45:23 UTC
Revision:     10ed9dc355dc39f6307cc98fbd8cea314bdd381c

Groovy:       2.4.12
Ant:          Apache Ant(TM) version 1.9.9 compiled on February 2 2017
JVM:          1.8.0_162 (Oracle Corporation 25.162-b12)
OS:           Mac OS X 10.12.6 x86_64
```

# Integrate Gradle with Eclipse? 
There is this buildship thing that seems to be the preferred thing 
http://download.eclipse.org/buildship/updates/e47/releases/2.x


## Building Java Projects with Gradle

https://spring.io/guides/gs/gradle/
Create an empty projet in github. 
https://github.com/kaunjovi/gradleJava101.git
Import into Oxygen as a general project
Add Gradle nature
Create a build.gradle and add java nature. 
Create a src/main/java and add a HelloWorld class
Run 'gradle build' and everything should compile
Apply application plugin and declare main class 
Run 'gradle run' and you should see the SOP 



# What is the latest Eclipse? 
Eclipse Oxygen 2 

## Does Oxygen work well with Gradle? 








## links 

[Ted talk on grit](https://www.ted.com/talks/angela_lee_duckworth_grit_the_power_of_passion_and_perseverance)




6th Jan 2015
27th Nov 2017


# Network 
- CTO @ Thoughtworks, Rebecca Parsons
- Tejasvita Saran


# Cartoons 
- http://www.alexcartoon.com/index.cfm?showall=1

# Benchmarking Java code using Junit 

- http://labs.carrotsearch.com/junit-benchmarks-tutorial.html

# How to annotate your test cases? 

- https://www.mkyong.com/java/java-custom-annotations-example/

# How to run your own behaviour on a Junit call? 

- https://dzone.com/articles/writing-your-own-junit
- http://cwd.dhemery.com/2010/12/junit-rules/
- https://garygregory.wordpress.com/2011/09/25/understaning-junit-method-order-execution/


Declare your own TestRule. 
Create an instance of that in the test class. 



TestRule.apply() allows you to intercept the flow. 
The regular statement is there. You can use that or create a new one and pass that. 

Satement.evaluate() is called. 
Do whatever you want in that one. 
Or you could call base.evaluate() to let the regular flow go on. 


BenchmarkOptions options = description.getAnnotation(BenchmarkOptions.class);
        if (options != null) return options;


# Integrate Gradle with EclipseOxygen 

# Install Gradle on mac, manually 

- https://kodejava.org/how-do-i-install-gradle-in-os-x/


sudo rm -fr /Library/Java/JavaVirtualMachines/jdk-9.0.1.jdk


System.out.println(${word_selection}${});${cursor}



${:import(org.slf4j.Logger,org.slf4j.LoggerFactory)}
private static final Logger log = LoggerFactory.getLogger(${enclosing_type}.class);



log.debug(${word_selection}${});${cursor}


# How to install Java 9 

- If you had a java installed already, 
- This is where you have it. 

```
$ echo $(/usr/libexec/java_home)
/Library/Java/JavaVirtualMachines/jdk-9.0.1.jdk/Contents/Home
```

- Now go ahead, download and install Java 9 version. 
- You might still get Java 8 at the terminal 
- If so you might have to edit your .bash_profile
- You might have set java home to be your older installation

```
open -e .bash_profile
```

- If everything is fine 
- You should see java version 9 in your terminal 

```
$ java -version 
java version "9.0.1"
Java(TM) SE Runtime Environment (build 9.0.1+11)
Java HotSpot(TM) 64-Bit Server VM (build 9.0.1+11, mixed mode)
```




# Invest in shares 

- https://www.linkedin.com/company/2160857/
- [Open an account with Zerodha](https://zerodha.com)

# Get fit 

- Get a bike and a reason to bike a couple of times a week.
- Get a good quality calorie counter 


## Samsung Gear Fit 2 Pro

- if
  - check physically. does it check heart beat. 
  - walk for 5000 steps for 30 days 
  -  
- [13590 on flipkart dec 24](https://www.flipkart.com/samsung-gear-fit-2-pro/p/itmfybewedu2qejg?pid=SBNEYDNFH2ZNMREH&sattr=color&st=color&otracker=hp_pmu_v2_Recently%2520Viewed_1_deskt-homep-2499f_Samsung%2520Gear%2520Fit%25202%2520Black%2520Smartwatch_SMWEHFT8DHJXS9YS_gamificationAndPersonalisation%252FrecentlyViewed_0)
- 


# get some music 
- do we have some good website to download music from anymore? 
- Is bittorent site working yet? 
- There is a slower manual process of doing it one by one from youtube. 
- [online video converter](https://www.onlinevideoconverter.com/mp3-converter) 

## fortuner 4X4 AT 

# What are the problems with Fortuner AT? 
- full transmission replacement.
- ECU reprogramming
- [click here](https://www.topgear.com.ph/news/industry-news/what-s-the-real-score-about-the-new-toyota-fortuner-s-auto-transmission-issue-a00058-a36-20160624)
- Clutch plate defect 
- https://www.complaintboard.in/complaints-reviews/toyota-fortuner-l55372.html
- Clutch plate wearing out too soon. 
- https://autoportal.com/newcars/toyota/fortuner/reviews/clutch-worn-out-at-9800-km-24348.html

  4x2 MT 
    I m getting mileage less than 09 kmpl in the city and 11 over the highway
    https://autoportal.com/newcars/toyota/fortuner/reviews/less-on-mileage-14316.html

  4X2 AT 
    7.8kmpl and 12.5kmpl 
    https://autoportal.com/newcars/toyota/fortuner/reviews/an-suv-with-pocket-drilling-13785.html


## endeavour, 4x4 AT 
- Endy does not come with ISOFIX.
- ACM and TCM updated. (PCM was updated last month)
- Ford puts a sticker on the shaft which starts to come off after some time. 
- I have one of those AQI monitors,
- Sync 2 **SUCKS**.
- The Sync3 system is fantastic and very responsive to use so is the touch screen.
- Is there a MyKey. What does that do? 
- Is the 5th tyre the same size? 
- Accelerator Pedal Vibration over 2000 rpm ( read somewhere it's the throttle wire ? )
- The car is a breeze below 80kmh. Above 80kmh the whistle noise from windshield is annoying.
- The light for high beam is a bit low. Would love to know if there is a fix and what should I do for it
- [click here](https://www.youtube.com/watch?v=RXYv7eymvHo)



# How to buy a property ? 
- go by location 
- know the area 
- know the builder - jeweller 
- builder - godrej 




## what does my car need to have 

Better reach that the current honda city. 
Easier to drive than honda city. Automatic. Or consider a driver. 
At par or less consumption of fuel. Diesel. If petrol it needs to be frugal. 
Something that I can keep in pristine condition. 
  Either the cost for upkeep is too less. 
  Or you factor in the cost. 


# where to go 

Shimla 
  March to June
  
  Jakhu Temple
    Jakhu Temple Park, Jakhu, Shimla, Himachal Pradesh 171001


Jaipur 
  October to March



## pune, kharadi 

- Kharadi | 6,486per sq.ft. | 6.22 %in last 1 year
- Marvel Cerise | 2bhk | 25k 
- Marvel Citrine | 3bhk | 28k 
- Marvel Citrine | 2bhk | 22k 



# what is the minimum appreciation required for a real estate be good buy? 


# buy a property in pune. 

https://housing.com/in/buy/real-estate-pune
[Home buying guide](https://housing.com/buying-guide)

# what is the minimum rental yield for the maths to work out. 



# is this the right time to buy a real estate. 



Gera Trinity 
1.5 km - 20 min walk 
rooms are square at least 
https://www.99acres.com/gera-trinity-towers-kharadi-pune-npxid-r5786
http://www.propreview.in/pune/gera-trinity-towers/
https://www.proptiger.com/pune/kharadi/gera-developments-trinity-towers-513519#discussionPopup513519
https://www.magicbricks.com/property-for-rent/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment,Residential-House,Villa&cityName=Pune&projectSocity=forest%20county

## Price movement in Kharadi 

- [8% up since Oct 15](https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune&projectSocity=forest%20county&price=Y&bar_propertyType_new=10002_10003_10021_10022&mbTrackSrc=tabChange)
- [3% up since Oct 15](https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune&projectSocity=forest%20county&price=Y&bar_propertyType_new=10002_10003_10021_10022&mbTrackSrc=tabChange)
- [3% up since Oct 15](https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune&bedrooms=11702&projectSocity=geras%20trinity%20towers&mbTrackSrc=tabChange&page=1&category=S)
- [2% up since Oct 15](https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune&projectSocity=forest%20county&price=Y&bar_propertyType_new=10002_10003_10021_10022&mbTrackSrc=tabChange)
- [3% down since Oct 15. Song of Joy](https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Pune&projectSocity=forest%20county&price=Y&bar_propertyType_new=10002_10003_10021_10022&mbTrackSrc=tabChange)



# How does OAuth integrate with Spring?? 

[Spring Boot and OAuth2](https://spring.io/guides/tutorials/spring-boot-oauth2/)







# ========== 

Clover Acropolis
  https://www.commonfloor.com/clover-acropolis-pune-rent/prns-yty4ox?f=sem_CF_DSA_Locality-Pune-Viman_Nagar-POVP&gclid=CjwKCAjw0qLOBRBUEiwAMG5xMI-DMaitQndEHbydFP1rzlz9ZDu0sZAUOgdN73DehTX7pfQ6cQhd9hoC6iYQAvD_BwE
  https://www.99acres.com/clover-acropolis-viman-nagar-pune-npxid-r10794

  3bhk - 1500sqft - 35,000


# ==========


iPhone 6 

Bounceback Premium P.U Leather Wallet Style Flip Flap Cover For Apple Iphone 6 / 6s - Brown
https://www.amazon.in/Bounceback-Premium-Leather-Wallet-Iphone/dp/B01LLDZRHK/ref=pd_sbs_107_4?_encoding=UTF8&psc=1&refRID=5EPFNVG4KMS7A8D2MANH
Sold by LD Retails (4.6 out of 5 | 257 ratings) and Fulfilled by Amazon. Gift-wrap available.








# ========

Build a Cryptocurrency Comparison Site with Vue.js



# javascript

A script is something that is used to stitch together an existing app. 




# people 

Jonathan Birnbaum 
Darren Dixon



# pancake 

1 egg 
1 cup of maida 
1.25 milk 
molten .5 cup butter 
baking powder - 3 spoons 

crushed sugar - .75 cup 

vanilla essence

== 

egg - fluffy 
milk + molten butter + vanilla


sugar + maida + baking powder - sieve - 

# Fix the wifi connection 
WEP - Wired Equivalent Privacy. 
WPA - Wifi protected access
WPA2 



# starting 

Savior syndrome - what is that ?? 

promote yourself 

Case study - Douglas Ivester 

Get advise and councel 
  Find power centers and align with them 
    Boss - What will make her look good? 
  Find knowledge centers and learn from them 
  Find colleagues interested in growth and collaborate with them
  Find the raw nerve on everyone and save it like a FD 

Analyze the type of the game 
  Startup 
    Start from scratch. Get things to work. 
  Troubled unit 
    Something is broken. Fix it now. 
  Realignments 
    Things are ambling along. Find the largest problem. Sell the solution. Execute. 

What are you doing ? 
  Is it important for power centers? 
  Is it something on which I can build future wins? 
  Is it something that I can get maximum collaboration on? 

  If it makes you enemies - it is not a contender for an early win. 

  Build your team. 
   


Questions 
  What is working well 
  What is not working well 
    Why is it not working well? 
    Why is it not getting fixed? 
    What will it take to fix it? 
  What is an opportunity that you think the team / I / organization should be jumping on 
  If you were me, what would you focus on? 
  Do you have any dependencies on the output of my current role? If yes, how was it being done till now. 

Ask your boss, “Who is it critical that I get to know?”
invite those people to coffee or lunch and pick their brains.

Dont 
  dont be late. 
  dont dress shabbily. 
  dont take exjob memorabilia with you. 

always listen before you speak. 

Do 
  Ask mgr 
    “Who is it critical that I get to know?”
    Understand how your manager's success is measured. Make sure you add to it. 
    How do we connect. Should I check in every once in a while or should we have a set up meeting.
    What is her work style? Does she like email over meetings. Does she like it if you just pop into her cabin once in a while. 
    What is the best way to connect. 
    How is her success measured? How is she doint with that? Any pain points? Can you help? 

  Get an early win 
    Ask boss + mentor       
  
  Find a office ally 
    We need someone who like to talk. Who is not threatened / impacted by you and dont have a vested interest in derailing you. 


  Also seek a mentor.
    Is there someone at the company who has done what you’re doing before?

  Colleagues - connect. grab a bit. get a coffee. 
    what do they do. 
    who do they report to. 
    what are their pain points 
    what is their view of the org. 

  Follow the company in social media. 
    They seem to be going for cloud. Hmmm :)
    Has there been any news with TIAA? 


Find centers of *power* and *knowledge*
  They are your colleagues. Srs. And juniors who are knowledge centers. 
  Take them out to coffee / lunch and forge a win win collaboration. 

Create a *timeline* of the product 
  Where did it start from 
  What does it do. 
  What does it get data from. What does it give data to. 
  Who are the strongest supporters. 
  Who are the loudest critics. 
  Who were the people in the history of the product. Where are they. 
  What did they try that worked. What did the try that bombed. 

Understand the role
  Who tried it before and succeeded. How?  
  Who tried it before and failed. Why? 

Create status reports. 
  Weekly status reports - should provide a talking point with boss. 
  Monthly status report - should give you a target to aim for. 
  Quarterly status report - what is the quick win that has been applauded by power centers. 

Right hand 
  Technology

Left hand 
  domain knowledge 
  connect with power centers 
  have names drilled in your mind

What do you expect from this role? 
  How was this role's output achieved till now? 
  Why has this not been possible till now? Has anyone tried and failed? Why? 

Under Promise and Over Deliver
  Use surprise as you ally. Dont let it be your foe. 

Take care of self - health. 
Start working before day one. 
Listen. Listen. Make note. Listen. Document. Speak. 
Make your boss look good. 
dont be uppity. be social. blend in. know the names. know their work. 
Say Yes / let me give it a try - to everything. 
Have lunch with your knowpow centers.




https://guykawasaki.com/how-to-rock-the-first-90-days-of-a-job/
https://www.forbes.com/sites/learnvest/2014/06/11/how-to-ace-your-new-job-in-the-first-90-days/3/#61d691654bdf
https://www.forbes.com/sites/quora/2015/05/01/18-useful-tips-for-your-first-90-days-of-any-new-job/
https://www.themuse.com/advice/how-to-own-the-first-90-days-of-a-new-job
https://www.slideshare.net/ramadd1951/the-first-90-days-21759552?next_slideshow=1



# tech-radar 

docker 3 
google compute engine 1 


# Angular
https://dzone.com/articles/real-world-angular-series-part-7a-relational-data?edition=311405&utm_source=Weekly%20Digest&utm_medium=email&utm_campaign=java%202017-08-02


# Startup, AWS 

AWS System Blueprint for a Startup
https://dzone.com/articles/aws-system-blueprint-for-a-startup?edition=311405&utm_source=Weekly%20Digest&utm_medium=email&utm_campaign=java%202017-08-02



# Apache Beam 


[Apache Beam WordCount Example](https://beam.apache.org/get-started/wordcount-example/)

# Docker 

- Docker Community Edition (CE) - looking to get started with Docker and experimenting with container-based apps. 

- [home page](https://www.docker.com)
- [What is Docker?](https://opensource.com/resources/what-docker)

## Read when you know more about docker
- [A Comparison of Docker GUIs](https://dzone.com/articles/a-comparison-of-docker-guis?edition=311395&edition=0&utm_source=Zone%20Newsletter&utm_medium=email&utm_campaign=devops%202017-07-28)
- [Java Memory Consumption in Docker and How We Employed Spring Boot](https://dzone.com/articles/how-to-decrease-jvm-memory-consumption-in-docker-u?utm_source=Top%205&utm_medium=email&utm_campaign=Top%205%202017-07-283)

# Python 

[4 Reasons You Should Learn Python](https://dzone.com/articles/4-reasons-you-should-learn-python?utm_source=Top%205&utm_medium=email&utm_campaign=Top%205%202017-07-283)

StackState


Bank amount 
  HDFC 
  CITI 

LIC 
  


Car : 303,556

Plot address 
  C wing 246

  a 346 

  Surajkund industrial address 
  USIDC  

A 352 

A 346 
Surajpur Site C
Uttar Pradesh 


  Site C 


puchu phone # : 95609 45666


# How to pay the tax challan 

go to https://www.tin-nsdl.com
click "pay taxes online"
click on "CHALLAN NO./ITNS 280  (Payment of Income tax & Corporation Tax)"
choose "(0021) Income Tax (Other than Companies)"




# New job 

Understand the politics first. Blend in. Listen before you speak. 

try to change their boss, and that doesn’t work
Ask how your boss prefers to be contacted—in person, via phone, by email—and how often.
Ask your boss, “Who is it critical that I get to know?”
  invite those people to coffee or lunch and pick their brains
Create “horizontal” alliances with colleagues  

Build credibility for yourself by being seen as someone who is learning and connecting with the organization.


===

Mgr 
  Understand how your manager's success is measured. 
  Your job is to make your manager successful and look good in front of her boss. 
  Make sure your interests are aligned with your manager's interests always.

Colleagues 
  Take each of your colleagues (at least the ones you will be directly working with) to lunch or coffee, and understand how their success is measured. 
  This will help frame the context of any requests/responses from them and you will know how to frame your requests in a way that matters to them.

Center of power 
  Identify centers of power and knowledge. Often, it is not obvious and they are not the same people. 

Center of knowledge 


To avoid / to be aware of 
  Identify the politicians and time wasters while you are at it. Every company has at least a few.
  When tasked with work no one else wants to do, understand why before you commit to it. It is one thing if it is boring (like documentation!) but it is a totally different ball game if no one wanted to take on that task because they know it is doomed to fail! Don't set yourself up to fail.


Documentation 
  You are looking at the situation through fresh eyes. Jot your thoughts and impressions down when they are still fresh. When you are jaded and out of ideas, look here for suggestions.
  Offer to document anything that needs to be documented. You will learn an astonishing amount in the process, strike up conversations with people you would not normally interact with, and uncover collective knowledge that "everyone" knows - it will serve you well in the future.

Understand the big picture even if your particular job is entry level. 

Understand how your company makes money, and how your specific job contributes to it. 

If at all possible, try to be in a role that is a profit center vs. a cost center. 

For example, a team that is building a product that customers pay for is a profit center. Working on the infrastructure team whose clients are internal to the company is often considered a cost center.

Set up a pattern of being trustworthy and following through on your commitments.
Make it a habit to keep track of your time and write status reports for yourself even if your boss doesn't want to see them. This will come in handy when you have to write a self-appraisal or update your resume or you need to justify your ask for a raise.
Set up regular one on one meetings with your manager and take the initiative to set the agenda ahead of every meeting. Share the agenda with your manager at least 24 hours before the meeting. Periodically, ask for feedback and find out how you are doing versus your manager's expectations. Use it to course correct as necessary.
If your performance doesn't match manager's expectations, create a pie chart of how you spent time the past week and share that with your manager. A quick glance is enough to identify if your priorities are misaligned or whether you are not investing as much time on a task as your manager was expecting, or, if you are simply overloaded with too many things on your plate to deliver at the level your manager expects.
Use your first 90 days to think over and document what you learned, so you can make the on boarding process easier for the next person your team hires! I guarantee you that your manager will be very appreciative.


/==



[How to Ace Your New Job in the First 90 Days](https://www.forbes.com/sites/learnvest/2014/06/11/how-to-ace-your-new-job-in-the-first-90-days/#6c20c71e360f)

# workout 
http://mensdressclub.com/2017/07/how-to-be-in-the-best-shape-after-40/


# investing in pune 
https://www.proptiger.com/guide/post/top-5-localities-for-investment-in-pune?







# tatasky 

paid on 30/1

pay by 30/7
1-75897728904
4,165.00




# [From Collections to Streams in Java 8 Using Lambda Expressions](https://app.pluralsight.com/library/courses/java-8-lambda-expressions-collections-streams/table-of-contents)

We create code and pass it as a parameter. 
It is executed by something else, later in point of time and in a different context. 
You can only use *anonymous class* to do this sort of thing, because you can only send classes, not functions. 

Now this can be done by using *lambda expression*

function() { return a;}
()-> a


And then there is function reference 


# Default methods / Defender methods in Interfaces @Java8 


Default methods enable you to add new functionality to the interfaces of your libraries and ensure binary compatibility with code written for older versions of those interfaces.


# Static methods in Interfaces @Java8

# Iterating over collections @Java8

[Iterating over collections in Java 8](http://www.javaworld.com/article/2461744/java-language/java-language-iterating-over-collections-in-java-8.html)

How to step through a set of objects. 
- index (for iterating over an array), 
- cursor (for iterating over the results of a database query), 
- enumeration (in early versions of Java), and 
- iterator (in more recent versions of Java).

Iterator
- An iterator provides a means of "looping" over an encapsulated collection of objects.
- An iterator should allow for the concept of nested looping. 
- An iterator should also be nondestructive in the sense that the act of iteration should not, by itself, change the collection. 
- Of course the operation being performed on the elements in a collection could possibly change some of the elements. 
- It might also be possible for an iterator to support removing an element from a collection or inserting a new element at a particular point in the collection, but such changes should be explicit within the program and not a byproduct of the iteration. In some cases, you will also need to have iterators with different traversal methods; for instance, preorder and postorder traversal of a tree, or depth-first and breadth-first traversal of a graph.

take the responsibility for access and traversal out of the list [ed. think collection] object and put it into an iterator object."


## active iterator / explicit iterator / external iterator
The client controls the iteration in the sense that the client creates the iterator, tells it when to advance to the next element, tests to see if every element has been visited, and so on. 


## passive iterator / implicit iterator / internal iterator / callback iterator
Iterator decides how to iterate 
Client provides the code to be run on the elements

# Iteration in Vector, Hashtables and Enumeration days 


# Iterable @Java8

- Interface Iterable<T>. java.lang.Iterable. 
- T - the type of elements returned by the iterator
- Collection<E> implements Iterable
- Implementing Iterable allows an object to be the target of the "for-each loop" statement.

[official document](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)

# Use static and default interface methods to add functionality to an API 

- [video](https://app.pluralsight.com/player?course=java-8-lambda-expressions-collections-streams&author=jose-paumard&name=java-8-lambda-expressions-collections-streams-m1&clip=13&mode=live)
- add new functionality to API of legacy code. 
- 


# Streams @Java8

- Why streams? 
-   Streams ought to be threadsafe (check and document??) and more easily parallelizable (check and document??)
-   Was there any performance benefit of parallelization?? 
- How to create streams? 
-   Collections and arrays can be used to generate streams. 
- How to use streams? 
-   Stream source (collection / array etc) -> Stream -> Stream -> ... -> result 
-   Stream source (collection / array etc) -> Stream -> Stream -> ... -> forEach - 

- What operations are provided off the shelf for streams? 
- Terminal operation 
-   count()
-   max()
-   average()
-   sum()
-   etc 
- Transformation operation 
-   filter()
-   distinct()
-   sorted()- 

- [good intro starting from arrays and collections](http://www.javaworld.com/article/2461744/java-language/java-language-iterating-over-collections-in-java-8.html?page=2)

# lambda 

- lambda expression in an instance of functional interface
- once again, lamdba expression is an instance of an interface, under the hood. 

```java
public interface Predicate <T> {
  boolean test (T t) ; 
} 
```

Java 7 way of using Predicate with anonymous class

Predicate<String> p = new Predicate <String>() {
  boolean test (String s ){
    return s.length()>0 ; 
  }
}

Java 8 way of doing the same thing 

```java
Predicate<String> p = (String s) -> return s.length()>0 ; 
```

Or your could make it more confusing. Take away the parameter and the return type. 

```java
Predicate<String> p = s -> s.length()>0 ; 
```

And how do you use this

```java 
p.test("Hello world. I am from lambda world.")
```

## How does Java compiler know that this s is a String? 

- Since this is a functional interface, the implementation is bound to be of the one and only one method that it has. 
- Since p is Predicate type, the lambda on the other side of the = has to be the implementation of the only method of the Predicate interface. 
- Hence the parameters and return types are also deducible. 
- 



# Functional Interface 

- It is an interface. A regular old world interface. 
- However, it can have only one abstract method. 
- *Default methods dont count*. You can have multiple of those. 
- *Static methods also dont count*. You can have multiple of those as well. 
- Interfaces are objects as well and inherit a bunch of *methods from Object class*. They dont count. 
- Be a good citizen. Put *@FunctionalInterface annotation* where required. If you dont, it does not break but this has been made optional for the legacy classes and should be used for the new classes. 

# java.util.function 

- There are 4 categories containing 43 total. 
  - Consumers : Consumers accept stuff. 
    + BiConsumer : Consumes two parameters instead of one. 
  - Supplier : Suppliers get stuff for clients. 
  - Functions : Functions apply logic on one object and return back another, changed object. 
    + BiFunction : You know it is a bi. 
    + UnaryOperator extends Function. BinaryOperator extends BiFunction. 
  - Predicates : Perdicates test and return boolean. 
    + BiPredicate 



```java
public interface Consumer <T> {
  public void accept (T t) ; 
}
```

```java 
public inteface BiConsumer <T,U>  {
  public void accept (T t, U u)
}
```

```java 
public interface Supplier <T> {
  public T get() ; 
}

Supplier <Person> personSupplier = () -> new Person() ; 
Supplier <Person> personSupplier = Person::new ; 

```

```
public interface Function < T, R >  {
  public R apply(T t)
}

Function <Person, Integer> ageMapper = (p) -> p.getAge() ; 
Function <Person, Integer> ageMapper = Person::getAge ; 
```

```java 
public interface Predicate <T> {
  public boolean test ( T t) ; 
}

Predicate<Person> ageGT20 = p -> p.getAge() > 20 ; 

```


# Blockchain

- [From barter to blockchain: A history of money](https://techcrunch.com/2017/08/03/from-barter-to-blockchain-a-history-of-money/)
- [Blockchain for non-techies: 1. Agreement](https://hackernoon.com/blockchain-for-non-techies-1-agreement-4a54857b82ba)

# [Blockchain for non-techies: 1. Agreement](https://hackernoon.com/blockchain-for-non-techies-1-agreement-4a54857b82ba)

It is nice to agree. Or agree to disagree. 
An obvious place to start is agreeing about the rules of the society, also known as the laws.


People *can not* enter into any binding agreement they wish. 
  Minimum wage is an example of one of these restrictions

The agreement about agreements is known as contract law.
You can ask the court to intervene should there be a differences in understanding. 

important to reach societal agreement about is whether people in the society can own things at all.
  for example in certain hippy communes owning things is not allowed. 
If individual ownership is allowed, 
  then the next step is to make sure there is agreement about who owns what.
For the big things, it is important that society agrees about who owns what.
Small tribe. Everyone knows everyone else. Everyone knows which hut belongs to what. The ownership is available in distributed memory of the community. 

Big tribe e.g. NY. Too many people. This distributed human memory to lop ownership of houses is not feasible. 
There is a single registry, maintained and updated by the govt. 

Apart from houses, cars (registry with registration plate), ledger in banks (balance of account holders) etc. 

Since the inter-subjective does not objectively exist, modern societies formalize these agreements by documenting them and claim them to be the truth. Trusted authorities are used for maintaining these single sources of “truth”. The agreements have been maintained in this centralized fashion, because there has been no other way to maintaining them.

Blockchain technology enables agreements to be collectively maintained by anyone, taking away the monopoly of “truth” maintenance from central authorities.




# acronyms 

# ISIN | International Securities Identification Number

It is used to uniquely identifies a security. It is originated from ISO 6166. ISIN is used to identify bonds, commercial paper, equities, warrants and most of the listed derivatives. The ISIN code is a 12 character alphanumerical code.
One distinction is that ISIN code doesn’t change by exchange or currency it trades. It is unique unlike symbol that may change based on exhcnage and currency.
To distinguish the exchange it has the same ISIN on each, though not the same ticker symbol. ISIN cannot specify a particular trading location in this case, and another identifier, typically MIC or the three-letter exchange code, will have to be specified in addition to the ISIN. The SEDOL board of the London Stock Exchange has revised their own standards to address this issue.

Example: LT0000610040 (12 character)


OPOL | Official Place of Listing  

## SEDOL (Stock Exchange Daily Official List)
a list of security identifiers used in the United Kingdom and Ireland for clearing purposes. The numbers are assigned by the London Stock Exchange, on request by the security issuer.
Example: B0WNLY7


# coding without framework 

https://dzone.com/articles/programming-without-a-framework?edition=306244&utm_source=weekly%20digest&utm_medium=email&utm_campaign=wd%202017-07-12




# buy - running shoes 

- https://shop.adidas.co.in/#!product/BI2983_adipacerelite20m - 2,519.00 
- https://shop.adidas.co.in/#!product/B42765_vigorbouncem - blue - 6,299.00
- https://shop.adidas.co.in/#!product/B42764_vigorbouncem - grey - 6,299.00
- https://shop.adidas.co.in/#!product/AQ7513_vigorbouncem - reddish - 6,299.00 
- https://shop.adidas.co.in/#!product/B49587_energybounce2m - black - 4,499


# buy - squash shoes 

- [might not be bad. what is the correct size though?](http://www.amazon.in/Yonex-SHB-35-Badminton-Shoes/dp/B06XB41JW2/ref=pd_sbs_309_1?_encoding=UTF8&refRID=XQCSSH76KSWAF7RPMMQT&th=1&psc=1)


# [Understanding Android Application Basics](https://app.pluralsight.com/library/courses/android-application-basics-understanding/table-of-contents)

- install android studio 
- create a new application
- choose api 23 
- choose "basic activity". activity is a screen with lifecycle etc attached to it. 
- Create a MyWorker class. With a public static method. Return double what you got. 
- Is there some significance of the green color of the test folders?? 
- emulator = AVD = android virtual device

```java
FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
fab.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        TextView textView = (TextView) findViewById(R.id.text_value);
        int oldValue = Integer.parseInt( textView.getText().toString()) ;
        int newValue = MyWorker.doubleThat(oldValue) ;
        textView.setText( Integer.toString(newValue));

        Snackbar.make(view, "Changed " + oldValue + " to " + newValue, Snackbar.LENGTH_LONG)
                .setAction("Action", null).show();
    }
});

```

UI built with classes derived from a View class. 
View draws an user interface. It takes care of event handling. 
It is screen and life cycle 
onCreate method is the birth method. 


There are ?? dp per inch. 160. 

Activity must load the layout resource. 
  load layout by setContentView(...)
  reference views by findViewById(...)

Generated class R 
  all layouts in R.layout 
  all ids in R.id 


## Constraint Layout @ Android 




# Connect  

DB - https://www.linkedin.com/in/stephen-hender-b8069738/



# Machine Learning - theory 


## Where all is machine-learning getting used? 
machine learning can potentially predict 
  fraudulent transaction 
  predicting customer churn i.e. whether a customer is going to switch services 
  when will a manufacturing robot e.g. those in automobile industry, is likely to need maintenance etc. 
  doctors diagnosing 
  stores are stocked with goods to buy when we need them


## How is machine-learning different from traditional programming, say in Java? 
Instead of using a static flow of instructions (as in java or such)
You create a model that has the intelligence
Can I see this model and read the intelligence?? I dont want to necessary deploy this unless I am convinced that it has not come up with some brilliant but incorrect logic. 



data - feeds into -> machine algorithms - which generates -> models 
application - uses the -> models - on new set of data -> to find probabilities of a match 
You need - lots of data - lots of compute power - deep knowledge of algorithms - all of these we have, to make machine learning work

You need to know / be willing to know 
  statistics 
  machine learning software
  the domain where you are going to apply this 

machine-learning are of two types 
- Supervised
- unsupervised

## What is supervised machine-learning?

A few examples 
  - might be your input data is a details of houses with the cost of each of them, and you use machine-learning to predict the cost. 
  - ?? 

## What is unsupervised machine-learning? 
?? 

## What are the differences between supervised and unsupervised machine-learning? 
?? 


Machine learning live more and more in the cloud 

Machine learning with open source language - R, Python 

How popular is R?? 

You might fail
Your likelihood of succeeding will increase if you can 
  Ask the right questions
  Ensure that you have the right data. 
  Clearly articulate how will you measure success. 


Start 
  Choose the raw data 
  scrub the data - deduplication, and the likes. 
  get the prpped data 
  apply machine-learning algorithms
  get a model. this is a candidate one and not the final. 
  choose the model you like and deploy for use by applications. 


Training data - you dont create a model. You train a model. 
Supervised / unsupervised learning
Classifying machine-learning problems and algorithms
Training, testing and using a model 


Training data
  Has columns. They are called *features*
  Has the column that we want to predict (in supervised learning). This is called *target value* 


## Categories of machine-learning

### Regression 
We have the data. Visualize a spattering of data in x-y graph. 
There is a line through that spattering, hugging the most density (I believe)
The problem is to predict which way the line would go. 
e.g. 

## Classification 
Is this transaction fraudulent? 
You tend to get back a percentage of probability of a classification

## Clustering - unsupervised
What are our customer segments? 


## Styles of machine-learning algorithms
Decision tree 
Neural networks 
Bayesian 
K means 


## Tutorials on machine-learning
[A tolerably well done, very high level intro to machine-learning](https://app.pluralsight.com/library/courses/understanding-machine-learning/recommended-courses)


# machine-learning with Python 


https://app.pluralsight.com/player?course=python-understanding-machine-learning&author=jerry-kurata&name=python-understanding-machine-learning-m0&clip=0&mode=live


## What are the different versions of Python that can / should be used for machine-learning? 
Python2 - static since 2012. 
Python3 - been around since 2010. This is the future one. We are going to use this for machine-learning. 
  Jupyter notebook, previously called IPython notebook. 
  installed via anaconda distribution
  trying graphical installer on mac
  Create a kaunjovi at anaconda cloud. 


  shift tab - show documentation. 
  shift tab X 2 - show documentation complete. 



## What are the Python libraries used for machine-learning? 

## How to pick the correct algorithm? 

There are more than 50 algorithms. Where??
Check if they are supervised or not. Supervised have around 28. 
Check if they are Regression (continuous value e.g. house price type) or Classification i.e. diagnosing diabetes type. About 20 algorithms. 
Keep this simple. Dont go for ensemble. About 14 are left. 
Basic or Basic++ i.e. Enhanced. Keep it simple for now. 
Lets go with these 3
  Naive Bayes - puts same weightage to all features
  Logistic Regression
  Decision tree 


## Tidy data 

variable = column 
observation = row 
observational unit = table
50 to 80% time will be spent on getting the data to this level 

[free online machine-learning data set](https://archive.ics.uci.edu/ml/datasets.html)
[sample code of machine-learning with python](https://github.com/JerryKurata/MachineLearningWithPython)













# Symphony

- http://www.economist.com/news/21664904-consortium-banks-have-15-competitor-bloombergs-1700-product-symphony-chat-service
- Competitor - Slack, email 
- Symphony’s ownership syndicate, which also includes Bank of America, BlackRock, Citi, JPMorgan, Morgan Stanley and other usual suspects.
- Three companies have agreed to provide news and data to Symphony’s initial release: Dow Jones, Standard & Poor’s Capital IQ, and Selerity,
- all messages on Symphony will be copied and held by an independent entity for at least seven years.

# Links 

[dilbert](http://dilbert.com)
[The Wall Street Journal](https://www.wsj.com)





# REST

- / is important. It is not required at the end of the line. It is required to show hierarchy. 
- Dash-should-be-used-for-readibility (spinal case). Underscore_to_be_avoided (snake case).
- lowercase is better than UPPERCASE. 
- There are no files and hence there are no file extensions in URIs 
- /spies are all the spies. /spies/007 is one of them. /spies/007/victims is a long list. 
- REST is for consumers. REST is not for underlying data structure. 

- [7 Rules for REST API URI Design](https://dzone.com/articles/7-rules-for-rest-api-uri-design-1?edition=305155&utm_source=weekly%20digest&utm_medium=email&utm_campaign=wd%202017-06-28) 
- [Lengthy. Could be exhaustive. Check when there is time. 5 Basic REST API Design Guidelines](http://blog.restcase.com/5-basic-rest-api-design-guidelines/)




# REST in MEAN on Heroku

- https://devcenter.heroku.com/articles/mean-apps-restful-api
- [Getting Started on Heroku with Node.js](https://devcenter.heroku.com/articles/getting-started-with-nodejs#introduction)
- 



http://finance.google.com/finance/info?client=ig&q=NSE:NIFTY,NSE:RELIANCE


# Can you pull data from a 3rd party and put it in mlab? 

Provider. http://services.groupkt.com/country/get/all

Country 
  name 
  alpha2_code 
  alpha3_code 

Install heroku client


mvn archetype:generate -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=5-SNAPSHOT


```
$ heroku apps --all
=== kaunjovi@gmail.com Apps
fetch-qse-data
```

heroku git:remote -a fetch-qse-data
heroku run "sh target/bin/fetchQSEData"


mongodb://alibaba:40chor@ds131512.mlab.com:31512/pine



# Scheduler 
https://devcenter.heroku.com/articles/scheduler
cron 




# Jersey - 
[RESTFul Services in Java using Jersey](https://app.pluralsight.com/library/courses/restful-services-java-using-jersey/table-of-contents)
[Jersey, Heroku, maven-archetype](https://blog.dejavu.sk/2014/01/09/running-jersey-2-applications-on-heroku/)


jaxrs specification - implementation - Jersey
problem - basic authentication - how to do better on security
who is posting to me - how to authenticate 
REST url - noun - not verbs 

tomcat 8.5 seems to be the stable one at the moment. 
http://localhost:8080/jersey/webapi/myresource




Can I start safari in spy mode always?? 


# Goods and Services Tax (GST)


Direct taxes. Income tax, which includes tax on company profits, is the exclusive domain of central government. 
Indirect taxes are taxes levied on manufacture of goods, provision of services and consumption.
indirect taxes levied on manufacture of goods or provision of services are the exclusive domain of central government. 
Taxes on consumption are the exclusive domain of state governments.

Center 
  Direct taxes e.g. that on company profit. 
  Manufacture of goods 
  
State 
  Consumption 


shirt has to first be manufactured before it is consumed. The central government, therefore, levies its indirect tax called central excise at the factory gate.

 a shirt reaches a retail outlet and is bought by a consumer. The state government, at this stage, levies a tax on consumption dubbed value added tax (VAT). 



## What is Goods and Services Tax (GST)? 
## How does GST impact me? 


# mLab

LMpzBIjI9X2ljrt_gaeyVl7Q2OwYKaMQ
mongodb://<dbuser>:<dbpassword>@ds131512.mlab.com:31512/pine
alibaba / challis 
mongodb://alibaba:challis@ds131512.mlab.com:31512/pine

# MongoDB with NodeJs

[RESTful API design with Node.js](https://hackernoon.com/restful-api-design-with-node-js-26ccf66eab09)
mLab - free .5gb space. 
Get the mongodb URI 



# [RESTful API design with Node.js](https://hackernoon.com/restful-api-design-with-node-js-26ccf66eab09)

Create a project folder. 

```
$ pwd 
/Users/parthabhattacharjee/code/restwithnodejs
```

Ensure that  you have got the basic requirements in place. 

```
$ node --version && npm --version && git --version 
v6.9.5
5.0.3
git version 2.10.1 (Apple Git-78)
```

Initiate a node project. 

```
$ npm init
This utility will walk you through creating a package.json file.
... 
... 

$ cat package.json 
{
  "name": "restwithnodejs",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}


```

Install the basic npm dependencies. Why do I need a body-parser? 

```
npm install express mongoose body-parser --save
```

# Nodejs to make google map call and then show the results. 
https://stackoverflow.com/questions/16148403/using-node-js-to-connect-to-a-rest-api


# What is there in the mac path? 

export PATH=<mongodb-install-directory>/bin:$PATH



# Get data 

Where to get data from 
Can nodejs create a REST service
Does heroku have a mongodb 


# Build RESTful web service with nodejs 

[Build Node.js RESTful APIs in 10 Minutes](https://www.codementor.io/olatundegaruba/nodejs-restful-apis-in-10-minutes-q0sgsfhbd)
[Build a Node.js API in Under 30 Minutes](https://medium.freecodecamp.com/building-a-simple-node-js-api-in-under-30-minutes-a07ea9e390d2)



# How to invest in stocks? 

A depository is a bank for securities like shares, debentures, bonds, government securities etc. 
depository participants, or DPs - branch of depository with which you can interact. 

## Short selling 

- Sell something at Y today although you dont have the item yet. 
- Hope to buy the samething at X. 
- Hope to make profit of (Y - X). 
- You stand to loose a huge amount, in case the X grows to some exceptional amount due to some event. 
- [Why bear market are called so i.e. the market in which the amount comes down and short sellers make money](http://www.investopedia.com/articles/basics/03/100303.asp)

## If the shares are all eletronic who is in charge of the safekeeping of those? 

- There are two depositories in India, 
-   CDSL (Central Depository Services (India) Ltd and 
-   NSDL (National Securities Depository Ltd).
- [download list of DPs from CDSL](https://www.cdslindia.com/dp/dplist.aspx)

## Where to open a demat account with? 


[Where to open the DMAT account](https://zerodha.com)
[Nitin Kamath, founder of zerodha](https://www.linkedin.com/in/nithin-kamath-81136242/)
[Zerodha Review](https://www.compareonlinebroker.com/zerodha-review/)
Zerodha uses IL&FS to provide DMAT services. 
IL&FS securities and services ltd. (ISSL) is a Depository Participant (DP) registered with both NSDL and CDSL. 

## What are some of the technical methods for investing in stocks? 

- Elliot Waves, 
- Head and Shoulders Patterns, 
- RSI, 
- MACD
- Dow Theory [link1](http://www.investopedia.com/terms/d/dowtheory.asp)
- Double Bottom

[The Pioneers Of Technical Analysis](http://www.investopedia.com/articles/financial-theory/10/pioneers-technical-analysis.asp)


### Elliot waves - developed by R.N. Elliott and popularized by Robert Prechter

- 1 up, 2 correction, 3 up, 4 correction, 5 topmost 
- A down, B correction, C bottom 
- The basic geometry keeps repeating both inside and outside any waves
- ----
- [Introduction to Elliott Wave Theory](http://www.investopedia.com/articles/technical/111401.asp)
- [Introduction to the Wave Principle](http://www.elliottwave.com/Free-Reports/Introduction-to-the-Wave-Principle)
- [Elliott Wave Basics](http://stockcharts.com/school/doku.php?id=chart_school:market_analysis:elliott_wave_theory)





[jarloo](http://www.jarloo.com/yahoo_finance/)
The service Yahoo finance provides for free stock quotes is REST based.
The API lets you specify multiple symbols to download with a maximum of 200 per call.

BSE, Bombay Stock Exchange, .BO 
NSE, National Stock Exchange of India, .NS


## Can finance yahoo get me indian stock data? 
http://finance.yahoo.com/d/quotes.csv?s=AAPL+GOOG+MSFT&f=nab
http://finance.yahoo.com/d/quotes.csv?s=AAPL+GOOG+MSFT&f=nab


RIIL : Reliance Industrial Infrastructure Limited
http://www.google.com/ig/api?stock=MY_STOCK_TICKER_GOES_HERE


## finance google. 

### Can finance google get me indian stock data? 
Yes. 

http://finance.google.com/finance/info?client=ig&q=NASDAQ%3AGOOG
http://finance.google.com/finance/info?client=ig&q=NSE%3ARELIANCE
http://finance.google.com/finance/info?client=ig&q=NASDAQ:GOOG,NSE:RELIANCE

### Is it deprecated? 
TODO




# How to keep space on the mac hd. 

https://www.howtogeek.com/184091/5-ways-to-free-up-disk-space-on-a-mac/
? Which apps am I not using? 


# Bond 

- A bond / fixed-income security, is a debt instrument created for the purpose of raising capital. 
- They are essentially loan agreements between the bond issuer and an investor.
- The bond issuer is obligated to pay a specified amount of money at specified future dates.


How does it work?
- Actors: Investor. Bond Issuer.
- When an investor purchases a bond, they are "loaning" that money (called the principal) to the bond issuer. 
- When the bond matures, the issuer repays the principal to the investor. 
- In most cases, the investor will receive regular interest payments from the issuer until the bond matures.
- A coupon is the interest paid on the face value of a bond. Annual - USA, Japs. Semi Annual - European. 
- A coupon might be floating. LIBOR (London Interbank Offered Rate)

Different types of bonds
- There are bonds that can be redeemed prior to their specified maturity date, and 
- Bonds that can be exchanged for shares of a company. 

Bond rating agencies

Moody's, S&P and Fitch Ratings — controlling approximately 95% of the ratings business.

- Moody's and 
- Standard & Poor's (S&P) provide a service to investors by grading fixed income securities based on current research. 
- https://en.wikipedia.org/wiki/Bond_credit_rating
- 

## What are other fixed income securities? 

## Can I invest in a bond in India? 

## Read more 

- http://www.investinganswers.com/financial-dictionary/bonds/bond-1287



# Credit Risk 
https://en.wikipedia.org/wiki/Credit_risk
http://www.investopedia.com/terms/c/creditrisk.asp


Actors 
  borrower or issuer of a debt obligation
  lender's or investor's

borrowers expect to use future cash flows to pay current debts

Instruments 
  mortgages, credit cards or other types of loans
  bond (issued by companies and bought by investors)
  insurance (issues by companies)




Credit risks are calculated based on the borrowers' overall ability to repay. 
  applicant's credit history, 
  his capacity to repay, 
  his capital, 
  the loan's conditions and 
  associated collateral.


Similarly, if an investor is thinking about buying a bond, he looks at the credit rating of the bond. 
Agencies such as Moody's and Fitch evaluate the credit risks of thousands of corporate bond issuers and municipalities on an ongoing basis.

For example, if an investor wants to limit his exposure to credit risk, he may opt to buy a municipal bond with a AAA rating. In contrast, if he doesn't mind a bit of risk, he may buy a bond with a lower rating in exchange for the potential of earning more interest.



If there is a higher level of perceived credit risk, investors and lenders demand a higher rate of interest for their capital. 
Similarly, bond issuers with less than perfect ratings offer higher interest rates than bond issuers with perfect credit ratings. The issuers with lower credit scores need to use high returns to entice investors to take a risk on their bonds




Read more: Credit Risk http://www.investopedia.com/terms/c/creditrisk.asp#ixzz4jsD2SNB8 
Follow us: Investopedia on Facebook



# [John Papa and the spec guy ](https://app.pluralsight.com/player?course=code-with-us-angular-quick-start&author=john-papa&name=code-with-us-angular-quick-start-m1&clip=1&mode=live)

NodeJs, Visual Studio Code, 


# *ngFor, *ngIf

Asterisk (*) signifies structural directive. 
Add or remove (not hide)

# How to mark a javascript class as Ng2 component


```
import { Component } from '@angular/core' // at the top of the file.

@Component() // at the top of the class. 

export class MyComponent{
  
}
```

You need a module and register the component with it. 
And you need a main file to bootstrap Ng2. 



# tsconfig.json 

What does this do 
 "noImplicitAny": false,



# [Angular 2 Fundamentals](https://app.pluralsight.com/library/courses/angular-fundamentals/table-of-contents)

https://jcoop.io
https://jcoop.io/angular-2-practice-exercises/


## Export functionality from a js file. 

export {
  foo : someFunction() 
}

## Import functionality in a js file. 

import { foo } from 'someFile.js'

## When and how to use system.js. 

Generally you would use <script> tag in HTML file to load your js files. 
If there are many of them that can be a problem and also there might be too many files loaded up although a particular user will use / need only a few. 
system.js will help. It will pull only those files that are required. 

Add only system.js file and a configuration file to the HTML 

```JavaScript
<script src="system.js" /> 
<script src="config.js" /> 
```

In the config tell the system.js where to find the js files to load from and which file is the main one. 

```JavaScript
var config = {
  // This is the map of the folders
  map : {
    'app' : '/folder/app'
  },  

  // this is the main file. 
  packages : {
    'app' : { main : 'main.js'}
  }
}
```

## Static typing with TypeScript

Valid js 
  let age ; 

Valid ts
  let age : number ; 

## Interfaces with TypeScript

interface ICar {
  is_awesome : boolean 
  reasonable? : boolean 
}

let myCar : ICar 

## Classes with TypeScript

```javascript
class Car {
  
  cost : number 
  color : string 
  constructor( color ){
    this.color = color 
  }

}
```

## Private, Public and the obnoxious shorthands. 
public by default. 

```javascript

class Cat {
  
  constructor ( private name){

  }
}

```

# Ng2 concept 

component contains HTML as well as code 
application has a component tree 
module is a group of related components 
everything within the module has to be registered with the module
Only services are available across ng2 modules 

```
$ node --version && npm --version && git --version 
v6.9.5
3.10.10
git version 2.10.1 (Apple Git-78)
```








# Use nodejs with Express 4 

This is required. The node starter with heroku is created with Express 4. 


# Getting Started on Heroku with Node.js

- https://devcenter.heroku.com/articles/getting-started-with-nodejs#introduction
- Install nodejs and npm. 
- Get a free heroku account. kaunjovi

```
$ node --version 
v6.9.5
$ npm --version 
3.10.10
```

```
$ heroku login
Enter your Heroku credentials.
Email: kaunjovi@gmail.com
Password (typing will be hidden): 
Logged in as kaunjovi@gmail.com

$ heroku create qse
```

Clone the starter nodejs example of heroku. 
Remove the existing .git file. 

```
git clone https://github.com/heroku/node-js-getting-started.git
cd node-js-getting-started/
rm -rf .git 
```

- Create an app in Herku. Choose a name. 
- Got to the Heroku admin panel. Choose build to be done automatically from github push. 
- Really happy to see that I can push code from Sublime to GitHub and that will make it available to the world on Heroku. Awesome. 
- [here is your app](https://qse.herokuapp.com)


Get all the dependencies. 
npm install 

Start the app locally. 
npm start


# Dev env setup for nodejs app 

You need lite server if you want auto view of the changes as you make them. 

  "devDependencies": {
    "lite-server": "^2.3.0"
  }


# mLab MongoDB 

- Once you have pulled data out of jarloo, come back to this. 
- [home page](https://elements.heroku.com/addons/mongolab)
- approx 500Mb free. Might help us get off the ground. 

```
heroku addons:create mongolab:sandbox
```

# Storj - pronounced Storage. 

- Needs further reading. But on the first read did not seem to be a DB in the conventional sense. 
- This is giving 5 GB for free. [home page](https://elements.heroku.com/addons/storj)
- Might be useful to provide caching of the json 
- How to use this? 
- [Using Storj Add-on with Heroku](https://devcenter.heroku.com/articles/storj#using-storj-add-on-with-heroku)
- [Local setup](https://devcenter.heroku.com/articles/storj#local-setup)
- [Using with Node.js](https://devcenter.heroku.com/articles/storj#using-with-node-js)



# How to get stock data

[jarloo](http://www.jarloo.com/real-time-google-stock-api/)
Does jarloo have a python client 



Visual Studio Code 



# Add in twitter 
john papa @john_papa
ward bell @WardBell 






AngularJS : Getting started. 

https://app.pluralsight.com/player?course=angularjs-get-started&author=scott-allen&name=angularjs-get-started-m0&clip=0

- builtwith.angularjs.com 
- plnkr.co 


# Angular 2 getting started

Install npm. Version 3 or above. 

```
$ node --version 
v6.9.5
$ npm --version 
3.10.10
```

http://wumo.com/wumo


## Jeff Bezos 
[1](https://www.youtube.com/watch?v=YlgkfOr_GLY)



# https://app.pluralsight.com/player?course=play-by-play-angular-2-quick-start-john-papa-ward-bell&author=john-papa&name=play-by-play-angular-2-quick-start-john-papa-ward-bell-m0&clip=0&mode=live


## How to get an ng2 archetype quickly on you machine. 

```
// Create the directory where you need this code. 
mkdir ng2001

// Clone the starter code here. 
git clone https://github.com/angular/quickstart ng2001

// Get in it and de-gitify it. We will add our git things here later. 
cd ng2001
rm -rf .git

// Create a local git for this code. We will add it to our github later. 
git init
git add . 
git commit -m "just getting warmed up"

```

You might want to delete the changelog and readme as well. 

There is of course the CLI (Command line interface). But it is too suave for me. 

!!! command K - clear screen . 

### How to get the dependencies for the archetype

```
// download npm dependencies. 
npm i 

```

This should get you node_modules folder in the project with all the goodies. 

```
npm run preprotractor
```

This does something that I am not too clear about. This is one time stuff. Something about updating selenium driver. 

selenium - testing engine
webdriver - lets selenium talk to browser 
protractor - glue for these to make them work with ng2 

### Does it work at all 

npm run start 

It will open the browser as well and show the hello world. 

You have already got live reload working on it. Change something and it will show up without browser update. 

Love the way installing an extension is helpful in Visual code. 
Although it feels a bit slower there. 
Evaluate Sublime for TS programming as well. 


!!! command shift = 
!!! command click = open the related component file. 

Get wallaby to work. It looks awesome. 


Emmet - what is that? What does it do? 






## Getting started with Node.js
What is in Nodes
  libuv - high performance. cross platform. Evented?? library. Took off various unix only libraries. Allows it to be used in Windows. 
  v8 - js engine of chrome. 
  js and c++ - developed for the node itself. 

What is the nvm. Do I need it. 
What is cloud9. Do I need it. 


var foo = require('foo')
foo.value ; 
foo.behaviour()

var Bar = require('Bar')
var obj = new Bar()


fs 
http
crypto 
os 

each .js is a module 
var code = require('./somewhere/mycode') 



### Python for Data Science

- [Python For Data Science Cheat Sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PythonForDataScience.pdf)
- [DataCamp, Intro to Python for Data Science. Just the first chatpter. Not too useful](https://www.datacamp.com/courses/intro-to-python-for-data-science)
- IPython. Interactive Python. 

- [Dataquest | Python basics | Paid](https://www.dataquest.io/m/1/python-basics)

## Python List, 0 based arrays. 

list, which is an object that represents a sequence of values

```python
# months is an empty list (contains no values).
months = []
months.append(1) # How the heck does that work. These are things that cause bugs.
months.append("January")
months.append(2)
months.append("February")
```

# or you could do this in one line. 
temps = ["China", 122.5, "India", 124.0, "United States", 134.1]

# And you can get the length 
len(temps)

# You could also get slices. 
# Values at index 2, 3, but not 4.
two_four = months[2:4]
three_six = months[3:ending_index]

```

```python
countries = []
countries.append("China")
countries.append("India")
countries.append("United States") 

temperatures = [] 
temperatures.append(122.5) 
temperatures.append(124.0) 
temperatures.append(134.1) 

print (countries) 
print (temperatures)
```

# Install Python 3 in Mac. 

- [Installing Python 3 on Mac OS X](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install3/osx/)
- Package managr for OSX. Homebrew. 
- Install Python3 and pip3. 
- Install virtualenv
- Create a dev folder. Cd to that. Create a virtualenv. It will put Python3 in the folder. 
- https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-1-python-basics?ex=9


```
-- Homebrew. The package manager for OSX. 
$ brew --version
Homebrew 0.9.5 (git revision 92c6c; last commit 2015-09-22)

-- Install Python3. 
$ brew install python3
--
-- There might be few issues. Use brew doctor for help. 
--

-- Check the version of Python3
$ python3 --version 
Python 3.6.1

-- You should have pip3 as well. 
$ pip3 --version 
pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)

-- Install virtualenv
$ pip3 install virtualenv
Successfully installed virtualenv-15.1.0
$ virtualenv --version
15.1.0

-- Go to your dev folder and create a virtualenv
$ pwd 
/Users/parthabhattacharjee/git/python003
$ virtualenv devenv
Using base prefix '/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6'
New python executable in /Users/parthabhattacharjee/git/python003/devenv/bin/python3.6
Also creating executable in /Users/parthabhattacharjee/git/python003/devenv/bin/python
Installing setuptools, pip, wheel...done.

-- Activate virtualenv
$ pwd 
/Users/parthabhattacharjee/git/python003
$ source devenv/bin/activate
(devenv) $ 



```


## Download songs using python

- [investigate. there is something wrong with unicode_literals](https://stackoverflow.com/questions/27473526/download-only-audio-from-youtube-video-using-youtube-dl-in-python-script)

### Install unicode_literals 

- why? 
- Why is that weird from __future__ 
- Why does it not install with pip 

```
(devenv) $ pip install unicode_literals
Collecting unicode_literals
  Could not find a version that satisfies the requirement unicode_literals (from versions: )
No matching distribution found for unicode_literals
```

### Install youtube dl 

```
(devenv) $ pip install youtube_dl
Collecting youtube_dl
  Downloading youtube_dl-2017.5.29-py2.py3-none-any.whl (1.6MB)
    100% |████████████████████████████████| 1.6MB 367kB/s 
Installing collected packages: youtube-dl
Successfully installed youtube-dl-2017.5.29
```

### Pick values from prop files that are not checked in the github. 

- We will need to put in passwords etc. We cant have them in the file that we upload in github. 
- We will need some properties file or likes that can be kept in the .gitignore files / folders. 
- [Would this work?](https://stackoverflow.com/questions/3595363/properties-file-in-python-similar-to-java-properties)
- [configparser - this might help with config values](https://docs.python.org/3/library/configparser.html)
- 

- Install configparser in developement virtualenv

```
$ pwd 
/Users/parthabhattacharjee/git/python002
$ source devenv/bin/activate
(devenv) $ pip install configparser
Collecting configparser
  Downloading configparser-3.5.0.tar.gz
Building wheels for collected packages: configparser
  Running setup.py bdist_wheel for configparser ... done
  Stored in directory: /Users/parthabhattacharjee/Library/Caches/pip/wheels/1c/bd/b4/277af3f6c40645661b4cd1c21df26aca0f2e1e9714a1d4cda8
Successfully built configparser
Installing collected packages: configparser
Successfully installed configparser-3.5.0
(devenv) $ pip freeze
appdirs==1.4.3
certifi==2017.4.17
chardet==3.0.3
configparser==3.5.0
idna==2.5
oauthlib==2.0.2
packaging==16.8
pyparsing==2.2.0
requests==2.16.5
requests-oauthlib==0.8.0
six==1.10.0
tweepy==3.5.0
urllib3==1.21.1
(devenv) $ 
```


# How to access Twitter data from Python? 

- [Here are a bunch of python libraries to access Twitter data](https://dev.twitter.com/resources/twitter-libraries#python)
- [Tweepy is Twitter library in Python](https://github.com/tweepy/tweepy)

- [They are using Tweepy. That is a problem](https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/)
- [Another one using Tweepy. If only Tweepy will work.](http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/)

- [Tweepy does not seem to install on my machine](https://stackoverflow.com/questions/20441931/installing-tweepy-on-os-x  )

### Install Tweepy. In devenv. 

```
-- where are you. 
$ pwd 
/Users/parthabhattacharjee/git/python002

-- call the nice devenv
$ virtualenv devenv
New python executable in /Users/parthabhattacharjee/git/python002/devenv/bin/python
Installing setuptools, pip, wheel...done.

-- check if we loaded the correct python
$ which python 
/usr/bin/python

-- bring up the devenv
$ source devenv/bin/activate
(devenv) $ which python 
/Users/parthabhattacharjee/git/python002/devenv/bin/python

-- install tweepy. 
(devenv) $ pip install tweepy 
Collecting tweepy
--
-- some lines deleted for brevity 
-- 
Successfully installed certifi-2017.4.17 chardet-3.0.3 idna-2.5 oauthlib-2.0.2 requests-2.16.5 requests-oauthlib-0.8.0 tweepy-3.5.0 urllib3-1.21.1
```

### Register the app in Twitter

- https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
- [Go to apps twitter](https://apps.twitter.com)
- Provide, name - MiningKaunJovi, description, and website. 
- You will get 
  + Consumer Key (API Key)  
  + Consumer Secret (API Secret)  
  + access_token
  + access_token_secret
- Try to get only read access. You can never be too careful. 


### Install Virtual Environment for Python


```bash

-- Install virtualenv

$ sudo pip install virtualenv

$ virtualenv --version 
15.1.0

-- go to the folder where you want to create your project. 

$ pwd 
/Users/parthabhattacharjee/git/python002

-- Create a virtualenv. Pick any name. 

$ virtualenv devenv
New python executable in /Users/parthabhattacharjee/git/python002/devenv/bin/python
Installing setuptools, pip, wheel...done.

-- This is the system python

$ which python 
/usr/bin/python

-- Activate the virtual ennvironment that you created. 

$ source devenv/bin/activate
(devenv) $ which python 
/Users/parthabhattacharjee/git/python002/devenv/bin/python

-- Now you can run your code for this virtual env. 

(devenv) $ python hello.py
Hello world

-- Once you are done you can come out of the dev Environment

(devenv) $ deactivate

-- back here your python has shifted back to the system Python

$ which python 
/usr/bin/python

```

- http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/
- https://tinwhiskers.net/setting-up-your-python-environment-with-pip-virtualenv-and-pycharm-mac/
- http://technologist.pro/development/developing-in-python-using-python-virtual-environments


### Virtual Environment with Sublime

- [Using Python Virtual Environments with Sublime Text](http://technologist.pro/development/using-python-virtual-environments-with-sublime-text)
- [VirtualEnv Builds in Sublime Text 3](https://inkdroid.org/2015/05/05/virtualenv-builds-in-sublime-text-3/)

```
{
  "build_systems":
  [
    {
      "name": "PYTHON_VENV",
      "shell_cmd": "env/bin/python"
    }
  ],
  "folders":
  [
    {
      "path": "."
    },
    {
      "path": "/Users/parthabhattacharjee/kaunjovi.github.io/_posts"
    }
  ],
  "virtualenv": "/Users/parthabhattacharjee/git/python002/devenv"
}

```



## How do I know if tweepy is successfully installed on my machine? 
## How to find out what all libraries are installed in my machine using pip? 
## Where are the libraries installed by pip in my machine? 


pip freeze 




# Which all packages do I have in my Sublime? 

# How to install Anaconda in Sublime? 

[What all does Anaconda get for me in Sublime?](http://damnwidget.github.io/anaconda/)


$ echo "export PATH=~/bin:$PATH" >> ~/.profile

S3cure123
S3cure098



# Big Data 
[Big Data and Hadoop Essentials on Udemy](https://www.udemy.com/cart/subscribe/course/225796/)

Volume 
Variety : Not strictly structured data. 
Velocity : Rate of growth of data. 

Data acts as DSS for an organisation. Decision Sypport System. 

Digital nervous system
Sense > Interpret > Decide > Act 

Doug and Mike 

- Challanges of BigData 
  - Storage : store stuff that is suitable for computation. 
  - Computational Efficiency : 
  - Data loss 
  - Cost 

# Kafka 

[this is a 2 part series. TODO](https://www.linkedin.com/pulse/kafka-streams-part-2-vishnu-viswanath?trk=v-feed&lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3BxFPgkg0tBf0TVJ%2B%2BSGNc%2Bg%3D%3D)


# Hadoop 

[Big Data and Hadoop Essentials on Udemy](https://www.udemy.com/cart/subscribe/course/225796/)
[Hadoop Starter Kit](https://www.udemy.com/hadoopstarterkit/)

- Hadoop vs 
  + RDBMS 
  + Grid computing 
  



MapReduce 
HDFS 
Name node manages the file system. 
Data nodes 

Map is distributed amongst Nodes. 
Reduce is only in one. 

Code moves to the data. 
On read schema ? 

Pig : scripting language for data scientists. 
Hive : SQL like stuff on MapReduce. Get reduced to MapReduce jobs. 
Sqoop / Flume : 
HBase : 


# Mahout 

# NoSQL 



# Spark




# zookeeper

http://www.tutorialspoint.com/zookeeper/


# Song 

[Kichudine mone mone](https://www.youtube.com/watch?v=Eg4RR8L74m4)


# Quant

The common choices of modelling languages these days include 
R, the open-source statistical language; 
Python, with its extensive data analysis libraries; 
or MatLab. 


[The Self Learning Quant](https://hackernoon.com/the-self-learning-quant-d3329fcc9915)

# R 


# Python

- [Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science)
- [seems to be a good hands on tutorial. TODO](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-learn-data-science-python-scratch-2/)
- [Is it by the python author?](http://python-history.blogspot.in/2009/01/pythons-design-philosophy.html)
- [Programming Foundations with Python](https://in.udacity.com/course/programming-foundations-with-python--ud036/)
- [Introduction to Python for Data Science by edX](https://www.edx.org/course/introduction-python-data-science-microsoft-dat208x-5)
- [Python from codecademy](https://www.codecademy.com/learn/python)
- [Quickstart tutorial SciPy](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)
- [Nice discussion on quora](https://www.quora.com/How-should-I-start-learning-Python-for-Data-Science)
- [The Case Against Python 3](https://learnpythonthehardway.org/book/nopython3.html)

## Python | pip 
pip (package manager for Python)
[How to install pip on mac](https://stackoverflow.com/questions/17271319/how-do-i-install-pip-on-macos-or-os-x)

```
$ python --version 
Python 2.7.10

$ pip -V
pip 9.0.1 from /Library/Python/2.7/site-packages (python 2.7)

```

## Python, offline books 

- [Book | Python for dummies](http://file.allitebooks.com/20151226/Python%20for%20Data%20Science%20For%20Dummies.pdf)
- [Book | Python for Data Analysis](http://www.cin.ufpe.br/~embat/Python%20for%20Data%20Analysis.pdf)

## Python | Installing through Anaconda bundle. 

- [Anaconda, home page](https://www.continuum.io/downloads)
- [youtube tutorial for installing Anaconda](https://www.youtube.com/watch?v=YJC6ldI3hWk)

## Python | code practice 

- https://codefights.com

## Python | LinkedIn API 

- http://thinktostart.com/download-your-linkedin-contacts-with-python/


# LinkedIn | Get API key 

http://thinktostart.com/download-your-linkedin-contacts-with-python/
https://www.linkedin.com/developer/apps/4907001/auth
Client ID:  75ebx4yydlmmjt
Client Secret:  SwL9nNWccTOzaXs0




## How to install in mac.
It is already there. 
However, there are articles about one shoul install  
## Is there an IDE that we could / should use. 



[there is one tutorial. check it out later](https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1?curriculum_id=4f89dab3d788890003000096)
[there is only first part free](https://www.codeschool.com/learn/python)
[some python stuff that I did not understand](https://hackernoon.com/the-self-learning-quant-d3329fcc9915)


# R vs Python 

[Choosing R or Python for data analysis?](https://www.datacamp.com/community/tutorials/r-or-python-for-data-analysis#gs.QIr7Jac)



# MNIST. the “Hello World” of machine learning

MNIST database (Modified National Institute of Standards and Technology database) 
It is a large database of handwritten digits 
MNIST is a database containing images of handwritten digits, with each image labeled by integer. 

Deeplearning4j is a domain-specific language to configure deep neural networks, which are made of multiple layers. Everything starts with a MultiLayerConfiguration, which organizes those layers and their hyperparameters.

- Hyperparameters are variables that determine how a neural network learns. 
  - how many times to update the weights of the model, 
  - how to initialize those weights, 
  - which activation function to attach to the nodes, 
  - which optimization algorithm to use, and 
  - how fast the model should learn.

you train the model with ```model.fit```

[The hello world of machine learning.](https://deeplearning4j.org/mnist-for-beginners)
[quickstart of deeplearning4j](https://deeplearning4j.org/quickstart)


# Machine learning

[machine learning course in pluralsight](https://app.pluralsight.com/library/courses/understanding-machine-learning/table-of-contents)

What are the softwares / tools and techniques that I need to learn to get started with machine learning?? 
How do you get to create a training at pluralsight??
Has machine learning been used to predict bugs in software / unstability in IT shops ?? 


Finds patterns in data. Use the patterns to predict future. 




# coursera on neural networks 

https://www.coursera.org/learn/machine-learning/lecture/zcAuT/welcome-to-machine-learning

What is machine learning? You probably use it dozens of times a day without even knowing it. Each time you do a web search on Google or Bing, that works so well because their machine learning software has figured out how to rank what pages. When Facebook or Apple's photo application recognizes your friends in your pictures, that's also machine learning. Each time you read your email and a spam filter saves you from having to wade through tons of spam, again, that's because your computer has learned to distinguish spam from non-spam email. So, that's machine learning. There's a science of getting computers to learn without being explicitly programmed. One of the research projects that I'm working on is getting robots to tidy up the house. How do you go about doing that? Well what you can do is have the robot watch you demonstrate the task and learn from that. The robot can then watch what objects you pick up and where to put them and try to do the same thing even when you aren't there. For me, one of the reasons I'm excited about this is the AI, or artificial intelligence problem. Building truly intelligent machines, we can do just about anything that you or I can do. Many scientists think the best way to make progress on this is through learning algorithms called neural networks, which mimic how the human brain works, and I'll teach you about that, too. In this class, you learn about machine learning and get to implement them yourself. I hope you sign up on our website and join us. 




# deep learning or deep structured learning or deep machine learning

Is a class of machine learning algorithms

[wikipedia, of course](https://en.wikipedia.org/wiki/Deep_learning)
[Seems to be java friendly](https://deeplearning4j.org/quickstart.html)

# machine learning 



K Means Clustering ? what the heck is that ? 
IRIS dataset ? what the heck is that ? 


First select a tool.if you are not a programmer and lazy like me I would suggest Weka,because it provides a GUI. If you are a programmer I would suggest scikit learn in python.R too is good. 
Then to get your hands dirty you can download dataset from Uci ML repository.try the iris classification problem.scikit learn already has the dataset.another problem you can try is to identify hand written digits using the MNIST dataset.


Tom Mitchell's Machine Learning - understanding concepts. 
which I think is a great read for understanding the concepts, not as much for code examples though) have used the dataset for the "Play Tennis" example as an introduction to Machine Learning. 

What the fk is that? 
https://www.quora.com/Whats-the-Hello-World-program-of-machine-learning
https://in.udacity.com/course/machine-learning-engineer-nanodegree--nd009/


# Fan-tastick rickshaw 

Auto rickshaws or autos 

[click here](https://pragprog.com/the-pragmatic-programmer/extracts/software-entropy)


https://en.wikipedia.org/wiki/Public_transport_in_Mumbai




# Use google play in your application. 

- Install google play services. 24
- [What is this thing for?](http://stacktips.com/how-to/installing-google-play-services-in-genymotion-emulator)

# Get location from google play on android application. 

- [Google link](https://classroom.udacity.com/courses/ud876-5/lessons/3987338872/concepts/43346201990923)

### edit build.gradle

```
compile com....play-services:7+ 
```

### edit manifest file. 

```
meta data android name com....gms.version 
user permission   access fine location 
```

### sequence of code 

- oncreate create google api client 
- onstart use google api client to connect to location service 
- if failed then on connection failed then start again 
- if suspended then on connection suspended then probably cache some information 
- if on connected create location request 
- on location changed get location. 
- [link for the flow](https://classroom.udacity.com/courses/ud876-5/lessons/3987338872/concepts/43251598620923)

### Create a SHA debug key. 

```
$ cd ~/.android

$ pwd 
/Users/parthabhattacharjee/.android

$ keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android
Alias name: androiddebugkey
Creation date: Aug 15, 2015
Entry type: PrivateKeyEntry
Certificate chain length: 1
Certificate[1]:
Owner: CN=Android Debug, O=Android, C=US
Issuer: CN=Android Debug, O=Android, C=US
Serial number: 7afc6549
Valid from: Sat Aug 15 20:29:25 IST 2015 until: Mon Aug 07 20:29:25 IST 2045
Certificate fingerprints:
   MD5:  95:AD:DC:9F:2F:5A:61:08:C2:67:8B:1A:77:58:CF:7D
   SHA1: 3D:3F:32:4C:52:4A:10:BC:E0:AC:71:D6:7B:0C:6F:EE:3B:A5:81:1B
   SHA256: 49:87:D5:AC:23:71:6B:18:AD:01:6D:7C:9D:B1:81:F5:02:05:79:77:80:50:0A:A4:2E:74:4F:B7:4D:A8:03:2E
   Signature algorithm name: SHA256withRSA
   Version: 3

Extensions: 

#1: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: D6 FE A9 5F 4F BF 5F 8F   23 22 3A 7F A4 9A EA FA  ..._O._.#":.....
0010: 97 31 8F 2C                                        .1.,
]
]

```

login to https://console.developers.google.com/iam-admin/projects
create project 
api and auth | apis | google plus api 
{"installed":{"client_id":"211205559617-jtfo5qbqsub063eqddb782vkhbubjad5.apps.googleusercontent.com","project_id":"hybrid-dominion-165017","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://accounts.google.com/o/oauth2/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}



v_saroha@hotmail.com

# Tips for online presence. 

Highlight. 
Online courses. 


# Where to learn android programming? 

- [Android courses by Google.](https://www.udacity.com/india)
- [Dont create your user login. Use google.](https://www.udacity.com/course/add-google-sign-in-to-your-android-apps--ud876-5)
Can we have linkedin provide user login as well. More likely to be verified. 
What else?? 



# How to open md file in Sublime with md format instead of JavaScript? 

- Open all files with current extension with the markdown extended. 


## [Lesson 1: Create Project Sunshine](https://classroom.udacity.com/courses/ud851/lessons/93affc67-3f0b-4f9b-b3a4-a7a26f241a86/concepts/338e2164-2dae-4b96-9600-4082ffea10f7)

  - adb shell am start -n com.package.name/com.package.name.ActivityName
  - Register your stuff in manifest file. 


# Android developement tutorials

- [Developing Android Apps by  Google](https://www.udacity.com/course/new-android-fundamentals--ud851)

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

### [Using phone to debug app rathe than emulator](https://classroom.udacity.com/courses/ud837/lessons/4034888704/concepts/43534185630923)

- Configure your android phone in developer mode. 
  + Browse to Settings / About phone / Build Number and click it 7 times. What. Why. 
  + Now you should see Developer{} available on the phone. 
  + Turn on USB Debugging. 
- Connect phone to mac. 
- Run app from AndroidStudio. Chose to run on the attached phone and not on emulator. 


### The basic main activity. 


package jovi.kaun.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}






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

