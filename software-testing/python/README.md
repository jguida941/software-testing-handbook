# Python Static Analysis Example

## Purpose

This module demonstrates **static testing** through practical Python examples, showing how code analysis tools catch issues **before runtime**. Unlike the Java module that found 162 runtime vulnerabilities through dynamic testing, this example shows how static analysis prevents different categories of bugs from ever reaching production.

## Connection to Main Concepts

This example demonstrates [static testing](../docs/static-dynamic-testing.md) by:
- **Analyzing code without execution** - Finding issues in source code structure
- **Early bug detection** - Catching problems at development time (cheapest to fix)
- **Enforcing code quality** - Maintaining consistent, readable, maintainable code

## What You'll Learn

1. **Static Analysis Benefits**: How tools catch bugs before they become runtime errors
2. **Type Safety**: How type hints prevent entire categories of bugs
3. **Code Quality**: Why style and structure matter for long-term maintainability
4. **Cost Savings**: Issues found here cost 10x less to fix than in production

## What's Inside

- `static_analysis_example.py` — **INTENTIONALLY FLAWED** sample used to demonstrate the lint/type findings (kept ugly on purpose). We added a minimal `__init__` solely so the runtime demo works; the rest of the issues remain untouched.
- `static_analysis_example_fixed.py` — clean reference implementation showing what “good” looks like after applying the fixes.

## Hands-On Exercises

### Exercise 1: Style and Quality Analysis with Pylint

```bash
# Install if needed
pip install pylint

# Run the linter
pylint static_analysis_example.py
```

**What Pylint Finds:**
- **Style Issues**: Naming conventions, line length, formatting
- **Potential Bugs**: Unused variables, dangerous defaults, unreachable code
- **Documentation**: Missing docstrings, unclear code
- **Refactoring Opportunities**: Code complexity, duplication

**Expected Findings (current run):**
- 22 total Pylint findings (naming issues, unused imports/vars, docstring gaps, complexity warnings, etc.)
- Command to count quickly:

```bash
pylint static_analysis_example.py 2>&1 | grep -E '^static_analysis_example' | wc -l
```

**Why This Matters:** Teams spend 60% of development time reading code. Clean, consistent code reduces this overhead significantly.

### Exercise 2: Type Safety with Mypy

```bash
# Install if needed
pip install mypy

# Run type checking
mypy static_analysis_example.py
```

**What Mypy Finds:**
- **Type Mismatches**: Function receiving wrong argument types
- **Return Type Issues**: Functions not returning expected types
- **Missing Annotations**: Untyped code that could hide bugs
- **None Safety**: Potential NoneType errors

**Expected Findings (current run):**
- 0 mypy errors (constructor now accepts the same parameters we pass so the runtime demo can execute; the file is still intentionally messy)

**Why This Matters:** Type-related bugs account for 15% of production issues. Static typing eliminates these entirely.

### Exercise 3: Dynamic Execution (Comparison)

```bash
# Run the script
python static_analysis_example.py
```

**Compare Static vs Dynamic:**
- Some issues found by static analysis may not cause immediate runtime errors
- Runtime might work "by accident" but fail with different inputs
- Static analysis finds issues across ALL code paths, not just the executed one

### Exercise 4: Confirm the Fixed Version Is Clean

```bash
pylint static_analysis_example_fixed.py
mypy static_analysis_example_fixed.py
```

Both commands should report **0 issues**. Use this file as the “after” snapshot when teaching remediation.

## Static Analysis Metrics (Updated)

| Tool | Issues Found (flawed file) | Severity | Time to fix |
|------|----------------------------|----------|-------------|
| Pylint | 22 issues | Low–Medium | 2–5 min each |
| Mypy | 0 issues (after adding runtime-safe `__init__`) | — | — |
| Combined | 22 issues | Mixed | 30–60 min total |

**Expected Results Snapshot**
- **Flawed version**: 22 lint issues (Pylint) + 0 type errors (Mypy) because we added the minimal constructor noted above
- **Fixed version**: 0 issues (both tools report success)

Compare this to the Java module's **162 vulnerabilities** found through dynamic testing—different tools find different problems!

## Integration with CI/CD

To prevent these issues from reaching production:

```yaml
# Example GitHub Actions workflow
name: Static Analysis
on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Pylint
        run: pylint **/*.py
      - name: Run Mypy
        run: mypy **/*.py
```

## Key Takeaways

1. **Static Analysis is Preventive**: Catches bugs before they exist in runtime
2. **Complements Dynamic Testing**: Different tools find different issues
3. **ROI is Massive**: Fixing issues here vs production = 10-100x cost savings
4. **Automation is Key**: These checks should run on every commit

## Next Steps

After completing these exercises:
1. Compare findings with the [Java dynamic testing results](../java/Module2.1/)
2. Implement both static and dynamic testing in your projects
3. Create custom Pylint rules for your team's standards
4. Add type hints to an existing Python project

## Real-World Impact

In production systems:
- **Google** reports 15% fewer bugs after adopting Python type hints
- **Dropbox** migrated 4 million lines to typed Python, preventing countless bugs
- **Instagram** uses extensive static analysis, catching 20% of bugs before testing

## Comparison: Static (Python) vs Dynamic (Java Module)

| Aspect | This Python Module | Java Module 2.1 |
|--------|-------------------|-----------------|
| **Testing Type** | Static Analysis | Dynamic Security Testing |
| **When Run** | During development | During build/deployment |
| **Issues Found** | Code quality, type errors | 162 security vulnerabilities |
| **Fix Cost** | Very low (immediate) | High (requires updates) |
| **Tools Used** | Pylint, Mypy | OWASP Dependency Check |

## Additional Resources

- [Pylint Documentation](https://pylint.org/)
- [Mypy Documentation](http://mypy-lang.org/)
- [Python Type Hints (PEP 484)](https://www.python.org/dev/peps/pep-0484/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

**Remember**: The 23 static-analysis findings here are just as important as the 162 vulnerabilities found in the Java module through dynamic testing. Together, they create comprehensive quality assurance.

---
[← Back to Main Documentation](../README.md) | [View Java Dynamic Testing Example →](../java/Module2.1/)
