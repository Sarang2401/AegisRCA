🛡 AegisRCA — AI-Assisted Root Cause Analysis for AWS Incidents

AegisRCA is an event-driven AWS incident response system that performs AI-assisted root cause analysis and safely executes limited auto-remediation using guardrail-enforced policies.

Built using AWS Lambda, EventBridge, CloudWatch, Auto Scaling, SSM, and S3 — fully compatible with AWS Free Tier.

🚀 Problem Statement

When infrastructure incidents occur (e.g., CPU spikes, application failures), engineers must:

Investigate logs and metrics

Identify root cause

Decide on safe remediation

Document everything

This process is slow, manual, and error-prone.

🧠 Solution Overview

AegisRCA automates incident analysis while enforcing strict safety controls.

When a CloudWatch alarm triggers:

📡 EventBridge invokes Collector Lambda

📊 Logs and metrics are gathered

🤖 AI module analyzes incident context

🛡 Decision engine enforces guardrails

⚙️ Safe actions execute automatically

📄 Incident report is generated and stored in S3

AI suggests.
Policy engine enforces.
Executor executes safely.

🏗 Architecture
CloudWatch Alarm
        ↓
EventBridge
        ↓
Collector Lambda
        ↓
AI Analysis Module
        ↓
Decision Engine (Guardrails)
        ↓
Remediation Lambda
        ↓
S3 (Markdown + JSON Audit Reports)

🧱 Tech Stack

AWS Lambda (Python 3.11)

CloudWatch Alarms & Metrics

EventBridge

Auto Scaling

SSM (EC2 restart)

S3 (audit storage)

boto3

IAM (least privilege design)

🔐 Safety Design

The system enforces strict guardrails:

❌ No deletion operations allowed

📏 Auto Scaling must respect min/max limits

⚠ EC2 restarts require approval

🔁 Idempotent remediation (prevents duplicate actions)

📝 Full audit logging of all decisions

AI has no direct execution privileges.

📦 Project Structure
aegis-rca/
│
├── collector_lambda/
├── ai_module/
├── decision_engine/
├── remediation_lambda/
├── report_generator/
├── infrastructure/
└── README.md

📄 Example Incident Output
AI Analysis Output
{
  "root_cause": "Database connection pool exhaustion",
  "confidence_score": 0.85,
  "suggested_actions": [
    {
      "action_type": "scale_asg",
      "parameters": {
        "asg_name": "app-prod-asg",
        "new_desired_capacity": 4
      }
    }
  ]
}

Generated Markdown Report (Stored in S3)
# Incident Report — inc-20260215-001

Root Cause: Database connection pool exhaustion
Confidence: 0.85

Approved Actions:
- scale_asg → SUCCESS

🎯 Key Engineering Highlights

Event-driven architecture

Structured AI integration with deterministic guardrails

Safe Auto Scaling automation

SSM-based EC2 recovery

IAM least privilege design

Audit-ready documentation pipeline

💰 AWS Free Tier Compatible

Lambda-based (no containers)

No RDS

No paid AI services

Minimal S3 usage

No long-running infrastructure

🔮 Future Improvements

DynamoDB for persistent idempotency

Slack/SNS approval workflow

Infrastructure-as-Code (Terraform/SAM)

Real LLM integration with prompt controls

👤 Author

Built as a cloud engineering portfolio project demonstrating event-driven AWS automation and safe AI-assisted remediation.