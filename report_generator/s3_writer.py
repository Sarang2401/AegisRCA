# report_generator/s3_writer.py

import boto3
import json

s3 = boto3.client("s3")

BUCKET_NAME = "aegis-rca-reports"  # create in Phase 7


def upload_report(incident_id, markdown_content, audit_json):

    md_key = f"reports/{incident_id}.md"
    json_key = f"audits/{incident_id}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=md_key,
        Body=markdown_content.encode("utf-8"),
        ContentType="text/markdown"
    )

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=json_key,
        Body=json.dumps(audit_json, indent=2).encode("utf-8"),
        ContentType="application/json"
    )

    return {
        "markdown_s3_key": md_key,
        "audit_s3_key": json_key
    }
