# REPLACE THIS FILE WITH YOUR OWN LAMBDA CODE FROM THE LAB.
# The sample below shows the general shape of a "stop EC2 instance" function.

import boto3

REGION = "us-east-1"                 # replace with your region
INSTANCE_IDS = ["i-xxxxxxxxxxxxxxxxx"]  # replace with your instance ID (remove before publishing if you prefer)

ec2 = boto3.client("ec2", region_name=REGION)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=INSTANCE_IDS)
    return {"stopped": INSTANCE_IDS}
