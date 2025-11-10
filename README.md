# Software Testing Handbook - Security Audit Educational Suite

## IMPORTANT: This Repository Contains Intentionally Vulnerable Code for Education

This repository demonstrates security vulnerability remediation by maintaining both vulnerable and significantly improved versions of a Spring Boot application.

---

## What This Is

An educational security audit project showing:
- **162+ real vulnerabilities** in outdated dependencies
- **How to fix them** with systematic upgrades
- **Before/after comparison** for learning

---

## Repository Structure - THREE BRANCHES

### 1. `master` (You are here)
- Base branch with initial vulnerable version
- Contains this README

### 2. `vulnerable-version`
- Preserved vulnerable code (162+ security issues)
- **DO NOT USE IN PRODUCTION**
- For educational comparison only

### 3. `secure-version` **RECOMMENDED**
- Contains `software-testing/java/Module2.1-IMPROVED` (91 % of CVEs mitigated, 15 remain in Tomcat 10.1.31)
- Upgraded to Spring Boot 3.3.5 / Java 17
- Hosts all documentation and reports in `software-testing/docs/`

---

## Quick Start

### To Use the IMPROVED Version:
```bash
# Switch to the secure branch
git checkout secure-version

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
# See massive reduction (15 residual Tomcat CVEs remain)
```

---

## Security Improvements Summary

| Version | Branch | Vulnerabilities | Status |
|---------|--------|----------------|---------|
| Original | `vulnerable-version` | 162+ (21 CRITICAL) | Educational Only |
| Improved | `secure-version` | 15 (4 CRITICAL / 8 HIGH / 3 MED) | Significantly improved, not zero |

> Production readiness still requires Tomcat 10.1.35+ or compensating controls (see `software-testing/docs/status/HONEST-SECURITY-STATUS.md`)

---

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

---

## Documentation

All docs live under `software-testing/docs/` (see [`software-testing/docs/README.md`](software-testing/docs/README.md) for the map).

- Theory & examples: `static-dynamic-testing.md`, `testing-examples-index.md`
- Audits archive: `software-testing/docs/audits/`
- Honest status & OSS Index steps: `software-testing/docs/status/`
- Generated reports: `software-testing/docs/reports/`

---

## Educational Use Cases

This repository is perfect for:
- Learning about common vulnerabilities
- Understanding dependency management
- Security testing practice
- Demonstrating remediation processes
- Training on secure coding

---

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

---

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

---

## Warning About Vulnerable Version

The `vulnerable-version` branch contains:
- CVE-2022-22965 (Spring4Shell) - RCE
- CVE-2022-1471 (SnakeYAML) - RCE
- CVE-2020-1938 (Ghostcat) - File disclosure
- SpEL Injection - Direct code execution
- 150+ other vulnerabilities

**NEVER run the vulnerable version in production or on important systems!**

---

## Results

- **Before**: 162+ vulnerabilities
- **After**: 91% reduction (162 → 15; 4 CRITICAL + 8 HIGH + 3 MED remain)
- **All critical custom code issues**: FIXED
- **Educational value**: PRESERVED

---

## Quick Links

- [View Improved Version](https://github.com/jguida941/software-testing-handbook/tree/secure-version)
- [View Vulnerable Version](https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version)
- [Compare Versions](https://github.com/jguida941/software-testing-handbook/compare/vulnerable-version...secure-version)

---

## License

Educational use only. Contains intentionally vulnerable code for learning purposes.

---

**Created**: November 9, 2025
**Purpose**: Security Education & Audit Documentation
**Status**: Complete
