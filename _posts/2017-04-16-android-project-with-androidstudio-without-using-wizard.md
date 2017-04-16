---
layout:     post
title:      Android project with AndroidStudio without using wizard
date:       2017-04-16 
summary:    Create Android project with AndroidStudio without using wizard. 
categories: howto 
---

  - Add AndroidManifest.xml. AndroidStudio figures out that this is an Android application. 
  - The basic AndroidManifest.xml

```
<?xml version="1.0" encoding="utf-8"?>

<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="fun.n.games"
    android:versionCode="1"
    android:versionName="1.0.0">

</manifest>
```

  - Run the ```gradle build```. The Android view should also start working. 
  - Run ```gradle installDebug```. At this point the app will **not** show up in the emulator. 
  - 

