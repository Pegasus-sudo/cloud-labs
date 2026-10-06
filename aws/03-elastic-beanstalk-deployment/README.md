# Application Deployment with AWS Elastic Beanstalk

> Deployed application code to Elastic Beanstalk and analyzed the infrastructure it provisions and manages.

**Platform:** AWS
**Source:** [AWS Academy / course name]
**Date completed:** [Month Year]
**Region:** [e.g., us-east-1]

## Objective
Understand how a managed platform handles deployment, scaling, and monitoring, and what it creates behind the scenes.

## Services used
- AWS Elastic Beanstalk
- Amazon EC2
- Auto Scaling
- Elastic Load Balancing
- Security Groups

## Architecture
![Architecture diagram](architecture/diagram.png)

Elastic Beanstalk environment → Load Balancer → Auto Scaling group → EC2 instances, protected by security groups.

## Steps
1. Created an Elastic Beanstalk application and environment [platform, e.g., Python / Node.js / PHP].
2. Deployed the application code [sample app / own code].
3. Opened the EC2, Auto Scaling, Load Balancer, and Security Group consoles to inspect the resources Beanstalk created.
4. Monitored environment health and application behavior using [Beanstalk health dashboard / CloudWatch].

## Verification
- Application reachable at the environment URL.
- Environment health shown as [Ok / Green].

![Environment health](screenshots/environment-health.png)
![Created resources](screenshots/created-resources.png)

## Key learnings
- How Beanstalk simplifies deployment, scaling, and monitoring.
- What the platform abstracts (EC2, ASG, load balancer, security groups) and where to find each.
- Trade-off between convenience and control in managed services.

## Cost and cleanup
Terminated the environment after the lab so the instances and load balancer stop billing.

## Possible improvements
- Compare with a manual EC2 + ALB + Auto Scaling build.
- Add a custom domain and HTTPS.
