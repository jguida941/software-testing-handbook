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
  echo "==> Scanning $label ($module_path)"
  (cd "$root_dir/$module_path" && \
    OSS_INDEX_USER="$OSS_INDEX_USER" OSS_INDEX_TOKEN="$OSS_INDEX_TOKEN" \
    mvn -q clean compile dependency-check:check -DskipTests \
      -DossIndexUsername="$OSS_INDEX_USER" \
      -DossIndexPassword="$OSS_INDEX_TOKEN")

  local src="$root_dir/$module_path/target"
  cp "$src/dependency-check-report.html" "$reports_dir/${label}-dependency-check-report.html"
  cp "$src/dependency-check-report.json" "$reports_dir/${label}-dependency-check-report.json"
}

scan_module "software-testing/java/Module2.1" "module2.1-vulnerable"
scan_module "software-testing/java/Module2.1-IMPROVED" "module2.1-improved"

echo "Reports saved to $reports_dir"
