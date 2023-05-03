# Building an AWS Multi-Tier Architecture W/ Flask webpage

## Built by: 

- Angel Gomez JR
- Aaron Parangan
- Andrew Friend

## Infrastructure by Code Using CloudFormation

Deploying a highly available multi-tier architecture using CloudFormation templates, using amazon RDS w/ Aurora(mySQL).

## Objective:

- Deploy a virtual network spread across multiple Availability Zones in a Region using a CloudFormation template.

- Deploy a highly available and fully managed relational database across those Available Zones (AZ) using Amazon CloudFormation. 

- Use Amazon S3 to provision a shared storage layer across multiple Availability Zones for the application tier.

- Create a group of web servers that will automatically scale in response to load variations to complete the application tier.

- Create a webportal that consists of a login/sign-up page, and the main page that will have the option to take a CCP exam or SAA exam to practice.
    *The questions will be pulled from the aurora database with the help of an API Gateway and Lambda functions.
    
- 

## Scenario:

Company wants to create a webportal that has questions for their users to practice for the CCP exam or SAA exam. They recently hired your team (StormTroopers) to work with the engineering teams to build out a proof of concept for their business. To date, they have hosted their client-facing application in an on-premises data center, but they recently decided to move their operations to the cloud in an effort to save money and transform their business with a cloud-first approach. Some members of their team have cloud experience and recommended the AWS Cloud services to build their solution.

In addition, they decided to redesign their web portal. Customers use the portal to access their account or if no account exists for the user, the sign-up feature helps them establish their presence on the webportal to gain access to the main website. They would like to have a working prototype in two weeks. You must design an architecture to support this application. Your solution must be fast, durable, scalable, and more cost-effective than their existing on-premises infrastructure.

## **Remember:** 

**Deploy InfrastructureCF.yaml into cloudformation first by creating new stack (adjust parameters ACCORDINGLY)**

**Note:** Take note of the following:

-Load balancer DNS name

-Incorporate Route 53 if possible.

##**Deploy STInstanceCF.yaml into cloudformation by creating new stack (adjust parameters ACCORDINGLY)**
1. Configure the Parameters in stack details

**Note:** This stack can take up to 5 minutes to create and deploy the resources. PATIENCE!

**Note:** This can take up to 5 minutes for health checks in target groups to show as healthy. PATIENCE!

##**ENJOY!!**
