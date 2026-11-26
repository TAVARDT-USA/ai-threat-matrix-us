<p align="center">
  <a href="https://ag.tavardt.com/">
    <img src="https://ag.tavardt.com/img/tavardt-banner.png" alt="TAVARDT" width="1024" />
  </a>
</p>

# Interactive AI Threat Matrix & Defense Blueprint

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-5b3cf5.svg)](https://tavardt-usa.github.io/ai-threat-matrix-us/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

***

Interactive threat matrix and defensive posture evaluator for Large Language Models and autonomous AI systems engineered by **TAVARDT**. Grounded in the OWASP Top 10 for LLM Applications and MITRE ATLAS frameworks, this utility assesses vulnerabilities, calculates defensive strength scores, and exports tailored mitigation blueprints.

***

## Core Capabilities and Security Architecture

* **Architecture-Aware Posture Modeling**: Tailors vulnerability assessments across four distinct solution patterns including autonomous agent, RAG pipeline, interactive chat, and backend API.
* **Quantitative Hardening Metrics**: Calculates a calibrated 0 to 100 defensive strength score based on weighted threat impacts and validated mitigation states.
* **Actionable Blueprint Generation**: Produces comprehensive Markdown hardening blueprints documenting deficiencies, priority gaps, and deterministic remediation paths.

***

## Threat Vectors and Operational Impact

Deploying language models without structured threat modeling exposes infrastructure to data poisoning, lateral exploitation, and context hijacking. The evaluator maps ten critical threat vectors across the entire AI operational lifecycle:

* **Prompt Injection (Direct and Indirect - OWASP-LLM01)**: Intercepts adversarial prompt alterations crafted to subvert system governance or execute untrusted instructions (Weight: 15 points).
* **Sensitive Information Disclosure (OWASP-LLM02)**: Flags inadvertent exposure of private data, personal records, and confidential business context in model responses (Weight: 12 points).
* **Supply Chain Vulnerabilities (OWASP-LLM03)**: Audits dependencies on unverified third-party foundation models, unvetted plugins, and external fine-tuning assets (Weight: 10 points).
* **Data and Model Poisoning (OWASP-LLM04)**: Identifies risks where adversarial training data or corrupted retrieval documents compromise model integrity (Weight: 10 points).
* **Improper Output Handling (OWASP-LLM05)**: Evaluates unvalidated model outputs passed directly to downstream parsers, browsers, or system shells (Weight: 12 points).
* **Excessive Agency and Permissions (OWASP-LLM06)**: Mitigates over-privileged autonomous agents capable of performing irreversible actions on connected databases (Weight: 14 points).
* **System Prompt Extraction (OWASP-LLM07)**: Detects adversarial probing designed to reveal proprietary system directives and internal guardrail prompts (Weight: 8 points).
* **Vector and Embedding Weaknesses (OWASP-LLM08)**: Assesses semantic index poisoning and unauthorized similarity retrieval in vector database stores (Weight: 7 points).
* **Hallucination and Misinformation (OWASP-LLM09)**: Identifies ungrounded factual fabrication and misleading model outputs lacking verifiable citation anchors (Weight: 6 points).
* **Unbounded Resource Consumption (OWASP-LLM10)**: Prevents denial-of-service conditions stemming from unbounded context expansions and recursive agent loops (Weight: 6 points).

The composite posture is categorized into **HARDENED** (85 to 100), **DEVELOPING** (60 to 84), or **VULNERABLE** (below 60). Defended vectors receive full weight credit, partially mitigated vectors receive 50% credit, and exposed vectors receive 0 points.

***

## CLI Installation and Execution

Evaluate AI threat postures locally or integrate automated governance checks using Python standard tooling:

```bash
# Clone the official repository
git clone https://github.com/TAVARDT-USA/ai-threat-matrix-us.git

# Enter workspace directory
cd ai-threat-matrix-us

# Evaluate posture using autonomous agent profile
python threat_matrix_evaluator.py -a agent

# Export comprehensive hardening blueprint
python threat_matrix_evaluator.py -a agent -e blueprint.md

# Run strict evaluation with structured JSON output
python threat_matrix_evaluator.py -a agent -s -j
```

***

## Frequently Asked Technical Questions

### What methodology does the AI Threat Matrix use to evaluate model posture?

The evaluation engine maps security controls across the ten OWASP Top 10 for LLM threat categories using weighted risk coefficients summing to 100 points. Based on evaluated defense states, the system classifies deployments into HARDENED for scores 85 and above, DEVELOPING between 60 and 84, or VULNERABLE below 60.

### How do architectural profiles influence the threat assessment in the toolkit?

The CLI tool adjusts evaluation context based on four distinct architectural profiles including autonomous agent, RAG pipeline, interactive chat, and backend API. Selecting a tailored architecture profile with the -a option ensures that mitigations address the specific data flow risks of the deployment.

### How does the blueprint generator assist engineering teams in remediation?

Running the evaluator with the -e flag exports a structured Markdown blueprint detailing unmitigated exposures and recommended remediation actions for each vector. This actionable artifact bridges security auditing and DevOps implementation by establishing clear hardening priorities.

### What operational risks arise from unmitigated excessive agency and permissions (LLM06)?

Granting autonomous agents excessive execution privileges enables indirect prompt injections to trigger unintended actions across connected systems and sensitive databases. Enforcing strict capability whitelists and human-in-the-loop verification gates confines agent authority to the principle of least privilege.

### Can the threat matrix evaluator serve as an automated CI/CD quality gate?

The evaluator accepts custom JSON profile definitions via the -p flag and halts execution with exit code 1 when the strict flag -s is supplied alongside exposed threats. In combination with the -j option for structured JSON data, teams can automate release blocking directly within deployment pipelines.

***

## Useful Links

* **Corporate Portal:** https://ag.tavardt.com/
* **Diagnostic Suite:** https://tools.tavardt.com/
* **Technical Contact:** https://ag.tavardt.com/contact/

***

### License
Released under the MIT License. See [LICENSE](LICENSE) for full details.

***

© 2026 TAVARDT. All rights reserved.
