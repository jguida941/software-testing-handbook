# Software Testing Handbook: Security Audit Educational Suite

### IMPORTANT: This Repository Contains Intentionally Vulnerable Code for Education

This repository demonstrates security vulnerability remediation by maintaining both vulnerable and significantly improved versions of a Spring Boot application.


## What This Is

An educational security audit project showing:
- **162+ real vulnerabilities** in outdated dependencies
- **How to fix them** with systematic upgrades
- **Before/after comparison** for learning



## Repository Structure: THREE BRANCHES

| Branch | Role | Key Assets |
|--------|------|------------|
| `master` | Documentation hub / branch map | Navigation README only - links to all resources |
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
# See massive reduction (15 residual Tomcat CVEs remain)
```



## Security Improvements Summary

| Version | Branch | Vulnerabilities | Status |
|---------|--------|----------------|---------|
| Original | `vulnerable-version` | 162+ (21 CRITICAL) | Educational Only |
| Improved | `secure-version` | 15 (4 CRITICAL / 8 HIGH / 3 MED) | Significantly improved, not zero |

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



## Documentation & Navigation

### Key README Files
| Location | Purpose | Link |
|----------|---------|------|
| Root | Main project overview (this file) | You are here |
| Project Map | Complete file structure | [`PROJECT_STRUCTURE.md`](PROJECT_STRUCTURE.md) |
| Testing Handbook | Complete testing concepts & overview | [`software-testing/README.md`](software-testing/README.md) |
| Documentation Hub | All docs, audits, reports | [`software-testing/docs/README.md`](software-testing/docs/README.md) |
| Java Examples | Both vulnerable & secure modules | [`software-testing/java/README.md`](software-testing/java/README.md) |
| Python Examples | Static analysis demonstrations | [`software-testing/python/README.md`](software-testing/python/README.md) |
| Vulnerable Module | Module2.1 with 162+ vulnerabilities | [`software-testing/java/Module2.1/README.md`](software-testing/java/Module2.1/README.md) |
| Secure Module | Module2.1-IMPROVED with fixes | [`software-testing/java/Module2.1-IMPROVED/README.md`](software-testing/java/Module2.1-IMPROVED/README.md) |
| Vulnerability Warning | Warning about Module2.1 | [`software-testing/java/Module2.1/README-VULNERABLE.md`](software-testing/java/Module2.1/README-VULNERABLE.md) |

### Key Documentation Files
- **Theory & examples**: [`static-dynamic-testing.md`](software-testing/docs/static-dynamic-testing.md), [`testing-examples-index.md`](software-testing/docs/testing-examples-index.md)
- **Vulnerability reports**: [`vulnerability-analysis-report.md`](software-testing/docs/vulnerability-analysis-report.md), [`vulnerability-fixes-guide.md`](software-testing/docs/vulnerability-fixes-guide.md)
- **Audits archive**: [`software-testing/docs/audits/`](software-testing/docs/audits/) - Full security audit reports
- **Status reports**: [`software-testing/docs/status/`](software-testing/docs/status/) - Current security status & setup guides
- **Generated reports**: `software-testing/docs/reports/` - Scan outputs (directory created when scripts run)



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

# See what's in each branch (using remote references)
git ls-tree --name-only -r origin/vulnerable-version | head
git ls-tree --name-only -r origin/secure-version | head
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
- **After**: 91% reduction (162 → 15; 4 CRITICAL + 8 HIGH + 3 MED remain)
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
