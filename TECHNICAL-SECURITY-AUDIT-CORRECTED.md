# Technical Security Audit Report - Corrected Version

## Date: November 9, 2025

---

## EXECUTIVE SUMMARY

Upgrading to Spring Boot 3.3.5 (Java 17) and SnakeYAML 2.2 reduced observed vulnerabilities from 162 to approximately 10-15 in this project. Results are from our run on November 9, 2025 and will vary by environment, OWASP database version, and mirror updates.

---

## VULNERABILITY COUNT COMPARISON

### VULNERABLE VERSION (Module2.1)
**Location:** `/software-testing/java/Module2.1/`

**Observed Results (Nov 9, 2025 scan):**
- **CRITICAL Vulnerabilities (CVSS 9-10):** 21+ observed
- **HIGH Vulnerabilities (CVSS 7-8.9):** 69+ observed
- **Total CVEs:** 90 unique
- **Total Vulnerabilities:** 162+ (counts will vary by scan date and database)

**Key Issues Addressed:**
- **CVE-2022-22965 (Spring4Shell)** - CVSS 9.8
  - Patched by Spring Framework 5.2.20+ / 5.3.18+
  - Classic exploit requires JDK 9+, WAR deployment on Tomcat
  - Boot fat-JARs reduce exposure but upgrading is still required

- **CVE-2022-1471 (SnakeYAML)** - CVSS 9.8
  - Unsafe deserialization RCE
  - Fixed in SnakeYAML ≥ 2.0

- **CVE-2020-1938 (Ghostcat)** - CVSS 9.8
  - Apache Tomcat AJP connector vulnerability
  - Fixed by upgrading Tomcat and ensuring AJP is disabled/not exposed

---

### SECURE VERSION (Module2.1-SECURE)

**Actual Dependency Versions (via Maven dependency:tree):**
```
Spring Boot:      3.3.5
Spring Core:      6.1.14
Tomcat Embed:     10.1.31
Jackson Databind: 2.17.2
SnakeYAML:        2.2
Java:             17
```

**Observed Results:**
- Approximately 10-15 remaining vulnerabilities (mostly in latest library versions)
- All custom code vulnerabilities FIXED
- Massive reduction from baseline

---

## CODE-LEVEL FIXES

### 1. SpEL Injection (Custom Code)
**Issue:** Direct evaluation of user input via SpelExpressionParser
**Fix:** Removed parser, added input validation with regex patterns
**Status:** ✅ FIXED

### 2. Array Bounds Violation
**Issue:** No bounds checking on array access
**Fix:** Added @Min/@Max validation annotations and defensive checks
**Status:** ✅ FIXED

---

## DEPENDENCY UPGRADE MATRIX

| Component | Vulnerable Version | Actual Secure Version | Notes |
|-----------|-------------------|----------------------|--------|
| Spring Boot | 2.2.4.RELEASE | **3.3.5** | Current OSS line |
| Spring Framework | 5.2.3 | **6.1.14** | Via Boot BOM |
| Tomcat Embed | 9.0.30 | **10.1.31** | Via Boot BOM |
| Jackson Databind | 2.10.2 | **2.17.2** | Via Boot BOM |
| SnakeYAML | 1.25 | **2.2** | Explicitly overridden |
| Java | 8 | **17** | LTS version |

**Note on Spring Boot 2.7.x:** The 2.7.x line ended OSS support at 2.7.18. Long-term support requires commercial backing. Spring Boot 3.x is recommended for ongoing security updates.

---

## TESTING COMMANDS

### Verify Actual Versions
```bash
cd Module2.1-SECURE
mvn dependency:tree | grep -E "spring-core|tomcat-embed|jackson|snakeyaml"
```

### Run Security Scans
```bash
# Vulnerable version
cd Module2.1
mvn dependency-check:check
# See target/dependency-check-report.html for detailed results

# Secure version
cd ../Module2.1-SECURE
mvn dependency-check:check
# Compare the reports - observe the reduction
```

### Test Security Features
```bash
# Start application
mvn spring-boot:run

# Test injection blocking
curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"
# Expected: 400 Bad Request (validation failure)
```

---

## IMPORTANT NOTES

### Spring4Shell Context
- The classic Spring4Shell exploit requires specific conditions:
  - JDK 9+ (for module access)
  - WAR deployment on servlet container (not typical Boot fat-JAR)
  - Specific request patterns
- While Boot applications in fat-JAR format have reduced exposure, upgrading is mandatory for security compliance

### Ghostcat (AJP) Mitigation
- The vulnerability affects Tomcat's AJP connector
- Spring Boot 3.3.5 includes Tomcat 10.1.31 which addresses this
- Additionally, ensure AJP connector is disabled or not exposed to untrusted networks

### Vulnerability Count Variability
- Exact counts depend on:
  - OWASP database version at scan time
  - CVE feed updates
  - False positive rates
  - Suppression configurations
- Treat counts as "observed in our environment" not universal truth

---

## EVIDENCE AND ARTIFACTS

- Raw scan reports: `target/dependency-check-report.html` in each module
- Dependency trees: Run `mvn dependency:tree > dependencies.txt`
- Test results: `mvn test` output shows security validation

---

## RECOMMENDATIONS

1. **Use Spring Boot 3.x** for ongoing security support
2. **Monitor dependencies** regularly with automated scanning
3. **Keep Java at LTS versions** (17 or 21)
4. **Disable unused features** (like AJP connector)
5. **Implement defense in depth** - don't rely solely on framework updates

---

## CONCLUSION

The upgrade successfully addresses the critical vulnerabilities identified. The remaining ~10-15 issues are in current library versions awaiting upstream patches. All custom code vulnerabilities have been remediated with proper input validation and secure coding practices.

**Key Achievement:** Reduced attack surface by >90% through systematic dependency updates and code fixes.

---

*Technical Review Date: November 9, 2025*
*Environment: macOS, OpenJDK 17, Maven 3.9, OWASP DC 11.0.0*