# Static and Dynamic Testing
_A concise overview of how static and dynamic testing complement each other in software quality assurance._

This document explains the purpose, methods, and differences between static and dynamic software testing.

## Static Testing

Static testing examines software and related documents without executing the code. It relies on reviews, walkthroughs, and automated tools that detect syntax, style, or logic issues early in development (a process known as static analysis).

This approach reduces cost and rework by identifying the causes of potential failures such as formatting mistakes, design flaws, or structural issues before they surface as runtime errors. The earlier a defect is found, the cheaper it is to fix.

Static testing can also involve reviewing requirements, designs, or plans to spot mistakes or ambiguous sections before any code is written. Sometimes, flaws exist in the design itself and only surface through static analysis.

### Example: Loose vs. Strict Equality in JavaScript

```javascript
if (user == "admin") {
  // Loose comparison
}

if (user === "admin") {
  // Strict comparison, safer
}
```

Using the loose `==` comparison could allow unintended access. If `user` were a truthy non-string value (such as `1` or `true`), JavaScript might still evaluate the condition as true, granting access incorrectly. Static analysis tools often flag this pattern as a potential security risk.

### Static Analysis Tools for Python

- `Pylint`: checks code quality and style consistency
- `Flake8`: detects syntax and formatting problems
- `Mypy`: performs static type checking

AI-based static analysis tools, such as CodeRabbit, can automatically review code but may raise false positives because they neither execute the program nor fully understand its runtime behavior.

### Static Tool Highlights

| Tool | Reason |
| --- | --- |
| Pylint | Finds style, naming, and logic issues without running the program. |
| Flake8 | Combines PyFlakes and pycodestyle checks for logic and formatting issues. |
| Mypy | Checks type consistency using annotations before execution. |

Overall, static testing helps detect and correct defects early, reducing issues that appear during execution and improving software quality.

## Benefits of Static Testing

- Prevent defects by uncovering inconsistencies, ambiguities, omissions, and redundancies in requirements.
- Increase productivity by tightening feedback loops and reducing development and downstream testing time.
- Lower the total cost of quality by catching issues long before release.
- Improve communication and shared understanding through code and document reviews.

## Common Defects Found Through Static Testing

- Requirement defects such as contradictions, ambiguities, or missing details.
- Design defects like inefficient algorithms, excessive coupling, or poor modularity.
- Coding defects including unused variables, unreachable code, or missing initialization.
- Security vulnerabilities such as buffer overflows or absent input validation.
- Standards deviations where naming, formatting, or documentation rules are not followed.

## Dynamic Testing

Dynamic testing runs the software (or one of its parts) to see how it behaves during real execution. It confirms that the program’s logic, data flow, and integrations work correctly under realistic conditions, revealing issues that static testing cannot: wrong calculations, timing problems, or environment-specific bugs.

Common forms include:
- Unit testing with tools like `pytest` or `unittest` to verify individual functions or modules.
- Integration and system testing to check how components work together.
- UI automation with tools such as Selenium to exercise real user flows.
- Runtime instrumentation, for example `coverage.py`, to track which code paths execute during tests.

### Dynamic Tool Highlights

| Tool | Reason |
| --- | --- |
| pytest / unittest | Execute tests to verify behavior and assertions at runtime. |
| coverage.py | Runs the program or tests and reports which code paths executed. |
| Selenium | Drives the application through the UI to observe real runtime behavior. |

## Differences Between Static and Dynamic Testing

- Static testing checks code, designs, and documents without executing them, while dynamic testing validates behavior during execution.
- Static testing focuses on work product quality: requirements, design logic, and documentation completeness.
- Dynamic testing focuses on functional correctness, confirming that the software behaves as expected at runtime.
- The approaches complement each other: static techniques prevent defects from entering runtime, and dynamic techniques confirm that executed paths behave correctly.

## Why Combine Static and Dynamic Testing

1. Catch defects as early as possible, reducing rework cost.
2. Cover more defect types by pairing structural checks via static testing with runtime checks via dynamic testing.
3. Improve confidence in releases by combining preventive (static) and detective (dynamic) quality controls.
4. Provide better audit trails: static test reports show design/code hygiene, while dynamic test results demonstrate runtime correctness and coverage.
