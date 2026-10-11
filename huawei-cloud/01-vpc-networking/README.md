# Huawei Cloud VPC Networking: Subnets, Security, VPC Peering and NAT Gateway

> Hands-on lab covering VPC creation, traffic security with security groups and network ACLs, and connectivity with VPC peering and a NAT gateway.

**Platform:** Huawei Cloud
**Source:** Huawei Cloud Solutions Architecture program [exact program name]
**Date completed:** [Month Year]
**Region:** [e.g., CN-Hong Kong / AP-Singapore]

## Objective
- Create VPCs and subnets
- Configure security groups and network ACLs to improve the security of resources in a VPC
- Configure VPC peering connections and a NAT gateway

## Services used
- Virtual Private Cloud (VPC) and subnets
- Security Groups
- Network ACLs
- VPC Peering
- NAT Gateway
- [Elastic Cloud Server (ECS), if used for testing]

## Lab sections

### 1. Basic configuration
Created VPC(s) and subnet(s):
- VPC A: 
- VPC B: 

### 2. Security configuration
- Configured **security group** rules: [e.g., allowed SSH/ICMP from specific sources]
- Configured **network ACL** rules at the subnet level: [rules you set]
- Verified the effect of the rules: [what you tested]

### 3. Connectivity configuration
- Created a **VPC peering connection** between [VPC A] and [VPC B] and added routes on both sides
- Configured a **NAT gateway** so resources in [subnet] could [reach the internet / outbound access]
- Verified connectivity: [e.g., ping between instances in peered VPCs]

## Verification
![Peering connection](screenshots/vpc-peering.png)
![Security group and ACL rules](screenshots/security-rules.png)

## Key learnings
- Security groups protect instances, while network ACLs protect subnets, giving layered defense.
- VPC peering requires non-overlapping CIDR blocks and routes on both sides.
- A NAT gateway lets private resources reach external networks without exposing them directly.
- These concepts map to my on-premises experience with VLANs, segmentation, and IP addressing, and mirror my [AWS VPC lab](../../aws/02-vpc-ec2-security/) on a different platform.

## Cost and cleanup
Resources released after the lab: [yes / no].
