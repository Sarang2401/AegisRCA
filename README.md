# 🛡 AegisRCA  
**AI-Assisted Root Cause Analysis & Safe Auto-Remediation for AWS**

AegisRCA is an event-driven AWS incident response system that performs structured AI-assisted root cause analysis and safely executes limited auto-remediation using guardrail-enforced policies.

Built using:
- AWS Lambda
- CloudWatch
- EventBridge
- Auto Scaling
- SSM
- S3
- Python (boto3)

Fully compatible with AWS Free Tier.

---

# 🚀 Problem Statement

When infrastructure incidents occur (e.g., CPU spikes or application instability), engineers must:

- Investigate metrics and logs
- Identify the root cause
- Decide on safe remediation
- Document the incident

This process is manual, slow, and error-prone.

---

# 🧠 Solution Overview

AegisRCA automates analysis while enforcing strict safety controls.

### Incident Flow

1. CloudWatch Alarm triggers  
2. EventBridge invokes Collector Lambda  
3. Logs and metrics are gathered  
4. AI module analyzes incident context  
5. Decision engine enforces guardrails  
6. Safe actions execute automatically  
7. Incident report is stored in S3  

AI suggests.  
Policy engine enforces.  
Executor executes safely.

---

# 🏗 Architecture

CloudWatch Alarm
│
▼
EventBridge Rule
│
▼
Collector Lambda
│
▼
AI Analysis Module
│
▼
Decision Engine (Guardrails)
│
├── SAFE → Remediation Lambda
│
└── NEEDS_APPROVAL → Hold
│
▼
Report Generator
│
▼
S3 (Markdown + JSON Audit Reports)


---

# 🧱 Tech Stack

- AWS Lambda (Python 3.11)
- CloudWatch Metrics & Alarms
- EventBridge
- Auto Scaling
- AWS Systems Manager (SSM)
- Amazon S3
- boto3
- IAM (Least Privilege Design)

---

# 🔐 Safety Design

The system enforces strict guardrails:

- ❌ No deletion operations allowed
- 📏 Auto Scaling must respect min/max limits
- ⚠ EC2 restarts require approval
- 🔁 Idempotent remediation (prevents duplicate actions)
- 📝 Full audit logging

The AI module has **no AWS execution privileges**.

---

# 📂 Project Structure

aegis-rca/
│
├── collector_lambda/
│ ├── handler.py
│ └── collector.py
│
├── ai_module/
│ ├── analyzer.py
│ ├── prompt_template.txt
│ └── mock_knowledge_base.json
│
├── decision_engine/
│ ├── safety_evaluator.py
│ └── policy_rules.py
│
├── remediation_lambda/
│ ├── handler.py
│ ├── executor.py
│ └── idempotency.py
│
├── report_generator/
│ ├── report_builder.py
│ └── s3_writer.py
│
├── infrastructure/
│ ├── iam_policies/
│ └── eventbridge_rule.json
│
└── README.md


---

# 📄 Example AI Output

```json
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
📄 Example Incident Report (Stored in S3)
# Incident Report — inc-20260215-001

Root Cause: Database connection pool exhaustion  
Confidence: 0.85  

Approved Actions:
- scale_asg → SUCCESS
📊 Demonstration (Add Screenshots Here)
You can add real AWS console screenshots in:

docs/screenshots/
Example:

## CloudWatch Alarm Triggered
![Alarm](docs/screenshots/alarm.png)

## Auto Scaling Updated
![ASG](docs/screenshots/asg_scaled.png)

## Generated Incident Report
![Report](docs/screenshots/report.png)
🎯 Engineering Highlights
Event-driven AWS architecture

Structured AI integration with deterministic guardrails

Safe Auto Scaling automation

EC2 restart via SSM

IAM least privilege enforcement

Audit-ready documentation pipeline

💰 AWS Free Tier Compatible
Lambda-based (no containers)

No RDS

No external paid AI service required

Minimal S3 storage

No long-running compute

🔮 Future Improvements
DynamoDB-backed idempotency

Slack/SNS approval workflow

Terraform or AWS SAM for IaC

Real LLM integration with structured output validation

👤 Author
Built as a cloud engineering portfolio project demonstrating event-driven AWS automation and safe AI-assisted remediation.