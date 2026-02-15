# remediation_lambda/idempotency.py

executed_actions = set()

def is_already_executed(incident_id, action_type):
    key = f"{incident_id}:{action_type}"
    return key in executed_actions

def mark_executed(incident_id, action_type):
    key = f"{incident_id}:{action_type}"
    executed_actions.add(key)
