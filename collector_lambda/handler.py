# collector_lambda/handler.py

import json
from collector import build_incident_context

def lambda_handler(event, context):
    try:
        incident_data = build_incident_context(event)

        return {
            "statusCode": 200,
            "body": json.dumps(incident_data)
        }

    except Exception as e:
        print(f"Error building incident context: {str(e)}")

        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to collect incident context"})
        }
