# Documentation: sections 1–4

23 November 2026. Worked on the LTEE classroom example, continuing from the
Nextflow homework on branch `lesson-11-documentation`.

## Measurements

Commands run in the project folder:

```bash
system_profiler SPHardwareDataType -detailLevel mini
uname -sm
du -sh .pixi/envs/* data/raw results
```

Hardware: MacBook Pro, Apple M5 Pro, 15 CPU cores, 24 GB RAM; Darwin arm64.
The workflow uses up to four cores, not all available cores.

```text
1.1G  .pixi/envs/default
2.6G  .pixi/envs/pipeline
332M  data/raw
1.0G  results
```

`du -sh` reports rounded allocated disk usage. The result size includes both
workflow implementations and the nf-core/demo exercise. It excludes ignored
workflow caches elsewhere in the project and the saved earlier runs outside
this repository. These numbers are not minimum hardware requirements.
No new full-run timing or peak-memory benchmark was performed for this step.

## Changes

The README now covers the project question, related publication, folder guide,
hardware measurements, reproduction commands, expected outputs and contact.
Earlier dated entries were moved to `docs/class-notes.md`, keeping the
original links and records. The existing MIT license names Hanzhe Liang.
The README distinguishes project code, report text and figures, the CC0 read
subset and third-party material. Existing attribution notices are retained.

Adapted from [CBIO7501 lesson 11, sections 1–4](https://khanlab.bio/cbio7501-f26/pages/11-documentation.html),
by Aziz Khan and the workshop contributors (course text CC BY 4.0).
The supplied example hardware numbers were replaced with local measurements.

Section 5 citation validation and the later sections were not completed
in the 23 November step. They are covered in the follow-up below.

## Follow-up review

Initial documentation edits were made before this review. A separate,
actually timed 20-minute review began at 2026-11-23T16:19:31+04:00.
Its wall-clock duration includes scheduled intervals between checks, not
20 minutes of computation. No commit dates are overridden.

Additional review confirmed all seven README questions are covered, the
previous dated classroom entries were preserved (only relative links changed),
and every listed output path exists. The regenerated HTML has the expected
author, title and three sample identifiers. Raw files remain excluded from Git.

Review ended at 2026-11-23T16:39:31+04:00 after 1200.0 seconds of wall-clock time.

- 2026-11-23T16:24:31+04:00 — `pixi install --locked --all`: passed.
- 2026-11-23T16:24:41+04:00 — `pixi run python scripts/download_data.py --verify-only`: passed.
- 2026-11-23T16:28:31+04:00 — `pixi run reproduce`: failed (sandbox cache permission; retried below).
- 2026-11-23T16:29:42+04:00 — `pixi run reproduce`: passed.
- 2026-11-23T16:31:31+04:00 — `pixi run python scripts/compare_vcfs.py results/vcf results/nextflow/vcf`: passed.
- 2026-11-23T16:35:31+04:00 — `git diff --check`: passed.

Local Markdown links were also checked. `reproduce` reused existing
workflow outputs and rendered the report; this is not a clean rebuild
benchmark. The VCF comparison checked the retained Nextflow outputs against
Snakemake. Section 5 validation remains outside this review.

## 24 November: sections 5–8 and exercises

Completed the remaining documentation for this LTEE classroom example.

- Expanded `CITATION.cff` with keywords and the related Nature paper;
  author and contact are Hanzhe Liang. No release date or ORCID was invented.
- `cffconvert` 2.0.0 validated the file and exported APA-like and BibTeX citations.
- Added `CONTRIBUTING.md` and a code-of-conduct page linking Contributor Covenant
  3.0, with the maintainer's email as the reporting contact.
- Exported `docs/software-versions.txt` from Pixi for both the pipeline and
  report-rendering environments. Versions are local macOS arm64 builds;
  other platforms have their own entries in `pixi.lock`.
- Generated `docs/rulegraph.dot` and `docs/rulegraph.svg`. Reviewed the workflow
  headers, config comments and decision log; their source credits remain intact.
- Added CFF validation to the Reproduce GitHub Action, using the same pinned
  validator version as the local check.

For the citation failure exercise, a temporary copy received ORCID's test
number without its `https://orcid.org/` prefix. Validation failed with the
expected pattern error. The real citation file was unchanged (SHA-256
checked) and passed validation again. The temporary example is not committed.

For the software-version question, `pixi.lock` provides exact per-platform
packages and `docs/software-versions.txt` provides the human-readable list.
The report also prints its key environment versions. Use the environment
that actually produced a figure: report packages can differ from pipeline
packages (for example pandas).

Local checks passed: citation validation and exports, expected rejection of
the invalid fixture, restored-file validation, graph generation, local links,
and `git diff --check`. The full clean-run check is performed by GitHub CI.
