# ai_module/analyzer.py

import json
import os


def load_knowledge_base():
    kb_path = os.path.join(os.path.dirname(__file__), "mock_knowledge_base.json")
    with open(kb_path, "r") as f:
        return json.load(f)


def analyze_incident(incident_json):

    logs = " ".join(incident_json.get("recent_logs", [])).lower()
    cpu = incident_json["metrics"].get("cpu_utilization_avg", 0)

    knowledge_base = load_knowledge_base()

    matched_pattern = None

    for entry in knowledge_base:
        if entry["pattern"] in logs:
            matched_pattern = entry
            break

    if matched_pattern:
        root_cause = matched_pattern["root_cause"]
        confidence = 0.85 if cpu > 70 else 0.65
        suggested_actions = build_actions(
            matched_pattern["suggested_actions"],
            incident_json
        )
    else:
        root_cause = "Unknown cause — high resource utilization"
        confidence = 0.5
        suggested_actions = build_actions(["scale_asg"], incident_json)

    return {
        "root_cause": root_cause,
        "confidence_score": round(confidence, 2),
        "suggested_actions": suggested_actions
    }
