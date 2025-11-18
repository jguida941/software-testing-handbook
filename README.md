# Software Testing Handbook - Security Audit Educational Suite
<p align="left">
  <!-- Secure snapshot (links to secure branch) -->
  <br/>
  <a href="https://github.com/jguida941/software-testing-handbook/tree/secure-version">
    <img alt="Secure Branch" src="https://img.shields.io/badge/BRANCH-secure--version-16A34A?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://github.com/jguida941/software-testing-handbook/tree/secure-version">
    <img alt="Vulnerabilities (secure)" src="https://img.shields.io/badge/VULNERABILITIES-18-22C55E?style=for-the-badge">
  </a>
  <img alt="Critical (secure)" src="https://img.shields.io/badge/CRITICAL-5-F97316?style=for-the-badge">
  <img alt="High (secure)" src="https://img.shields.io/badge/HIGH-9-FBBF24?style=for-the-badge">
  <img alt="Medium (secure)" src="https://img.shields.io/badge/MEDIUM-4-38BDF8?style=for-the-badge">
  <img alt="Reduction" src="https://img.shields.io/badge/VULN%20REDUCTION-91%25-3B82F6?style=for-the-badge">
  <img alt="Spring Boot 3.3.5" src="https://img.shields.io/badge/Spring%20Boot-3.3.5-22C55E?style=for-the-badge&logo=springboot&logoColor=white">
  <img alt="Java 17" src="https://img.shields.io/badge/Java-17-2563EB?style=for-the-badge&logo=openjdk&logoColor=white">
  <img alt="Tomcat 10.1.31" src="https://img.shields.io/badge/Tomcat-10.1.31-FACC15?style=for-the-badge&logo=apachetomcat&logoColor=black">
</p>

This repository demonstrates security vulnerability remediation by maintaining both vulnerable and significantly improved versions of a Spring Boot application.



> ##### **NOTE:** This branch contains the improved, significantly hardened version of the application. A small number of residual Tomcat CVEs remain for educational transparency; do **NOT** treat this as a production security baseline without further hardening.



## What This Is

An educational security audit project showing:
- **162+ real vulnerabilities** in outdated dependencies
- **How to fix them** with systematic upgrades
- **Before/after comparison** for learning


## Repository Structure - THREE BRANCHES

| Branch | Role | Key Assets |
|--------|------|------------|
| `master` | Documentation hub / branch map | Overview README, `agents.md`, `audit.md` |
| `vulnerable-version` | Intentionally vulnerable lab | `software-testing/java/Module2.1`, flawed Python example |
| `secure-version` (current) | Remediated implementation & docs | `software-testing/java/Module2.1-IMPROVED`, `scripts/`, `software-testing/docs/` |

> You are currently on `secure-version`. Switch to `master` for the handbook overview or `vulnerable-version` to explore the unpatched code.



## Quick Start

### To Use the IMPROVED Version:
```bash
# Ensure we're on the secure branch (this is the current branch)
git status -sb

# Navigate to improved module
cd software-testing/java/Module2.1-IMPROVED

# Run the improved application
mvn spring-boot:run
```

### To Compare Both Versions:
```bash
# Check vulnerable version (DO NOT RUN IN PRODUCTION)
git checkout vulnerable-version
cd software-testing/java/Module2.1
mvn dependency-check:check
# See 162+ vulnerabilities

# Check improved version
git checkout secure-version
cd software-testing/java/Module2.1-IMPROVED
mvn dependency-check:check
# See massive reduction (18 residual Tomcat CVEs remain)
```


## Security Improvements Summary

| Version | Branch | Vulnerabilities | Status |
|---------|--------|----------------|---------|
| Original | `vulnerable-version` | 162+ (21 CRITICAL) | Educational Only |
| Improved | `secure-version` | 18 (5 CRITICAL / 9 HIGH / 4 MED) | Significantly improved, not zero |

> Production readiness still requires Tomcat 10.1.35+ or compensating controls (see `software-testing/docs/status/HONEST-SECURITY-STATUS.md`)


## Key Fixes Applied

1. **Dependency Updates:**
   - Spring Boot: 2.2.4 → 3.3.5
   - Java: 8 → 17
   - Tomcat: 9.0.30 → 10.1.31
   - SnakeYAML: 1.25 → 2.2

2. **Code Fixes:**
   - SpEL injection vulnerability patched
   - Array bounds checking added
   - Input validation implemented


## Documentation

All docs live under `software-testing/docs/` (see [`software-testing/docs/README.md`](software-testing/docs/README.md) for the map).

- Theory & examples: `static-dynamic-testing.md`, `testing-examples-index.md`
- Audits archive: `software-testing/docs/audits/`
- Honest status & OSS Index steps: `software-testing/docs/status/`
- Generated reports: `software-testing/docs/reports/`



## Educational Use Cases

This repository is perfect for:
- Learning about common vulnerabilities
- Understanding dependency management
- Security testing practice
- Demonstrating remediation processes
- Training on secure coding



## Quick Commands

```bash
# Clone the repository
git clone https://github.com/jguida941/software-testing-handbook.git
cd software-testing-handbook

# List all branches
git branch -a

# Switch to secure version (RECOMMENDED)
git checkout secure-version

# See what's in each branch
git ls-tree --name-only -r vulnerable-version | head
git ls-tree --name-only -r secure-version | head
```



## Security Testing

### Test the Improved Version:
```bash
git checkout secure-version
cd software-testing/java/Module2.1-IMPROVED
mvn spring-boot:run

# In another terminal:
# This should be BLOCKED (400 Bad Request)
curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"

# This should WORK
curl "http://localhost:8080/greeting?name=John"
```

### Automated Vulnerability Scans
```bash
export OSS_INDEX_USER="you@example.com"
export OSS_INDEX_TOKEN="token-from-oss-index"
./scripts/run_scans.sh
# HTML/JSON reports saved to software-testing/docs/reports/<timestamp>/
```



## Warning About Vulnerable Version

The `vulnerable-version` branch contains:
- CVE-2022-22965 (Spring4Shell) - RCE
- CVE-2022-1471 (SnakeYAML) - RCE
- CVE-2020-1938 (Ghostcat) - File disclosure
- SpEL Injection - Direct code execution
- 150+ other vulnerabilities

**NEVER run the vulnerable version in production or on important systems!**


## Results

- **Before**: 162+ vulnerabilities
- **After**: 91% reduction (162 → 18; 5 CRITICAL + 9 HIGH + 4 MED remain)
- **All critical custom code issues**: FIXED
- **Educational value**: PRESERVED



## Quick Links

- [View Improved Version](https://github.com/jguida941/software-testing-handbook/tree/secure-version)
- [View Vulnerable Version](https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version)
- [Compare Versions](https://github.com/jguida941/software-testing-handbook/compare/vulnerable-version...secure-version)



## License

Educational use only. Contains intentionally vulnerable code for learning purposes.



**Created**: November 9, 2025
**Purpose**: Security Education & Audit Documentation
**Status**: Complete
