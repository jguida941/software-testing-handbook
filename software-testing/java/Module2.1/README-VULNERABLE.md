# ⚠️ WARNING: VULNERABLE APPLICATION ⚠️

## 🚨 CRITICAL SECURITY NOTICE 🚨

**This application contains 162+ KNOWN SECURITY VULNERABILITIES and is FOR EDUCATIONAL PURPOSES ONLY!**

---

## DO NOT USE IN PRODUCTION

This version of the application is **INTENTIONALLY VULNERABLE** and contains:

- **21 CRITICAL vulnerabilities** (CVSS 9-10)
- **69 HIGH severity vulnerabilities** (CVSS 7-8.9)
- **69 MEDIUM severity vulnerabilities** (CVSS 4-6.9)
- **3 LOW severity vulnerabilities** (CVSS 0-3.9)
- **2 Code-level vulnerabilities** (SpEL Injection & Array Bounds)

### Most Dangerous Vulnerabilities:
1. **CVE-2022-22965 (Spring4Shell)** - Remote Code Execution
2. **SpEL Injection** - Direct code execution from user input
3. **CVE-2022-1471** - SnakeYAML deserialization RCE
4. **CVE-2020-1938 (Ghostcat)** - Apache Tomcat file read/RCE

---

## Purpose

This vulnerable version exists ONLY for:
- 📚 **Educational demonstrations** of security vulnerabilities
- 🔍 **Security testing tool validation**
- 🎓 **Training on vulnerability identification**
- 📊 **Comparison with the secure version**

---

## Safe Alternative Available

✅ **USE THE SECURE VERSION INSTEAD**: `Module2.1-SECURE/`

The secure version has:
- All 162 vulnerabilities fixed
- Modern dependencies (Spring Boot 3.2.11)
- Security headers configured
- Input validation implemented
- Comprehensive security tests

---

## If You Must Run This Version

### ⚠️ Safety Precautions:

1. **NEVER expose to the internet**
2. **Run only in isolated environments**:
   - Use Docker with `--network none`
   - Run in a VM with network disabled
   - Use only on localhost

3. **Limit execution time**:
   ```bash
   # Auto-terminate after 5 minutes
   timeout 300 mvn spring-boot:run
   ```

4. **Monitor for exploitation**:
   - Check logs for suspicious activity
   - Monitor system processes
   - Watch for unexpected network connections

---

## Known Attack Vectors

### 1. Remote Code Execution via SpEL
```bash
# THIS WILL EXECUTE CODE - DO NOT RUN ON IMPORTANT SYSTEMS
curl "http://localhost:8080/greeting?name=T(java.lang.Runtime).getRuntime().exec('calc')"
```

### 2. System Information Disclosure
```bash
# Leaks system properties
curl "http://localhost:8080/greeting?name=T(java.lang.System).getProperty('user.home')"
```

### 3. Application Crash (DoS)
```bash
# Causes ArrayIndexOutOfBoundsException
curl "http://localhost:8080/number/999"
```

---

## How to Test Safely

### Option 1: Use Docker (Recommended)
```dockerfile
FROM openjdk:8-jdk-alpine
COPY . /app
WORKDIR /app
# Disable network for safety
RUN addgroup -g 1000 -S appuser && adduser -u 1000 -S appuser -G appuser
USER appuser
CMD ["timeout", "300", "mvn", "spring-boot:run"]
```

### Option 2: Use the Secure Version
```bash
cd ../Module2.1-SECURE
mvn spring-boot:run
```

---

## Vulnerability Report

Full vulnerability report available in:
- Original documentation: `README.md`
- OWASP scan results: `target/dependency-check-report.html`
- Comparison report: `../../docs/comparison-report.md`

---

## Legal Disclaimer

**By running this application, you acknowledge:**
- This software is PROVIDED AS-IS for educational purposes
- You assume ALL RISKS associated with running vulnerable software
- The authors are NOT responsible for any damage or security breaches
- You will NOT use this for any malicious purposes
- You will NOT expose this to any network without proper authorization

---

## Educational Resources

To learn about fixing these vulnerabilities:
1. Review the secure version: `Module2.1-SECURE/`
2. Read the fix documentation: `../../docs/vulnerability-fixes-guide.md`
3. Study the testing strategy: `../../docs/testing-strategy.md`
4. Compare versions: `../../docs/comparison-report.md`

---

## Contact

If you accidentally exposed this application or suspect compromise:
1. Immediately terminate the application
2. Review system logs for suspicious activity
3. Consider the system compromised
4. Report to your security team

---

**Remember: Security is everyone's responsibility. Use this vulnerable version responsibly and ONLY for learning!**

---

*Last Updated: 2025-11-09*
*Vulnerable Version: 0.0.1-SNAPSHOT*
*Secure Alternative: Module2.1-SECURE v1.0.0*