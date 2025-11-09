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

### 1. `master` (You are here)
- Base branch with initial vulnerable version
- Contains this README

### 2. `vulnerable-version`
- Preserved vulnerable code (162+ security issues)
- **DO NOT USE IN PRODUCTION**
- For educational comparison only

### 3. `secure-version` **RECOMMENDED**
- All security fixes implemented
- Upgraded to Spring Boot 3.3.5
- Contains the secure code and documentation

---

## Quick Start

### To Use the SECURE Version:
```bash
# IMPORTANT: Module2.1-SECURE only exists on the secure-version branch
# You MUST switch branches first

# Switch to the secure branch
git checkout secure-version

# NOW the secure module exists
cd software-testing/java/Module2.1-SECURE

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
cd software-testing/java/Module2.1-SECURE
mvn dependency-check:check
# Result: Significant reduction in vulnerabilities
```

---

## Security Improvements Summary

| Version | Branch | Vulnerabilities | Status |
|---------|--------|----------------|---------|
| Original | `vulnerable-version` | 162+ (21 CRITICAL) | Educational Only |
| Secure | `secure-version` | ~10-15 (latest libs) | Production Ready* |

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

Current branch (master) documentation:
- `/software-testing/README.md` - Main handbook
- `/software-testing/java/Module2.1/README.md` - Vulnerable version details

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
# FIRST: Switch to secure-version branch (Module2.1-SECURE doesn't exist on master)
git checkout secure-version

# THEN: Navigate and run
cd software-testing/java/Module2.1-SECURE
mvn spring-boot:run

# In another terminal:
# This should be BLOCKED (400 Bad Request)
curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"

# This should WORK
curl "http://localhost:8080/greeting?name=John"
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