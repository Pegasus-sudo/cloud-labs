# Cloud Labs

Hands-on cloud computing labs, documented step by step. Built on a networking and security foundation.

**About me:** Final-year BS Cyber Security student at the Islamia University of Bahawalpur (IUB), Network Intern at IUB's data center, CEH and ISC2 CC holder. I am moving into cloud engineering, with a focus on cloud networking and security.

- LinkedIn: [Chaudhary M Hussnain](https://www.linkedin.com/in/chaudhary-mhussnain-bbb7a7269)
- Email: mhassnain378@gmail.com

## Labs

### AWS

| # | Lab | Services | Focus |
|---|-----|----------|-------|
| 01 | [Serverless EC2 Automation](aws/01-lambda-eventbridge-ec2-automation/) | Lambda, EventBridge, IAM, EC2 | Event-driven automation, least privilege |
| 02 | [Secure Network Design: VPC + EC2](aws/02-vpc-ec2-security/) | VPC, Subnets, Security Groups, EC2 | Network isolation, instance protection |
| 03 | [Application Deployment with Elastic Beanstalk](aws/03-elastic-beanstalk-deployment/) | Elastic Beanstalk, EC2, ALB, Auto Scaling | Managed deployment, scaling |
| 04 | [IAM: Users, Groups and Policies](aws/04-iam-users-groups-policies/) | IAM | Access control (AWS Academy Cloud Foundations) |

### Huawei Cloud

In progress. See [huawei-cloud/](huawei-cloud/).

## Repository structure

```
cloud-labs/
├── README.md
├── docs/
│   └── LAB_TEMPLATE.md
├── aws/
│   ├── 01-lambda-eventbridge-ec2-automation/
│   ├── 02-vpc-ec2-security/
│   ├── 03-elastic-beanstalk-deployment/
│   └── 04-iam-users-groups-policies/
└── huawei-cloud/
```

Each lab folder contains a README (objective, architecture, steps, results, key learnings), an `architecture/` folder for diagrams, and a `screenshots/` folder.

## Notes

- Some labs were completed in guided environments (for example AWS Academy). Each lab README states its source.
- No credentials, keys, or account IDs are stored in this repository.

## Skills demonstrated

AWS (EC2, VPC, IAM, Lambda, EventBridge, Elastic Beanstalk, Auto Scaling, Elastic Load Balancing) · Cloud security fundamentals · Network segmentation · Linux · TCP/IP
