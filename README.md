# Software Testing Handbook: Vulnerable Version
<!-- Badge splash (vulnerable-version) -->
<p align="left">
  <img src="https://img.shields.io/badge/branch-vulnerable--version-red?style=flat-square" alt="Branch">
  <img src="https://img.shields.io/badge/Vulnerabilities-162-red?style=flat-square" alt="Total vulns">
  <img src="https://img.shields.io/badge/Critical-21-red?style=flat-square" alt="Critical">
  <img src="https://img.shields.io/badge/High-69-orange?style=flat-square" alt="High">
  <img src="https://img.shields.io/badge/Medium-69-yellow?style=flat-square" alt="Medium">
  <img src="https://img.shields.io/badge/Low-3-lightgrey?style=flat-square" alt="Low">
  <img src="https://img.shields.io/badge/Spring%20Boot-2.2.4-inactive?style=flat-square&logo=springboot" alt="Spring Boot">
  <img src="https://img.shields.io/badge/Java-8-blue?style=flat-square&logo=openjdk" alt="Java">
  <img src="https://img.shields.io/badge/Tomcat-9.0.30-lightgrey?style=flat-square&logo=apachetomcat" alt="Tomcat">
</p>

> ##### **⚠️ WARNING:** This branch intentionally contains vulnerable dependencies and insecure code for educational purposes. Do **NOT** deploy to production!

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
