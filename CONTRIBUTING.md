# Contributing

> **Project owner and original creator: Chris Cruz | h4ckd4d**

Contributions are welcome when they improve defensive detection quality, portability, validation, documentation, or analyst usability.

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
- synthetic or sanitized validation evidence.

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

Add or update the corresponding entry in `metadata/rule-catalog.json` whenever a maintained rule changes materially.

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

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
