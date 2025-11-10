# Software Testing Handbook - Security Audit Educational Suite

## IMPORTANT: This Repository Contains Intentionally Vulnerable Code for Education

This repository demonstrates security vulnerability remediation by maintaining both vulnerable and secure versions of a Spring Boot application.

---

## What This Is

An educational security audit project showing:
- **162+ real vulnerabilities** in outdated dependencies
- **How to fix them** with systematic upgrades
- **Before/after comparison** for learning

---

## Repository Structure - THREE BRANCHES

| Branch | Role | Key Assets |
|--------|------|------------|
| `master` (current) | Documentation hub | This README only - links to everything |
| `vulnerable-version` | Intentionally vulnerable code | Module2.1 (162 vulns), Python (18 issues) |
| `secure-version` | Fixed + vulnerable code | Module2.1-IMPROVED (15 vulns), Python fixed (0 issues), full docs |

> **Need the secure application?** Run `git checkout secure-version` before following any `Module2.1-IMPROVED` instructions.

---

## Quick Start

### To Use the SECURE Version:
```bash
# IMPORTANT: Module2.1-IMPROVED only exists on the secure-version branch
# You MUST switch branches first

# Switch to the secure branch
git checkout secure-version

# NOW the secure module exists
cd software-testing/java/Module2.1-IMPROVED

# Run the secure application
mvn spring-boot:run
```

### To Compare Both Versions:
```bash
# Check vulnerable version (exists on all branches)
cd software-testing/java/Module2.1
mvn dependency-check:check
# Result: 162 vulnerabilities, 90 unique CVEs

# Check secure version (ONLY on secure-version branch)
git checkout secure-version
cd software-testing/java/Module2.1-IMPROVED
mvn dependency-check:check
# Result: Significant reduction in vulnerabilities
```

> **Note:** The first run downloads the OWASP Dependency-Check/NVD feeds (auto-update is enabled). Expect a short delay while the database initializes. For restricted networks run `./mvnw dependency-check:update-only` ahead of time.

---

## Security Improvements Summary

| Version | Branch | Java Vulnerabilities | Python Issues | Status |
|---------|--------|---------------------|---------------|---------|
| Original | `vulnerable-version` | 162 (21 CRITICAL) | 18 (17 pylint + 1 mypy) | Educational Only |
| Secure | `secure-version` | 15 (Tomcat CVEs) | 0 (fixed version) | Production Ready* |

*With additional security measures

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

Additional documentation is available on the `secure-version` branch:

```bash
# Switch to secure-version branch to access these files:
git checkout secure-version

# The following files will then be available:
# - /TECHNICAL-SECURITY-AUDIT-CORRECTED.md - Technical report
# - /software-testing/docs/vulnerability-fixes-guide.md - Detailed fixes
# - /software-testing/docs/testing-strategy.md - How to test
# - /software-testing/docs/comparison-report.md - Before/after
```

## Complete Project Index

### What's Available on Each Branch

#### Master Branch (You Are Here)
- **Purpose**: Central documentation hub
- **Contents**: This README only
- **Usage**: Start here, then switch to other branches for code

#### Vulnerable-Version Branch
**Purpose**: Educational vulnerable code examples

**Java Content**:
- `software-testing/java/Module2.1/`
  - Spring Boot 2.2.4 application
  - **162 total vulnerabilities**
  - 21 CRITICAL (including Spring4Shell, Ghostcat)
  - 69 HIGH severity
  - 69 MEDIUM severity
  - 3 LOW severity
  - Includes OWASP Dependency Check configuration

**Python Content**:
- `software-testing/python/static_analysis_example.py`
  - **18 total issues**
  - 17 Pylint warnings (style, complexity, missing docstrings)
  - 1 Mypy type error
  - Intentionally flawed for learning

**Documentation**:
- Basic READMEs explaining the vulnerabilities
- Warning labels about not using in production

#### Secure-Version Branch
**Purpose**: Demonstrates vulnerability remediation

**Java Content**:
- `software-testing/java/Module2.1/` - Original vulnerable version (kept for comparison)
- `software-testing/java/Module2.1-IMPROVED/`
  - Spring Boot 3.3.5 (upgraded from 2.2.4)
  - Java 17 (upgraded from Java 8)
  - **15 residual vulnerabilities** (Tomcat CVEs pending upstream fix)
  - 91% reduction in vulnerabilities
  - Security headers implemented
  - Input validation added
  - SpEL injection fixed

