---
layout:     post
title:      Upgrade Node.js
date:       2017-02-05 
summary:    Upgrade Node.js on your mac. 
categories: howto 
---

## Upgrade node.js on your mac. 

  - Check your versios before starting. 

```bash 
$ node --version 
v4.2.3
$ npm --version 
2.14.7
```

  - Run these commands. 

```bash
$ sudo npm cache clean -f 
npm WARN using --force I sure hope you know what you are doing.
$ sudo npm install -g n 
/usr/local/bin/n -> /usr/local/lib/node_modules/n/bin/n
n@2.1.4 /usr/local/lib/node_modules/n
$ sudo n stable 

     install : node-v7.4.0
       mkdir : /usr/local/n/versions/node/7.4.0
       fetch : https://nodejs.org/dist/v7.4.0/node-v7.4.0-darwin-x64.tar.gz
######################################################################## 100.0%
   installed : v7.4.0
```

  - Check your node version again. 

```bash
$ node --version 
v7.4.0
$ npm --version 
4.0.5
```

  - Thanks to [solution provided at stackoverflow](http://stackoverflow.com/questions/11284634/upgrade-nodejs-to-the-latest-version-on-mac-os)
