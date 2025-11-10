# Testing Examples Index

## Overview

This index provides a comprehensive catalog of all testing examples in the Software Testing Handbook, organized by testing type, language, and severity of findings.

## Important: Branch Structure

This repository uses three branches:
- **`master`** (current): Documentation hub linking to other branches
- **`vulnerable-version`**: Contains intentionally vulnerable code (162 Java vulnerabilities, 18 Python issues)
- **`secure-version`**: Contains fixed/secure code (15 residual Java vulnerabilities, 0 Python issues in fixed version)

To access the actual code examples, switch branches:
```bash
git checkout vulnerable-version  # For vulnerable examples
git checkout secure-version      # For secure examples
```

## Examples by Testing Type

### Static Testing Examples

#### Python Static Analysis
- **Location**: Available on `vulnerable-version` and `secure-version` branches
- **Tools Used**: Pylint, Mypy
- **Issues Found**:
  - `vulnerable-version`: 17 Pylint warnings, 1 Mypy error
  - `secure-version`: 22 Pylint warnings, 1 Mypy error (flawed) / 0 issues (fixed)
- **Learning Focus**: Early bug detection, type safety, code maintainability
- **Time to Complete**: 15-20 minutes

### Dynamic Testing Examples

#### Java Security Testing
- **Module2.1** (Vulnerable): Available on all branches
  - **Issues Found**: 162 vulnerabilities (21 CRITICAL, 69 HIGH)
- **Module2.1-IMPROVED** (Secure): Only on `secure-version` branch
  - **Issues Found**: 15 vulnerabilities (residual Tomcat CVEs)
- **Tools Used**: OWASP Dependency Check
- **Learning Focus**: Security vulnerability detection, dependency management
- **Time to Complete**: 30-45 minutes

## Examples by Severity of Findings

### Critical Severity (Immediate Action Required)
1. **Spring4Shell (CVE-2022-22965)** - Remote Code Execution
   - Location: Java Module 2.1
   - CVSS Score: 9.8
   - Impact: Complete system compromise

2. **Ghostcat (CVE-2020-1938)** - Apache Tomcat Vulnerability
   - Location: Java Module 2.1
   - CVSS Score: 9.8
   - Impact: File read and potential RCE

3. **SnakeYAML Deserialization (CVE-2022-1471)**
   - Location: Java Module 2.1
   - CVSS Score: 9.8
   - Impact: Arbitrary code execution

### High Severity
- **Jackson XXE (CVE-2020-25649)** - XML External Entity attack
- **Spring URL Parsing (CVE-2024-22259)** - SSRF vulnerability
- **Type Safety Issues** - Found in Python static analysis

### Medium Severity
- **Code Quality Issues** - Python Pylint findings
- **Documentation Gaps** - Missing docstrings
- **Complexity Issues** - Refactoring opportunities

## Comparative Analysis

| Branch | Example | Language | Tools | Issues Found | Business Impact |
|--------|---------|----------|-------|--------------|-----------------|
| vulnerable-version | Python Static | Python | Pylint, Mypy | 18 (17+1) | Code maintainability |
| vulnerable-version | Java Module2.1 | Java | OWASP DC | 162 | Critical security risk |
| secure-version | Python Fixed | Python | Pylint, Mypy | 0 | Clean code |
| secure-version | Java Module2.1-IMPROVED | Java | OWASP DC | 15 | Reduced risk |

## Learning Paths by Role

### For Developers
1. Start with Python static analysis (understand code quality)
2. Move to Java security testing (understand vulnerability impact)
3. Implement both in your projects

### For Security Engineers
1. Focus on Java Module 2.1 (162 vulnerabilities analysis)
2. Study CVE remediation strategies
3. Implement security gates in CI/CD

### For QA Engineers
1. Understand static vs dynamic testing theory
2. Run both examples to see different bug categories
3. Design comprehensive test strategies

### For Engineering Managers
1. Review the business impact sections
2. Understand ROI of early testing (10-100x cost savings)
3. Plan testing strategy for your team

## How to Access Examples

### For Vulnerable Code Examples:
```bash
git checkout vulnerable-version
# Python and Java vulnerable examples are available here
```

### For Secure/Fixed Code Examples:
```bash
git checkout secure-version
# Both vulnerable and fixed versions available here
# Module2.1-IMPROVED only exists on this branch
```

## Summary of What's Available

### On `vulnerable-version` Branch:
- Python example with intentional issues for learning
- Java Module2.1 with 162 security vulnerabilities
- Educational documentation explaining the vulnerabilities

### On `secure-version` Branch:
- All vulnerable examples PLUS:
- Fixed Python example showing best practices
- Module2.1-IMPROVED with remediated vulnerabilities
- Complete security audit documentation
- Testing strategies and fix guides

## Next Examples to Add

### Planned Additions
1. **JavaScript** - ESLint and security scanning with npm audit
2. **Go** - Static analysis with go vet and security with gosec
3. **Rust** - Clippy for lints and cargo-audit for vulnerabilities
4. **Container Security** - Docker image scanning with Trivy

### Community Contributions Welcome
- Performance testing examples
- Integration testing patterns
- API security testing
- Mobile app testing

## Branch Links

### View on GitHub:
- [Vulnerable Version Branch](https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version)
- [Secure Version Branch](https://github.com/jguida941/software-testing-handbook/tree/secure-version)
- [Compare Branches](https://github.com/jguida941/software-testing-handbook/compare/vulnerable-version...secure-version)

### Local Branch Commands:
```bash
# List all branches
git branch -a

# Switch to vulnerable version
git checkout vulnerable-version

# Switch to secure version
git checkout secure-version

# Return to master
git checkout master
```

## Key Insights

1. **Different Tools, Different Bugs**: Static and dynamic testing find completely different issue categories
2. **Real Impact**: The 162 vulnerabilities in Java represent actual exploitable security risks
3. **Cost Efficiency**: Issues found in static analysis cost 10-100x less to fix than production bugs
4. **Comprehensive Coverage**: Using both approaches catches 70%+ of potential issues

## Certification Preparation

These examples align with:
- **ISTQB** - Software Testing Certification
- **CEH** - Certified Ethical Hacker (security testing)
- **AWS Security** - Cloud security best practices
- **OWASP** - Application security standards

---

**Remember**: Each example in this handbook represents real-world scenarios:
- **vulnerable-version**: 162 Java vulnerabilities, 18 Python issues (17 Pylint + 1 Mypy)
- **secure-version**: 15 residual Java vulnerabilities, 0 Python issues in fixed version

Switch branches to explore the actual code and run the tests yourself!

---
[← Back to Main Documentation](./README.md)
