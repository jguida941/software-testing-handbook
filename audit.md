# Repository Audit Log — 2025-11-09

## Scope & Method
- Repository intentionally ships two flavors: `master`/`vulnerable-version` retain the insecure baseline for teaching, while `secure-version` demonstrates the remediated build. Audit respects that split—no fixes were applied to the vulnerable branch.
- Reviewed all documentation, source, and build assets on `master`.
- Inspected `secure-version` via `git show <branch>:<path>` to verify the secure implementation without modifying the working tree.
- Focused on accuracy of claims (vulnerability counts, commands, instructions), code-level security posture, and operational hygiene.

## Key Findings Snapshot
1. **Python static-analysis documentation is inaccurate** – the described issues do not exist in the checked-in code.
2. **Branch documentation disagrees on vulnerability counts and framework versions**, undermining trust in the comparison story.
3. **`Module2.1` intentionally retains exploitable SpEL injection and array bounds bugs**, but the README over-promises that the secure branch is “production ready” while core controls (authn/HSTS) are missing or misrepresented.
4. **Tooling was brittle out of the box** – dependency-check auto-update used to be disabled, causing fresh scans to fail until the CVE database was seeded. Auto-update is now enabled (2025‑11‑10) but keep the `.m2` artifact issue in mind.
5. **Secure test suite expects HTTPS-only headers over HTTP**, so `mvn test` will fail even though the README claims 40+ passing tests.

## Documentation Accuracy Gaps
- `software-testing/python/README.md:23` and `software-testing/python/README.md:47` claim the sample contains missing type hints, docstrings, and other lint failures, yet `software-testing/python/static_analysis_example.py:7`–`:31` already uses dataclasses, full annotations, and docstrings. Running pylint/mypy as instructed will report a clean file, so the exercise does not match its description.
- `software-testing/docs/testing-examples-index.md:14` and `software-testing/docs/testing-examples-index.md:48` repeat the same “~15 issues / type safety findings” story and even link to `../java/Module2.1/target/dependency-check-report.html` at `software-testing/docs/testing-examples-index.md:144`, but that report is not tracked. Readers need clarity that they must run the scan to generate the file.
- `software-testing/docs/vulnerability-analysis-report.md:17` states “~15 code quality issues” were found, again contradicting the pristine Python source; the same page references HTML/JSON reports at `software-testing/docs/vulnerability-analysis-report.md:28` that are absent from the repo.
- Vulnerability counts conflict:
  - Root README promises “162 vulnerabilities, 90 unique CVEs” at `README.md:58`.
  - The secure comparison report claims “96 unique CVEs” at `software-testing/docs/comparison-report.md:27`.
  - `secure-version` README says all **162+ vulnerabilities are reduced to zero** at `software-testing/java/Module2.1-SECURE/README.md:11`.
  - Both `secure-version` technical reports (`TECHNICAL-SECURITY-AUDIT-CORRECTED.md:9` and `SECURITY-AUDIT-FINAL-REPORT.md:48`) explicitly admit **10–15 High** findings remain.
  These inconsistencies make it impossible to cite a single authoritative metric.
- Version drift: the secure README advertises “Spring Boot 3.2.11” at `software-testing/java/Module2.1-SECURE/README.md:19` and the application banner repeats the same at `software-testing/java/Module2.1-SECURE/src/main/java/com/snhu/Module21/Application.java:14`, while the actual POM uses 3.3.5 at `secure-version:software-testing/java/Module2.1-SECURE/pom.xml:13`.
- The secure README guarantees “Strict-Transport-Security” headers on `http://` traffic at `software-testing/java/Module2.1-SECURE/README.md:139` and tells readers to expect them via plain `curl` at `software-testing/java/Module2.1-SECURE/README.md:149`, but Spring only emits HSTS over HTTPS, so the doc is misleading.

## Code & Security Review

