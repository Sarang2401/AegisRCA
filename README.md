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

