# Comprehensive Testing Strategy for Security Vulnerability Fixes

## Overview

This document provides a complete testing strategy to verify that all 162+ security vulnerabilities have been successfully remediated. It serves both **educational purposes** (teaching security testing) and **audit requirements** (proving fixes work).

---

## Table of Contents
1. [Testing Phases](#testing-phases)
2. [Pre-Testing Setup](#pre-testing-setup)
3. [Phase 1: Dependency Vulnerability Testing](#phase-1-dependency-vulnerability-testing)
4. [Phase 2: Code Vulnerability Testing](#phase-2-code-vulnerability-testing)
5. [Phase 3: Security Header Verification](#phase-3-security-header-verification)
6. [Phase 4: Penetration Testing](#phase-4-penetration-testing)
7. [Phase 5: Automated Test Suite](#phase-5-automated-test-suite)
8. [Test Results Documentation](#test-results-documentation)

---

## Testing Phases

| Phase | Focus | Tools | Expected Outcome |
|-------|-------|-------|------------------|
| 1 | Dependency Vulnerabilities | OWASP DC | 0 HIGH/CRITICAL |
| 2 | Code Vulnerabilities | Manual/Automated | All injections blocked |
| 3 | Security Headers | curl, browser | All headers present |
| 4 | Penetration Testing | Custom scripts | All attacks fail |
| 5 | Automated Tests | JUnit/Maven | 100% pass rate |

---

## Pre-Testing Setup

### Environment Preparation
```bash
# 1. Ensure Java 17 is installed (for secure version)
java -version
# Expected: openjdk version "17.x.x"

# 2. Ensure Maven is available
mvn -version
# Expected: Apache Maven 3.x.x

# 3. Clone or navigate to project
cd /Users/jguida941/new_github_projects/software-testing-handbook

# 4. Ensure both versions exist
ls -la software-testing/java/
# Should show: Module2.1/ and Module2.1-SECURE/
```

### Build Both Versions
```bash
# Build vulnerable version (for comparison)
cd software-testing/java/Module2.1
mvn clean compile

# Build secure version
cd ../Module2.1-SECURE
mvn clean compile
```

---

## Phase 1: Dependency Vulnerability Testing

### Objective
Verify that all 162 dependency vulnerabilities are fixed.

### Test 1.1: Baseline Vulnerability Scan (Vulnerable Version)
```bash
cd software-testing/java/Module2.1
mvn dependency-check:check

# Examine report
open target/dependency-check-report.html
# OR
grep -c "severity.*CRITICAL\|HIGH" target/dependency-check-report.html
```

**Expected Result**:
- 90+ HIGH/CRITICAL vulnerabilities
- 162 total vulnerabilities

### Test 1.2: Secure Version Scan
```bash
cd ../Module2.1-SECURE
mvn dependency-check:check

# Check for remaining vulnerabilities
grep -c "severity.*CRITICAL\|HIGH" target/dependency-check-report.html
```

**Expected Result**:
- 0 CRITICAL vulnerabilities
- 0 HIGH vulnerabilities
- Only LOW severity (if any) acceptable

### Test 1.3: Dependency Tree Comparison
```bash
# Generate dependency trees
cd ../Module2.1
mvn dependency:tree > /tmp/vulnerable-deps.txt

cd ../Module2.1-SECURE
mvn dependency:tree > /tmp/secure-deps.txt

# Compare versions
diff /tmp/vulnerable-deps.txt /tmp/secure-deps.txt | head -50
```

**Verify**:
- Spring Boot: 2.2.4 → 3.2.11
- Tomcat: 9.0.30 → 10.1.33
- SnakeYAML: 1.25 → 2.2

---

## Phase 2: Code Vulnerability Testing

### Test 2.1: SpEL Injection Prevention

#### Start the Applications
```bash
# Terminal 1 - Vulnerable version (DO NOT RUN IN PRODUCTION)
cd software-testing/java/Module2.1
mvn spring-boot:run
# Runs on port 8080

# Terminal 2 - Secure version
cd software-testing/java/Module2.1-SECURE
mvn spring-boot:run
# Also on 8080 (run one at a time)
```

#### Test SpEL Injection Attempts
```bash
# Test 1: System property access attempt
curl "http://localhost:8080/greeting?name=T(java.lang.System).getProperty('user.home')"

# Vulnerable version: Returns system property in response
# Secure version: Returns 400 Bad Request

# Test 2: Runtime execution attempt
curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"

# Vulnerable version: May execute command
# Secure version: Returns 400 Bad Request

# Test 3: Class loading attempt
curl "http://localhost:8080/greeting?name=T(java.lang.Class).forName('java.lang.Runtime')"

# Vulnerable version: Processes expression
# Secure version: Returns 400 Bad Request
```

### Test 2.2: Array Bounds Protection

```bash
# Test 1: Negative index
curl "http://localhost:8080/number/-1"

# Vulnerable: 500 Internal Server Error (ArrayIndexOutOfBoundsException)
# Secure: 400 Bad Request

# Test 2: Out of bounds positive
curl "http://localhost:8080/number/999"

# Vulnerable: 500 Internal Server Error
# Secure: 400 Bad Request

# Test 3: Valid boundary
curl "http://localhost:8080/number/6"

# Both: Should work (last valid index)
```

---

## Phase 3: Security Header Verification

### Test 3.1: Check Security Headers
```bash
# Get all headers from secure version
curl -I http://localhost:8080/greeting

# Expected headers:
# X-Content-Type-Options: nosniff
# X-Frame-Options: DENY
# X-XSS-Protection: 1; mode=block
# Content-Security-Policy: [policy]
# Referrer-Policy: strict-origin-when-cross-origin
# Strict-Transport-Security: max-age=31536000
```

### Test 3.2: Automated Header Check Script
```bash
#!/bin/bash
echo "Checking Security Headers..."

HEADERS=$(curl -sI http://localhost:8080/greeting)

check_header() {
    echo "$HEADERS" | grep -q "$1" && echo "✅ $1 present" || echo "❌ $1 MISSING"
}

check_header "X-Content-Type-Options"
check_header "X-Frame-Options"
check_header "X-XSS-Protection"
check_header "Content-Security-Policy"
check_header "Referrer-Policy"
check_header "Strict-Transport-Security"
```

---

## Phase 4: Penetration Testing

### Test 4.1: Injection Attack Suite
Create file `security-tests.sh`:

```bash
#!/bin/bash
BASE_URL="http://localhost:8080"
FAILED=0
PASSED=0

test_payload() {
    NAME="$1"
    PAYLOAD="$2"
    EXPECTED="$3"

    RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/greeting?name=$PAYLOAD")

    if [ "$RESPONSE" == "$EXPECTED" ]; then
        echo "✅ PASS: $NAME (Got $RESPONSE)"
        ((PASSED++))
    else
        echo "❌ FAIL: $NAME (Expected $EXPECTED, Got $RESPONSE)"
        ((FAILED++))
    fi
}

echo "=== Security Penetration Tests ==="

# SpEL Injections
test_payload "SpEL Runtime.exec" "T(java.lang.Runtime).getRuntime().exec('calc')" "400"
test_payload "SpEL System Property" "T(java.lang.System).getProperty('user.dir')" "400"
test_payload "SpEL Expression" "\${7*7}" "400"

# SQL Injection
test_payload "SQL OR Attack" "admin'+OR+'1'='1" "400"
test_payload "SQL Comment" "admin--" "400"

# XSS Attempts
test_payload "Script Tag" "<script>alert('XSS')</script>" "400"
test_payload "Event Handler" "<img+src=x+onerror=alert(1)>" "400"

# Command Injection
test_payload "Pipe Command" "test+|+ls+-la" "400"
test_payload "Semicolon Command" "test;+rm+-rf+/" "400"

# Path Traversal
test_payload "Path Traversal" "../../../etc/passwd" "400"

echo "=== Results ==="
echo "Passed: $PASSED"
echo "Failed: $FAILED"

[ $FAILED -eq 0 ] && echo "✅ ALL SECURITY TESTS PASSED!" || echo "❌ SECURITY ISSUES DETECTED!"
```

Run: `bash security-tests.sh`

### Test 4.2: Fuzzing Test
```bash
# Install fuzzing wordlist if needed
# Use SecLists or similar

# Basic fuzzing with common payloads
for payload in $(cat /path/to/fuzzing-wordlist.txt); do
    response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8080/greeting?name=$payload")
    if [ "$response" != "400" ] && [ "$response" != "200" ]; then
        echo "Unexpected response $response for payload: $payload"
    fi
done
```

---

## Phase 5: Automated Test Suite

### Test 5.1: Run All Unit Tests
```bash
cd software-testing/java/Module2.1-SECURE
mvn clean test

# Expected output:
# Tests run: 40+, Failures: 0, Errors: 0, Skipped: 0
```

### Test 5.2: Run Security-Specific Tests
```bash
# Run only security tests
mvn test -Dtest=SecurityTests

# Expected: All 30+ security tests pass
```

### Test 5.3: Run With Coverage
```bash
# Add JaCoCo for coverage
mvn clean test jacoco:report

# Check coverage
open target/site/jacoco/index.html
# Expected: >80% code coverage
```

### Test 5.4: Integration Tests
```bash
# Full integration test
mvn clean verify

# This runs:
# - Unit tests
# - Integration tests
# - OWASP dependency check
# - Any configured security scanners
```

---

## Test Results Documentation

### Generate Test Report
```bash
#!/bin/bash
# generate-test-report.sh

echo "# Security Test Results Report" > test-results.md
echo "## Date: $(date)" >> test-results.md
echo "" >> test-results.md

echo "### Dependency Scan Results" >> test-results.md
echo "\`\`\`" >> test-results.md
cd Module2.1-SECURE
mvn dependency-check:check 2>&1 | grep -A 5 "One or more dependencies"
echo "\`\`\`" >> test-results.md

echo "### Unit Test Results" >> test-results.md
echo "\`\`\`" >> test-results.md
mvn test 2>&1 | grep "Tests run:"
echo "\`\`\`" >> test-results.md

echo "### Security Test Results" >> test-results.md
echo "\`\`\`" >> test-results.md
mvn test -Dtest=SecurityTests 2>&1 | grep "Tests run:"
echo "\`\`\`" >> test-results.md

echo "Report generated: test-results.md"
```

### Success Criteria Checklist

- [ ] **Dependency Vulnerabilities**
  - [ ] 0 CRITICAL vulnerabilities in OWASP scan
  - [ ] 0 HIGH vulnerabilities in OWASP scan
  - [ ] Dependency versions match requirements

- [ ] **Code Vulnerabilities**
  - [ ] SpEL injection attempts return 400
  - [ ] Array bounds violations return 400
  - [ ] No stack traces exposed

- [ ] **Security Headers**
  - [ ] X-Content-Type-Options present
  - [ ] X-Frame-Options present
  - [ ] Content-Security-Policy present
  - [ ] All 6+ security headers configured

- [ ] **Test Coverage**
  - [ ] All unit tests pass
  - [ ] All security tests pass
  - [ ] Integration tests pass
  - [ ] >80% code coverage

- [ ] **Penetration Testing**
  - [ ] All injection attempts blocked
  - [ ] No unexpected error responses
  - [ ] Fuzzing reveals no issues

---

## Continuous Testing Strategy

### CI/CD Integration
```yaml
# .github/workflows/security.yml
name: Security Tests
on: [push, pull_request]

jobs:
  security-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-java@v2
        with:
          java-version: '17'

      - name: Run OWASP Dependency Check
        run: |
          cd Module2.1-SECURE
          mvn dependency-check:check

      - name: Run Security Tests
        run: |
          cd Module2.1-SECURE
          mvn test -Dtest=SecurityTests

      - name: Check for vulnerabilities
        run: |
          if grep -q "CRITICAL\|HIGH" target/dependency-check-report.html; then
            echo "Security vulnerabilities found!"
            exit 1
          fi
```

### Scheduled Scanning
```bash
# Cron job for daily security scan
0 2 * * * cd /path/to/Module2.1-SECURE && mvn dependency-check:check
```

---

## Troubleshooting

### Common Issues and Solutions

1. **Port Already in Use**
   ```bash
   # Find process using port 8080
   lsof -i :8080
   # Kill process
   kill -9 <PID>
   ```

2. **Java Version Mismatch**
   ```bash
   # Secure version needs Java 17
   export JAVA_HOME=/path/to/java17
   ```

3. **Maven Build Failures**
   ```bash
   # Clean Maven cache
   mvn dependency:purge-local-repository
   ```

4. **OWASP Database Update**
   ```bash
   # Force database update
   mvn dependency-check:update-only
   ```

---

## Conclusion

This comprehensive testing strategy ensures:
- All 162 vulnerabilities are verified as fixed
- Security improvements are measurable
- Fixes are properly implemented
- No regressions occur
- Compliance requirements are met

Regular execution of these tests maintains security posture and provides audit trail documentation.