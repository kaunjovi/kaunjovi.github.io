---
layout:     post
title:      Hello World with ML
date:       2024-05-12
summary:    Hello World with ML 
categories: 
---


## Hello World of ML 
- [Google Say hello to the "Hello, World" of machine learning](https://developers.google.com/codelabs/tensorflow-1-helloworld#0)

```
import tensorflow as tf
```
- TensorFlow makes it easy to create ML models that can run in any environment. 


```
import numpy as np
from tensorflow import keras
```

```
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
```

But first, here's how we tell it to use 'MEAN SQUARED ERROR' for the loss and 'STOCHASTIC GRADIENT DESCENT' for the optimizer

```
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)
```

- The process of training the neural network, where it 'learns' the relationship between the Xs and Ys is in the model.fit call.





## pip 

- Ensure pip is uptodate 

```
python3 -m pip install --upgrade pip
python3 -m pip --version
```

## venv - virtual environment 




## Install packages in a virtual environment using pip and venv (Python 3.8 and higher)
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments
- 
- This guide discusses how to create and activate a virtual environment 
- using the standard library’s virtual environment tool venv and install packages. 
- Create and activate a virtual environment
- Prepare pip
- Install packages into a virtual environment using the pip command
- Use and create a requirements file
- 
- venv (for Python 3) allows you to manage separate package installations for different projects. 
- It creates a “virtual” isolated Python installation. 
- When you switch projects, you can create a new virtual environment which is isolated from other virtual environments. 
- You benefit from the virtual environment since packages can be installed confidently and will not interfere with another project’s environment.

```
python3 -m venv .venv
```

### Activate a virtual environment
- Before you can start installing or using packages in your virtual environment 
- you’ll need to activate it. 
- Activating a virtual environment will put the virtual environment-specific 
- python and pip executables into your shell’s PATH.

```
source .venv/bin/activate
which python
.venv/bin/python
```


For my hobby projects on Neural Networks, using TensorFlow2, I have generally found Google Colab quite sufficient. It allows me to get to writing code immediately, and not have to bother about installations and configurations at all. Sharing code is a breeze as well. 

All that convenience comes at a cost though. I needed to port one of my hobby projects to my dev machine and all was not well. First hurdle, TensorFlow2 needs a 3.11 version of Python, while 3.12 version of Python has been around since 2023. Python virtual environments saved the day. Second hurdle, the code that executed alright in Colab notebook, refused to behave in dev machine. Small issues, data type incompatibilities here and there, but it costs time. Reminds me of the phrase "write once, debug everywhere". By the time dev setup is happy, weekend has rolled away. 

To all the fellow ai machine learning enthusiasts out there, sharing my lesson learnt here, web based IDEs are really great, but move to proper dev setup as soon as convenient. 