**Python Content**:
- `software-testing/python/static_analysis_example.py` - Original flawed version
- `software-testing/python/static_analysis_example_fixed.py`
  - **0 issues** (all Pylint and Mypy errors resolved)
  - Best practices demonstrated
  - Clean code example

**Complete Documentation Suite**:
- `/software-testing/docs/vulnerability-analysis-report.md` - Full vulnerability analysis
- `/software-testing/docs/vulnerability-fixes-guide.md` - How each vulnerability was fixed
- `/software-testing/docs/testing-strategy.md` - Security testing methodology
- `/software-testing/docs/comparison-report.md` - Before/after metrics
- `/software-testing/docs/audits/` - Security audit reports
- `/scripts/run_scans.sh` - Automated security scanning

---
- **Purpose**: Central documentation hub
- **Contents**: This README only
- **Usage**: Start here, then switch to other branches for code

#### Vulnerable-Version Branch
**Purpose**: Educational vulnerable code examples

**Java Content**:
- `software-testing/java/Module2.1/`
  - Spring Boot 2.2.4 application
  - **162 total vulnerabilities**
  - 21 CRITICAL (including Spring4Shell, Ghostcat)
  - 69 HIGH severity
  - 69 MEDIUM severity
  - 3 LOW severity
  - Includes OWASP Dependency Check configuration

**Python Content**:
- `software-testing/python/static_analysis_example.py`
  - **18 total issues**
  - 17 Pylint warnings (style, complexity, missing docstrings)
  - 1 Mypy type error
  - Intentionally flawed for learning

**Documentation**:
- Basic READMEs explaining the vulnerabilities
- Warning labels about not using in production

#### 🟢 Secure-Version Branch
**Purpose**: Demonstrates vulnerability remediation

**Java Content**:
- `software-testing/java/Module2.1/` - Original vulnerable version (kept for comparison)
- `software-testing/java/Module2.1-IMPROVED/`
  - Spring Boot 3.3.5 (upgraded from 2.2.4)
  - Java 17 (upgraded from Java 8)
  - **15 residual vulnerabilities** (Tomcat CVEs pending upstream fix)
  - 91% reduction in vulnerabilities
  - Security headers implemented
  - Input validation added
  - SpEL injection fixed

**Python Content**:
- `software-testing/python/static_analysis_example.py` - Original flawed version
- `software-testing/python/static_analysis_example_fixed.py`
  - **0 issues** (all Pylint and Mypy errors resolved)
  - Best practices demonstrated
  - Clean code example

**Complete Documentation Suite**:
- `/software-testing/docs/vulnerability-analysis-report.md` - Full vulnerability analysis
- `/software-testing/docs/vulnerability-fixes-guide.md` - How each vulnerability was fixed
- `/software-testing/docs/testing-strategy.md` - Security testing methodology
- `/software-testing/docs/comparison-report.md` - Before/after metrics
- `/software-testing/docs/audits/` - Security audit reports
- `/scripts/run_scans.sh` - Automated security scanning

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

### Test the Secure Version:
```bash
# FIRST: Switch to secure-version branch (Module2.1-IMPROVED doesn't exist on master)
git checkout secure-version

# THEN: Navigate and run
cd software-testing/java/Module2.1-IMPROVED
mvn spring-boot:run

# In another terminal:
# This should be BLOCKED (400 Bad Request)
curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"

# This should WORK
curl "http://localhost:8080/greeting?name=John"
```

> Security scans in both modules also download the latest CVE data automatically; initial execution may take a few minutes.

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
- **After**: ~90% reduction
- **All critical custom code issues**: FIXED
- **Educational value**: PRESERVED

---

## Quick Links

- [View Secure Version](https://github.com/jguida941/software-testing-handbook/tree/secure-version)
- [View Vulnerable Version](https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version)
- [Compare Versions](https://github.com/jguida941/software-testing-handbook/compare/vulnerable-version...secure-version)

---

## License

Educational use only. Contains intentionally vulnerable code for learning purposes.

---

**Created**: November 9, 2025
**Purpose**: Security Education & Audit Documentation
**Status**: Complete
