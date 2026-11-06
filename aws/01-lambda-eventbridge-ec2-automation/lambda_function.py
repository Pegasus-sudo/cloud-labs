import logging
import os

import boto3
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS Lambda sets AWS_REGION automatically.
ec2 = boto3.client("ec2", region_name=os.environ.get("AWS_REGION"))


def _configured_instance_ids():
    """Read and validate the comma-separated EC2_INSTANCE_IDS setting."""
    raw_value = os.environ.get("EC2_INSTANCE_IDS", "")
    instance_ids = [value.strip() for value in raw_value.split(",") if value.strip()]

    if not instance_ids:
        raise ValueError(
            "Set EC2_INSTANCE_IDS to one or more comma-separated EC2 instance IDs."
        )

    invalid_ids = [
        instance_id
        for instance_id in instance_ids
        if not instance_id.startswith("i-") or len(instance_id) < 10
    ]
    if invalid_ids:
        raise ValueError(f"Invalid EC2 instance ID format: {invalid_ids}")

    return instance_ids


def lambda_handler(event, context):
    """Stop configured EC2 instances that are currently running."""
    instance_ids = _configured_instance_ids()

    try:
        response = ec2.describe_instances(InstanceIds=instance_ids)

        running_ids = []
        skipped = []

        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instance_id = instance["InstanceId"]
                state = instance.get("State", {}).get("Name", "unknown")

                if state == "running":
                    running_ids.append(instance_id)
                else:
                    skipped.append({"instance_id": instance_id, "state": state})

        if running_ids:
            stop_response = ec2.stop_instances(InstanceIds=running_ids)
            logger.info("Stop requested for instances: %s", running_ids)
        else:
            stop_response = {"StoppingInstances": []}
            logger.info("No configured instances are currently running.")

        return {
            "stopped_or_stopping": running_ids,
            "skipped": skipped,
            "stop_response": stop_response.get("StoppingInstances", []),
        }

    except (BotoCoreError, ClientError):
        logger.exception("Failed to inspect or stop the configured EC2 instances.")
        raise
