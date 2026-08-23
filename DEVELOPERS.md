# Developers and Community

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**h4ckd4d Detection Engineering** welcomes developers, detection engineers, SOC analysts, Blue Team practitioners, researchers, educators, and security-tool maintainers who want to improve high-quality defensive detection content.

## How to help

Professional contributions are especially valuable in these areas:

- Snort 3 and Suricata rule engineering;
- Sigma detections for Windows, Linux, identity, cloud, and network telemetry;
- synthetic fixtures and regression tests;
- false-positive reduction and tuning methodology;
- ATT&CK mapping review;
- detection metadata and coverage analysis;
- CI/CD, linting, schemas, and validation tooling;
- documentation, diagrams, and analyst playbooks;
- portability testing across SIEM and IDS/IPS platforms.

## Contribution workflow

1. Open or select an issue describing the detection gap, bug, documentation improvement, or engineering proposal.
2. Fork the repository and create a focused branch.
3. Add or revise detection content using the standards in `docs/rule-standard.md`.
4. Add synthetic or sanitized validation evidence where applicable.
5. Update `metadata/rule-catalog.json` and coverage metadata when needed.
6. Run repository validation locally.
7. Open a pull request explaining the detection hypothesis, telemetry assumptions, expected false positives, validation performed, and any ATT&CK mapping.

## Review philosophy

Pull requests are reviewed for defensive value, technical correctness, reproducibility, false-positive control, portability, safe test data, and maintainability. A contribution does not need to be complex to be valuable; a precise correction, stronger test, clearer explanation, or better tuning note can materially improve the project.

## Contributor credit

Accepted contributors retain credit through Git history, pull requests, release notes, and project acknowledgments where appropriate. Project ownership and original authorship remain attributed to **Chris Cruz | h4ckd4d**.

## Code of professional collaboration

Be technically rigorous, respectful, evidence-driven, and transparent about limitations. Do not include real victim data, credentials, sensitive third-party infrastructure, live malicious payloads, or content whose main purpose is exploitation.

## Project mission

The goal is to build an open, professional-quality Detection Engineering knowledge base that helps defenders improve visibility, reduce noise, and make better security decisions.

**Developers are invited to propose new engines, tests, schemas, integrations, documentation, and detections through GitHub Issues and Pull Requests.**

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
