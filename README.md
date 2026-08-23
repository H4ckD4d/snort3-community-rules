# h4ckd4d Detection Engineering

> **Original creator, project owner, and primary maintainer: Chris Cruz | h4ckd4d**

**h4ckd4d Detection Engineering** is a defensive detection-content framework for building, documenting, testing, and maintaining portable security detections across **Snort 3**, **Suricata**, and **Sigma**.

The project evolves the original `snort3-community-rules` collection into a structured Blue Team / SOC engineering repository focused on detection quality, reproducibility, false-positive control, ATT&CK-aware context, and safe synthetic validation.

> **Defensive use only:** The repository is designed for monitoring environments you own or administer. Test fixtures use documentation-safe or synthetic data and are not intended to reproduce harmful activity.

## Detection lifecycle

```text
Threat / Behavior Hypothesis
          ↓
Telemetry Selection
          ↓
Detection Logic
          ↓
Rule Metadata
          ↓
Synthetic Validation
          ↓
False-Positive Review
          ↓
ATT&CK Context
          ↓
Peer Review / CI
          ↓
Deployment
          ↓
Tuning / Revision
```

## Engines

| Engine | Purpose | Location |
| --- | --- | --- |
| Snort 3 | Network IDS/IPS detection content | `rules/snort3/` |
| Suricata | Network IDS/IPS detection content | `rules/suricata/` |
| Sigma | Vendor-neutral SIEM detections | `rules/sigma/` |

The root [`community.rules`](community.rules) remains as the compact Snort 3 starter pack for backward compatibility.

## Rule quality standard

Every maintained detection should document:

1. Detection objective.
2. Required telemetry.
3. Detection logic.
4. Expected benign matches.
5. False-positive considerations.
6. Severity and confidence.
7. ATT&CK mapping when evidence supports one.
8. Test fixture or validation method.
9. Unique rule identifier and revision history.

See [`docs/rule-standard.md`](docs/rule-standard.md).

## Repository structure

```text
.
├── README.md
├── community.rules
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── docs/
│   ├── architecture.md
│   ├── rule-standard.md
│   ├── testing.md
│   └── mitre-mapping.md
├── rules/
│   ├── snort3/
│   ├── suricata/
│   └── sigma/
├── metadata/
│   └── rule-catalog.json
├── tests/
│   └── fixtures/
├── scripts/
│   └── validate_catalog.py
└── .github/
    └── workflows/
```

## Initial detection families

The first professionalized release focuses on conservative signals that are useful in defensive lab and SOC environments:

- inbound ICMP visibility;
- inbound SSH exposure monitoring;
- legacy clear-text remote-access visibility;
- repeated TCP SYN activity requiring review;
- Windows failed-logon telemetry through Sigma.

These are **signals for analyst review**, not automatic proof of malicious activity.

## ATT&CK-aware, not ATT&CK-driven

MITRE ATT&CK mapping is used as analytical context only when the detection logic actually observes behavior relevant to a technique. A rule is not made better simply by attaching more ATT&CK tags.

See [`docs/mitre-mapping.md`](docs/mitre-mapping.md).

## Validation philosophy

A detection is considered maintainable when:

- syntax can be validated by the relevant engine or schema tooling;
- identifiers are unique;
- metadata is complete;
- fixtures are synthetic or sanitized;
- expected matches and expected non-matches are documented;
- tuning decisions are revision-controlled.

## Official references

- Snort 3 Rule Writing Guide: https://docs.snort.org/
- Suricata Rules Documentation: https://docs.suricata.io/en/latest/rules/
- Sigma Specification: https://github.com/SigmaHQ/sigma-specification
- MITRE ATT&CK: https://attack.mitre.org/

## Project relationship

This repository is the **Detection / SOC / Blue Team** pillar of Project h4ckd4d. It complements the separate Internet Exposure Intelligence / EASM / OSINT framework maintained in `Shodan-Dorks-for-Advanced-OSINT`.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions should favor high-confidence defensive detections, documented assumptions, minimal false positives, and reproducible tests.

## Security

See [`SECURITY.md`](SECURITY.md).

## License

Released under the MIT License. See [`LICENSE`](LICENSE).

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