### Module2.1 (master, intentionally vulnerable)
- `software-testing/java/Module2.1/src/main/java/com/snhu/Module21/GreetingController.java:21` instantiates a `SpelExpressionParser` and line `27` evaluates raw user input, enabling trivial RCE (e.g., `name=T(java.lang.Runtime)...`). Documented as intentional, but worth flagging for anyone who might accidentally run it.
- `software-testing/java/Module2.1/src/main/java/com/snhu/Module21/GreetingController.java:33` indexes a fixed-size array without validating `id`, so `/number/999` throws `ArrayIndexOutOfBoundsException`, leaking stack traces and enabling denial-of-service.
	- `software-testing/java/Module2.1/pom.xml:57`–`:59` now enables dependency-check auto-update so new users automatically download the NVD feeds; keep highlighting that initial run may take time. The committed resolver artifact at `software-testing/java/Module2.1/.m2-repo/.../spring-boot-starter-parent-2.2.4.RELEASE.pom.lastUpdated:4` still indicates past failures and should be removed.

### Module2.1-SECURE (secure-version branch)
- Positives: Uses Spring Boot 3.3.5 with Java 17 (`secure-version:software-testing/java/Module2.1-SECURE/pom.xml:13` & `:26`), adds bean validation for inputs (`secure-version:software-testing/java/Module2.1-SECURE/src/main/java/com/snhu/Module21/GreetingController.java:31`–`:65`) and security headers (`secure-version:software-testing/java/Module2.1-SECURE/src/main/java/com/snhu/Module21/config/SecurityConfig.java:40`–`:83`).
- Still, the filter chain allows all requests (`secure-version:software-testing/java/Module2.1-SECURE/src/main/java/com/snhu/Module21/config/SecurityConfig.java:35`–`:38`), so the README’s “production ready” promise at `README.md:74` / `software-testing/java/Module2.1-SECURE/README.md:16` needs the caveat that authentication/authorization is disabled.
- HSTS handling: `SecurityConfig` configures HSTS at `secure-version:software-testing/java/Module2.1-SECURE/src/main/java/com/snhu/Module21/config/SecurityConfig.java:72`, but Spring Security only sends that header on HTTPS requests. The test suite never marks requests as secure, so `secure-version:software-testing/java/Module2.1-SECURE/src/test/java/com/snhu/Module21/SecurityTests.java:225` will always fail. This contradicts the README’s “40+ tests pass” claim at `software-testing/java/Module2.1-SECURE/README.md:156`.
- Documentation vs tooling: the README insists `mvn dependency-check:check` “should show 0 high/critical” at `software-testing/java/Module2.1-SECURE/README.md:55`, yet both `TECHNICAL-SECURITY-AUDIT-CORRECTED.md:53` and `SECURITY-AUDIT-FINAL-REPORT.md:48` acknowledge residual High findings. The repo lacks any generated reports to prove either assertion.

## Operational & Repo Hygiene
- `.m2` artifacts should be removed (`software-testing/java/Module2.1/.m2-repo/...lastUpdated`). They expose developer machine metadata and do not belong in source control.
- Generated reports/logs referenced throughout the docs (`target/dependency-check-report.html`, log files) are ignored by Git, so readers cannot verify claims without rerunning the scans. Consider checking in redacted samples or at least stating explicitly that the files must be generated locally.

## Recommendations
1. **Align documentation with reality**: Update all Python/static-analysis guides and testing indexes to describe the actual sample (or introduce a purposely broken script). Pick a single authoritative CVE count and propagate it across `README.md`, `comparison-report.md`, and the secure README.
2. **Clarify secure-branch capabilities**: Note prominently that auth is disabled (`permitAll`) and that HSTS/security header expectations require HTTPS. Adjust `SecurityTests` (set `.secure(true)` or drop the assertion) so `mvn test` reflects reality.
3. **Improve tooling setup**: (Resolved 2025‑11‑10) dependency-check auto-update is now enabled in `software-testing/java/Module2.1/pom.xml:58`, but we still need to document the first-run download (done) and remove the committed `.m2` cache file.
4. **Provide evidence**: If citing “0 high/critical vulnerabilities,” include the corresponding dependency-check reports (even as screenshots or summarized tables) in version control so auditors can reproduce the numbers.
5. **Document branch-specific files** clearly: remind readers that secure-only docs (e.g., `software-testing/docs/vulnerability-fixes-guide.md`) live on `secure-version`, and ensure no empty directories (like `Module2.1-SECURE` containing only ignored build output) remain on `master` to confuse newcomers.

The combination of these fixes will make the educational narrative consistent, keep the secure sample trustworthy, and prevent false failures when users follow the documented commands.
