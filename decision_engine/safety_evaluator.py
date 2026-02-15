# decision_engine/safety_evaluator.py

from policy_rules import FORBIDDEN_ACTIONS, SAFE_ACTIONS


def evaluate_actions(incident_context, ai_output):

    approved_actions = []
    pending_approval = []
    policy_passed = []
    policy_failed = []

    metadata = incident_context.get("deployment_metadata", {})

    min_size = metadata.get("min_size", 1)
    max_size = metadata.get("max_size", 5)
    current_capacity = metadata.get("desired_capacity", 1)

    for action in ai_output.get("suggested_actions", []):

        action_type = action.get("action_type")

        # Rule 1: Block forbidden actions
        if action_type in FORBIDDEN_ACTIONS:
            policy_failed.append(f"{action_type} is forbidden")
            continue

        # Rule 2: Only allow known safe actions
        if action_type not in SAFE_ACTIONS:
            policy_failed.append(f"{action_type} is not whitelisted")
            continue

        # Rule 3: Validate ASG scaling bounds
        if action_type == "scale_asg":
            new_capacity = action["parameters"].get("new_desired_capacity")

            if new_capacity < min_size or new_capacity > max_size:
                policy_failed.append(
                    f"Scaling outside allowed bounds ({min_size}-{max_size})"
                )
                pending_approval.append({
                    "action": action,
                    "status": "NEEDS_APPROVAL"
                })
                continue

            policy_passed.append("Scaling within ASG limits")

        # Rule 4: Restart EC2 requires approval
        if action_type == "restart_ec2":
            pending_approval.append({
                "action": action,
                "status": "NEEDS_APPROVAL"
            })
            policy_passed.append("Restart requires human approval")
            continue

        # If all checks passed → SAFE
        approved_actions.append({
            "action": action,
            "status": "SAFE"
        })

    return {
        "incident_id": incident_context.get("incident_id"),
        "approved_actions": approved_actions,
        "pending_approval": pending_approval,
        "audit_log": {
            "policy_checks_passed": policy_passed,
            "policy_checks_failed": policy_failed
        }
    }
