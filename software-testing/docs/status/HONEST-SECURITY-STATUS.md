# Honest Security Assessment (Module 2.1-IMPROVED)

## Snapshot (2025-11-10)

| Metric | Vulnerable (`Module2.1`) | Improved (`Module 2.1-IMPROVED`) |
|--------|-------------------------|----------------------------------|
| Total vulnerabilities | 162 | 15 |
| Critical (CVSS ≥ 9) | 21 | 4 (Tomcat 10.1.31) |
| High (CVSS 7–8.9) | 69 | 8 |
| Medium (CVSS 4–6.9) | 69 | 3 |
| Low | 3 | 0 |

> **Status**: 91 % reduction, **not** zero. Dependency-Check still fails the CVSS≥7 threshold because of Tomcat CVEs bundled with Spring Boot 3.3.5.

## Why Issues Remain

- Spring Boot 3.3.5 currently ships Tomcat 10.1.31; the remaining CVEs are fixed only in 10.1.35+ (not yet released via Spring Boot).
- Exploitation typically requires unusual connectors (e.g., AJP) or admin access, but we treat them as outstanding until upstream patches.
- “Zero CVEs” is unrealistic for modern frameworks; documenting residual risk is more honest for students.

## Recommended Actions

1. Track Spring Boot/Tomcat release notes and upgrade as soon as patched starters ship.
2. For now, deploy behind TLS terminators/WAFs and disable unused connectors to reduce exposure.
3. Keep dependency-check reports (`software-testing/java/Module2.1-IMPROVED/target/dependency-check-report.*`) under version control snapshots for transparency.

## Evidence

- Latest scan: `scripts/run_scans.sh` (see OSS Index Setup)  
- Generated reports stored under `software-testing/docs/reports/2025-11-10/`.
