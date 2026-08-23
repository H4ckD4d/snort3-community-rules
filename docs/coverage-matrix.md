# Detection Coverage Matrix

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

The coverage matrix connects each maintained detection to its engine, telemetry, status, severity, confidence, validation state, and ATT&CK context. Its purpose is to make gaps visible and prevent the repository from becoming an unstructured list of rules.

## Coverage dimensions

Each detection is evaluated across:

| Dimension | Meaning |
| --- | --- |
| Detection ID | Stable project identifier |
| Engine | Snort 3, Suricata, Sigma, or future supported engine |
| Domain | Network, endpoint, identity, cloud, DNS, HTTP, TLS, or other defensive telemetry domain |
| Data source | Required telemetry or event source |
| Status | Experimental, test, stable, or deprecated |
| Severity | Potential impact if the observation is validated |
| Confidence | Confidence that the detection logic represents the intended behavior |
| ATT&CK | Technique mapping only when directly supported by the observable |
| Test coverage | Synthetic fixture, static validation, engine validation, or analyst review |
| Tuning notes | Known benign causes and environment-specific considerations |

## Coverage interpretation

Coverage is not measured simply by counting ATT&CK techniques. A larger number of mapped techniques does not automatically mean better detection engineering.

The project prioritizes:

1. reliable telemetry;
2. clear detection intent;
3. reproducible tests;
4. controlled false positives;
5. documented assumptions;
6. defensible ATT&CK context.

## Current coverage

The machine-readable representation is maintained in [`metadata/coverage-matrix.json`](../metadata/coverage-matrix.json).

Initial coverage focuses on:

- network visibility through Snort 3 and Suricata;
- repeated inbound connection activity;
- legacy clear-text remote-access visibility;
- Windows failed-logon telemetry through Sigma.

## Gap management

A gap should become a new detection proposal only when the required telemetry exists and a useful observable can be defined. Contributors are encouraged to open an issue describing:

- the defensive behavior or condition to detect;
- required telemetry;
- why existing rules do not cover it;
- likely benign cases;
- proposed validation approach.

See [`DEVELOPERS.md`](../DEVELOPERS.md) for the contribution workflow.

---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
