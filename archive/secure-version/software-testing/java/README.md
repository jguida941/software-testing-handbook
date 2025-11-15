# Java Dynamic Testing Examples

The `java/` directory houses hands-on examples that highlight how dynamic testing and dependency analysis uncover runtime issues that static analysis alone may miss.

## Module Index

| Module | Description | Key Takeaways |
|--------|-------------|---------------|
| [`Module2.1`](./Module2.1/) | Spring Boot REST API instrumented with OWASP Dependency-Check | Shows how vulnerable transitive dependencies (e.g., Spring4Shell, Ghostcat) are discovered and documented |

## How to Use These Examples

1. Pick a module (start with [`Module2.1`](./Module2.1/README.md) if you need the rubric-ready example).
2. Follow the module README to run the project and its security scan (`./mvnw clean compile dependency-check:check -DskipTests`).
3. Open the generated report under `target/` and document the CVEs, severity, and mitigation steps.
4. Cross-reference the findings with the [testing theory guide](../docs/static-dynamic-testing.md) to connect practice with principles.

## Requirements

- JDK 17+ (Module2.1 also runs on Java 8 if needed)
- Maven or the included Maven Wrapper (`mvnw`)
- Internet access the first time you download dependencies (or a pre-populated local Maven repository)

## Extending the Folder

If you add more Java examples:
- Include a dedicated subfolder with its own README.
- Document which testing technique it demonstrates (dynamic security testing, integration tests, load tests, etc.).
- Provide exact commands so others can reproduce the findings.

Need help deciding where a new example belongs? Drop it into this folder and update the table above. This keeps the handbook organized while making it clear how each Java project supports the broader static-vs-dynamic testing narrative.
