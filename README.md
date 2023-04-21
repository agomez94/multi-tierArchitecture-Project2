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

## **Remember:** 

Even though i have the CloudFormation templates in here to use doesn't mean you dont have to build anything else or configure them to your liking.
You still have to adjust the templates or EXPECT charges on your account.

**Deploy InfrastructureCF.yaml into cloudformation first by creating new stack (adjust parameters ACCORDINGLY)**

**Then**

##**Create an Amazon RDS**
1. First create a new DB subnet group
2. Create new Aurora database with MySQL
3. Properly set up Database 

**Note:** Take notes of the following:
-Master username/password
-Initial database name
-Writer endpoint

##**Create an Amazon EFS file system**
1. Create new EFS file system and properly set it up
2. Assign in APPSUBNET1 and APPSUBNET2

**Note:** Take note of the following:
-File system ID

##**Creating an Application Load Balancer and Target group
1. Create target group first
2. Properly configure to your liking
3. For Health check path enter **/wp-login.php**
4. **NO TARGETS TO REGISTER CURRENTLY**
5. Create ALB
6. Mapping will be in PublicSubnet 1 & 2
7. Listener HTTP:80 with target group created

**Note:** Take note of the following:
-Load balancer DNS name

##**Deploy WPInstanceCF.yaml into cloudformation by creating new stack (adjust parameters ACCORDINGLY)**
1. Configure the Parameters in stack details
- DB name: Initial database name
- Database endpoint: Writer endpoint
- Username/password
- Wordpress admin username: defaults to wpadmin (can change)
- Wordpress admin password: (Make one dont forget)
- Wordpress admin email address: (youremail@gmail.com)
- Instance Type: whatever you think is best
- ALBdnsNAME: Load balancer DNS name
- WPElasticFileSystemID: File System ID

**Note:** This stack can take up to 5 minutes to create and deploy the resources. PATIENCE!

##**Create the application servers by configuring an Auto Scaling Group and a Scaling policy**
1. Create Autoscalling group
- Choose launch template
- Choose Appsubnet1 and AppSubnet2
- Existing Load balancer and target groups
- Health checks ELB and Monitoring Within CloudWatch
2. Configure group size and scaling policies 
3. Notifications and tags (optional BUT recommended)
4. Create 

**Note:** This can take up to 5 minutes for health checks in target groups to show as healthy. PATIENCE!

##Once all is done:

Copy the load balancer's DNS name and paste into new tab, **appending the following:* /wp-login.php to the end of the DNS name before pressing enter.

The **WordPress** login page is displayed
-Use the appropiate login credintials and ##**ENJOY!!**
