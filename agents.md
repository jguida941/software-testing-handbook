# Agents Guide

## Mission & Context
- This repository is an educational comparison between an intentionally vulnerable Spring Boot app and its remediated counterpart. Learners run scans, study findings, and review fixes.
- **Do not “fix” the vulnerable code on `master` or `vulnerable-version`.** All security improvements live on `secure-version`; the risky behavior is preserved on purpose for lab work.
- Before making changes, read `audit.md` for the latest review notes and open issues.

## Branch Map
- `master`: default branch; mirrors `vulnerable-version`. Contains Python static-analysis example plus the insecure Java Module2.1 project. Keep it vulnerable.
- `vulnerable-version`: archival copy of the same insecure code. Rarely touched.
- `secure-version`: hardened implementation (Module2.1-SECURE, extra docs, audit reports). Switch to this branch when you need to modify or inspect the secure sample.

## Workflow Expectations
1. **Determine intent first.** If the task is to analyze vulnerabilities, stay on `master`. If it is to adjust fixes or documentation for the secure build, use `secure-version`.
2. **Accessing secure files from another branch:** run `git show secure-version:path/to/file` instead of checking out branches unless explicitly asked.
3. **Scans/tests:**
   - Vulnerable sample: `cd software-testing/java/Module2.1 && ./mvnw clean compile dependency-check:check -DskipTests`
   - Secure sample: `cd software-testing/java/Module2.1-SECURE && mvn clean test && mvn dependency-check:check`
4. Generate dependency-check reports locally; they are ignored by Git. Mention this when referencing report paths.

## Known Constraints
- Dependency-Check auto-update is enabled everywhere now; first runs will download the NVD feeds (expect a delay). For offline labs run `./mvnw dependency-check:update-only` in each module before the main scan.
- The secure project’s security tests expect HTTPS headers; MockMvc calls must be marked `.secure(true)` or those assertions will fail.
- Module2.1-SECURE adds validation/security headers but still permits all requests. Documentation should never claim production-grade authn unless that changes.

## Documentation Pointers
- Overview: `README.md`
- Handbook docs: `software-testing/README.md` plus files under `software-testing/docs/`
- Vulnerable module details: `software-testing/java/Module2.1/README.md`
- Secure module details: `secure-version:software-testing/java/Module2.1-SECURE/README.md`
- Latest audit: `audit.md`

## When Updating Content
- Keep vulnerability counts and version numbers consistent across README files and reports.
- Call out whether commands require `secure-version` (e.g., Module2.1-SECURE directories do not exist on `master`).
- Preserve intentionally vulnerable examples but add warnings if clarity is needed.
