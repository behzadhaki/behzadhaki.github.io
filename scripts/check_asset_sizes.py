#!/usr/bin/env python3
"""
Check assets/ against GitHub's size limits.

Per-file limits (hard rules):
  WARN  : >= 50 MB  (GitHub warns)
  BLOCK : >= 100 MB (GitHub hard-rejects the push)

Repo-level guidelines (soft):
  WARN  : >= 500 MB total (cloning becomes slow)
  LARGE : >= 1 GB total   (GitHub strongly discourages)
"""

import sys
from pathlib import Path

FILE_WARN_MB  = 50
FILE_BLOCK_MB = 100
REPO_WARN_MB  = 500
REPO_LARGE_MB = 1024

TOP_N = 20  # always show the N largest files

def fmt(size_bytes):
    for unit in ("B", "KB", "MB", "GB"):
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"

def main():
    repo_root  = Path(__file__).resolve().parent.parent
    assets_dir = repo_root / "assets"

    if not assets_dir.is_dir():
        sys.exit(f"ERROR: assets/ not found at {assets_dir}")

    file_warn_limit  = FILE_WARN_MB  * 1024 ** 2
    file_block_limit = FILE_BLOCK_MB * 1024 ** 2
    repo_warn_limit  = REPO_WARN_MB  * 1024 ** 2
    repo_large_limit = REPO_LARGE_MB * 1024 ** 2

    blocked = []
    warned  = []
    all_files = []

    for path in sorted(assets_dir.rglob("*")):
        if not path.is_file():
            continue
        size = path.stat().st_size
        rel  = path.relative_to(repo_root)
        all_files.append((rel, size))
        if size >= file_block_limit:
            blocked.append((rel, size))
        elif size >= file_warn_limit:
            warned.append((rel, size))

    total_size = sum(s for _, s in all_files)

    # ── Per-file summary ────────────────────────────────────────────────
    print(f"Per-file check ({len(all_files)} files)")
    print(f"  Blocked  (>= {FILE_BLOCK_MB} MB): {len(blocked)} file(s)")
    print(f"  Warned   (>= {FILE_WARN_MB} MB):  {len(warned)} file(s)")
    print()

    if blocked:
        print(f"  ✗ BLOCKED — GitHub will reject these:")
        for rel, size in blocked:
            print(f"      {fmt(size):>10}  {rel}")
        print()

    if warned:
        print(f"  ⚠ WARNING — consider compressing or hosting externally:")
        for rel, size in warned:
            print(f"      {fmt(size):>10}  {rel}")
        print()

    if not blocked and not warned:
        print("  ✓ All individual files are within GitHub's limits.\n")

    # ── Repo-level total ────────────────────────────────────────────────
    if total_size >= repo_large_limit:
        repo_flag = "✗"
        repo_note = f"repo is very large — GitHub strongly discourages repos over {REPO_LARGE_MB} MB"
    elif total_size >= repo_warn_limit:
        repo_flag = "⚠"
        repo_note = f"repo is getting large — cloning will be slow above {REPO_WARN_MB} MB"
    else:
        repo_flag = "✓"
        repo_note = "total size is fine"

    print(f"Total assets size: {fmt(total_size)}  {repo_flag} {repo_note}")
    print()

    # ── Top N largest files (always shown) ──────────────────────────────
    print(f"Top {TOP_N} largest files:")
    for rel, size in sorted(all_files, key=lambda x: x[1], reverse=True)[:TOP_N]:
        flag = "✗" if size >= file_block_limit else ("⚠" if size >= file_warn_limit else " ")
        print(f"  {flag}  {fmt(size):>10}  {rel}")

if __name__ == "__main__":
    main()
