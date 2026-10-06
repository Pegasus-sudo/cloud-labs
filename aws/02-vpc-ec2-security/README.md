# Secure Network Design on AWS: VPC, Subnets, Security Groups and EC2

> An isolated VPC with controlled traffic, plus an EC2 web server configured with security and operational protections.

**Platform:** AWS
**Source:** [AWS Academy / course name]
**Date completed:** [Month Year]
**Region:** [e.g., us-east-1]

## Objective
Apply cloud security fundamentals: reduce attack surface through network isolation, control traffic with security groups, and protect and monitor an EC2 instance.

## Services used
- Amazon VPC (subnets)
- Security Groups
- Amazon EC2
- Amazon CloudWatch (instance monitoring, confirm tool used)

## Architecture
![Architecture diagram](architecture/diagram.png)

VPC [CIDR, e.g., 10.0.0.0/16] with [number] subnets. The EC2 instance sits inside the controlled boundary and only accepts the traffic allowed by its security group.

## Part A: Secure VPC environment
1. Created isolated subnets to reduce attack surface [subnet names and CIDRs].
2. Applied security group rules to control traffic flow and block unauthorized access.
3. Launched an EC2 instance inside the VPC and validated connectivity within the boundary.

## Part B: EC2 web server operations and protection
1. Launched an EC2 instance with **termination protection** to prevent accidental deletion.
2. Configured a security group rule to allow **HTTP (port 80)** securely.
3. Monitored instance performance and health.
4. Resized the instance (changed instance type) to support scalability, then enabled **stop protection**.
5. Reviewed EC2 service limits and validated the protections with controlled stop tests.

## Verification
- Web server reachable over HTTP only through the allowed rule.
- Stop/terminate attempts blocked while protection was enabled.

![Security group rules](screenshots/security-group.png)
![Termination protection](screenshots/termination-protection.png)

## Key learnings
- How subnet isolation and security groups limit exposure.
- Operational safeguards (termination and stop protection) that prevent accidental outages.
- How VLAN and segmentation concepts from on-premises networks map to VPC design.

## Cost and cleanup
Resources deleted after the lab: [yes / no].

## Possible improvements
- Add public and private subnets with an Internet Gateway and NAT Gateway.
- Add network ACLs as a second layer.
- Put the instance behind a load balancer.
