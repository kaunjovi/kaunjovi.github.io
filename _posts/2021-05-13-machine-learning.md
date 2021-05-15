---
layout:     post
title:      Machine Learning
date:       2021-04-03 
summary:    Machine Learning
categories: 
---

# [MOVETO] Equity strategy 

- For Wealth - be wealthy, even after retirement, till death at ripe old age. 
- For Profit - keep vigil on wealth makers. onboard and phase out based on performance. 
- For Tea - earn the daily tea in mkt. make habit. 

## Equity, for wealth

- be wealthy, even after retirement, till death at ripe old age. 

- 20% CAGR is ok. More is better. But 20% is fine. 
- But security of capital is paramount. Non negotiable. 
  - How do we ensure security of capital ? 
    - GBR is correct. 
    - SL @ R(-5%) 
    - 
- We know it was gold. How do we know it is still gold. 
- Check quarterly reports. 
- Are quarterly average delivery percentages healthy? 
- Any negative changes in promo holding? 

### Find 'WEALTH' category tickers
- Is it a ticker from a stable sector? Does the sector have any reason to remain for another 10 years.  
- Is the ticker a sector leader? Has to be 1,2,3. Can a new comer, new innovation change the game.
- CAGR 10,5,3,1 is at least 20%
- Promo holding is good and stable. 
- Pledged shares not significant. 
- Expect the company to be around for another 5 - 10 years at least. 

### Confirm that a 'WEALTH' ticker is still 'WEALTH' category 
- After quarterly reports, within a week or so, check the parameters still hold. 

### Assume all study and hypothesis fail, how to safeguard capital. 
- SIP only. Never bulk at one go. 
- Expect GBR to be correct. Expect LTP above R. 
- If hit R temp exit
- If there is a chance of jump down, multiple SL R-5%, R-10%, R-15% 

### How to buy 
- If all well ... will come to it later. 
- If there is a catastrophe, pandemic, power coup in the making 
- Continue SIP with only 1 share each. 
- Keep the rest in XLS. Pour it in when SMA44 becomes positive. Not negative. Not flat. 


### How to SIP 
- Begining of the month - 
- put an order that is way too less. If you are lucky you shall get it. 
- put another order that catches b/out scenario. If the price runs you shall not have to run. 
- Every week keep adjusting these to trap a price in. 
- It is ok to make the trade at the month end. No rush. 
- But at the month end, it has to be done. 

### How to exit - TGT 

- Dont exit. You are not trying to make money right now. You are just trying to collect. 
- However, 
- Every month put a TGT way too high. Illogical high for that month. If for any reason there is a windfall you should get it. 
- If there is an illogical run like so, you should of course be able to sell, wait and buy at the next dip. 
- You want to put the money back in the same stock as quickly as you can. 


### How to exit - SL 

- Hits R, sit out for the time being. Always have SL=R-5% 
- In fact have SL under R as well to capture any gap down start. 
- Safeguarding capital is the biggest concern. More than making money. 






















# References

- [Series of video on youtube](https://www.youtube.com/playlist?list=PLqFaTIg4myu9-T-fat2zjC5HmTpSybNfa) - Yet to check 
- [Intro to Machine Learning @ Kaggle](https://www.kaggle.com/dansbecker/how-models-work) - Work in progress 


# Intro to Machine Learning @ Kaggle

## [How Models Work](https://www.kaggle.com/dansbecker/how-models-work)

- We use data to decide how to break the houses into two groups, 
- and then again to determine the predicted price in each group. 
- This step of capturing patterns from data is called fitting or training the model. 
- The data used to fit the model is called the training data.
- you can apply it to new data to predict prices of additional homes
- The point at the bottom where we make a prediction is called a leaf.

## [Using Pandas to Get Familiar With Your Data](https://www.kaggle.com/dansbecker/basic-data-exploration)

```python
import pandas as pd
# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()
```

count, shows how many rows have non-missing values.
mean, which is the average
std is the standard deviation, which measures how numerically spread out the values are.
