"""Compare VCF records exactly; headers contain run-specific metadata.

Usage: python scripts/compare_vcfs.py FIRST_FOLDER SECOND_FOLDER
Adapted from CBIO7501 Lesson 09, Aziz Khan and workshop contributors (MIT).
https://khanlab.bio/cbio7501-f26/pages/09-snakemake.html
Changes: check the file-name sets in both directions and fail for empty inputs.
"""
import sys
from pathlib import Path


def records(path):
    with path.open() as stream:
        return [line.rstrip("\n") for line in stream if not line.startswith("#")]


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    first, second = map(Path, sys.argv[1:])
    names_a = {p.name for p in first.glob("*_final_variants.vcf")}
    names_b = {p.name for p in second.glob("*_final_variants.vcf")}
    if not names_a or not names_b:
        sys.exit("Both folders must contain *_final_variants.vcf files")
    differ = 0
    for name in sorted(names_a | names_b):
        if name not in names_a or name not in names_b:
            print(f"{name}: missing in {first if name not in names_a else second}")
            differ += 1
            continue
        a, b = records(first / name), records(second / name)
        if a == b:
            print(f"{name}: identical ({len(a)} variants)")
        else:
            print(f"{name}: DIFFERENT ({len(a)} vs {len(b)} variants; "
                  f"{len(set(a) - set(b))} only in first, {len(set(b) - set(a))} only in second)")
            differ += 1
    sys.exit(1 if differ else 0)


if __name__ == "__main__":
    main()
