# Contributing

> **Project owner and original creator: Chris Cruz | h4ckd4d**

Contributions are welcome when they improve defensive detection quality, portability, validation, documentation, analyst usability, or engineering rigor.

## Who should contribute

The project welcomes:

- detection engineers;
- SOC and Blue Team analysts;
- Snort 3 and Suricata rule authors;
- Sigma contributors;
- SIEM and security-platform engineers;
- Python / CI/CD developers;
- threat researchers;
- educators and technical writers;
- maintainers of defensive security tooling.

See [`DEVELOPERS.md`](DEVELOPERS.md) for the broader collaboration roadmap.

## Detection contribution requirements

Every proposed detection should include:

- a clear defensive objective;
- the required telemetry source;
- expected match conditions;
- expected benign or non-match conditions;
- false-positive considerations;
- severity and confidence;
- a stable identifier and revision;
- ATT&CK mapping only when the observable behavior supports it;
- synthetic or sanitized validation evidence;
- corresponding catalog and coverage metadata.

## Rule safety

Do not submit:

- credentials, tokens, private keys, or personal data;
- sensitive third-party infrastructure details;
- real victim data;
- live malicious payloads or weaponized proof-of-concept material;
- rules whose only purpose is to operationalize exploitation.

Use documentation-safe domains, IP ranges, event samples, and synthetic fixtures.

## Engine organization

- Snort 3 rules: `rules/snort3/`
- Suricata rules: `rules/suricata/`
- Sigma rules: `rules/sigma/`

## Metadata

Add or update the corresponding entry in `metadata/rule-catalog.json` whenever a maintained rule changes materially. Every cataloged rule must also have an entry in `metadata/coverage-matrix.json`.

## Pull request expectations

A professional pull request should explain:

1. the detection hypothesis or engineering problem;
2. the telemetry assumption;
3. what the rule is expected to match;
4. known benign cases;
5. validation performed;
6. tuning implications;
7. ATT&CK mapping rationale, when applicable;
8. files and metadata affected.

Small, focused pull requests are preferred over large mixed changes.

## Validation

Before opening a pull request:

```bash
python scripts/validate_catalog.py
```

When the relevant engine is installed, also run its native syntax/schema validation.

## Commit prefixes

- `feat:` new detection content
- `fix:` logic or metadata correction
- `docs:` documentation
- `test:` fixtures or validation
- `ci:` automation
- `chore:` maintenance

## Credit and ownership

Accepted contributors receive attribution through Git history and the pull request record, and may also be acknowledged in release notes or project documentation for substantial contributions.

**Original authorship, project ownership, and primary maintenance remain attributed to Chris Cruz | h4ckd4d.** Contributor credit does not remove or replace the original project attribution.

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
