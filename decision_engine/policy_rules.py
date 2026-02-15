# decision_engine/policy_rules.py

FORBIDDEN_ACTIONS = [
    "delete_ec2",
    "delete_asg",
    "terminate_instance"
]

SAFE_ACTIONS = [
    "scale_asg",
    "restart_ec2"
]
