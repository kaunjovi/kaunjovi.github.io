---
layout: post
title: AWS Machine Learning Best Practices
categories: [AWS, ML, Best Practices] 
---


1. https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45287081#notes
1. AWS well architected Machine Learning Lens (?)
1. ML System Architecture 
1. Best Practices for designing Machine Learning Systems 

1. **Responsible AI**
1. Fairness - not biased 
1. Explainability - be able to explain why it said what it said. 
1. Controllability 
1. Privacy and Security - Dont train on PII or sensitive data 
1. Safety 
1. Veracity and Robustness - veractiy is accuracy. It is not hallucinating. 
1. Governance - prove that I am in compliance with any regulaations that policy makers mmight think of 
1. Transparency - publish about capabilities, short comings etc. of the model. 

1. Tools to help with Explainability 
1. **Amazon Bedrock** is the GenAI part. Has model Evaluation tools. 
    1. accuracy. 
    1. send test "prompts" and see that the output is as expected. 
1. **SageMaker Clarify** 
    1. Fairness - bias detection - for this sample there is some impbalance in the data. Tools to rebalance the data. 
    1. Explainability - remove a feature and see what is the impact on the output. 
        1. Output is primarly being driven by these features in the training data. 
        1. These features are friendzoned. 
    1. Mode Evaluation (??) - continuously as it is being run. 
1. **SageMaker Model Monitors** 
    1. Get alert if the Model output is naughty, in production as it is being run. 
1. **Amazon Augmented AI**
    1. Inset human in the loop.      
1. SageMaker ML Governance
    1. **SageMaker Role Manager** Allow people to do things and others not. Is that not IAM? 
    1. **Model Dashboard** to show **Model Cards** - You write high level infomration about your model and publish that. 


## ML Design Principles 

1. Assign Ownership - 
1. Have security controls in place - who is touching the Model. What kind of data is going in and coming out of it. 
1. Resilient - Fault Tolerance and Recoverability - 
    1. Training is time consuming and expensive. 
    1. If things fail 2/3rd of the way, and set up is not recoverable, you will have to do it all over again. 
1. Reusable - these things are expensive, particuarly training. Plan to reuse. 
1. Reproducible - version control - what did this model say 15 days ago to this set of data. 
1. Optimize resources - most efficient hardware. Best model for the purpose. Can SML work instead of LLM. 
1. Reduce cost 
1. Enable automation - CI/CD, CT (training) -  monitor that the training data is not introducing bias 
1. Enable continuous improvement - automatically monitoring and analysing - keeping eye on Model drift 
1. Minimize Environmental Impact - 

## [ML lifecycle](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45287091#notes)

1. Business Goal - what are you trying to do. Find some customer facing result to work backwards from. 

1. Is this a ML problem? Or something else is better suited? 
1. Collect data. Transform it in the form that the Model requires. 
1. Model Development 
1. Collecting, transforming data and creating Model could be an iterative process. 
1. Now deploy. Make it available to the rest of the world. Bedrock and SageMaker can help you create endpoints. 
1. Monitor - is it continuously up and running - what is the quality of the result - 
    1. Any model drift? Hey Model response quality is going worse over time. Lets tweak the model. 
1. Keep calm and keep kaam se kaam. Keep paying EMI. 

## [ML lifecycle / Business Goal Identification](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45287103#notes)

1. https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45287103#notes
1. Get right skills. Accountability and Empowerment. 
1. What is the level of explainability expected. 
1. There is tradoff between Explainability and power of the Model. 
1. If it was explainable as a long nested if statement, might be ML was not required in the first place. (??)
1. Less complicated, more Explainable, less magic. 
1. Use **SageMaker Clarify** - what features are driving the output of your Model the most. 
1. Run experiments. Drop one feature at a time and see how much the output changes. 
1. Model Monitor 
    1. What to monitor? How to measure drift? 
1. Data requirement 
    1. What do we need. Do we have access.     
    1. Do we need license. 
    1. May we use it ethically. 
1. What is your KPI?
1. What is the ROI? 
1. What is the cost of opportunity? 
1. Reduce Total Cost of Ownership (TCO)? 
1. Overall environmental impact / benefit? 

## [ML lifecycle / ML Lifecycle](https://www.udemy.com/course/aws-certified-machine-learning-engineer-associate-mla-c01/learn/lecture/45287107#notes)

1. Collect the data that the ML needs to be trained with 
1. Prepare that data for ML - Process data and Feature engineering 
    1. Store information about the features in **feature store** e.g. SageMaker Feature store. 
1. Train, Tune and Evaluate the Model 
    1. Pull data from Features and Feature Store (both online and offline)
1. Once we do have a Model, store it in a **Model Registry**. Keep the mode with versions. 
1. Do we have a Model? Deploy it to the outside world. 
    1. Pull the appropriate version of the Model from the Model Registry 
    1. Pull infromation from Feature Store. 
1. Applications will hit the model realtime to infer what the output should be for a given prompt / input 
    1. Monitor the results 
    1. Hook up to alarm system. 
    1. Schedule to run the Monitor 
    1. Is there any data being generated in the process that the Model can learn from? Put that back into the system. 



