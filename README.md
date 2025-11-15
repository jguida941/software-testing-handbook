# Software Testing Handbook — Secure Branch

## ⚠️ Important Disclaimer
This repository intentionally contains vulnerable code for education. The `secure-version` branch (current) showcases the remediated implementation; `vulnerable-version` keeps the unsafe baseline for comparison. Never deploy the vulnerable branch outside an isolated lab.

---

## 1. What This Is
An educational security-audit project that demonstrates:
- **162+ real vulnerabilities** discovered via OWASP Dependency-Check
- **Systematic remediation**: dependency upgrades + code fixes
- **Before/after comparisons** to teach static vs dynamic testing

---

## 2. Branch Map
| Branch                  | Purpose                      | Key Assets                                                               |
|-------------------------|------------------------------|--------------------------------------------------------------------------|
| `master`                | Hub / overview               | Project summary, contributor guidance, links to branch READMEs           |
| `vulnerable-version`    | Intentionally vulnerable lab | `software-testing/java/Module2.1`, Python flawed sample                  |
| `secure-version` (here) | Hardened version + docs      | `software-testing/java/Module2.1-IMPROVED`, `scripts/`, reports & audits |

> Stay on `secure-version` for the improved app. Switch to `vulnerable-version` only when you need to inspect the insecure sample.

---

## 3. Quick Start
### Improved Module
```bash
git status -sb                     # confirm branch
cd software-testing/java/Module2.1-IMPROVED
mvn clean compile
mvn spring-boot:run
```
- Blocked payload: `curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"`
- Valid payload: `curl "http://localhost:8080/greeting?name=John"`

### Compare With Vulnerable Module
```bash
git checkout vulnerable-version
cd software-testing/java/Module2.1
./mvnw clean compile dependency-check:check -DskipTests
open target/dependency-check-report.html
```
Return via `git checkout secure-version`.

### Automation Script
```bash
export OSS_INDEX_USER="you@example.com"
export OSS_INDEX_TOKEN="oss-token"
./scripts/run_scans.sh
```
HTML/JSON reports saved to `software-testing/docs/reports/<timestamp>/`.

---

## 4. Documentation Hub
All previous markdown guides live in `archive/secure-version/…` for reference. Their content has been merged below:
- **Theory**: Static vs dynamic testing (from `static-dynamic-testing.md`)
- **Testing catalog**: Python + Java lab index (`testing-examples-index.md`)
- **Security analysis**: Vulnerability findings report (`vulnerability-analysis-report.md`)
- **Fix plan**: Complete remediation guide (`vulnerability-fixes-guide.md`)
- **Testing strategy**: Phase-by-phase validation plan (`testing-strategy.md`)
- **Status/Audits**: Honest risk snapshot & audit logs (status + audits folder)

Use this README as the single reference; consult `archive/secure-version/...` only if you need the historical wording.

---

## 5. Theory — Static vs Dynamic Testing
**Static testing** inspects artifacts without execution (reviews, linting, type checks). Tools: Pylint, Flake8, Mypy. Benefits: early defect detection, lower cost, strengthened standards.

**Dynamic testing** executes the software to observe runtime behaviour. Tools: JUnit/MockMvc, OWASP Dependency-Check, Selenium, curl probes. Benefits: reveals dependency CVEs, timing and integration bugs, confirms fixes actually work.

These approaches complement each other: static keeps defects out, dynamic proves the running system is secure.

---

## 6. Testing Examples Index
| Example                 | Branch             | Testing Type          | Tooling                            | Findings                                            |
|-------------------------|--------------------|-----------------------|------------------------------------|-----------------------------------------------------|
| Python static analysis  | secure-version     | Static                | `pylint`, `mypy`                   | 22 lint findings + 0 type errors in the flawed file |
| Java Module 2.1         | vulnerable-version | Dynamic security scan | OWASP Dependency-Check 11.0.0      | 162 vulns (21 CRIT / 69 HIGH / 69 MED / 3 LOW)      |
| Java Module2.1-IMPROVED | secure-version     | Hardened build        | Spring Boot 3.3.5 + security tests | 18 residual Tomcat CVEs (5 CRIT / 9 HIGH / 4 MED)   |

