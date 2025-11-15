# Module 2.1: Spring Boot Application Security Analysis

## Executive Summary

This module demonstrates **dynamic security testing** in action, showcasing how modern dependency scanning tools can uncover critical vulnerabilities that traditional static code analysis would miss. Using OWASP Dependency-Check, we discovered **162 vulnerabilities** including **21 CRITICAL** severity issues in a typical Spring Boot application.

### Key Findings at a Glance
- **90 unique CVEs** identified, including actively exploited vulnerabilities
- **Spring4Shell (CVE-2022-22965)** - Remote code execution vulnerability
- **Ghostcat (CVE-2020-1938)** - Apache Tomcat file read/RCE vulnerability
- **SnakeYAML (CVE-2022-1471)** - Deserialization leading to RCE
- **91 HIGH/CRITICAL** vulnerabilities requiring immediate attention

### Learning Outcomes
This example teaches:
1. **Why Dynamic Testing Matters**: Static analysis alone would not detect these third-party dependency vulnerabilities
2. **Real Security Impact**: These are not theoretical issues—they're actively exploited in the wild
3. **Practical Remediation**: How to fix vulnerabilities through dependency updates and configuration changes

### Connection to Testing Concepts
This module exemplifies [dynamic testing](../../docs/static-dynamic-testing.md) by:
- Analyzing runtime dependencies rather than source code
- Discovering vulnerabilities that only manifest during execution
- Demonstrating the complementary nature of static and dynamic approaches



## Project Overview
This is a Spring Boot 2.2.4 application configured with OWASP Dependency-Check for vulnerability scanning. The project demonstrates security vulnerability detection in Java dependencies through dynamic analysis.

## OWASP Dependency-Check Setup and Execution

### Prerequisites
- Java 8 or higher installed
- Maven (project includes Maven wrapper, so global installation not required)
- Internet connection (for initial plugin download)

### Configuration
The OWASP Dependency-Check plugin is already configured in `pom.xml`:

```xml
<plugin>
    <groupId>org.owasp</groupId>
    <artifactId>dependency-check-maven</artifactId>
    <version>11.0.0</version>
    <configuration>
        <failOnError>false</failOnError>
        <autoUpdate>false</autoUpdate>
        <nvdApiKey></nvdApiKey>
        <formats>
            <format>HTML</format>
            <format>JSON</format>
        </formats>
        <suppressionFiles>
            <suppressionFile>suppression.xml</suppressionFile>
        </suppressionFiles>
        <skipSystemScope>true</skipSystemScope>
        <skipTestScope>false</skipTestScope>
        <skipProvidedScope>false</skipProvidedScope>
        <skipRuntimeScope>false</skipRuntimeScope>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>aggregate</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### Running the Security Scan

#### Step 1: Navigate to the project directory
```bash
cd software-testing/java/Module2.1
```

#### Step 2: Run the dependency check
```bash
# Clean build and run dependency check (recommended)
./mvnw clean compile dependency-check:check -DskipTests

