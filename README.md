# Building an AWS Multi-Tier Architecture for WordPress Project
Deploying a highly available multi-tier architecture using CloudFormation templates, using amazon RDS w/ Aurora.

## Objective:

- Deploy a virtual network spread across multiple Availability Zones in a Region using a CloudFormation template.

- Deploy a highly available and fully managed relational database across those Available Zones (AZ) using Amazon 

- Use Amazon Elastic File System (Amazon EFS) to provision a shared storage layer across multiple Availability Zones for the application tier, powered by Network File System (NFS).

- Create a group of web servers that will automatically scale in response to load variations to complete the application tier.

## Scenario:

    Company creates marketing campaigns for small-sized to medium-sized businesses. They recently hired you to work with the engineering teams to build out a proof of concept for their business. To date, they have hosted their client-facing application in an on-premises data center, but they recently decided to move their operations to the cloud in an effort to save money and transform their business with a cloud-first approach. Some members of their team have cloud experience and recommended the AWS Cloud services to build their solution.

    In addition, they decided to redesign their web portal. Customers use the portal to access their accounts, create marketing plans, and run data analysis on their marketing campaigns. They would like to have a working prototype in two weeks. You must design an architecture to support this application. Your solution must be fast, durable, scalable, and more cost-effective than their existing on-premises infrastructure.