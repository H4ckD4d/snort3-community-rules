# Detection Engineering Architecture

## Objective

The repository treats a detection as a versioned engineering artifact rather than a standalone signature.

```text
Behavior Hypothesis
      ↓
Telemetry Source
      ↓
Detection Logic
      ↓
Engine Representation
      ↓
Metadata + ATT&CK Context
      ↓
Synthetic Validation
      ↓
False-Positive Review
      ↓
CI / Peer Review
      ↓
Deployment
      ↓
Tuning / Revision
```

## Trust boundaries

Detection logic may operate on telemetry from owned or administered environments. Test content stored in this repository should be synthetic, sanitized, or documentation-safe.

## Content layers

### Engine layer

Contains executable rule formats:

- Snort 3
- Suricata
- Sigma

### Metadata layer

`metadata/rule-catalog.json` provides a vendor-neutral inventory of detections, including identifier, engine, severity, confidence, data source, status, and ATT&CK context.

### Validation layer

Scripts and CI validate repository consistency independently of deployment tooling. Native engine validation should be added whenever the engine is available in CI.

### Analyst layer

Documentation explains what a detection observes, what it does not prove, common benign matches, and recommended tuning considerations.

## Design principles

1. **Behavior before signature** — define the defensive hypothesis before writing syntax.
2. **Telemetry aware** — document exactly which telemetry is required.
3. **Portable where practical** — maintain equivalent logic across engines when semantics remain meaningful.
4. **Evidence proportionality** — do not overstate what an alert proves.
5. **False-positive first** — document expected benign causes before production deployment.
6. **Revision controlled** — changes to logic require revision and catalog updates.
7. **Synthetic testing** — repository fixtures must not contain sensitive real-world data.

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