# Or if you want to run tests as well
./mvnw clean verify dependency-check:aggregate
```

#### Step 3: View the reports
The scan generates reports in the `target` directory:
- **HTML Report**: `target/dependency-check-report.html` (human-readable)
- **JSON Report**: `target/dependency-check-report.json` (machine-readable)

Open the HTML report in a browser:
```bash
open target/dependency-check-report.html
```

## Scan Results Summary (November 9, 2025)

### Statistics
- **Total Vulnerabilities Found**: 162 (across 90 unique CVEs)
- **Report Size**: 2.4MB (HTML), 1.6MB (JSON)
- **OWASP DC Version**: 11.0.0
- **NVD Database Version**: 11.0 (from November 5, 2025)

### Vulnerability Severity Distribution
| Severity | Count | Percentage |
|----------|-------|------------|
| **CRITICAL** | 21 | 13% |
| **HIGH** | 69 | 42.6% |
| **MEDIUM** | 69 | 42.6% |
| **LOW** | 3 | 1.8% |
| **TOTAL** | **162** | 100% |

### Most Vulnerable Dependencies
| Library | Vulnerabilities | Risk Level |
|---------|----------------|------------|
| tomcat-embed-websocket-9.0.30.jar | 46 | CRITICAL |
| tomcat-embed-core-9.0.30.jar | 45 | CRITICAL |
| spring-web-5.2.3.RELEASE.jar | 13 | HIGH |
| spring-core-5.2.3.RELEASE.jar | 12 | HIGH |
| spring-webmvc-5.2.3.RELEASE.jar | 12 | HIGH |
| snakeyaml-1.25.jar | 8 | CRITICAL |
| jackson-databind-2.10.2.jar | 6 | HIGH |
| spring-data-rest-webmvc-2.6.5.RELEASE.jar | 4 | CRITICAL |

## Critical Security Vulnerabilities (CVSS ≥ 9.0)

### 1. CVE-2022-1471 (CVSS: 9.8) - SnakeYAML Deserialization RCE
**Affected**: snakeyaml-1.25.jar
**Risk**: Remote Code Execution
**Description**: SnakeYAML's Constructor() class does not restrict types during deserialization. An attacker can provide malicious YAML content that, when deserialized, executes arbitrary code on the server.
**Why It's Dangerous**: Allows complete server compromise through crafted YAML payloads.

### 2. CVE-2023-20873 (CVSS: 9.8) - Spring Boot Cloud Foundry Security Bypass
**Affected**: spring-boot-starter-web-2.2.4.RELEASE.jar
**Risk**: Security Bypass
**Description**: Applications deployed to Cloud Foundry can be susceptible to security bypass, allowing unauthorized access to protected resources.
**Why It's Dangerous**: Bypasses authentication/authorization mechanisms in cloud deployments.

### 3. CVE-2022-22965 (CVSS: 9.8) - Spring4Shell RCE
**Affected**: spring-webmvc-5.2.3.RELEASE.jar
**Risk**: Remote Code Execution
**Description**: Spring MVC/WebFlux applications on JDK 9+ are vulnerable to RCE via data binding when deployed as WAR on Tomcat.
**Why It's Dangerous**: Widely exploited vulnerability allowing full system compromise through specially crafted requests.

### 4. CVE-2017-8046 (CVSS: 9.8) - Spring Data REST PATCH RCE
**Affected**: spring-data-rest-webmvc-2.6.5.RELEASE.jar
**Risk**: Remote Code Execution
**Description**: Malicious PATCH requests can use specially crafted JSON to execute arbitrary code on the server.
**Why It's Dangerous**: Allows attackers to execute commands through REST API endpoints.

### 5. CVE-2018-1273 (CVSS: 9.8) - Spring Data Commons Property Binder RCE
**Affected**: spring-data-rest-webmvc-2.6.5.RELEASE.jar
**Risk**: Remote Code Execution
**Description**: Improper neutralization of special elements in property binder allows code execution.
**Why It's Dangerous**: Exploitable through normal application functionality, requiring no authentication.

### 6. CVE-2020-1938 (CVSS: 9.8) - Ghostcat (Apache Tomcat AJP)
**Affected**: tomcat-embed-websocket-9.0.30.jar
**Risk**: File Read/Remote Code Execution
**Description**: AJP connector treats connections as trusted, allowing file read and potential RCE.
**Why It's Dangerous**: Exposes sensitive files (configs, source code) and enables further exploitation.

### 7. CVE-2024-50379 (CVSS: 9.8) - Tomcat TOCTOU Race Condition
**Affected**: tomcat-embed-websocket-9.0.30.jar
**Risk**: Remote Code Execution
**Description**: Race condition during JSP compilation on case-insensitive file systems when default servlet has write permissions.
**Why It's Dangerous**: Allows uploading and executing malicious JSP files.

### 8. CVE-2016-1000027 (CVSS: 9.8) - Spring Framework Deserialization RCE
**Affected**: spring-web-5.2.3.RELEASE.jar
**Risk**: Remote Code Execution
**Description**: Java deserialization of untrusted data can lead to RCE.
**Why It's Dangerous**: Common attack vector in Java applications, easily exploitable with tools like ysoserial.

## High Security Vulnerabilities (CVSS 7.0-8.9)

### 1. CVE-2024-22259 (CVSS: 8.1) - Spring URL Parsing Vulnerability
**Affected**: spring-webmvc-5.2.3.RELEASE.jar
**Risk**: Security Bypass
**Description**: Applications using UriComponentsBuilder to parse external URLs may bypass host validation.
**Why It's Dangerous**: Can lead to Server-Side Request Forgery (SSRF) attacks.

### 2. CVE-2022-27772 (CVSS: 7.8) - Spring Boot Directory Hijacking
**Affected**: spring-boot-starter-web-2.2.4.RELEASE.jar
**Risk**: Privilege Escalation
**Description**: Temporary directory hijacking vulnerability in AbstractConfigurableWebServer.
**Why It's Dangerous**: Local attackers can escalate privileges by manipulating temp directories.

### 3. CVE-2020-25649 (CVSS: 7.5) - Jackson XXE Vulnerability
**Affected**: jackson-databind-2.10.2.jar
**Risk**: XML External Entity Attack
**Description**: Improper entity expansion allows XXE attacks.
**Why It's Dangerous**: Can read local files, perform SSRF, or cause denial of service.

### 4. CVE-2020-36518 (CVSS: 7.5) - Jackson Stack Overflow DoS
**Affected**: jackson-databind-2.10.2.jar
**Risk**: Denial of Service
**Description**: Deep nested objects cause StackOverflow exception.
**Why It's Dangerous**: Easy DoS attack vector through malformed JSON.

## Security Impact Analysis

### Attack Vectors Enabled
1. **Remote Code Execution (RCE)**: 12+ vulnerabilities allow arbitrary code execution
2. **Denial of Service (DoS)**: 15+ vulnerabilities can crash or degrade the application
3. **Information Disclosure**: 8+ vulnerabilities expose sensitive data
4. **Security Bypass**: 5+ vulnerabilities bypass authentication/authorization
5. **XML External Entity (XXE)**: Multiple XXE vulnerabilities in XML processors
6. **Server-Side Request Forgery (SSRF)**: URL parsing vulnerabilities enable SSRF

### Business Impact
- **Data Breach Risk**: HIGH - Multiple RCE and info disclosure vulnerabilities
- **Service Availability Risk**: HIGH - Multiple DoS vulnerabilities
- **Compliance Risk**: CRITICAL - Using components with known vulnerabilities violates PCI-DSS, HIPAA, and other standards
- **Reputation Risk**: HIGH - Public exploitation would damage trust

### Real-World Exploitation
Many of these vulnerabilities have:
- **Public exploits available**: Spring4Shell, Ghostcat, Log4Shell patterns
- **Active exploitation in the wild**: Automated scanners target these CVEs
- **Metasploit modules**: Professional penetration testing tools include exploits
- **Low complexity**: Many require no authentication and basic HTTP requests

## Recommended Mitigations

### Immediate Critical Fixes (Do These First!)

#### 1. Update Spring Boot and All Spring Dependencies
```xml
<!-- In pom.xml, update parent version -->
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.7.18</version>  <!-- or 3.2.0 for latest -->
</parent>
```

#### 2. Update Vulnerable Direct Dependencies
```xml
<!-- Update Spring Data REST -->
<dependency>
    <groupId>org.springframework.data</groupId>
    <artifactId>spring-data-rest-webmvc</artifactId>
    <version>3.7.18</version>  <!-- Compatible with Spring Boot 2.7.x -->
