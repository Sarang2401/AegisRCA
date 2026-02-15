# remediation_lambda/executor.py

import boto3
from idempotency import is_already_executed, mark_executed

autoscaling = boto3.client("autoscaling")
ssm = boto3.client("ssm")


def execute_actions(decision_output):

    incident_id = decision_output.get("incident_id")
    approved_actions = decision_output.get("approved_actions", [])

    execution_results = []

    for item in approved_actions:

        action = item.get("action")
        action_type = action.get("action_type")

        if is_already_executed(incident_id, action_type):
            execution_results.append({
                "action_type": action_type,
                "status": "SKIPPED_ALREADY_EXECUTED"
            })
            continue

        if action_type == "scale_asg":
            result = scale_asg(action)

        elif action_type == "restart_ec2":
            result = restart_ec2(action)

        else:
            result = {
                "action_type": action_type,
                "status": "UNKNOWN_ACTION"
            }

        if result["status"] == "SUCCESS":
            mark_executed(incident_id, action_type)

        execution_results.append(result)

    return {
        "incident_id": incident_id,
        "execution_results": execution_results
    }