### Python Commands (verified)
```bash
cd software-testing/python
pip install -r requirements.txt
pylint static_analysis_example.py   # expect 22 findings
mypy static_analysis_example.py     # expect 0 (constructor fixed)
python static_analysis_example.py
pylint static_analysis_example_fixed.py
mypy static_analysis_example_fixed.py
```

### Java Vulnerable Scan (verified)
```bash
cd software-testing/java/Module2.1
./mvnw clean compile dependency-check:check -DskipTests
```
Outputs 162 findings and generates reports under `target/` (open HTML for details).

### Java Improved Scan + Tests (verified)
```bash
cd software-testing/java/Module2.1-IMPROVED
mvn clean test
mvn dependency-check:check    # fails build on CVSS ≥ 7 (expected: Tomcat CVEs)
```
> JDK 21+: set `export MAVEN_OPTS="--add-opens java.base/java.lang=ALL-UNNAMED -Djdk.attach.allowAttachSelf=true"` before `mvn test`.

---

## 7. Vulnerability Analysis Highlights
- Tool: OWASP Dependency-Check 11.0.0
- Vulnerable module results: **162** total (21 CRIT, 69 HIGH, 69 MED, 3 LOW) across ~90 unique CVEs.
- Most dangerous: CVE-2022-22965 (Spring4Shell), CVE-2022-1471 (SnakeYAML RCE), CVE-2020-1938 (Ghostcat), CVE-2017-8046 (Spring Data REST), custom SpEL injection, array bounds DoS.
- Secure module results: **18** remaining CVEs, all from tomcat-embed-core-10.1.31 (5 CRIT / 9 HIGH / 4 MED). No custom-code vulns remain.

---

## 8. Security Improvements Summary
| Component   | Before               | After                            | Impact                                            |
|-------------|----------------------|----------------------------------|---------------------------------------------------|
| Spring Boot | 2.2.4.RELEASE        | 3.3.5                            | Fixes 140+ CVEs, requires Java 17                 |
| Java        | 8                    | 17                               | Modern language + security features               |
| Tomcat      | 9.0.30               | 10.1.31                          | Removes Ghostcat; 18 residual CVEs until patched release |
| SnakeYAML   | 1.25                 | 2.2                              | Fixes RCE (CVE-2022-1471)                         |
| Jackson     | 2.10.2               | 2.17.2                           | Fixes XXE + DoS                                   |
| Custom code | SpEL RCE & array DoS | Validated inputs, bounded arrays | Blocks runtime exploits                           |

---

## 9. Testing & Validation Plan
| Phase | Goal                     | Commands                                    | Expected Result                                                  |
|-------|--------------------------|---------------------------------------------|------------------------------------------------------------------|
| 1     | Dependency Scan          | `mvn dependency-check:check` (both modules) | Vulnerable: 162 findings; Secure: 18 (all Tomcat CVEs; build fails intentionally) |
| 2     | Automated security tests | `mvn test -Dtest=SecurityTests`             | All injection/validation tests pass                              |
| 3     | Manual probes            | curl payloads listed below                  | Secure module returns 400; vulnerable executes/throws            |
| 4     | Header verification      | `curl -I http://localhost:8080/greeting`    | All headers except HSTS on plain HTTP                            |
| 5     | Regression               | `mvn clean test`                            | 43 tests pass                                                    |

Manual payloads:
```bash
curl "http://localhost:8080/greeting?name=T(java.lang.System).getProperty('user.home')"   # 400
curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')" # 400
curl "http://localhost:8080/number/-1"    # 400
curl "http://localhost:8080/number/3"     # OK
```
ng t
---

## 10. Automation & OSS Index Setup
1. Create token at <https://ossindex.sonatype.org> → Profile → API Token.
2. Export credentials:
   ```bash
   export OSS_INDEX_USER="name@example.com"
   export OSS_INDEX_TOKEN="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
   ```
3. Run combined scans:
   ```bash
   ./scripts/run_scans.sh
   ```
   - Scans both modules.
   - Stores HTML/JSON reports under `software-testing/docs/reports/<timestamp>/`.
4. Troubleshooting:
   - Missing creds → script exits early.
   - First run downloads ~200 MB NVD DB. Use `dependency-check:update-only` to prefetch if offline.
   - Reports are gitignored; copy relevant ones into docs/reports when needed.

---

