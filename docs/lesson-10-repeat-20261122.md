# Nextflow two-hour repeat

Hanzhe Liang · 22 November 2026

Repeated Lesson 10 sections 1–9 and Break it in Terminal. The previous run
and its local outputs were preserved. This was a scheduled two-hour repeat
with code review and pauses; two hours is wall-clock time, not CPU time.

Started **20:15:30**, finished **22:15:30** (Asia/Dubai).

| Stage | Actual start | Actual finish |
|---|---|---|
| Preserve previous run; verify raw data | 20:15:30 | 20:15:35 |
| Toy and resume | 20:20:30 | 20:20:39 |
| Locked environments | 20:30:30 | 20:30:46 |
| Full LTEE run | 20:40:30 | 20:41:12 |
| QC-only workflow | 20:55:30 | 20:56:10 |
| Inspect a task | 21:05:30 | 21:05:31 |
| Full resume and depth 10 | 21:15:30 | 21:16:10 |
| Recreate Pixi tasks and compare | 21:33:30 | 21:34:06 |
| Execution report | 21:45:30 | 21:45:49 |
| Wrong launch directory | 21:53:30 | 21:53:32 |
| nf-core/demo with Docker | 22:00:30 | 22:01:50 |
| Clean old cache; verify outputs | 22:10:30 | 22:10:50 |

All stages exited successfully. The first full run completed 32 tasks and
matched Snakemake records exactly (25, 775 and 10 variants). The toy completed
two tasks and then cached both. Restoring the full workflow after QC reused
the three FastQC tasks and MultiQC; 28 other tasks ran. At depth 10, only
three filters and three statistics tasks reran, with 26 tasks cached. Its
16, 415 and 5 variant records matched Snakemake at depth 10.

The report run cached all 32 tasks. Published outputs were copies, and the
execution report remains in `results/nextflow/execution-report.html`.
The wrong-directory run failed with the expected missing sample-sheet error;
its temporary files were removed without changing the main VCFs.

nf-core/demo 1.2.0 ran with `test,docker`: eight new tasks completed. Its
published outputs are in `results/nf-core-demo/`. Old main-workflow cache
and temporary QC/depth-10 outputs were cleaned after a deletion preview.
Main VCFs still matched Snakemake, and all seven raw checksums passed.

See [the main Nextflow notes](lesson-10-nextflow.md) for commands and the
macOS launcher fix. Logs and traces for this repeat are retained locally.
No source-history timestamps were changed. Published outputs and caches
are excluded from Git.
