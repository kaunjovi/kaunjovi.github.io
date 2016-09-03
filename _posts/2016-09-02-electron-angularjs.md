---
layout:     post
title:      Electron Angularjs
date:       2016-09-02 
summary:    Getting Angularjs with Electron
categories: notes Electron Angularjs
---

# Electron, AngularJs 
  - [click here](http://electron.rocks/electron-angular-creating-sample-application/)
  - [Password keychain](https://github.com/stephanepericat/toptal-electron-loki-demo)
  - Let's create package.json
  - npm init
  - install Electron binary
  - npm install electron-prebuilt --save 
  - This will create folder node_modules and place electron-prebuilt folder in it.
  - Use --save to add this dependency to our package.json
  - Run npm install and it will install all of dependencies listed in package.json.
  - Npm creates also hidden folder .bin which contains executable binaries
  - Execute you Electron app can be found in node_modules/.bin/electron.

```bash
sudo npm install bower -g  
sudo bower init  
sudo bower install angular --save  --allow-root
sudo bower install angular-material --save  --allow-root
```
```html
<script src="/bower_components/my_component/component.js"></script>
```


