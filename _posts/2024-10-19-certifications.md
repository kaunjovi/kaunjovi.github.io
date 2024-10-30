---
layout: post
title: Certifications
categories: [certifications] 
---


## Certifications 

1. Cloud 
    1. AWS 
    1. Google 
1. AI/ML 
    1. edX  

## AWS certifications / What is available @ Q4 2024

1. Foundational - No prior experience needed.
    1. Cloud Practitioner 
    1. AI Practitioner 
1. Associate
    1. ML Engineer 
    1. Data Engineer 
    1. *AWS Certified Solutions Architect - Associate (SAA-C03)*
    1. Developer, SysOps Administrator 
1. Professional - 2 years of prior AWS Cloud experience recommended.
    1. Solution Architect / Professional
    1. DevOps Engineer 
1. Speciality 
    1. machine Learning 
    1. Security, Advanced Network 

1. [AWS certification](https://aws.amazon.com/certification/)

## How much study is requried for AWS certifications ? 

1. typically between 40 to 80 total hours of study is required. 
1. Our AWS Certified Associate Courses are 10 to 20 hours long, and 
1. require about 4 hours of study for every 1 hour of video.

1. https://pamit.medium.com/how-i-prepared-for-aws-certification-exams-solutions-architect-and-developer-21892f935768

I am a fan of Cloud services and in particular AWS Cloud. 
I have been working with AWS services since 2018 when 
I realized how powerful the AWS infrastructure is and how convenient its services are for developers, 
compared with equivalent services offered by traditional hosting services in data centers.

Recently I was able to receive 2 AWS certifications, 
Solutions Architect Associate (SAA-C03) and 
Developer Associate (DVA-C02). 
And in this short article I want to share my journey and study plan and resources which helped me prepare for the exams. You can check out my certifications on LinkedIn.

# AWS Exam structure

1. multiple choice and multiple response (??)

1. Choosing the best service for a particular scenario (e.g. KMS vs Secrets Manager vs Parameter Store to store application credentials)
1. Choosing a chain of services to solve a problem (e.g. using an Application Load Balancer with EC2 Auto Scaling vs Lambda functions with API Gateway)
1. Optimizing existing services for a specific use case (e.g. adding RDS read replicas for huge read traffic or converting to Multi-AZ for disaster recovery)
1. Service options (e.g. S3 encryption options: SSE-S3 vs SSE-KMS vs SSE-C)
1. you should also consider the cost factor when selecting an answer. 
1. if a solution suggests using EC2 On-Demand instances and another solution is about using a single Lambda function (or Spot instances), you should probably choose the second answer.


1. once registered - training academy - ?? 
1. udemy course - sample examps - 500 
1. sample exams - scenario based - twist a bit 
1. sample test for 
1. couple of weeks - 1hr / 2hr 
1. 2hr to 3hr - 80 questions 


## US elections 2024 

1. Republican 
1. Democrat 
1. https://medium.com/40fathoms/official-2024-election-prediction-7c09fd9048c6
1. Trump - Red - **Re**publican 
1. Harris - Blue - 
1. P. VP. 
1. US Presidential Election Date 2024	November 5, 2024
1. Office Allotment to the Winner 	January 20, 2025

## SDXL 

1. https://stablediffusionxl.com/
1. Stable Diffusion XL – SDXL 1.0 Modeln - GenAI image generation 

## [Random Forests @ Kaggle](https://www.kaggle.com/code/dansbecker/random-forests)

1. A deep tree with lots of leaves will overfit 
1. because each prediction is coming from historical data from only the few houses at its leaf. 
1. But a shallow tree with few leaves will perform poorly because it fails to capture as many distinctions in the raw data.
1. Even today's most sophisticated modeling techniques face this tension between underfitting and overfitting. 
1. But, many models have clever ideas that can lead to better performance. 
1. We'll look at the random forest as an example.
1. The random forest uses many trees, and it makes a prediction by averaging the predictions of each component tree. 
1. It generally has much better predictive accuracy 
1. than a single decision tree and it works well with default parameters. 
1. If you keep modeling, you can learn more models with even better performance, but many of those are sensitive to getting the right parameters.

```
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
```

1. Import Random Forest 

```
from sklearn.ensemble import RandomForestRegressor
```

1. Instantiate the model and fit 
```
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
```

1. Make some predictions 

```
melb_preds = forest_model.predict(val_X)
```

1. Check how much are we off on average 

```
print(mean_absolute_error(val_y, melb_preds))
```



## AWS Glue DataBrew 
1. visual data preparation tool 
1. users : data analysts and data scientists 
1. to clean and normalize data to prepare it for analytics and machine learning (ML).
1. [youtube / AWS Glue DataBrew Demo Video For Beginners](https://www.youtube.com/watch?v=G8o5ekfbBO4)
1. [youtube / Detailed Demo on AWS DataBrew](https://www.youtube.com/watch?v=tQYBHelHrgE)
