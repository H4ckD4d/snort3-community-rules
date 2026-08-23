# Changelog

**Project owner:** Chris Cruz | h4ckd4d

## [Unreleased]

### Added

- Detection Coverage Matrix documentation.
- Machine-readable `metadata/coverage-matrix.json`.
- `DEVELOPERS.md` with professional community invitation and contribution workflow.
- CI validation that every cataloged detection has corresponding coverage metadata.
- Planned coverage tracks for DNS, HTTP, TLS, Linux, cloud, and identity telemetry.

### Changed

- Expanded README from rule inventory to detection-coverage and collaboration model.
- Expanded contributor requirements to include coverage metadata and professional PR rationale.
- Strengthened original-author and project-owner attribution throughout collaboration documentation.

## [2.1.0-rc.1] - 2026-08-23

Detection-coverage and developer-community milestone.

## [2.0.0-rc.1] - 2026-08-23

First release-candidate milestone for the Detection Engineering redesign.

### Added

- Snort 3, Suricata, and Sigma repository structure.
- Detection-engineering architecture and rule standard.
- Machine-readable rule catalog.
- Synthetic validation fixtures.
- Catalog validation tooling and CI.
- ATT&CK-aware mapping guidance.

### Changed

- Repositioned the project from a basic Snort rule collection to a multi-engine detection-engineering framework.
- Replaced broad `any -> any` starter logic with environment-aware `$EXTERNAL_NET` / `$HOME_NET` examples.
- Standardized rule identifiers, revisions, severity, confidence, and analyst-review guidance.

<!-- h4ckd4d-brand-signature:start -->
---

**Chris Cruz | h4ckd4d**  
Cybersecurity • Red Team • Advanced Cyber Defense & Intelligence  
OSCP | CEH | CISSP | MITRE ATT&CK® Contributor

**Founder — Project h4ckd4d**  
Technology for Child Protection • OSINT • Threat Intelligence

*"Protect. Detect. Defend."*
<!-- h4ckd4d-brand-signature:end -->
