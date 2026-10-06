# AWS IAM: Users, Groups and Policies

> Hands-on IAM lab from AWS Academy Cloud Foundations covering permissions through groups and policies.

**Platform:** AWS
**Source:** AWS Academy Cloud Foundations (guided lab)
**Date completed:** [Month Year]

## Objective
Understand how IAM controls access to AWS services using users, groups, and policies.

## Services used
- AWS Identity and Access Management (IAM)

## Steps
1. Explored pre-created IAM users and groups.
2. Inspected the IAM policies attached to each group.
3. Worked through a scenario: assigned users to groups so they received the right permissions.
4. Located and used the IAM sign-in URL.
5. Tested how different policies change access to AWS services.

## Verification
- Users could or could not access services depending on their group's policy.

![IAM groups](screenshots/iam-groups.png)

## Key learnings
- Permissions are best managed through groups, not individual users.
- Policies define exactly what is allowed or denied.
- Least privilege reduces risk.

## Possible improvements
- Add MFA and a password policy.
- Practice writing a custom policy from scratch.
