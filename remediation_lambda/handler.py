# remediation_lambda/handler.py

import json
from executor import execute_actions

def lambda_handler(event, context):

    try:
        result = execute_actions(event)

        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        print(f"Execution error: {str(e)}")

        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Remediation failed"})
        }
