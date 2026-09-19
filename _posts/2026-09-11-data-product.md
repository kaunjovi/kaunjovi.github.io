
# Data Product 

In Zhamak’s framing, a data product is an independently deployable, high-cohesion component that bundles the data and metadata, the code for ingesting, processing, serving, and governing it, and the infrastructure to run all of that.

Chad Sanderson
It is the sum of data components that are organized to serve a business need.
Thus, for example, a dashboard is a data product.


When a source system changes upstream, that team finds out the same way everyone else does: some downstream use cases break.
push ownership out to the people closest to the domain (who actually understand the data).
If the domain team is responsible for a (data) product, something with an owner, an interface, a defined shape, instead of just a dump of tables somewhere in the warehouse, then “who broke this and why it breaks” stops being a mystery. 

“the data contract should be built in service of these products, not the other way around.” The contract must be there to guardrail the data product.

His actual diagnosis isn’t “why do we need data products”; it’s “why do the data products keep breaking?”

catalogs and monitoring only see the damage after it’s done

## Open Data Product Standard

1. [Open Data Product Standard home page](https://bitol-io.github.io/open-data-product-standard/v1.1.0/)


## Entropy 

1. [Welcome to Demo Data Marketplace](https://demo.entropy-data.com/demo353279284398/marketplace)


2. [The Consumer-Defined Data Contract](https://dataproducts.substack.com/p/the-consumer-defined-data-contract)
3. Chad Sanderson
4. I’ve been hard at work building Gable these last few months
5. modern federated implementation leveraging schema registries and CI/CD checks has much less organizational overhead than hand-written data-SLA documents
6. Producer-defined data contracts do not work
7. The producer acts as a data vendor maintaining the spec and ensuring their data is discoverable through a marketplace or catalog
8. contract should be enforced as close to the production code as possible through integration tests, code review, and monitoring
9. If data producers don’t understand how downstream teams are using their data or the expectations they have of it, how can they vend data that consumers want/need?
10. In the same way, the initial data requirements (contract) must be defined by the team with the use cases: consumers


1. [An Engineer's Guide to Data Contracts - Pt. 1](https://dataproducts.substack.com/p/an-engineers-guide-to-data-contracts)
2. **Contracts, Services, and Change Data Capture (CDC)**

> A Verbal Contract Isn't Worth the Paper It's Written On

1. Data contracts are public. The implementation needs to support evolving contracts over time without breaking downstream consumers, which necessitates versioning and strong change management.
2. Data contracts cover semantics. In API design, altering the APIs behavior is considered a breaking change even if the API signature remains the same. Similarly, changing the underlying meaning of the data being produced should break the data contract. As an example - if you have an entity with length and width as numeric fields, switching the values from being stored in inches to centimeters is a breaking change. In practice, this means contracts must contain additional metadata beyond the schema, including descriptions, value constraints, and so on.



## Open Data Contract Standard (ODCS)


```yaml
# ODPS high-level information.
# Source: https://bitol-io.github.io/open-data-product-standard/v1.0.0/#table-of-content
apiVersion: v1.0.0
kind: DataProduct
name: Customer Data Product
id: fbe8d147-28db-4f1d-bedf-a3fe9f458427
domain: seller
status: draft
tenant: RetailCorp
description:
  purpose: Enterprise view of a customer.
  limitations: No known limitations.
  usage: Check the various artefacts for their own description.
tags: ['customer']
```