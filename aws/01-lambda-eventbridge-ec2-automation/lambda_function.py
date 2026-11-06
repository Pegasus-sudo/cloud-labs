import logging
import os

import boto3
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS Lambda sets AWS_REGION automatically.
ec2 = boto3.client("ec2", region_name=os.environ.get("AWS_REGION"))


def _configured_instance_id():
    """Read and validate the target EC2 instance ID."""
    instance_id = os.environ.get("EC2_INSTANCE_ID", "").strip()

    if not instance_id:
        raise ValueError("Set EC2_INSTANCE_ID to the target EC2 instance ID.")

    if not instance_id.startswith("i-") or len(instance_id) < 10:
        raise ValueError("EC2_INSTANCE_ID does not look like a valid instance ID.")

    return instance_id


def lambda_handler(event, context):
    """Stop the configured EC2 instance only when it is running."""
    instance_id = _configured_instance_id()

    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instances = [
            instance
            for reservation in response.get("Reservations", [])
            for instance in reservation.get("Instances", [])
        ]

        if not instances:
            raise RuntimeError(f"EC2 instance was not returned by DescribeInstances: {instance_id}")

        state = instances[0].get("State", {}).get("Name", "unknown")

        if state != "running":
            logger.info("No stop action required for %s; current state is %s.", instance_id, state)
            return {"instance_id": instance_id, "action": "skipped", "state": state}

        stop_response = ec2.stop_instances(InstanceIds=[instance_id])
        logger.info("Stop requested for EC2 instance %s.", instance_id)

        return {
            "instance_id": instance_id,
            "action": "stop_requested",
            "stop_response": stop_response.get("StoppingInstances", []),
        }

    except (BotoCoreError, ClientError):
        logger.exception("Failed to inspect or stop EC2 instance %s.", instance_id)
        raise
