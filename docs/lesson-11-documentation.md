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

Section 5 citation validation and the later sections have not been completed
as part of this step. The existing `CITATION.cff` is retained.

## Follow-up review

Initial documentation edits were made before this review. A separate,
actually timed 20-minute review began at 2026-11-23T16:19:31+04:00.
Its wall-clock duration includes scheduled intervals between checks, not
20 minutes of computation. No commit dates are overridden.
