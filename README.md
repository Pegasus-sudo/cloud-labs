# Cloud Infrastructure Labs

A technical portfolio of hands-on cloud and container-infrastructure projects across **AWS**, **Huawei Cloud**, and **Docker**, with an emphasis on infrastructure design, cloud networking, application deployment, operations, observability, and security fundamentals.

The repository documents practical work completed through guided training and local lab environments. Each entry explains the architecture, configuration activities, verification approach, and lessons learned—not just a list of services.

## Portfolio at a glance

| Platform | Focus areas |
|---|---|
| AWS | VPC networking, EC2 operations, IAM, serverless automation, managed application deployment |
| Huawei Cloud | VPC networking, load balancing, auto scaling, storage, managed databases, monitoring, and log management |
| Containers | Docker, Docker Compose, microservices, Nginx API Gateway, service discovery, and API rate limiting |

## AWS labs

| # | Lab | Services and concepts | Documentation |
|---|---|---|---|
| 01 | Serverless EC2 lifecycle automation | Lambda, EventBridge, IAM, EC2 | [Open lab](aws/01-lambda-eventbridge-ec2-automation/) |
| 02 | VPC and EC2 security fundamentals | VPC, subnets, security groups, EC2 protections | [Open lab](aws/02-vpc-ec2-security/) |
| 03 | Managed application deployment | Elastic Beanstalk, EC2, Auto Scaling, Elastic Load Balancing | [Open lab](aws/03-elastic-beanstalk-deployment/) |
| 04 | Identity and access management | IAM users, groups, and policies | [Open lab](aws/04-iam-users-groups-policies/) |

## Huawei Cloud labs

| # | Lab | Services and concepts | Documentation |
|---|---|---|---|
| 01 | VPC networking and connectivity | VPC, subnets, security groups, network ACLs, VPC peering, NAT Gateway | [Open lab](huawei-cloud/01-vpc-networking/) |
| 02 | Scalable web architecture | ECS, LAMP, ELB, Auto Scaling | [Open lab](huawei-cloud/02-scalable-web-architecture/) |
| 03 | Auto Scaling policies | AS configuration and groups, alarm-based and scheduled policies, ELB | [Open lab](huawei-cloud/03-auto-scaling-policies/) |
| 04 | Cloud storage services | EVS, OBS, SFS Turbo, ECS | [Open lab](huawei-cloud/04-storage-services/) |
| 05 | RDS for MySQL management and connectivity | RDS for MySQL, automated backups, database ports, DAS, private and public connectivity | [Open lab](huawei-cloud/05-rds-mysql-management-connectivity/) |
| 06 | O&M monitoring and log management | Cloud Eye, LTS, ICAgent, SMN, resource monitoring, host-log ingestion, alarm notifications | [Open project](huawei-cloud/06-om-monitoring-and-log-management/) |

## Container and DevOps labs

| # | Lab | Tools and concepts | Documentation |
|---|---|---|---|
| 01 | Dockerized microservices with Nginx API Gateway | Docker, Docker Compose, Flask, Node.js, Nginx, bridge networking, service discovery, rate limiting | [Open lab](containers/01-docker-microservices-api-gateway/) |

## How the labs are documented

Where the available evidence supports it, project documentation covers:

- **Objective and scope** — the task being performed and the skills practiced.
- **Architecture** — the cloud or container components and how traffic or data moves between them.
- **Implementation** — important configuration steps and decisions.
- **Verification** — how the result was checked.
- **Security and operations** — access control, exposure, availability, backup, monitoring, and cleanup considerations.
- **Evidence** — console screenshots or sanitized command output, where available.

Some exercises were completed in guided training environments, including AWS Academy and Huawei Cloud training. They are identified as learning projects and should not be interpreted as production deployments.

## Repository structure

~~~text
cloud-labs/
├── README.md
├── docs/
│   └── LAB_TEMPLATE.md
├── aws/
│   ├── 01-lambda-eventbridge-ec2-automation/
│   ├── 02-vpc-ec2-security/
│   ├── 03-elastic-beanstalk-deployment/
│   └── 04-iam-users-groups-policies/
├── huawei-cloud/
│   ├── README.md
│   ├── 01-vpc-networking/
│   ├── 02-scalable-web-architecture/
│   ├── 03-auto-scaling-policies/
│   ├── 04-storage-services/
│   ├── 05-rds-mysql-management-connectivity/
│   └── 06-om-monitoring-and-log-management/
└── containers/
    └── 01-docker-microservices-api-gateway/
        ├── README.md
        ├── docker-compose.yml
        ├── gateway/
        ├── user-service/
        ├── order-service/
        ├── product-service/
        └── Screenshots/
~~~

## About

I'm a final-year BS Cyber Security student at **The Islamia University of Bahawalpur (IUB)**, developing practical skills in cloud infrastructure, networking, operations, and security.

My background includes a completed networking internship with the IUB Directorate of IT and current Huawei Cloud Solution Architecture training.

- **LinkedIn:** [Chaudhary M Hussnain](https://www.linkedin.com/in/chaudhary-m-hussnain-bbb7a7269/)
- **GitHub:** [Pegasus-sudo](https://github.com/Pegasus-sudo)

## Responsible lab practices

- No cloud credentials, private keys, access tokens, or account secrets belong in this repository.
- Credentials, active session tokens, and reusable authentication URLs must never be published. Review sandbox account/resource identifiers and temporary public IP addresses in context rather than automatically treating them as credentials.
- Cloud resources should be reviewed and released after exercises to avoid unintended charges.
- Local development services should not be exposed directly to the public internet without appropriate authentication, TLS, network restrictions, and monitoring.
- Service behavior and available features may vary by region, account permissions, and training environment.

---

*Learn. Build. Document. Improve.*
