# Serverless EC2 Automation with AWS Lambda and EventBridge

> A scheduled, event-driven workflow that stops a running EC2 instance using Lambda, triggered by EventBridge, with a least-privilege IAM role.

**Platform:** AWS
**Source:** [course name / self-guided]
**Date completed:** [Month Year]
**Region:** [e.g., us-east-1]

## Objective
Automate EC2 lifecycle management without managing any server. This pattern is commonly used to stop idle instances and reduce cost.

## Services used
- AWS Lambda
- Amazon EventBridge (scheduled rule)
- AWS IAM (execution role)
- Amazon EC2
- Amazon CloudWatch Logs (if used for monitoring, confirm)

## Architecture
![Architecture diagram](architecture/diagram.png)

EventBridge rule (every minute) → Lambda function → EC2 `StopInstances` API. The Lambda function assumes an IAM role that only allows the actions it needs.

## Steps
1. Launched an EC2 instance and noted its instance ID.
2. Created an IAM role for Lambda with permissions limited to describing and stopping instances (see [`iam-policy.json`](iam-policy.json)).
3. Created the Lambda function [runtime, e.g., Python 3.x] and attached the role (see [`lambda_function.py`](lambda_function.py)).
4. Created an EventBridge rule with a schedule of every 1 minute and set the Lambda function as the target.
5. Waited for the rule to fire and watched the instance state change from `running` to `stopped`.

## Verification
- Instance state changed to `stopped` after the rule triggered.
- Function invocations visible in [CloudWatch Logs / Lambda monitoring tab].

![Instance stopped](screenshots/instance-stopped.png)
![EventBridge rule](screenshots/eventbridge-rule.png)

## Key learnings
- How event-driven and serverless architecture works in practice.
- Why least-privilege IAM matters: the function can only do what the policy allows.
- How scheduled automation can reduce cost and manage resources.

## Cost and cleanup
Deleted the EventBridge rule, Lambda function, IAM role, and EC2 instance after the lab. A one-minute schedule triggers many invocations, so the rule should not be left enabled.

## Possible improvements
- Use tags to select instances instead of a hard-coded ID.
- Change the schedule to a realistic one (for example, stop at night, start in the morning).
- Add an SNS notification when an instance is stopped.
