# Interactive AI Threat Matrix & Defense Blueprint

[![Live Demo](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-38bdf8?style=for-the-badge)](https://tavardt-usa.github.io/ai-threat-matrix-us/)
[![Standard](https://img.shields.io/badge/Standard-OWASP%20LLM%20%26%20MITRE-3b82f6?style=for-the-badge)](https://tavardt-usa.github.io/ai-threat-matrix-us/)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Client-Side-10b981?style=for-the-badge)](https://tavardt-usa.github.io/ai-threat-matrix-us/)
[![License](https://img.shields.io/badge/License-MIT-slate?style=for-the-badge)](LICENSE)

Interactive threat matrix and mitigation blueprint for Large Language Models and AI systems. Grounded in OWASP LLM and MITRE ATLAS.

Engineered for organizations, security researchers, and AI engineers in **United States**, this repository provides a structured interactive matrix and evaluation engine for AI threat mapping, defensive posture assessment, and technical hardening blueprints across Large Language Models and autonomous AI agent architectures.

***

## Operational Modalities

### 1. In-Browser Client Web Application (GitHub Pages)
Access the interactive dashboard directly in any modern browser:
- **Official URL**: [https://tavardt-usa.github.io/ai-threat-matrix-us/](https://tavardt-usa.github.io/ai-threat-matrix-us/)
- **Privacy by Design**: Executes 100% in your browser's local JavaScript engine. No architecture schemas, parameters, or evaluations are transmitted to external servers.

### 2. Command Line Interface (CLI Tool)
For automated CI/CD pipeline gating or headless local audits:

```bash
# Basic evaluation using autonomous agent architecture profile
python threat_matrix_evaluator.py -arch agent

# Export comprehensive hardening blueprint in Markdown
python threat_matrix_evaluator.py -arch rag -export-blueprint hardening-blueprint.md

# Evaluate using structured defensive profile JSON
python threat_matrix_evaluator.py -profile profile.json -strict

# Structured JSON output for reporting and pipeline integration
python threat_matrix_evaluator.py -arch agent -json
```

***

## 10 Critical Threat Vectors Mapped (OWASP Top 10 for LLMs)

1. **Prompt Injection (Direct & Indirect)**: Subversion of model instructions via user prompts or retrieved external context.
2. **Sensitive Information Disclosure**: Inadvertent leakage of proprietary data, credentials, or PII in generated outputs.
3. **Supply Chain Vulnerabilities**: Compromised third-party packages, vulnerable plugins, or unverified model weights.
4. **Data and Model Poisoning**: Manipulation of fine-tuning datasets or knowledge repositories to introduce backdoors.
5. **Improper Output Handling**: Passing unsanitized model completions directly into downstream interpreters or databases.
6. **Excessive Agency & Permissions**: Autonomous agent tools granted uncontained system permissions without human oversight.
7. **System Prompt Extraction**: Adversarial exfiltration of core business logic or guardrail specifications.
8. **Vector & Embedding Weaknesses**: Poisoning of RAG retrieval indexes to hijack model reasoning paths.
9. **Hallucination & Misinformation**: Unchecked factual fabrication in critical operational workflows.
10. **Unbounded Resource Consumption**: Denial-of-wallet or service degradation via excessive token requests.

***

## CI/CD Pipeline Integration (GitHub Actions)

Example workflow enforcing zero-trust AI security posture:

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
          python threat_matrix_evaluator.py -arch agent -strict
```

***

## Compliance and Technical Standards

- **Jurisdiction**: United States
- **Compliance Standard**: OWASP Top 10 for LLM Applications & MITRE ATLAS
- **Maintaining Organization**: [TAVARDT-USA](https://github.com/TAVARDT-USA)

## Official Portals

- **Main National Portal**: [Portal Institucional](https://ag.tavardt.com/us/)
- **Tools Hub**: [Central de Ferramentas](https://tools.tavardt.com/us/)
- **Technical Support Channel**: [Canal de Contato](https://ag.tavardt.com/us/contact/)

***

### License
Released under the MIT License. See [LICENSE](LICENSE) for full details.
