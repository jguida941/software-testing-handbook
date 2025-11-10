# OSS Index + Dependency-Check Setup

## 1. Create API Credentials

1. Visit <https://ossindex.sonatype.org>.
2. Sign in (GitHub/Google) → **Profile** → **API Token**.
3. Generate a token and copy the username/token pair.

## 2. Export Credentials Safely

```bash
export OSS_INDEX_USER="name@example.com"
export OSS_INDEX_TOKEN="aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"
```

> Do **not** check these values into Git. The provided `scripts/run_scans.sh` reads them from the environment.

## 3. Run the Standard Scan Script

```bash
./scripts/run_scans.sh
```

The script:
- Scans `software-testing/java/Module2.1` (vulnerable) and `software-testing/java/Module2.1-IMPROVED`.
- Stores HTML/JSON reports under `software-testing/docs/reports/<timestamp>/`.
- Prints a summary table with total, critical, and high counts.

## 4. Troubleshooting

- **Missing credentials**: the script exits with an error if either env var is unset.
- **Sandboxed network**: run from an environment with outbound HTTPS to `ossindex.sonatype.org` and NVD mirrors.
- **First run is slow**: dependency-check downloads the NVD data (~200 MB). Subsequent runs reuse the cache.
