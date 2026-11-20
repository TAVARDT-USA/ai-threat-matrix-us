#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TAVARDT United States
Interactive AI Threat Matrix & Hardening Blueprint
Interactive threat modeling matrix and security posture validator for LLMs and AI agent architectures. NIST AI RMF and OWASP LLM aligned.

Standard: NIST AI Risk Management Framework, OWASP LLM, and MITRE ATLAS
Repository: https://github.com/TAVARDT-USA/ai-threat-matrix-us
Online Web App: https://tavardt-usa.github.io/ai-threat-matrix-us/
"""

import os
import sys
import json
import argparse
from datetime import datetime

THREAT_DEFINITIONS = [
    {"id": "LLM01", "code": "OWASP-LLM01", "title": "Prompt Injection (Direct & Indirect)", "weight": 15, "default": "exposed"},
    {"id": "LLM02", "code": "OWASP-LLM02", "title": "Sensitive Information Disclosure", "weight": 12, "default": "partial"},
    {"id": "LLM03", "code": "OWASP-LLM03", "title": "Supply Chain Vulnerabilities", "weight": 10, "default": "exposed"},
    {"id": "LLM04", "code": "OWASP-LLM04", "title": "Data and Model Poisoning", "weight": 10, "default": "exposed"},
    {"id": "LLM05", "code": "OWASP-LLM05", "title": "Improper Output Handling", "weight": 12, "default": "exposed"},
    {"id": "LLM06", "code": "OWASP-LLM06", "title": "Excessive Agency & Permissions", "weight": 14, "default": "exposed"},
    {"id": "LLM07", "code": "OWASP-LLM07", "title": "System Prompt Extraction", "weight": 8,  "default": "defended"},
    {"id": "LLM08", "code": "OWASP-LLM08", "title": "Vector & Embedding Weaknesses", "weight": 7,  "default": "partial"},
    {"id": "LLM09", "code": "OWASP-LLM09", "title": "Hallucination & Misinformation", "weight": 6,  "default": "defended"},
    {"id": "LLM10", "code": "OWASP-LLM10", "title": "Unbounded Resource Consumption", "weight": 6,  "default": "exposed"}
]

def evaluate_posture(arch, profile_states):
    total_score = 0
    defended_count = 0
    exposed_count = 0
    eval_items = []

    for item in THREAT_DEFINITIONS:
        tid = item["id"]
        state = profile_states.get(tid, item["default"]).lower()
        if state == "defended":
            total_score += item["weight"]
            defended_count += 1
        elif state == "partial":
            total_score += (item["weight"] * 0.5)
        else:
            state = "exposed"
            exposed_count += 1

        eval_items.append({
            "id": tid,
            "code": item["code"],
            "title": item["title"],
            "weight": item["weight"],
            "status": state
        })

    score = round(total_score)
    if score >= 85:
        posture = "HARDENED"
    elif score >= 60:
        posture = "DEVELOPING"
    else:
        posture = "VULNERABLE"

    return {
        "architecture": arch,
        "score": score,
        "posture": posture,
        "defended_count": defended_count,
        "exposed_count": exposed_count,
        "items": eval_items
    }

def generate_blueprint_md(evaluation):
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    md = []
    md.append("# AI Security Hardening Blueprint")
    md.append(f"- **Organization**: TAVARDT United States")
    md.append(f"- **Evaluation Date**: {ts} UTC")
    md.append(f"- **Architecture Profile**: {evaluation['architecture'].upper()}")
    md.append(f"- **Compliance Standard**: NIST AI Risk Management Framework, OWASP LLM, and MITRE ATLAS")
    md.append(f"- **Hardening Score**: {evaluation['score']} / 100")
    md.append(f"- **Defensive Posture**: {evaluation['posture']}")
    md.append("")
    md.append("## Threat Vector Status and Gaps")
    md.append("")
    for it in evaluation["items"]:
        md.append(f"### [{it['code']}] {it['title']} - Status: {it['status'].upper()}")
        if it["status"] == "exposed":
            md.append("- **Deficiency**: Unmitigated exposure. Direct security risk.")
            md.append("- **Remediation**: Implement mandatory heuristic guardrails, context sandboxing, and execution whitelists.")
        elif it["status"] == "partial":
            md.append("- **Deficiency**: Partial controls active.")
            md.append("- **Remediation**: Introduce secondary confirmation gates and automated red-teaming checks.")
        else:
            md.append("- **Status**: Verified defensive controls documented.")
        md.append("")
    return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="AI Threat Matrix Evaluator and Defensive Hardening Blueprint Generator.")
    parser.add_argument("--arch", choices=["agent", "rag", "chat", "api"], default="agent", help="AI architecture profile (agent, rag, chat, api)")
    parser.add_argument("--profile", help="Path to JSON file containing threat defense states")
    parser.add_argument("--export-blueprint", help="Export hardening blueprint to Markdown file")
    parser.add_argument("--strict", action="store_true", help="Exit with code 1 if any threat vector is exposed")
    parser.add_argument("--json", action="store_true", help="Output evaluation in structured JSON format")

    args = parser.parse_args()

    states = {}
    if args.profile:
        if not os.path.exists(args.profile):
            print(f"Error: Profile file not found: {args.profile}", file=sys.stderr)
            sys.exit(2)
        try:
            with open(args.profile, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    states = data.get("threat_states", data)
        except Exception as e:
            print(f"Error reading JSON from {args.profile}: {e}", file=sys.stderr)
            sys.exit(2)

    eval_res = evaluate_posture(args.arch, states)

    if args.export_blueprint:
        bp_content = generate_blueprint_md(eval_res)
        with open(args.export_blueprint, "w", encoding="utf-8") as bf:
            bf.write(bp_content)
        print(f"Hardening blueprint successfully written to: {args.export_blueprint}")

    if args.json:
        print(json.dumps(eval_res, indent=2, ensure_ascii=False))
    else:
        print("=" * 64)
        print(f"AI THREAT MATRIX: TAVARDT United States")
        print(f"Standard: NIST AI Risk Management Framework, OWASP LLM, and MITRE ATLAS")
        print(f"Architecture: {eval_res['architecture'].upper()}")
        print(f"Hardening Score: {eval_res['score']} / 100")
        print(f"Defensive Posture: {eval_res['posture']}")
        print(f"Active Defended Controls: {eval_res['defended_count']} / 10")
        print(f"Exposed Vectors: {eval_res['exposed_count']} / 10")
        print("=" * 64)

        for it in eval_res["items"]:
            status_label = it["status"].upper()
            print(f"[{it['code']}] {it['title']}: {status_label}")

    if args.strict and eval_res["exposed_count"] > 0:
        sys.exit(1)
    if eval_res["score"] < 60:
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
