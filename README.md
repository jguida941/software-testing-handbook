# Software Testing Handbook – Vulnerable Version

> **Warning:** This branch intentionally contains vulnerable dependencies and insecure code for educational purposes. Do **not** deploy it to production systems.

## Branch Purpose
- Preserve the original `Module2.1` Spring Boot application with 162 known vulnerabilities
- Provide the intentionally flawed Python static-analysis example
- Serve as the "before" snapshot when comparing against `secure-version`

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
pylint static_analysis_example.py   # expect 22 issues
mypy static_analysis_example.py     # expect 1 issue
```

## Looking for the Fixes?
```bash
# Switch to the hardened implementation
git checkout secure-version
cd software-testing/java/Module2.1-IMPROVED
```

See the root README on `master` for the full handbook and documentation map.
