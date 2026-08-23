# Detection Testing Strategy

## Testing goals

Every detection should answer two questions:

1. Does the rule match the intended synthetic condition?
2. Does the rule avoid matching a documented benign condition?

## Test layers

### Static repository validation

Checks:

- unique project IDs;
- unique Snort/Suricata SIDs;
- required catalog fields;
- valid rule paths;
- supported severity/confidence values;
- ATT&CK identifiers in expected format.

Run:

```bash
python scripts/validate_catalog.py
```

### Native engine validation

When installed in a controlled lab, use the engine's built-in configuration or rule-validation mode. Native validation is authoritative for engine syntax.

### Synthetic fixtures

Fixtures stored in this repository must be synthetic or sanitized. They should represent metadata or event structures required to exercise parsing and repository logic without embedding sensitive data.

### Analyst validation

Before production deployment, review:

- expected event volume;
- environment-specific false positives;
- NAT/proxy/load-balancer effects;
- monitoring and vulnerability-scanner allowlists;
- asset criticality;
- telemetry completeness.

## Test evidence

For each stable detection, maintain a concise record of:

- positive case;
- negative case;
- engine/schema version where validated;
- expected alert/rule identifier;
- tuning notes.

## Safety requirement

Repository tests should not require interacting with third-party systems. Network tests belong in isolated, authorized lab environments.

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
