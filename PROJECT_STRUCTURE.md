# Project Structure Map

## Complete File Tree

```
software-testing-handbook/
├── README.md                                    # ROOT - Start here
├── PROJECT_STRUCTURE.md                         # This file
├── .gitignore
├── scripts/
│   └── run_scans.sh                            # Automation for vulnerability scans
└── software-testing/
    ├── README.md                                # Testing handbook overview
    ├── docs/
    │   ├── README.md                            # Documentation hub/index
    │   ├── static-dynamic-testing.md            # Theory guide
    │   ├── testing-examples-index.md           # Examples catalog
    │   ├── testing-strategy.md                 # Testing approach
    │   ├── vulnerability-analysis-report.md    # Vulnerability findings
    │   ├── vulnerability-fixes-guide.md        # How to fix issues
    │   ├── comparison-report.md                # Vulnerable vs Secure
    │   ├── audits/
    │   │   ├── SECURITY-AUDIT-FINAL-REPORT.md
    │   │   └── TECHNICAL-SECURITY-AUDIT-CORRECTED.md
    │   ├── status/
    │   │   ├── HONEST-SECURITY-STATUS.md       # Current security status
    │   │   └── OSS-INDEX-SETUP.md              # How to setup OSS Index
    │   └── reports/                             # Generated scan reports (empty until run)
    ├── java/
    │   ├── README.md                            # Java examples overview
    │   ├── Module2.1/                           # VULNERABLE version
    │   │   ├── README.md                        # Main docs for vulnerable
    │   │   ├── README-VULNERABLE.md             # WARNING file
    │   │   ├── pom.xml                          # Maven config
    │   │   ├── src/                             # Source code
    │   │   └── target/                          # Build output (generated)
    │   └── Module2.1-IMPROVED/                  # SECURE version
    │       ├── README.md                        # Main docs for secure
    │       ├── pom.xml                          # Maven config
    │       ├── src/                             # Source code
    │       └── target/                          # Build output (generated)
    └── python/
        ├── README.md                            # Python examples overview
        ├── static_analysis_example.py           # Intentionally flawed
        └── static_analysis_example_fixed.py     # Fixed version
```

## README Files Navigation Chain

1. **START**: `/README.md` (Root)
   - Links to → `software-testing/README.md`
   - Links to → `software-testing/docs/README.md`
   - Links to → All 8 READMEs

2. **Testing Handbook**: `software-testing/README.md`
   - Links to → `docs/` documentation
   - Links to → `java/` examples
   - Links to → `python/` examples

3. **Documentation Hub**: `software-testing/docs/README.md`
   - Links to → All .md files in docs/
   - Links to → audits/ subdirectory
   - Links to → status/ subdirectory

4. **Java Overview**: `software-testing/java/README.md`
   - Links to → Module2.1/
   - Links to → Module2.1-IMPROVED/

5. **Python Overview**: `software-testing/python/README.md`
   - References → Example .py files

6. **Module READMEs**:
   - `Module2.1/README.md` - Vulnerable version docs
   - `Module2.1/README-VULNERABLE.md` - Warning
   - `Module2.1-IMPROVED/README.md` - Secure version docs

## Key Principles

1. **No External References**: Each README only references files within its directory or subdirectories
2. **Clear Hierarchy**: Root → Section → Module → Component
3. **No Duplication**: Each piece of information lives in ONE place
4. **Working Commands**: All commands tested and work from their respective directories
5. **Accurate Paths**: All paths relative to where the README lives