## 11. Honest Security Status (Nov 2025)
| Metric      | Vulnerable | Improved           |
|-------------|------------|--------------------|
| Total vulns | 162        | 18                 |
| Critical    | 21         | 5 (Tomcat 10.1.31) |
| High        | 69         | 9                  |
| Medium      | 69         | 4                  |
| Low         | 3          | 0                  |

Residual risk: Spring Boot 3.3.5 still ships Tomcat 10.1.31, which currently carries 18 open CVEs (5 CRIT / 9 HIGH / 4 MED). Monitor Spring Boot release notes and upgrade once a patched 10.1.x becomes available, or override Tomcat in `pom.xml` and re-run the full regression suite.

---

## 12. Warning About the Vulnerable Branch
- ⚠️ Contains 162+ known vulnerabilities (Spring4Shell, SnakeYAML RCE, Ghostcat, SpEL injection, array DoS).
- Run only in isolated environments (VM, Docker, disabled networking). Consider any host compromised after executing it.
- Example exploit: `curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"` will execute code on the vulnerable branch.

---

## 13. Audit Snapshot
- **Final Security Audit (Nov 9, 2025):** Verified dependency scan reduction 162 → 18; documented commands to reproduce results.
- **Technical Audit – Corrected (Nov 9, 2025):** Recorded actual dependency versions (Spring Boot 3.3.5, Tomcat 10.1.31, SnakeYAML 2.2) and code fixes.
- **Repository Audit Log (Nov 9–10, 2025):** Captured documentation fixes, testing expectations, .gitignore cleanup, and warnings about “zero CVEs” claims.

Full text for each report remains in `archive/secure-version/software-testing/docs/audits/`.

---

## 14. Reference Commands
| Task                     | Command                                                                                                                                 |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| List branches            | `git branch -a`                                                                                                                         |
| Switch to secure branch  | `git checkout secure-version`                                                                                                           |
| Run vulnerable scan      | `git checkout vulnerable-version && cd software-testing/java/Module2.1 && ./mvnw clean compile dependency-check:check -DskipTests`      |
| Run secure tests         | `cd software-testing/java/Module2.1-IMPROVED && mvn clean test`                                                                         |
| Run secure scan          | `cd software-testing/java/Module2.1-IMPROVED && mvn dependency-check:check`                                                             |
| Python lint / type check | `cd software-testing/python && pip install -r requirements.txt && pylint static_analysis_example.py && mypy static_analysis_example.py` |
| Generate both reports    | `./scripts/run_scans.sh`                                                                                                                |

---

## 15. Maintenance Rules
1. Keep this README as the single source of truth for the secure branch.
2. Archive legacy markdown files before deletion (`archive/secure-version/...`).
3. Update the vulnerability counts and residual-risk table whenever scans change.
4. Note branch requirements before any command block so readers know where to run it.
5. Preserve `software-testing/docs/reports/` for generated evidence.

---

## 16. Appendices
### A. Attack vs Defense (Vulnerable vs Secure)
| Payload                                  | Vulnerable Result                                | Secure Result                                                                                 |
|------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `/greeting?name=T(java.lang.Runtime)...` | Executes arbitrary code                          | 400 Bad Request                                                                               |
| `/number/999`                            | ArrayIndexOutOfBoundsException, stack trace leak | 400 Bad Request                                                                               |
| Dependency-Check                         | 162 findings                                     | 18 findings (Tomcat only)                                                                     |
| Security headers                         | Missing                                          | X-Content-Type-Options, X-Frame-Options, X-XSS-Protection, CSP, Referrer-Policy, HSTS (HTTPS) |

### B. Dependency Upgrade Checklist
- Update Spring Boot BOM, Java version, Tomcat, SnakeYAML, Jackson.
- Enable OWASP Dependency-Check auto-update and fail build on CVSS ≥ 7.
- Add Bean Validation + explicit checks for user inputs.
- Configure Spring Security headers.
- Remove devtools and other insecure dependencies from production builds.

### C. Evidence Locations
| Artifact                           | Location                                               |
|------------------------------------|--------------------------------------------------------|
| Dependency-Check HTML/JSON reports | `software-testing/docs/reports/<timestamp>/`           |
| Audit PDFs/Markdown                | `archive/secure-version/software-testing/docs/audits/` |
| Archived READMEs                   | `archive/secure-version/**`                            |

---
Updated: November 2025 (secure README reconstruction)
