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

Everett Enterprises is a startup that provides online practice exams for individuals preparing for the AWS Solutions Architect Associate (SAA) and AWS Certified Cloud Practitioner (CCP) exams. They currently host their website and exam questions in an on-premises data center but have decided to move to the cloud due to the financial and performance improvements. It is critical that the website and exam questions are available to users without any interruption, and the company needs a fast, scalable, reliable, and cost-effective solution for their business requirements.
We have been hired to assist the company with the transition. Your task is to design a cloud-based infrastructure that can meet the needs of the business, including hosting the website, storing exam questions and data, and ensuring high availability and scalability of the system.
![image](https://user-images.githubusercontent.com/130075700/236952779-8a97b2e4-f9cf-46bd-abfa-31e964421c4e.png)


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
