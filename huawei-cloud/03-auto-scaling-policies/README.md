# Auto Scaling on Huawei Cloud: Configurations, Scaling Policies and Stability Test

> Hands-on lab on Huawei Cloud Auto Scaling (AS): creating an AS configuration and group, configuring alarm-based, scheduled/periodic and bandwidth scaling policies, and testing stability behind a load balancer.

**Platform:** Huawei Cloud
**Source:** Huawei Cloud HCCDP-Solution Architectures program
**Date completed:** [Month Year]
**Region:** [e.g., AP-Singapore]

## Objective
- Understand the basic process of using Auto Scaling
- Configure different types of scaling policies
- Verify that an AS group behaves correctly behind a load balancer

## Services used
- Auto Scaling (AS): configuration, group, scaling policies
- Elastic Cloud Server (ECS): instances launched by the AS group
- Elastic Load Balance (ELB)
- [Cloud Eye (alarms), if used: confirm]
- [Bandwidth service, if used: confirm]

## Architecture
![Architecture diagram](architecture/diagram.png)

[One or two lines: how the AS group, ECS instances and load balancer connect.]

## What I did

### 1. Basic process of using AS
- Created an **AS configuration** (the template for new instances): [image, flavor/instance type, disk, security group]
- Created an **AS group** with min [X] / max [Y] instances in [VPC/subnet]

### 2. Scaling policies
- **Alarm-based policy:** scales based on [metric, e.g., CPU usage] with a threshold of [value] for [duration]. Action: [add / remove N instances]
- **Scheduled or periodic policy:** triggers [once at a set time / on a recurring schedule, e.g., daily at HH:MM]. Action: [change capacity]
- **Periodic bandwidth scaling policy:** adjusts [bandwidth] on a schedule [details]

### 3. Stability test
- Created a **load balancer** and associated it with the AS group
- Checked AS stability: [what you observed, e.g., new instances registered automatically with the load balancer and traffic was served without interruption]

## Verification
![AS group](screenshots/as-group.png)
![Scaling policies](screenshots/scaling-policies.png)
![Load balancer association](screenshots/elb-association.png)

## Key learnings
- An AS configuration is a reusable template; the AS group controls how many instances run.
- Different policy types fit different patterns: alarm-based for unpredictable load, scheduled/periodic for predictable load.
- Associating a load balancer with the AS group lets new instances receive traffic automatically.
- This builds on my [scalable web architecture lab](../02-scalable-web-architecture/) with a deeper look at scaling policies.

## Cost and cleanup
Resources released after the lab: [yes / no].

## Possible improvements
- Combine alarm-based and scheduled policies for peak hours
- Tune cooldown periods to avoid rapid scaling in and out
- Add health checks and notifications
