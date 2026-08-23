# MITRE ATT&CK Mapping Guidance

## Purpose

ATT&CK provides a shared vocabulary for describing adversary behaviors. This repository uses ATT&CK to add analytical context to detections, not to inflate rule coverage claims.

## Mapping rule

A detection should map to an ATT&CK technique only when its observable telemetry directly supports that behavior at a useful level of confidence.

Avoid mappings based only on:

- a port number;
- a product name;
- generic protocol use;
- a vague similarity to an adversary technique.

## Example

A Windows Security Event ID `4625` records a failed logon. A single event alone is not sufficient to claim brute-force activity, so the starter Sigma rule is treated as authentication-failure telemetry rather than proof of ATT&CK `T1110`.

A future correlation rule that evaluates repeated failures within an appropriate time window may support `T1110` when the behavior and environment justify that interpretation.

## Mapping levels

| Level | Meaning |
| --- | --- |
| direct | Rule observes behavior strongly aligned with a technique |
| contextual | Rule contributes useful evidence but requires correlation |
| none | Mapping would overstate what the telemetry proves |

## Review questions

Before adding a mapping, ask:

1. What exact observable is present?
2. Could common benign activity generate the same observable?
3. Does the detection observe the technique or only infrastructure associated with it?
4. Is correlation required before the technique claim is justified?
5. Would removing the ATT&CK tag make the detection less useful operationally?

If the answer to question 5 is no, the mapping may be unnecessary.

## Reference

Use the current MITRE ATT&CK Enterprise knowledge base as the authoritative technique reference: https://attack.mitre.org/

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
