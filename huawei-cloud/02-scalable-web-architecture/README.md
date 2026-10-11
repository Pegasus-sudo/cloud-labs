# Scalable Web Architecture on Huawei Cloud: LAMP, ELB and Auto Scaling

> A website hosted on Huawei Cloud with a separate database tier, a load balancer in front of the web servers, and auto scaling that adds or removes servers as traffic changes.

**Platform:** Huawei Cloud
**Source:** Huawei Cloud Solutions Architecture program [exact program name], Module 2
**Date completed:** [Month Year]
**Region:** [e.g., AP-Singapore]

## Scenario
A company wants to host its website on Huawei Cloud. The database and the web/application servers must run on separate instances, and the setup must handle traffic that goes up and down without anyone adding servers manually.

## Objective
- Deploy a LAMP stack with the database on its own server
- Distribute traffic across multiple web servers with a load balancer
- Scale web servers automatically with demand
- Monitor resource behavior under load

## Services used
- Elastic Cloud Server (ECS): web servers and database server
- Elastic Load Balance (ELB)
- Auto Scaling (AS)
- [Monitoring service, e.g., Cloud Eye: confirm]
- [VPC, subnets, security groups: confirm]

## Architecture
![Architecture diagram](architecture/diagram.png)

Users → ELB → web tier (Apache + PHP, ECS instances in an Auto Scaling group) → database tier (MySQL on a separate ECS).

[One or two lines: VPC/subnet layout and how the web tier reaches the database.]

## What I built
1. **LAMP stack (Linux, Apache, MySQL, PHP):** the database runs on its own ECS, separate from the web server.
2. **Elastic Load Balancer:** placed in front so incoming traffic is spread across multiple web servers instead of one.
3. **Auto Scaling:** ECS instances are added when traffic increases and removed when it drops, so there is no paying for idle capacity.
   - Scaling policy: [metric, e.g., CPU utilization] [scale-out threshold] / [scale-in threshold]
   - Instance range: min [X], max [Y]
4. **Monitoring:** watched how the resources behaved under load using [tool].

## Verification
Visited the website through the load balancer to confirm it was served correctly end to end.
[Optional: how you tested scaling, e.g., generated load and observed new instances being added.]

![Site served through ELB](screenshots/site-via-elb.png)
![Auto scaling group](screenshots/auto-scaling.png)
![Monitoring](screenshots/monitoring.png)

## Key learnings
- Separating the database from the web tier is what makes independent scaling possible. Web servers cannot scale on their own if the database sits on the same machine.
- A load balancer and auto scaling work together: one distributes traffic, the other adjusts capacity.
- Scaling in as well as out controls cost.

## Cost and cleanup
Resources released after the lab: [yes / no].

## Possible improvements
- Use a managed database service with replication for high availability
- Add health checks and alarms to the scaling policy
- Add HTTPS on the load balancer
