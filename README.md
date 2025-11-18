# Software Testing Handbook - Vulnerable Version
<p align="left">
<!-- Vulnerable snapshot (links to vulnerable branch) -->
  <br/>
  <a href="https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version">
    <img alt="Vulnerable Branch" src="https://img.shields.io/badge/BRANCH-vulnerable--version-DB4545?style=for-the-badge&logo=github&logoColor=white">
  </a>
  <a href="https://github.com/jguida941/software-testing-handbook/tree/vulnerable-version">
    <img alt="Vulnerabilities (vulnerable)" src="https://img.shields.io/badge/VULNERABILITIES-162-DB4545?style=for-the-badge">
  </a>
  <img alt="Critical (vulnerable)" src="https://img.shields.io/badge/CRITICAL-21-DB4545?style=for-the-badge">
  <img alt="High (vulnerable)" src="https://img.shields.io/badge/HIGH-69-FD7E14?style=for-the-badge">
  <img alt="Medium (vulnerable)" src="https://img.shields.io/badge/MEDIUM-69-F1C40F?style=for-the-badge">
  <img alt="Low (vulnerable)" src="https://img.shields.io/badge/LOW-3-9CA3AF?style=for-the-badge">
  <img alt="Spring Boot 2.2.4" src="https://img.shields.io/badge/Spring%20Boot-2.2.4-6DB33F?style=for-the-badge&logo=springboot&logoColor=white">
  <img alt="Java 8" src="https://img.shields.io/badge/Java-8-007396?style=for-the-badge&logo=openjdk&logoColor=white">
  <img alt="Tomcat 9.0.30" src="https://img.shields.io/badge/Tomcat-9.0.30-F8DC75?style=for-the-badge&logo=apachetomcat&logoColor=black">


> ##### **WARNING:** This branch intentionally contains vulnerable dependencies and insecure code for educational purposes. Do **NOT** deploy to production!

## Branch Purpose
- Preserve the original vulnerable `Module2.1` Spring Boot application with **162 known vulnerabilities**
- Provide the intentionally flawed Python static-analysis example (17 pylint issues, 1 mypy error)
- Serve as the "before" snapshot for security education

## What's on This Branch vs Others

| Content | This Branch (vulnerable-version) | secure-version | master |
|---------|----------------------------------|----------------|--------|
| Module2.1 (vulnerable) | ✅ Full vulnerable implementation | ✅ Also included for comparison | ❌ |
| Module2.1-IMPROVED | ❌ Placeholder only | ✅ Full secure version | ❌ |
| Python flawed example | ✅ Only flawed version | ✅ Both flawed + fixed | ❌ |
| Python fixed example | ❌ Not here | ✅ `static_analysis_example_fixed.py` | ❌ |
| Documentation | Basic READMEs | Full docs + audits | Overview only |

## Getting Started
```bash
git checkout vulnerable-version
cd software-testing/java/Module2.1
./mvnw clean compile dependency-check:check -DskipTests
```
- Expected result: 162 total vulnerabilities (21 CRITICAL / 69 HIGH / 69 MEDIUM / 3 LOW)
- Reports written to `software-testing/java/Module2.1/target/dependency-check-report.{html,json}`

## Python Static Analysis Lab
```bash
cd software-testing/python
python3 static_analysis_example.py  # intentionally flawed runtime
pylint static_analysis_example.py   # expect 17 issues
mypy static_analysis_example.py     # expect 1 type error
```

## Looking for the Fixes?
```bash
# Switch to the hardened implementation
git checkout secure-version
cd software-testing/java/Module2.1-IMPROVED
```

See the root README on `master` for the full handbook and documentation map.
