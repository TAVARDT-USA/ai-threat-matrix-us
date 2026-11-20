# Interactive AI Threat Matrix & Hardening Blueprint

[![Live Demo](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-38bdf8?style=for-the-badge)](https://tavardt-usa.github.io/ai-threat-matrix-us/)
[![Standard](https://img.shields.io/badge/Standard-OWASP%20LLM%20%26%20MITRE-3b82f6?style=for-the-badge)](https://tavardt-usa.github.io/ai-threat-matrix-us/)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Client--Side-10b981?style=for-the-badge)](https://tavardt-usa.github.io/ai-threat-matrix-us/)
[![License](https://img.shields.io/badge/License-MIT-slate?style=for-the-badge)](LICENSE)

Interactive threat modeling matrix and security posture validator for LLMs and AI agent architectures. NIST AI RMF and OWASP LLM aligned.

Engineered for organizations and engineering teams in **United States**, this repository provides a structured threat assessment matrix and automated hardening blueprint generator for Large Language Models and autonomous AI agent applications.

---

## Operational Interfaces

### 1. In-Browser Web Application (GitHub Pages)
Interactive visual interface accessible directly from your browser:
- **Live Demo**: [https://tavardt-usa.github.io/ai-threat-matrix-us/](https://tavardt-usa.github.io/ai-threat-matrix-us/)
- **Privacy by Design**: All processing executes 100% locally in your client JavaScript engine. No configurations or security metrics are ever transmitted to any external server.

### 2. Standalone Python CLI Tool
For automated security gating in CI/CD pipelines, pre-commit hooks, or local workstation auditing:

```bash
# Basic evaluation with autonomous agent profile
python threat_matrix_evaluator.py --arch agent

# Generate Hardening Blueprint in Markdown format
python threat_matrix_evaluator.py --arch rag --export-blueprint hardening-blueprint.md

# Strict mode for CI/CD gates (exits with code 1 upon any vulnerable vector)
python threat_matrix_evaluator.py --profile profile.json --strict

# Output structured JSON report
python threat_matrix_evaluator.py --arch agent --json
```

---

## 10 Audited Threat Vectors (OWASP Top 10 for LLMs)

1. **Prompt Injection (Direct & Indirect)**: Subversion of LLM instructions via untrusted user inputs or retrieved third-party context.
2. **Sensitive Information Disclosure**: Inadvertent leakage of proprietary data, credentials, or PII in generated outputs.
3. **Supply Chain Vulnerabilities**: Compromised third-party packages, vulnerable plugins, or unverified model weights.
4. **Data and Model Poisoning**: Manipulation of fine-tuning datasets or knowledge repositories to introduce backdoors.
5. **Improper Output Handling**: Passing unsanitized model completions directly into downstream interpreters or databases.
6. **Excessive Agency & Permissions**: Autonomous agent tools granted uncontained system permissions without human oversight.
7. **System Prompt Extraction**: Adversarial exfiltration of core business logic or guardrail specifications.
8. **Vector & Embedding Weaknesses**: Poisoning of RAG retrieval indexes to hijack model reasoning paths.
9. **Hallucination & Misinformation**: Unchecked factual fabrication in critical operational workflows.
10. **Unbounded Resource Consumption**: Denial-of-wallet or service degradation via excessive token requests.

---

## GitHub Actions CI/CD Integration

```yaml
name: AI Threat Matrix Gate
on: [push, pull_request]

jobs:
  evaluate-ai-security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Run AI Threat Matrix Assessment
        run: |
          python threat_matrix_evaluator.py --arch agent --strict
```

---

## Compliance and Technical Standards

- **Jurisdiction**: United States
- **Compliance Standard**: NIST AI Risk Management Framework, OWASP LLM, and MITRE ATLAS
- **Maintaining Organization**: [TAVARDT-USA](https://github.com/TAVARDT-USA)

## TAVARDT Ecosystem & Official Portals

- **Main National Portal**: [https://ag.tavardt.com/us/](https://ag.tavardt.com/us/)
- **Cybersecurity & Web Tools Hub**: [https://tools.tavardt.com/](https://tools.tavardt.com/)
- **Technical Support Channel**: [https://ag.tavardt.com/us/contact/](https://ag.tavardt.com/us/contact/)

---

### License
Released under the MIT License. See [LICENSE](LICENSE) for full details.