</dependency>

<!-- Update SnakeYAML -->
<dependency>
    <groupId>org.yaml</groupId>
    <artifactId>snakeyaml</artifactId>
    <version>2.2</version>  <!-- Fixes CVE-2022-1471 -->
</dependency>
```

#### 3. Force Transitive Dependency Updates
```xml
<!-- Add to pom.xml to override vulnerable transitive dependencies -->
<dependencyManagement>
    <dependencies>
        <!-- Force Jackson to latest secure version -->
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.15.3</version>
        </dependency>
        <!-- Force Tomcat to latest -->
        <dependency>
            <groupId>org.apache.tomcat.embed</groupId>
            <artifactId>tomcat-embed-core</artifactId>
            <version>9.0.83</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### Security Configuration Hardening

#### 1. Disable Dangerous Features
```java
// In application.properties
# Disable AJP connector (CVE-2020-1938 Ghostcat)
server.ajp.enabled=false

# Disable actuator endpoints in production
management.endpoints.web.exposure.include=health,info
management.endpoints.web.exposure.exclude=*

# Disable Spring Boot DevTools in production
spring.devtools.restart.enabled=false
```

#### 2. Add Security Headers
```java
@Configuration
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.headers()
            .contentSecurityPolicy("default-src 'self'")
            .and()
            .frameOptions().deny()
            .xssProtection().and()
            .contentTypeOptions();
    }
}
```

