---
layout: post
title: Running Notes 
categories: [Running Notes] 
---


## Certification 

## MCP Certification from Huggingface 

https://huggingface.co/learn/mcp-course/en/unit0/introduction
https://huggingface.co/mcp-course
[Hugging Face MCP Course](https://huggingface.co/mcp-course?joined=true)
[Introduction to Model Context Protocol (MCP)](https://huggingface.co/learn/mcp-course/unit1/introduction#introduction-to-model-context-protocol-mcp)
[Key Concepts and Terminology](https://huggingface.co/learn/mcp-course/unit1/key-concepts)
[Architectural Components of MCP](https://huggingface.co/learn/mcp-course/unit1/architectural-components)
[MCP SDK](https://huggingface.co/learn/mcp-course/unit1/sdk)


## MCP resources 
1. What are the MCP resources. 
1. How to use them. 
1. [MCP Resources explained (and how they differ from MCP Tools)](https://medium.com/@laurentkubaski/mcp-resources-explained-and-how-they-differ-from-mcp-tools-096f9d15f767)




## **DeepEval**
1. the open-source LLM evaluation framework
1. Getting started with DeepEval : https://deepeval.com/docs/getting-started

## **Evidently AI** 
1. You can’t trust what you don’t test. Make sure your AI is safe, reliable and ready — on every update.
1. Quick start : https://docs.evidentlyai.com/quickstart_llm


## LLM-as-a-Judge Approach

1. Open-Source Frameworks: 
    1. Libraries like **DeepEval** allow you to implement both single-output and pairwise LLM judges in just a few lines of code. 
    1. **Evidently AI** is another open-source option focused on evaluating and monitoring ML models.
1. Application Development Platforms: 
    1. **LangSmith** and **Langfuse** provide built-in functionality 
    1. to define and run LLM-as-a-Judge evaluators directly on your application traces and datasets, often with no-code solutions.
1. Cloud Services: 
    1. Amazon Bedrock offers a fully managed "LLM-as-a-judge" feature. 
    1. It provides pre-selected judge models and optimized prompts, requiring you only to prepare your dataset in the required format.


## Data, that is ready for AI 

Is your data architecture ready for agents that don’t wait for humans? 
Agentic AI depends on deep, real-time access to machine data, 
not just nicely structured tables, 
but messy logs, traces, and security events. 

We must make a powerful case for a federated data fabric that stitches these sources together 
into a single, governed view so autonomous systems can act fast without flying blind. 




## LangGraph

1. Dictionary 


1. **Typed Dictionary**
1. code the type of the data in the Dictionary as well. 
1. from typing import TypedDict

1. **Union** 
1. from typing import Union 
1. when x can be both int and float 
1. x: Union[int, float]

1. **Optional**
1. You could give it a value or it will be None
1. def some_function ( name : Optional[str]): 
1. Now name can be a string e.g. "Partha" or None. 
1. But it can't be 1, or some other data type. 

1. from typing import **Any**
1. If it can take any value then how is it different from what we already have ?? 

1. square = **lambda** x: x*x
1. shortcut to write small functions. 

1. Different **Elements** in LangGraph
1. **State**
1. The notebook, whiteboard for the Agents?? / Participants / Nodes. 

1. **Nodes**
1. Anything that can receive a state. 
1. Individual functions etc. that does one very specific function in the graph. 
1. They receive input and give output 
1. Often the input, output is updated State.
1. They can use specialized functions call **Tools**
1. **Tool Nodes** are specialized nodes. 
1. They call the Tools and write output back in State. 


1. **Start Node** : Does not do anything itself, but gets started. 
1. **End Node**

1. **Graph**
1. The workflow of the connection of Nodes. 
1. They work on the some common task and update the State. 

1. **Edge** and **Conditional Edge** (traffic light)


1. **State Graph** : Builds and compiles graph 

1. **Runnable** : Anything that can Run. 

1. **Messages** 5 types 
    1. Human 
    1. AI 
    1. System : Set the persona. You are a helpful ... 
    1. Tool : System message but specific to Tool ?? 
    1. Function : Represens the result of a function call 
















1. **Reference**
1. https://docs.langchain.com/oss/python/langgraph/overview
1. [LangGraph Complete Course for Beginners – Complex AI Agents with Python](https://www.youtube.com/watch?v=jGg_1h0qzaM)



## XGBoost (eXtreme Gradient Boosting)

1. It is an optimized implementation of **Gradient Boosting** 
1. and is a type of **ensemble learning method** that **combines multiple weak models to form a stronger model**.
1. builds decision trees sequentially with each tree attempting to correct the mistakes made by the previous one
1. XGBoost uses **decision trees** as its base learners 
    1. combines them sequentially to improve the model’s performance. 
    1. Each new tree is trained to correct the errors made by the previous tree and 
    1. this process is called **boosting**.
1. parallel processing to train models on large datasets quickly






1. **Reference**
1. [Implementation of XGBoost (eXtreme Gradient Boosting)](https://www.geeksforgeeks.org/machine-learning/implementation-of-xgboost-extreme-gradient-boosting/)
1. https://www.geeksforgeeks.org/machine-learning/xgboost/
1. https://www.linkedin.com/posts/swatee-singh-phd-b237916_ai-agenticai-datascience-activity-7394064479321288704-755g?utm_source=share&utm_medium=member_desktop&rcm=ACoAAACOR8UB3zqZApJHm3jXnrFZcfmFgwNtOq4
1. 


## What is ? 
1. similar to ZoomInfo, Uplead


## TOON vs JSON 

1. TOON - Token-Oriented Object Notation.
1. ? Do you have pure tabular data ? CSV would be more efficient. 
    1. So, why are we hearing that Coli. export is CSV is not helping. 
1. the TOON encoder can be used in Node.js or Python environments for batch conversions without performance loss

1. ** Who made TOON and why? ** 
1. At Scalevise, we handle thousands of API requests daily across ChatGPT, Claude, and other large language model platforms. 
1. Every token counts because it costs money.
1. A large portion of our API spend wasn’t tied to actual content but to data structure overhead
1. JSON, the web’s default data format, has brackets, commas, and quotes may seem trivial, but at scale, they add up quickly.
1. That’s when we decided to build our own optimized structure: TOON.

1. **Reference :**
1. https://medium.com/data-science-in-your-pocket/toon-bye-bye-json-for-llms-91e4fe521b14
1. https://youtu.be/oCWfB1lnvLA

## Konnect 
1. Konnect is the fastest way to deploy and manage API and AI gateways.
1. The unified platform for APIs and AI
1. https://cloud.konghq.com/in/welcome
1. 30 day trial - to what ?? 
1. ??? 

## Konnect AI Gateway 

1. Route, secure, and govern AI traffic across any provider.
1. Loved by developers. Trusted by enterprises.
1. ??? 

## Konnect AI Gateway providers
1. https://developer.konghq.com/ai-gateway/ai-providers/
1. ???

## Service Mesh - what is ??? 

## The Fundamentals of Quantum Computing

Learn quantum computing, starting with qubits and quantum mechanics. 
Discover quantum gates, circuits, and algorithms as Grover’s search and Shor’s factoring. 
Explore potential applications.

https://www.educative.io/courses/fundamentals-quantum-computing/what-is-quantum-computing?openHLOPage=true

1. **Qubits** : quantum computing posits a quantum bit (or qubit for short) as the centerpiece and most basic computation unit. Qubits are conceptually very similar to the bits. But unlike bits that can exist in a state of either 0 or 1 at any given time, a qubit has a larger state space. This essentially means that a qubit has more possible states to choose from beyond 0 and 1, and can therefore encode a lot more information compared to a classical bit.
1. quantum computers can use the quantum mechanical properties of **superposition** and **entanglement** of the qubits 

1. Powered by multiple qubits that have superposition and entanglement up their sleeve, 
1. quantum computers represent a new model of computation. 
1. Researchers have used quantum computers to solve and propose solutions to NP-hard problems 
1. (e.g. Protein Folding and the Traveling Salesman Problem) and produced 
1. quantum analogs of classical algorithms. 
1. In most cases, quantum computers and algorithms exhibit polynomial and sometimes exponential time speedup over their classical counterparts.
1. 

1. **NP-hard problems** - ??? 
1. **Traveling Salesman Problem** - ??? 

1. Big tech companies are adopting and investing heavily in quantum computing. 
1. Most quantum computers today are ensconced in expensive refrigerated laboratories, 
1. but these companies have connected their quantum computers to the cloud. 
1. These computers are now free for anyone to access and use. 
1. In the last few years, there has also been an active shift to recognize the power of quantum computers in industrial and commercial use cases. 
1. In short, 2021 is a fun time to be learning quantum computing.
1. Let us first turn our attention back to qubits and how they revolutionize the world of computation.

## The classical bit

1. The bit is the most basic unit of information. 
1. It either represents a 1 or a 0. 
1. It as analogous to a switch being on or off. 
1. A bit’s current status, either 1 or 0, is known as its state.

1. The transistor
1. The value of the bit being 1 or 0 are just abstractions. 
1. it is just a transistor, the building block of all modern computers. 
1. When the transistor allows the passage of current through it we consider this event to represent the 1 and 
1. when the transistor blocks the passage of current we consider this event to represent the 0.

## The quantum bit

1. The quantum bit can represent 0, 1, or both simultaneously. Kaise ??? 
1. This phenomenon is called superposition. 
1. For now, we just need to accept that it’s possible to be 0 and 1 at once.

1. A qubit can be built using any two-level quantum system. An example could be a phosphorus atom within a silicon superconductor.
1. Tangle Lake, Intel's 49-qubit chip.
1. The first takeaway here is that the superposition of 0 and 1 is not some third possible state of a bit. It is a special state that we cannot describe by using a classical bit.
1. 


Think of a slider moving between the values from 0 to 1. 
A superposition of 0 and 1 means our current state is somewhere on the slider, 
it could be a little more towards the 0 side, or it could be a little more towards the 1 side. 
We see from this slider analogy that there are infinitely many possible states 
that we can call “being both 0 and 1 at the same time”.

An equal superposition state would mean 50% of the qubit is a 0 and the other 50% of it is a 1. 

An equal superposition state would mean 50% of the qubit is a 0 and the other 50% of it is a 1. Using this way, we can think of the 
|0> state to be 100% 0 and 0% 1. 
Similarly, we can say the 
|1> state is 0% 0 and 100% 1.


One of the key differences is that all these operations have to be reversible.


## Quantum Computing Fundamentals 

Barron Stone (https://www.linkedin.com/in/barronstone/)  
Olivia Chiu Stone

1. Steps to understand Quantum
    1. How to represent quantum information
    1. Operations on a single quantum bit 
    1. Operations on a multiple quantum bit 
    1. entanglement
    1. Real quantum hardware 
    1. Quantum algorithms



## Volcano for AI 
1. https://volcano.dev/docs#installation



1. https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/
1. Willow quantum chip
1. first-ever algorithm
1. quantum computer can successfully run a verifiable algorithm on hardware, surpassing even the fastest classical supercomputers (13,000x faster)
1. 2019 - Back in 2019, we demonstrated that a quantum computer could solve a problem that would take the fastest classical supercomputer thousands of years.
1. 2024 - Late last year (2024), our new Willow quantum chip showed how to dramatically suppress errors, solving a major issue that challenged scientists for nearly 30 years


1. Introducing Microsoft Agent Framework
1. https://azure.microsoft.com/en-us/blog/introducing-microsoft-agent-framework/



## Decade of agents - it is still years away. 
Andrej Karpathy — AGI is still a decade away
https://www.dwarkesh.com/p/andrej-karpathy

Human limits are features 
Our forgetfulness helps us see patterns and stay creative. AI remembers everything — and often gets trapped in repetition instead of abstraction.


## Of course! Here is a longer story, set in Pune, written from the perspective of an 8-year-old.




## My Super Dooper Big Moon Adventure!**

**Chapter 1: My Didi and the Sky Full of Stars**

Hellow! My name is Abhro. I am eight years old and I live in Pune. I like it here. We have big mountains and nice weather, except in summer when it gets so hot I think I will melt like an ice-cream. My most favrit thing is space. I think about it all the time. The sun is a giant, I mean a GIANT ball of fire. If you put one million Earths inside it, it will just go *poof*! And a supernova is when a star gets so old it goes boom! It’s the biggest boom in the whole universe.

Every summer, when school is closed, we have the best time. All the kids from our society go to the big garden in the evening. And there, under the biggest tree you ever saw, sits Didi. She is not my real grandma, but she is every kid's grandma in our whole society. She tells us stories. She told us one about a monkey who built a bridge to Lanka. Another one about a boy who had a moon on his forehead! That one was my favrit.

My best frends are always there with me. There’s Reyansh. He is amazing. He can hear a song one time and then sing it perfectly. He even knows the old songs my dad listens to in the car. Then there is Arshita. She is the tallest in our class. She plays basketball and she runs so fast, she looks like a rocket! And Akshara. She is so pretty. She always has two nice braids with colourful ribbons and she stands like she is always ready for a photo. But she is also very kind and shares her tiffin with me.

**Chapter 2: The Big News from the Newspaper**

One Tuesday morning, I was eating my poha. My Papa was reading the newspaper. Suddenly, he made a loud noise. "WAH!" I got such a fright I spilled my milk. I thought I was in big trouble.

But Papa was smiling! His eyes were all wide. "Abhro! Listen to this! ISRO... you know, our space people... they have done it! They are making a special, one-time-only, 'Chandrayaan Kids Mission'! They will choose five children from all over India to go to the moon for one whole day!"

I think my heart stopped. For a real second. GO TO THE MOON? The actual moon?

I didn't even finish my poha. I ran out of the house. I ran to Reyansh's house first. I banged on his door. "REYANSH! WE CAN GO TO THE MOON!" He was practizing a song on his little keyboard. He stopped and said, "Really? I will compose a moon song! I will sing it for the Earth from up there!"

Then we ran to Arshita's house. She was bouncing a ball in her driveway. When we told her, she got so excited she threw the ball super high and it got stuck on their roof. She said, "I will take my basketball! I bet I can bounce it from one crater to another!"

Lastly, we found Akshara. She was helping her mom water the plants. She heard the news and got a very serious face. She said, "I will need a very good space suit. One that looks nice in pictures. And I will take a pink flag."

We all decided we had to apply.

**Chapter 3: The Application and The Long, Long Wait**

Applying was hard. We had to write an essay. The question was: "Why do you want to go to the moon?"

I thought and thought. Then I wrote: "I want to go to the moon becos it is our closest neighbour in space. I want to see if the marks on it are really holes or just shadows. I want to jump in low gravity and see if I can touch the Earth from there (just kidding). I will bring back a moon rock for my Didi so she can put it next to her tulsi plant. Also, I want to see if there is any cheese, just for checking."

Reyansh wrote that he wants to sing where there is no sound, to see what true silence feels like before a song. Arshita wrote that she wants to test how high she can really jump. Akshara wrote that she wants to show every girl in India that they can be beautiful and smart and an astronaut all at the same time.

We sent our applications. Then the waiting started. It felt like one billion, trillion years. Every day I would ask my mom, "Did ISRO call? Did they send an email?" She would just laugh and say, "No, beta, not today."

I even told Didi about it. She smiled her crinkly-eyed smile and said, "The moon is very patient, Abhro. It has been waiting for us for a long, long time. It can wait a little more for you."

**Chapter 4: The Big Surprise at School**

One normal day, we were in class learning about fractions. I don't like fractions. They are confusing. Suddenly, our principal, Ma'am, came on the loudspeaker. Her voice was all shaky and excited.

"Would students Abhro, Reyansh, Arshita, and Akshara from Class 3B please come to the principal's office immediately. Thank you."

My stomach did a flip. Oh no. What did we do? Did Reyansh sing too loud in the library? Did Arshita bounce a ball in the hallway? Did Akshara and I talk too much during lunch?

We all walked to the office, feeling very scared. But when we opened the door, we saw two people in cool blue ISRO uniforms! And they were smiling! One uncle had a big camera.

The ISRO aunty knelt down and said, "Are you Abhro?"

I could only nod. My voice was gone.

She said, "On behalf of India and ISRO, I would like to tell you that you have been selected for the Chandrayaan Kids Mission. You are going to the moon."

I think I screamed a little bit. Then Reyansh started singing a happy song right there! Arshita jumped so high she almost hit the ceiling! Akshara was crying happy tears and fixing her ribbons. It was the most amazing, crazy, best moment of my whole entire life. Our whole gang was going to the moon!

**Chapter 5: Getting Ready to be Astronauts**

The next few weeks were a super fun blur. We had to go to special training. Not in Pune, but in a big city. We got to wear puffy white astronaut suits. They made a *swish-swish* noise when we walked. Akshara said, "This fabric is not very flattering," but she still looked cool.

We learned about G-forces. They put us in a big machine that spins around super fast. It felt like a giant was squishing my face! It was weird but fun. Arshita loved it and said "AGAIN!" when it stopped.

We learned about zero gravity in a special plane. It goes up and down and for a few minutes, you float! It was the best feeling in the world. I did three somersaults. Reyansh tried to sing but his voice wobbled all over the place. We laughed so hard. Arshita tried to dribble her basketball, but it just floated away and hit an engineer on the head! We said sorry lots of times.

The food was funny. It was all in packets and tubes. You squeeze it into your mouth. I had mashed potato tube. It was okay. Reyansh got mango pulp and he was very happy.

**Chapter 6: Blast Off!**

The big day came. We went to the big ISRO place in Sriharikota. The rocket was there. It was so, so, so big. It was white and orange and it looked like it could punch a hole in the sky. My mom and dad were there. Mom was crying and taking photos. Dad was trying not to cry but his eyes were red.

We waved to everyone. We saw Didi in the crowd! She waved a white hanky. I felt so brave.

We climbed up the tall tower and got into our seats in the rocket. The seats were like big comfy chairs that hugged us very tight.

The countdown started. A loud voice said: "10... 9... 8..." I held Reyansh's hand. "7... 6... 5..." I heard Arshita whisper, "Goodbye, gravity!" "4... 3... 2... 1... IGNITION! MAIN ENGINE START! LIFT OFF!"

There was a ROAR. The whole rocket shook like our old mixer-grinder when mom makes chutney. I was pushed back into my seat. It felt like an elephant was sitting on my chest. It was scary for a minute, but then I saw the blue sky outside the window get darker and darker.

Then, suddenly, the shaking stopped. The roar stopped. It was very quiet. We were in space!

**Chapter 7: Hello, Zero Gravity!**

The first thing that happened was my pencil floated away from my pocket! It just floated in the air. Then I realised I wasn't sitting in my seat anymore. I was floating! The belt was holding me down, but the rest of me was floating.

"WE'RE FLOATING!" I shouted.

Everyone unbuckled. We became like superman! We flew around the cabin. It was so much fun. Arshita did a perfect somersault. Akshara's hair floated all around her head like a halo. She looked like an angel, but she was worried about her ribbons. Reyansh closed his eyes and said, "This is what music feels like inside my head before I sing it."

We looked out the window. The Earth was below us. It was a giant, beautiful blue and white and green marble. I could see India! I think I saw Pune, but it was very small. It made me feel very small, but also very special. We all live on that one beautiful marble.

**Chapter 8: One Small Step for Kids**

After what felt like a short time, the captain said, "Prepare for lunar landing." The moon got bigger and bigger. It was all grey and covered in circles and mountains. It looked like a giant, dusty playground.

We put on our big helmets and big gloves. We looked like real astronauts from TV.

The landing was a soft *thump*. The door opened. I was chosen to go first because my essay said I would. My heart was beating like a drum.

I carefully climbed down the ladder. The ground was soft and dusty. I took the last step.

"One small step for a kid," I said, my voice all shaky, "one giant... jump for kid-kind!" Then I jumped. I JUMPED! I flew up, like, three meters high! It was easy! I landed softly in the dust.

My friends came down next. Arshita immediately took out her basketball. She bounced it. It bounced so high we almost lost it! It went whoosh! She laughed and said, "I am the moon basketball champion!"

Akshara planted the Indian flag. It had a little pink ribbon tied to it, just for her. She posed next to it, and the camera on the rover took her photo. She looked like a movie star.

Reyansh said, "This is my concert." He turned on his microphone inside his helmet and started singing "Saare Jahan Se Achha". We couldn't hear it outside, but we could hear it in our helmets. It was the most beautiful song ever.

I collected rocks. I got a big grey one for Didi and a small white one for my mom.

We looked up. The Earth was in the black sky. It was a bright blue circle. It looked so peaceful and quiet. There were no borders. It was just... home.

**Chapter 9: The Return Home and The Best Story Ever**

Going back was faster. We blasted off from the moon and landed in the sea near India. A big ship came and picked us up.

When we got back to Pune, it was crazy! There was a big parade! People were throwing flowers and shouting our names. We felt like heroes.

The next day, we went straight to the garden. Didi was waiting under the tree. All the other kids were there too, looking at us with big, round eyes.

We walked up to her. I took out the moon rock. "This is for you, Didi. From the moon."

She took it in her wrinkly hands. She didn't say anything for a long time. She just looked at it and smiled. Then she looked at us. Her eyes were shiny.

"In all my years," she said, her voice soft like old paper, "I have told many stories about magic and gods and heroes. But today, the greatest story is not from me. It is from you. You, my children, are the new storytellers."

She made us sit down. "Now," she said, "Abhro, you tell us. Tell us the story of the boy who went to the moon."

So I did. I told them everything. About the scary blast-off, and the funny floating food, and about Arshita's bouncing ball, and Reyansh's silent concert, and Akshara's flag with the pink ribbon. My friends added parts too.

It was the best story we ever told under that tree.

And now, when we sit there, sometimes Didi tells her old stories, and sometimes we tell our new one. And I look up at the moon at night, and I smile. I know a secret. It's not made of cheese. It's made of memories. And I left a little piece of my heart there, right next to my footprint.

The End.

(P.S. My teacher said this story is too long. But I had lots to say. Going to the moon is a big thing you know.)