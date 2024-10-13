## Data Mesh / Why. Who. When. 

1. Zhamak Dehghani in 2019


## Resources 

1. Kafka Cluster 
1. Clusters hold your data and enable you to process and analyze streaming data in real-time. 
1. Let's create your first Basic cluster starting at $0/hr for the first ECKU, $0/hr thereafter, 
1. with the Stream Governance Essentials Package included!
1. Cluster name : kaun_jovi, AWS : Ohio (us-east-2)
1. Naaaaaaah. Credit card. 

1. [Use case : Saxo Bank’s Best Practices for a Distributed Domain-Driven Architecture Founded on the Data Mesh](https://www.confluent.io/blog/distributed-domain-driven-architecture-data-mesh-best-practices/)



## [Use case : Saxo bank, Data Mesh](https://www.confluent.io/blog/distributed-domain-driven-architecture-data-mesh-best-practices/)

1. Al data til folket (all data to the people) 
1. is a compelling proposition in an enterprise context. 
1. quickly address integration challenges and deliver data 
1. to those *who can unlock insight and innovate* 

1. **General Data Protection Regulation (GDPR)**
1. European Union (EU) law that protects the privacy of EU citizens and their data 
1. adopted in 2016 and became enforceable on May 25, 2018
1. applies to all organizations that process personal data from the EU
1. regardless of their location (How is that??? What if the firm is in XXX country that does not have extradition treaty with EU???)
1. protects data beyond customer data, including human resources records of employees
1. fines for GDPR violations, €345 million to TikTok, €1.2 billion to Meta, and €90 million to Google. 

1. **Basel Committee on Banking Supervision's standard number 239 (BCBS 239)**
1. strengthen banks' risk data aggregation capabilities and internal risk reporting practices
1. published in January 2013 and applies from 1st January 2016


1. **data mesh architecture** 
1. Driven by the **Data Platforms** team, 

## [Distributed data management at scale](https://www.confluent.io/blog/distributed-domain-driven-architecture-data-mesh-best-practices/)

1. Data mesh is an architectural paradigm
    1. ways of working 
        1. start thinking about data as a product
        1. Data creator : consider the ease with which it can be published, 
        1. Data consumer : discovered, understood, and consumed.
    1. technological change. 

1. Distributed domain-driven architecture
    1. decentralized, federated architecture that forces you to rethink the locality of processing and ownership.
    1. Instead of flowing the data from domains into a centrally owned data lake or platform, 
    1. data mesh stipulates that data domains should host and serve their domain datasets in an easily consumable way.

1. Self-serve platform design
    1. 2020 State of DevOps Report, 
    1. a high DevOps evolution correlates strongly with self-service capabilities, 
    1. as it allows application teams to be more efficient, 
    1. controls to be improved, and 
    1. platform teams to focus on continuous infrastructure improvement.
    1. self-service platform moves beyond pure infrastructure to one that is 
    1. focused on enabling domain teams to publish their own data assets and 
    1. use those published by other teams.

1. Data and product thinking convergence
    1. we think about data as a product and 
    1. believe that the product’s usability can be directly attributed to 
    1. the ease with which it can be discovered, understood, and used. 
    1. Domain data teams are encouraged to apply product thinking to the datasets that 
    1. they provide with the same rigour as they would with any other capabilities.

## [Distributed domain-driven architecture](https://www.confluent.io/blog/distributed-domain-driven-architecture-data-mesh-best-practices/#convergence)

1. Producer-aligned domains 
    1. such as trading represent the transactions (facts) of the business, 
1. master datasets such as the party provide the context for such domains, and 
1. consumer-aligned domains 
    1. such as risk tend to 
    1. consume a lot of data but produce very little (e.g., metrics).

1. Central team? Too small to keep up with the work. Keep central team to oversight. 
1. federated the ownership of domain data and their representations and 

1. the whole is greater than the sum of the parts—
1. that domains “mesh” and do not live in a vacuum. 

1. DGDQ needs to be just enough so that the following can be enabled and governed
    1. Consumers to be decoupled from producers (events over commands)
    1. Authoritative sources to be identified and agreed upon
    1. A standard language to emerge and ensure that information can be efficiently used across the business; 
    1. this standard or “ubiquitous” language is central to the idea of domain-driven design (DDD) 
    1. as a means for removing barriers between developers and domain experts
    1. The common domain plays a key role in this as we look to standardise the fundamental concepts in use across the Bank

1. Domains, are group of people who are SME and owner of the pieces of Data called Data Products.  
    1. They own applications / platforms that are **Authorative Data Sources**
    1. There are **Domain Engineers** (hopefully they know their data)
    1. They collaborate some Data Products (as governed by **Enterprise Data Model**) to the central pool. 
    1. The Domain Team is responsible for:
    1. Identifying the authoritative source for a dataset
    1. Creating the relevant data model(s)
    1. Making data products available to other teams through the data fabric
    1. Remediation of data quality (DQ) issues; 
    1. issues should be fixed at the source, not on consumption

1. Enterprise Data Architect - “data custodian.” Learn, iterate, and improve.
    1. Create and maintain the **Enterprise Domain Model**
    1. This **Domain Model** dictates the constituents of the **Data Model**. 
    1. The **Domain Engineer** and **Data Architect** work together to maintain the Data Model. 
    1. Collaborating with domain teams to develop the conceptual model / Enterprise Domain Model
    1. Curating and shaping our data domains into something that has long term value / a product 
    1. Approving changes to physical domain models


1. Data Governance Office - “Activating” data domains
    1. identifies Data Owner - and what does that person do? 
    1. The Data Governance Office is responsible for:
    1. including identifying ownership, 
    1. known data quality issues, etc.

1. Data Office 
    1. Who all is there in the Data Office? 

The domain language 
the conceptual model (the challenge is to keep it as light as possible) and 
the physical model (which we embellish with metadata). 

We are not concerned with generating the physical model from a conceptual diagram as we believe that this switches the focus away from reasoning about a domain to visual programming. So, who does that?

## [Self-service platform design](https://www.confluent.io/blog/distributed-domain-driven-architecture-data-mesh-best-practices/#convergence)

1. Data mesh is an architectural paradigm that is technology agnostic. 
1. One option is - Confluent as the foundational layer of our data fabric (huh?? what is data fabric now??)
1. an authoritative interface to data domains, (what is that ??)
1. alongside a more traditional request-response interface. (and what is that in case of data??)

## [Data Mesh via DataHub](https://opensource.optum.com/blog/2022/03/23/data-mesh-via-datahub)

1. Data Forge, Data Mesh & DataHub










## Data Mesh / architecture ( https://www.datamesh-architecture.com/#why )



## When to even bother about Data Mesh ? When not? 

1. https://www.kainos.com/insights/blogs/thinking-about-data-mesh
1. [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html)


## What are the benefits of being a Data Driven organization ? 

1. providing the best customer experience based on data and hyper-personalization; 
1. reducing operational costs and time through data-driven optimizations; 
1. and giving employees super powers with trend analysis and business intelligence. 
1. They have been investing heavily in building enablers such as data and intelligence platforms. 

## What are the headwinds to transform data platform in any firm ? 

1. migrating from decades of legacy systems, 
1. resistance of legacy culture to rely on data, and 
1. ever competing business priorities. 

## [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html)

1. Zhamak Dehghani - principal technology consultant at Thoughtworks
1. Many enterprises are investing in their next generation data lake, 
1. with the hope of *democratizing data at scale* 
1. Data platforms based on the data lake architecture have common failure modes that lead to unfulfilled promises at scale. 
1. To address these failure modes we need to shift from the centralized paradigm 
1. of a lake, or its predecessor data warehouse. 
1. shift to a paradigm that draws from modern *distributed architecture*: 
1. considering domains as the first class concern, 
1. applying platform thinking to create self-serve data infrastructure, and treating data as a product.


## The current enterprise data platform architecture - Data Lake 

1. What is 3rd generation data and intelligence platform ???

1. The first generation: 
    1. proprietary enterprise data warehouse and business intelligence platforms; 
    1. solutions with large price tags that have left companies with equally large amounts of technical debt; 
    1. Technical debt in thousands of unmaintainable ETL jobs, tables and reports 
    1. that only a small group of specialized people understand, 
    1. resulting in an under-realized positive impact on the business.

1. The second generation: 
    1. big data ecosystem with a data lake 
    1. complex big data ecosystem and long running batch jobs operated by 
    1. a central team of hyper-specialized data engineers 
    1. have created data lake monsters that at best has enabled pockets of R&D analytics; 

1. The third and current generation data platforms are similar to the previous generation, with a modern twist towards 
    1. streaming for real-time data availability with architectures such as Kappa, 
    1. unifying the batch and stream processing for data transformation with frameworks such as Apache Beam, as well as 
    1. fully embracing cloud based managed services for storage, data pipeline execution engines and machine learning platforms. 

## Why does it fail - Architectural failure modes

1. domain of internet media streaming business 
1. such as Spotify, SoundCloud, Apple iTunes, etc. 

1. Centralized and monolithic
1. Sources to Ingest (a,b,c,d) -> Big Data Platform -> Consumers to serve (x,y,z)
1. Ingest data from all corners of the enterprise, 
1. ranging from operational and transactional systems and domains 
1. that run the business, or external data providers that augment the knowledge of the enterprise. 

1. For example in a media streaming business, data platform is responsible for ingesting large variety of data: 
    1. the 'media players performance', 
    1. how their 'users interact with the players', 
    1. 'songs they play', 
    1. 'artists they follow', 
    1. as well as 'labels and artists' that the business has onboarded, 
    1. the 'financial transactions' with the artists, and 
    1. external market research data such as 'customer demographic' information.


1. The monolithic data platform hosts and owns the data that logically belong to different domains, e.g. 
1. 'play events', 'sales KPIs', 'artists', 'albums', 'labels', 'audio', 'podcasts', 
1. 'music events', etc.; data from a large number of disparate domains.

??? 



## [Domain Driven Design (DDD) / Bounded Context](https://martinfowler.com/bliki/BoundedContext.html)

1. Bounded Context is a central pattern in Domain-Driven Design (DDD) - dealing with large models and teams
1. DDD deals with large models by dividing them 
1. into different *Bounded Contexts* and 
1. being explicit about their interrelationships.

1. DDD is about designing software based on models of the underlying domain. 
1. A model acts as a UbiquitousLanguage to help communication between software developers and domain experts. 
1. It also acts as the conceptual foundation for the design of the software itself - 
1. how it's broken down into objects or functions. 
1. a model needs to be unified - that is to be internally consistent so that there are no contradictions within it.
    1. Where will we get this internal consistent domain? 
    1. Is the expectation that there is an inherent consistent model of the business that someone knows and will be able to document and/or approve? 
    1. What if there is none and/or there is none interested in owning putting that on paper? 


## Speak the same language. 

1. But can you influence the world? 
1. It is your job, being in the middle of it all to make sense of everyone and hence you have a vested interest in having everybody speak the same language, but the other domains do not have that need. 
1. Why will they not speak language that is nuanced about their niche. 
1. ============
1. As you try to model a larger domain, 
1. it gets progressively harder to build a single unified model. 
1. Different groups of people will use subtly different vocabularies in different parts of a large organization. 
1. The precision of modeling rapidly runs into this, 
1. often leading to a lot of confusion. 
1. Typically this confusion focuses on the central concepts of the domain. 
1. Early in my career I worked with a electricity utility - 
1. here the word “meter” meant subtly different things to different parts of the organization: 
1. was it the connection between the grid and a location, 
1. the grid and a customer, 
1. the physical meter itself (which could be replaced if faulty). 
1. These subtle polysemes could be smoothed over in conversation but not in the precise world of computers. 
1. Time and time again I see this confusion recur with polysemes like “Customer” and “Product”.

In those younger days we were advised to build a unified model of the entire business, *Not happening* 

1. DDD recognizes that 
1. “total unification of the domain model for a large system will not be feasible or cost-effective” 1. 
1. DDD divides up a large system into Bounded Contexts, 
1. each of which can have a unified model - essentially a way of structuring MultipleCanonicalModels.
1. So, have a namespace 

## [Domain Driven Design (DDD) / Bounded Context]

Bounded Contexts have both unrelated concepts (such as a support ticket only existing in a customer support context) but 
also share concepts (such as products and customers). 
Different contexts may have completely different models of common concepts with mechanisms to map between these polysemic concepts for integration. 
Several DDD patterns explore alternative relationships between contexts.

Various factors draw boundaries between contexts. 
Usually the dominant one is human culture, 
since models act as Ubiquitous Language, you need a different model when the language changes. 
You also find multiple contexts within the same domain context, 
such as the separation between in-memory and relational database models in a single application. 
This boundary is set by the different way we represent models.

DDD's strategic design goes on to describe a variety of ways that you have relationships between Bounded Contexts. 
It's usually worthwhile to depict these using a context map.



## [Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html)

1. Ubiquitous Language is the term Eric Evans uses in 
    1. Kaun hai bhai ye ??? Eric Evans. Could only find book writer reference. 21 years in some company. 
1. Domain Driven Design for the practice of building up a 
1. common, rigorous language between developers and users. 
1. This language should be based on the Domain Model used in the software - 
1. hence the need for it to be rigorous, since software doesn't cope well with ambiguity.
1. Huh ??? Software -defines-> Domain Model -defines-> Ubiquitous Language ??? So it is based on software and not on business?


1. Evans makes clear that using the ubiquitous language in conversations with domain experts 
1. is an important part of testing it, and hence the domain model. 
1. He also stresses that the language (and model) should evolve as the team's understanding of the domain grows.
1. By using the model-based language pervasively and not being satisfied until it flows, 
1. we approach a model that is complete and comprehensible, made up of simple elements that combine to express complex ideas.
1. Domain experts should object to terms or structures that are awkward or inadequate to convey domain understanding; 
1. developers should watch for ambiguity or inconsistency that will trip up design.
1. -- Eric Evans

1. Dont see how this can be used in Tcompany. 

## Data Mesh vs Data Fabric

1. https://www.linkedin.com/pulse/data-mesh-vs-fabric-innovant-us/?trackingId=Bs8b9vrhSY2eAdZaSCCBUw%3D%3D



1. https://www.datamesh-architecture.com

1. [Zhamak Dehghani](https://www.linkedin.com/in/zhamak-dehghani/) in 2019 
1. O'reilly "Data Mesh" - [Delivering Data-Driven Value at Scale](https://www.amazon.in/Data-Mesh-Delivering-Data-driven-Value/dp/1492092398)
1. Decntralized sociotechnical approach to 
    1. It is about organizational issue about ownership 
    1. Technology comes second. It is only one of the enablers to the intended end state. 
1. Share and manage analytical data in 
1. complex and large scale environment 
1. within and across organizations
1. [What is Data Mesh? Managing Data for Speed and Scale](https://www.youtube.com/watch?v=Keax6_SP77A&t=103s)

## Data Mesh / Foundational Principle 
1. [What is Data Mesh? Managing Data for Speed and Scale](https://www.youtube.com/watch?v=Keax6_SP77A&t=103s)


## How do you engineer this? 

1. In API space, OpenAPI. AsyncdAPI 


## domain ownership 

1. The domain ownership principle mandates the domain teams to take responsibility for their data. 
1. analytical data should be composed around domains, 
1. similar to the team boundaries aligning with the system’s bounded context. 
1. Following the domain-driven distributed architecture, analytical and operational data ownership is moved to the domain teams, 
1. away from the central data team.

1. What is the meaning of taking ownership? 
    1. Do they have dollar, resource, and skill? 
    1. If they had why did they not set up the team to start with? 
    1. What happens to the dollar saving that the firm was supposed to show, due to centralization. 

## data as a product 

1. The data as a product principle projects a product thinking philosophy onto analytical data.
    1. What does that mean beyond thinking? 
    1. What is the responsibility? To who? 
    1. What are they suppsoed to get back - money, budget, headcount? 
1. This principle means that there are consumers for the data beyond the domain. 
1. The domain team is responsible for satisfying the needs of other domains by providing high-quality data. 
    1. Are these "clients"? In the sense that they are commiting some budget to this effort. 
1. Basically, domain data should be treated as any other public API.

## self-serve data infrastructure platform

1. You do own the data platform. The technical platform. 
1. Domain teams can come in, create data products, and consume data products. 
1. So, they have to follow some standards at least. Have the same nomenclature / data dicitionary. How does that work. 
    1. And they never do. Why would they do? There is fight between them to name things their way. 
1. Adopt platform thinking to data infrastructure. 
1. A dedicated data platform team provides domain-agnostic functionality, tools, and systems to build, execute, and maintain interoperable data products for all domains. 
1. With its platform, the data platform team enables domain teams to seamlessly consume and create data products.

## federated governance

1. What are the roles required in governance
1. Who owns which role. 
1. The federated governance principle achieves interoperability of all data products through standardization, 
1. which is promoted through the whole data mesh by the governance group. 
1. Who forms to governance group? Who owns it? 
1. The main goal of federated governance is to create a data ecosystem with adherence to the organizational rules and industry regulations.


## design principle 

1. The design should allow domain teams to perform cross-domain data analysis on their own. 
1. Domain with its responsible team and its operational and analytical data. 
1. The domain team ingests operational data and builds analytical data models as data products 
1. The data products are to perform their own analysis. 
1. They **may also** choose to publish data products with data contracts to serve other domains’ data needs.
1. What are data contracts. 


## Actors in the Data Mesh 

1. Domain Team - The protagonist (XXX are not interested, but VD is playing proxy)
    1. Ingest operational data 
    1. Create data products to power analysis for self 
    1. (I dont know why) publish data contracts and publish Data Products 
    1. And who is domain. They are doing their job just fine. They dont need any of this s**t.
1. Data Platform Team (D2)
    1. Data storage facility. Data Query Engine. 
    1. Data Product Catalog. 
    1. Data contract management (what is this?)
    1. Policy automation. Which policy are we automating here?
        1. Policy as code. The Data Quality rules? Or there is more? 
        1. What about data retention? 
        1. What about security and data access? 
    1. Monitoring ( monitoring what? usage of data product? )
1. Governance Group (RZ)
    1. Create policies. interoperability. Documentation. Security. 
    1. Privacy. Compliance. 
    1. Are they governance or policy writers? 
    1. What is their Role? They dont have tech know-how to help with platform. 
    1. They are not the best with Domain knowledge. The Domain Teams are. 


## Data Product / What exactly is it? 

1. A data product is a logical unit (so it could be anything as far as tech goes)
1. that contains all components to process and store domain data 
1. for analytical or data-intensive use cases and 
1. makes them available to other teams via output ports. 
1. You can think of a module or microservice, but for analytical data.

1. https://www.datamesh-architecture.com/data-product-canvas
1. [Jacek Majchrzak](https://www.linkedin.com/in/jacekmajchrzak/)
    1. Co-author of "Data Mesh in Action" by Manning.
1. "data product is an autonomous, read-optimized, standardized data unit containing at least one dataset (Domain Dataset), created for satisfying user needs". 
    1. autonomous - ??? - so it has to be the entire slice, from SOR(s), input ports, slice of database, slice of query engine, slice of codified policies, output ports, the whole nine yards. 
    1. read-optimized - this is definitely past the operational database and in the zone of reading for analytics, predictive ananlytics, BI etc. 
    1. standardization - interoperability hinges on standardization. 
    1. created for user - dont make anything for the sake of the architecture or the idea. Execution i.e. spending resource and time always must have a user and ROI. 


## Data Mesh 

1. Conceptually, a mesh is a graph, a network, consisting of nodes and connecting edges. 
1. Each node in a data mesh is called data product. 
1. Every data product exists within a bounded context and 
1. one bounded context might contain several data products -- we need some name for the "bounded context" 

## Architecture / is sociotechnical in nature / technology, people, process, usage 

1. data architecture has a sociotechnical perspective. 
1. Technology. People. Processes. 
1. Consumer. Context. Usage e.g. accessible. Expectation e.g. Quality 
1. Thus, the sociotechnical perspective pushes us to adopt the product thinking philosophy for data - data products.

1. What is product thinking ???

## How does a data product look like? 

1. Any data representation that has value for its consumers can be a good candidate. 
1. Does it need a data quality definition, measure and certification? 
1. Does it need a metadata i.e. a data definition, critical information for effective usage 
1. Does it need to be available in a data marketplace where it can be looked up, accessed, and commented upon e.g. tickets, feedback etc. 
1. Examples
    1. A database table or view
    1. Raw unstructured files: e.g., images or videos uploaded by users of a video portal; however, to be valuable to consumers, they should be provided with metadata
    1. Data stream of data entities from a transaction system
    1. Data stream representing the history of changes to the application: For example, events that relate to changes made within a billing account
    1. Simple files: Data in CSV format, excel files
    1. Partitioned files in optimized (Parquet) format
    1. REST API: Read-optimized data exposed from applications
    1. Master Data Management database
    1. Features for the machine learning models
    1. Visualizations and dashboard
1. Cost 
1. Building and maintaining data products is a financial investment and 
    1. takes up domain team's, platform teams, governance teams capacity.  
    1. Therefore, the value and costs need to be evaluated upfront.
    1. To ensure best value for the investment, there should be a buyer for data product, and monetized. 

## Soda - has some nice dashboards for data quality 

## Prophet - has some inbuilt data trend analysis - with seasonal trend in row count? 


## Data Mesh Manager 

- https://app.datamesh-manager.com/kaunjovi/datacontracts/add
- https://demo.datamesh-manager.com/demo663615866159

#datamesh.



## Data Product / What do they do? 

1. Data products connect to sources, 
1. such as operational systems or 
1. other data products and 
1. perform data transformation. 

1. Data products serve data sets in one or many output ports. 
1. Output ports are typically structured data sets, 
1. as defined by a data contract. Some examples:


## [Data + AI summit 2022. Data Lakehouse and Data Mesh](https://www.youtube.com/watch?v=3znQs0MzZ-k)

1. Data Mesh using Databricks at Zalando (fashion house in europe)

## [Build Trust in Data through Automatable Data Contracts – Max Schultze, HelloFresh](https://www.youtube.com/watch?v=Wj2WHp3ZJUU)

1. Automatable data contracts. 
1. Data contracts - could be as simpled as both sides sitting down and documenting what they need and prepared to provide in data. 
1. [Soda](https://www.soda.io/) for data quality checks. 
1. Process of creating Data Contracts
    1. Data Owner creates and owns the data contract.
    1. Pre flight checks - before the data is published. 
        1. Format of the data. Schema is good. 
    1. Publish the data product 
        1. Continuous streaming. Batch - hourly, daily etc. 
    1. Post poblish - Data quality checks 
        1. Analyse the data. Check for null values. Distributions are totally off etc. 
        1. Owner needs to be alerted immediately 
        1. Also notify the data users. 
    1. All well? Then high quality data. 
1. Technology of Data contract automation 
    1. Data contract document goes to GitHub 
    1. Might be we want some sort of a workflow / UI to manage this process of working on creating a contract. 
    1. Once document pushed into Github automatically 
        1. Generate Airflow DAGs 
        1. Generate Prometheus alerts. 
        1. Executions of the SLOs (???) - time based, signal based. 
            1. Execute at a given time as the data is expected. 
            1. Once data is loaded send a signal on a channel and that triggers checks on the data. 
        1. Soda, Snowflake 
    1. The contract mentions the versions. 
        1. There is one source, and one ore more consumers. 
        1. There is one live version. Everyone is on it. 
        1. There might be more early access versions. 
        1. Finally the SLOs e.g. Row counts, Freshness check, etc. 
        1. The SLOs can execute SQLs to run checks, while taking parameters from the SLO yaml files. 
1. Impact of Data contract
    1. Users should not need deep technical knowledge 
    1. Data creators and consumers should be able to co-author the contracts. 
    1. The contracts should allow sharing of data as a product, with features like versions, backwards compatible etc. 
    1. Features like monitoring and alerting should be out of the box. 
    1. It should allow for reuse of code 
    1. It is a part of the data platform
    1. Must be visible in the catalog 
    1. Should allow of information user consumer lineage graph and webs

## How to use Soda for DQ? 

- Soda Checks Language (SodaCL)


## [The data guy](https://www.youtube.com/@thedataguygeorge)

## [Intro to Airflow! Beginner's Guide to Getting Started with Airflow](https://www.youtube.com/watch?v=ntpI4m-rQTg)

1. You can do by hand. Might be some day. Or use [AstroCLI](https://www.astronomer.io/docs/astro/cli/overview) 
1. The Astro CLI is the command line interface for data orchestration. 
1. It's the easiest way to get started with Apache Airflow and can be used with all Astronomer products.
1. Run Airflow on your local machine in minutes.
1. [Astrnomer / Astro](https://www.astronomer.io/docs/astro)
1. You also need Docker desktop. 


```
brew install astro 
```



