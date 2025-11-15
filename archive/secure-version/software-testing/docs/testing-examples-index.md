# Testing Examples Index

## Overview

This index provides a comprehensive catalog of all testing examples in the Software Testing Handbook, organized by testing type, language, and severity of findings.

## Examples by Testing Type

### Static Testing Examples

#### Python Static Analysis
- **Location**: [`/python/static_analysis_example.py`](../python/) (flawed) and [`/python/static_analysis_example_fixed.py`](../python/) (clean reference)
- **Tools Used**: Pylint, Mypy
- **Issues Found**: 23 findings (22 Pylint, 1 Mypy) in the flawed sample; 0 in the fixed sample
- **Learning Focus**: Early bug detection, type safety, code maintainability
- **Time to Complete**: 15-20 minutes

### Dynamic Testing Examples

#### Java Security Testing (Module 2.1)
- **Location**: [`/java/Module2.1/`](../java/Module2.1/)
- **Tools Used**: OWASP Dependency Check
- **Issues Found**: 162 vulnerabilities (21 CRITICAL, 69 HIGH)
- **Learning Focus**: Security vulnerability detection, dependency management
- **Time to Complete**: 30-45 minutes
- **Secure Version**: Available on `secure-version` branch as Module2.1-IMPROVED (run `git checkout secure-version`)

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

| Example         | Language | Testing Type | Tools        | Issues Found | Business Impact        |
|-----------------|----------|--------------|--------------|--------------|------------------------|
| Static Analysis | Python   | Static       | Pylint, Mypy | 23           | Code maintainability   |
| Security Scan   | Java     | Dynamic      | OWASP DC     | 162          | Critical security risk |

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

## Quick Command Reference

### Python Static Testing
```bash
cd python/
pylint static_analysis_example.py    # Code quality
mypy static_analysis_example.py       # Type checking
python static_analysis_example.py     # Dynamic execution
pylint static_analysis_example_fixed.py  # Should report 0 findings
mypy static_analysis_example_fixed.py    # Should report 0 findings
```

### Java Dynamic Testing (Vulnerable Version)
```bash
cd java/Module2.1/
./mvnw clean compile dependency-check:check -DskipTests
open target/dependency-check-report.html
```

### Java Security Testing (Secure Version)
```bash
# Note: Module2.1-IMPROVED only exists on secure-version branch
git checkout secure-version
cd java/Module2.1-IMPROVED/
./mvnw clean compile dependency-check:check -DskipTests
open target/dependency-check-report.html
```

## Metrics Summary

### Total Issues Found Across All Examples
- **Security Vulnerabilities**: 162
- **Code Quality Issues**: 22 (Pylint)
- **Type Safety Issues**: 1 (Mypy)
- **Total**: 185 issues

### Time Investment vs Value
| Activity               | Time       | Issues Found | Value                  |
|------------------------|------------|--------------|------------------------|
| Python Static Analysis | 20 min     | 23           | High (early detection) |
| Java Security Scan     | 45 min     | 162          | Critical (security)    |
| **Total**              | **65 min** | **185**      | **Exceptional ROI**    |

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

## Cross-References

### Theory Documentation
- [Main README](../README.md) - Handbook overview
- [Static vs Dynamic Testing](./static-dynamic-testing.md) - Conceptual guide

### Tool Documentation
- [OWASP Dependency Check](https://jeremylong.github.io/DependencyCheck/)
- [Pylint User Guide](https://pylint.org/)
- [Mypy Documentation](http://mypy-lang.org/)

### Vulnerability References
- [CVE-2022-22965 (Spring4Shell)](https://nvd.nist.gov/vuln/detail/CVE-2022-22965)
- [CVE-2020-1938 (Ghostcat)](https://nvd.nist.gov/vuln/detail/CVE-2020-1938)
- [Full vulnerability list](../java/Module2.1/target/dependency-check-report.html)

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

**Remember**: Each example in this handbook represents real-world scenarios. The 162 vulnerabilities found in Java and 23 static-analysis issues in Python are typical of what you'll encounter in production systems.

---
[← Back to Main Documentation](./README.md)
