# collector_lambda/collector.py

import boto3
import datetime
import uuid

cloudwatch = boto3.client("cloudwatch")
logs_client = boto3.client("logs")
ec2 = boto3.client("ec2")


def build_incident_context(event):

    incident_id = f"inc-{datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')}-{str(uuid.uuid4())[:6]}"
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"

    alarm_name = event.get("detail", {}).get("alarmName", "UnknownAlarm")

    # For simplicity, assume EC2 instance is tagged with alarm
    resource_id = extract_resource_id(event)

    metrics = fetch_metrics(resource_id)
    recent_logs = fetch_recent_logs(resource_id)
    deployment_metadata = mock_deployment_metadata()

    return {
        "incident_id": incident_id,
        "timestamp": timestamp,
        "alarm_name": alarm_name,
        "resource_id": resource_id,
        "metrics": metrics,
        "recent_logs": recent_logs,
        "deployment_metadata": deployment_metadata
    }