### Temporary Workarounds (If Unable to Update Immediately)

1. **WAF Rules**: Configure Web Application Firewall to block known exploit patterns
2. **Network Segmentation**: Limit exposure of vulnerable services
3. **Input Validation**: Implement strict input validation for all user inputs
4. **Disable Features**: Disable PATCH method if not needed (CVE-2017-8046)
5. **Monitor**: Implement logging and monitoring for exploitation attempts

### Verification After Fixes
```bash
# Re-run dependency check after updates
./mvnw clean dependency-check:check

# Verify specific fixes
./mvnw dependency:tree | grep jackson
./mvnw dependency:tree | grep tomcat
./mvnw dependency:tree | grep snakeyaml
```

### Long-term Security Practices
1. **Automated Scanning**: Add OWASP DC to CI/CD pipeline
2. **Dependency Updates**: Monthly dependency update reviews
3. **Security Subscriptions**: Subscribe to Spring Security advisories
4. **Version Policy**: Never use versions older than 2 years
5. **Supply Chain Security**: Use tools like Dependabot or Renovate

## Troubleshooting

### Common Issues and Solutions

#### Issue: "No documents exist" error
**Cause**: NVD database is not initialized or corrupted
**Solution**:
1. Delete the cache: `rm -rf ~/.m2/repository/org/owasp/dependency-check-data/`
2. Get an NVD API key from https://nvd.nist.gov/developers/request-an-api-key
3. Add to pom.xml: `<nvdApiKey>YOUR-API-KEY</nvdApiKey>`
4. Run: `./mvnw dependency-check:update-only`

#### Issue: HTTP 403 Forbidden errors
**Cause**: NIST has deprecated old JSON feeds, requires API key for updates
**Solution**: Use version 11.0.0+ with existing database or obtain NVD API key

#### Issue: Tests failing during build
**Solution**: Skip tests with `-DskipTests` flag

#### Issue: Build timeout
**Solution**: Increase timeout or run with offline database:
```bash
./mvnw dependency-check:check -DskipTests -Ddependency-check.autoUpdate=false
```

## Project Structure
```
Module2.1/
├── pom.xml                           # Maven configuration with OWASP DC plugin
├── suppression.xml                   # Vulnerability suppression rules (if any)
├── README.md                         # This file
├── mvnw                             # Maven wrapper (Unix)
├── mvnw.cmd                         # Maven wrapper (Windows)
├── .mvn/                            # Maven wrapper configuration
├── src/
│   ├── main/
│   │   ├── java/                   # Java source code
│   │   └── resources/              # Application resources
│   └── test/                       # Test files
└── target/                          # Build output (created after compilation)
    ├── dependency-check-report.html # Vulnerability report (HTML)
    └── dependency-check-report.json # Vulnerability report (JSON)
```

## Additional Resources
- [OWASP Dependency-Check Documentation](https://jeremylong.github.io/DependencyCheck/)
- [NVD (National Vulnerability Database)](https://nvd.nist.gov/)
- [Spring Boot Security Best Practices](https://spring.io/projects/spring-security)
- [CVE Details](https://www.cvedetails.com/)

## Notes
The generated report includes:
- Scan date and time
- Engine version (11.0.0)
- Project name (Module2.1)
- Comprehensive list of all dependencies
- Detailed vulnerability information with CVE IDs
- Severity scores and descriptions

---
*Last Updated: November 9, 2025*
*Report Generated with OWASP Dependency-Check 11.0.0*
