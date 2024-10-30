---
layout: post
title: Intro to Machine Learning by Kaggle 
categories: [Kaggle, Certification, ML] 
---

1. [How Models Work](https://www.kaggle.com/code/dansbecker/how-models-work)
1. Take some existing data e.g. data about cost of houses sold in an area. 
1. Now, divide the data into buckets based on features that you think is impacting the outcome i.e. sale price. 
1. Simple, naive scenario. The sale price is only depended on whether the house had more than 2 bedrooms or not. 
1. Then predicted prices is the historical average of all sales in that category. 
1. We could use data to find more such patterns. 
1. **fitting** / **training** the model = the process of finding such patterns. 
1. **training data** is the data used to **fit** the model. 
1. This model is then used to **predict** prices for new set of homes. 
1. As you add more levels of **splits** you get **deeper** trees. 
1. The trees culminate in a **leaf** where the predicted value is to be found. 

## [Basic Data Exploration](https://www.kaggle.com/code/dansbecker/basic-data-exploration)

```python 
import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()

```

1. count = number of non missing values. 
1. std = standard deviation. How spread out the values are. 
1. 25th percentile = Sort from min to max. Go 25% down the list. The number is bigger than 25% of the values. 

