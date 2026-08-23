# Detection Rule Standard

## Required fields

Every maintained detection should have a stable project identifier and corresponding catalog entry.

Recommended metadata:

| Field | Purpose |
| --- | --- |
| `id` | Stable project identifier |
| `title` | Human-readable detection name |
| `engine` | Snort 3, Suricata, Sigma, or future engine |
| `status` | experimental, test, stable, deprecated |
| `severity` | informational, low, medium, high |
| `confidence` | low, medium, high |
| `data_source` | Required telemetry |
| `description` | Behavior the rule observes |
| `false_positives` | Expected benign causes |
| `attack` | ATT&CK mappings supported by evidence |
| `references` | Primary technical references |
| `revision` | Logic revision |

## Detection documentation template

```markdown
## Detection title

### Objective

What defensive question does this detection answer?

### Telemetry

What data must be available?

### Detection logic

What observable condition causes a match?

### What this does not prove

Explain the analytical limitations.

### False positives

List expected benign causes.

### ATT&CK context

Add only evidence-supported technique mappings.

### Validation

Describe synthetic positive and negative fixtures.
```

## Snort and Suricata identifiers

Project-local SIDs use the `1000000+` range in this repository. New rules must use unique SIDs and increment `rev` whenever detection logic changes.

## Sigma identifiers

Sigma rules use stable UUIDs. A semantic logic change should update the `modified` date while preserving the rule ID unless the rule becomes conceptually different.

## Severity vs confidence

Severity describes potential impact **if** the observed condition is meaningful. Confidence describes how strongly the telemetry supports the interpretation.

Examples:

- high severity + low confidence: important condition with noisy evidence;
- low severity + high confidence: clearly observed but low-impact behavior.

Do not use severity as a substitute for confidence.

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
