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

## Supervised Learning / Decision Trees 

1. A decision tree is a non-parametric supervised learning algorithm, 
1. which is utilized for both classification and regression tasks. 
1. It has a hierarchical, tree structure, which consists of a root node, branches, internal nodes and leaf nodes.
1. There are two types of decision trees; 
1. classification trees and regression trees. 
1. From there, they are split into different algorithms and use various nodes and branches to make them whole.
1. Scikit-learn provides two main decision tree algorithms: 
    1. CART (Classification and Regression Trees) and 
        1. CART is the default algorithm used in scikit-learn's DecisionTreeClassifier and DecisionTreeRegressor classes
    1. ID3 (Iterative Dichotomiser 3). 

## Supervised Learning / Decision Trees / DecisionTreeRegressor

1. https://www.geeksforgeeks.org/python-decision-tree-regression-using-sklearn/

## Underfitting and Overfitting 

1. https://www.kaggle.com/code/dansbecker/underfitting-and-overfitting
1. For a tree, if there is only one level of depth, there are two nodes. 
1. For 10 levels there are 1024 nodes. 
1. **overfitting** - too many levels. too less sample in each group. less reliable for new set of data. 
1. **undefitting** - too less levels. the model does not capture enough trends. not reliable for new data. 
1. Use **max_leaf_nodes** in DecisionTreeRegressor to control the depth. 

