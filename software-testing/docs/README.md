# Documentation Hub

This folder holds every guide, audit, and reference for the Software Testing Handbook. Start here when you need to understand the repo.

## Quick Links

| Topic | File / Location | Purpose |
|-------|-----------------|---------|
| Theory overview | `static-dynamic-testing.md` | Explains static vs dynamic testing concepts. |
| Example catalog | `testing-examples-index.md` | Lists every hands-on lab (Python + Java). |
| Vulnerability findings | `vulnerability-analysis-report.md` | Summarises dependency-check results. |
| Fix instructions | `vulnerability-fixes-guide.md` | Step-by-step remediation notes. |
| Testing strategy | `testing-strategy.md` | How to run scans/tests in each module. |
| Automated scans | `../../scripts/run_scans.sh` | Runs OSS Index + dependency-check for vulnerable & improved modules. |
| Honest status & OSS Index | `status/` (see below) | Current CVE counts + OSS Index setup. |
| Audit history | `audits/` | Full audit trails, chronological. |
| Reports | `reports/` | Saved dependency-check outputs (HTML/JSON). |

## Status & Setup

- `status/HONEST-SECURITY-STATUS.md` – Snapshot of the latest “secure” (Module2.1-IMPROVED) risk, including the 15 residual Tomcat CVEs.
- `status/OSS-INDEX-SETUP.md` – How to create OSS Index API tokens and run the automated scan script.

## Audit Archive

The `audits/` directory contains every deep-dive report:
- `TECHNICAL-SECURITY-AUDIT-CORRECTED.md` – Corrected walkthrough.
- `SECURITY-AUDIT-FINAL-REPORT.md` – Final formatted write-up.

## Adding New Docs

1. Create a descriptive filename under `software-testing/docs/`.
2. Link it from this README so others can find it.
3. If it’s an audit or report, place it under the relevant subfolder.
