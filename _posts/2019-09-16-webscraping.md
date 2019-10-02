---
layout:     post
title:      Webscraping
date:       2019-09-16 
summary:    Webscraping, the Java way
categories: howto 
---

## Webscraping in Java 

## Jsoup 

- if you just needed to connect to a static website
- get some static html 
- and fetch some information from that HTML
- https://mvnrepository.com/artifact/org.jsoup/jsoup

```java
Document doc = Jsoup.connect("https://beta.nseindia.com/get-quotes/equity?symbol=YESBANK").get();
logger.debug(doc.title());
logger.debug(doc.select("#securityWiseDQTQ").text());
```

- This does not work because 
  - The page loads but does not fetch all data right at that moment. 
  - Many data are fetched later only on some action
  - e.g. on click of a tab which was supposed to show that part of the page. 

- [A guide to Web Scraping without getting blocked in 2019](https://www.scrapingninja.co/blog/web-scraping-without-getting-blocked)
- https://antoinevastel.com/


## Selenium and Puppeteer

- This problem of managing lots of Chrome headless instances 
- is one of the many things we solve with ScrapingNinja API

## Getting started with chromedriver, Selenium

- download geckodriver. https://github.com/mozilla/geckodriver/releases/tag/v0.25.0
- geckodriver-v0.25.0-macos.tar.gz, should be good for mac
- java.lang.IllegalStateException: The driver is not executable: 

```bash
chmod +x geckodriver
```

## Headless chrome driver please

- PhantomJS was the leader in this space
- After hearing the news about Headless Chrome, the PhantomJS maintainer said 
- that he was stepping down as maintainer because of 
- I quote "Google Chrome is faster and more stable than PhantomJS [...]" 
- HtmlUnit, PhantomJS, and the other headless browsers are very useful tools
- they are not as stable as Chrome, and 
- sometimes you will encounter JS errors that would not have happened with Chrome

```java 
System.setProperty("webdriver.chrome.driver", CHROME_DRIVER_PATH);

ChromeOptions options = new ChromeOptions();
// This is the headless option.
//options.addArguments("--headless", "--window-size=1920,1200", "--ignore-certificate-errors");

// And this is the non headless one.
// options.addArguments("--window-size=1920,1200", "--ignore-certificate-errors");
options.addArguments("--window-size=800,800", "--ignore-certificate-errors");

WebDriver driver = new ChromeDriver(options);
WebDriverWait wait = new WebDriverWait(driver, 40);

```
