# Software Testing Handbook - Security Audit Educational Suite

## IMPORTANT: This Repository Contains Intentionally Vulnerable Code for Education

An educational security audit project demonstrating how to identify and fix 162+ real vulnerabilities through a three-branch learning system.

---

## Repository Navigation

You are on **master** - the documentation hub for this educational security project.

| Branch | Purpose | When to Use | Switch Command |
|--------|---------|-------------|----------------|
| **master** (current) | Documentation & orientation | Finding resources, understanding structure | You are here |
| **vulnerable-version** | Intentionally vulnerable code | Learning about vulnerabilities | `git checkout vulnerable-version` |
| **secure-version** | Fixed code + documentation | Running secure apps, reading docs | `git checkout secure-version` |

---

## First Time Here?

1. **Clone the repository:** `git clone https://github.com/jguida941/software-testing-handbook.git`
2. **Choose a learning path** below based on your goals
3. **Start with Path 1** if you're unsure where to begin
4. **Remember:** The vulnerable code is for education only - never deploy it to production!

---

## Learning Paths

### Path 1: Security Auditor (Recommended for beginners)
1. Start here on master to understand the project structure
2. Switch to `vulnerable-version` to explore 162 real vulnerabilities
3. Run security scans to identify CVEs and code issues
4. Switch to `secure-version` to see how each vulnerability was fixed
5. Review the [Comparison Report](https://github.com/jguida941/software-testing-handbook/blob/secure-version/software-testing/docs/comparison-report.md) to understand the impact

### Path 2: Hands-On Developer
1. Clone the repo and immediately switch to `vulnerable-version`
2. Run `mvn dependency-check:check` to see 162 vulnerabilities
3. Document 5-10 critical vulnerabilities you find interesting
4. Switch to `secure-version` and compare the code differences
5. Run the [automated scanning script](https://github.com/jguida941/software-testing-handbook/blob/secure-version/scripts/run_scans.sh) to see CI/CD integration

### Path 3: Security Researcher
1. Review the complete [Security Audit Reports](https://github.com/jguida941/software-testing-handbook/tree/secure-version/software-testing/docs/audits)
2. Analyze the [Vulnerability Fixes Guide](https://github.com/jguida941/software-testing-handbook/blob/secure-version/software-testing/docs/vulnerability-fixes-guide.md)
3. Study the remediation methodology in the [Testing Strategy](https://github.com/jguida941/software-testing-handbook/blob/secure-version/software-testing/docs/testing-strategy.md)
4. Understand residual risks and mitigation strategies

---

## Hands-On Labs

| Lab | What You'll Learn | Branch | Time |
|-----|------------------|--------|------|
| **Discover Real Vulnerabilities** | OWASP Dependency Check, CVE analysis | `vulnerable-version` | 15 min |
| **Fix Critical Security Issues** | Dependency upgrades, code remediation | `secure-version` | 30 min |
| **Python Static Analysis** | Pylint, Mypy, type safety | Both branches | 20 min |
| **Automated Security Scanning** | CI/CD integration, scan automation | `secure-version` | 25 min |

Each lab has step-by-step instructions in its branch-specific README.

---

## Documentation by Intent

### Getting Started
- [Vulnerable Module README](https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version/software-testing/java/Module2.1) - Start here to see vulnerable code
- [Secure Module README](https://github.com/jguida941/software-testing-handbook/tree/secure-version/software-testing/java/Module2.1-IMPROVED) - Production-ready implementation
- [Python Examples](https://github.com/jguida941/software-testing-handbook/tree/secure-version/software-testing/python) - Static analysis demonstrations

### Understanding Vulnerabilities
- [Vulnerability Analysis Report](https://github.com/jguida941/software-testing-handbook/blob/secure-version/software-testing/docs/vulnerability-analysis-report.md) - What we found
- [Vulnerability Fixes Guide](https://github.com/jguida941/software-testing-handbook/blob/secure-version/software-testing/docs/vulnerability-fixes-guide.md) - How we fixed each issue
- [Comparison Report](https://github.com/jguida941/software-testing-handbook/blob/secure-version/software-testing/docs/comparison-report.md) - Before/after metrics

### Security Testing & Automation
- [Testing Strategy](https://github.com/jguida941/software-testing-handbook/blob/secure-version/software-testing/docs/testing-strategy.md) - Comprehensive testing approach
- [Automated Scanning Script](https://github.com/jguida941/software-testing-handbook/blob/secure-version/scripts/run_scans.sh) - CI/CD ready automation
- [Security Audit Reports](https://github.com/jguida941/software-testing-handbook/tree/secure-version/software-testing/docs/audits) - Complete audit trail

---

## What's Available Where

### On this branch (master)
- This README - your navigation hub to all resources

### On vulnerable-version branch
- **Java:** Module2.1 with 162 vulnerabilities (Spring Boot 2.2.4)
- **Python:** Flawed example with 18 issues (17 Pylint + 1 Mypy)
- **Purpose:** Learn what can go wrong
- [View branch →](https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version)

### On secure-version branch
- **Java:** Module2.1-IMPROVED with 91% vulnerability reduction (15 residual Tomcat CVEs)
- **Python:** Fixed example with 0 issues
- **Documentation:** Complete security analysis and remediation guides
- **Automation:** Security scanning scripts
- **Purpose:** Learn how to fix vulnerabilities
- [View branch →](https://github.com/jguida941/software-testing-handbook/tree/secure-version)

---

## Security Improvements Summary

| Metric | Vulnerable Version | Secure Version | Improvement |
|--------|-------------------|----------------|-------------|
| **Java Vulnerabilities** | 162 (21 CRITICAL) | 15 (4 CRITICAL)* | 91% reduction |
| **Python Issues** | 18 (17 Pylint + 1 Mypy) | 0 | 100% fixed |
| **Spring Boot** | 2.2.4 | 3.3.5 | Major upgrade |
| **Java Version** | 8 | 17 | LTS upgrade |

*Residual CVEs are in Tomcat 10.1.31, pending upstream fixes

---

## Safety Guidelines

### DO:
- Use for learning and education
- Run in isolated environments (VMs, containers)
- Share with other security learners
- Follow the learning paths above

### DO NOT:
- Deploy vulnerable-version to production
- Expose vulnerable code to the internet
- Use on systems with sensitive data
- Skip the security warnings in module READMEs

---

## Quick Start Examples

### Example 1: See the vulnerabilities
```bash
git checkout vulnerable-version
cd software-testing/java/Module2.1
mvn dependency-check:check
# View the report: open target/dependency-check-report.html
```

### Example 2: Run the secure version
```bash
git checkout secure-version
cd software-testing/java/Module2.1-IMPROVED
mvn spring-boot:run
# Test it: curl http://localhost:8080/health
```

### Example 3: Compare both versions
```bash
# Online: https://github.com/jguida941/software-testing-handbook/compare/vulnerable-version...secure-version
# Or locally: git diff vulnerable-version secure-version
```

---

## Quick Links

- [Secure Version Branch](https://github.com/jguida941/software-testing-handbook/tree/secure-version)
- [Vulnerable Version Branch](https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version)
- [Compare Versions](https://github.com/jguida941/software-testing-handbook/compare/vulnerable-version...secure-version)
- [All Documentation](https://github.com/jguida941/software-testing-handbook/tree/secure-version/software-testing/docs)

---

## License

Educational use only. Contains intentionally vulnerable code for learning purposes.

---

**Created**: November 2025
**Purpose**: Security Education & Vulnerability Remediation Training
**Status**: Active Learning Resource