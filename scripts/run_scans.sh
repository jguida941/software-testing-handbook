#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
reports_dir="$root_dir/software-testing/docs/reports/$(date +%Y-%m-%d_%H-%M-%S)"
mkdir -p "$reports_dir"

if [[ -z "${OSS_INDEX_USER:-}" || -z "${OSS_INDEX_TOKEN:-}" ]]; then
  echo "OSS_INDEX_USER and OSS_INDEX_TOKEN must be exported before running this script." >&2
  exit 1
fi

scan_module() {
  local module_path=$1
  local label=$2
  local continue_on_failure=${3:-false}

  echo "==> Scanning $label ($module_path)"
  set +e
  (cd "$root_dir/$module_path" && \
    OSS_INDEX_USER="$OSS_INDEX_USER" OSS_INDEX_TOKEN="$OSS_INDEX_TOKEN" \
    mvn -q clean compile dependency-check:check -DskipTests \
      -DossIndexUsername="$OSS_INDEX_USER" \
      -DossIndexPassword="$OSS_INDEX_TOKEN")
  local exit_code=$?
  set -e

  if [[ $exit_code -ne 0 ]]; then
    if [[ "$continue_on_failure" != "true" ]]; then
      echo "Scan failed for $label (exit code $exit_code). Aborting." >&2
      exit $exit_code
    fi
    echo "Scan failed for $label (exit code $exit_code). Continuing so reports are still captured." >&2
  fi

  local src="$root_dir/$module_path/target"
  if [[ -f "$src/dependency-check-report.html" ]]; then
    cp "$src/dependency-check-report.html" "$reports_dir/${label}-dependency-check-report.html"
  fi
  if [[ -f "$src/dependency-check-report.json" ]]; then
    cp "$src/dependency-check-report.json" "$reports_dir/${label}-dependency-check-report.json"
  fi
}

scan_module "software-testing/java/Module2.1" "module2.1-vulnerable"
scan_module "software-testing/java/Module2.1-IMPROVED" "module2.1-improved" "true"

echo "Reports saved to $reports_dir"
