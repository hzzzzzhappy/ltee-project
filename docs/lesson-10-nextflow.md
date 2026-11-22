# Nextflow notes

Hanzhe Liang · 22 November 2026

[Lesson 10](https://khanlab.bio/cbio7501-f26/pages/10-nextflow.html), sections
1–9 and Break it. Nextflow 26.10.6 and OpenJDK 25.0.2, through Pixi.

## Processes, channels and the first run

The separate `nextflow-practice` folder contains the toy text workflow.
Two processes produced `THIS IS A.TXT` and `THIS IS B.TXT`. A second run
with `-resume` reused both tasks from the cache.

A process declares the files and values it needs, the command to run, and
the outputs it produces. Channels carry one item per sample. The workflow
connects them; `publish:` and the `output` block select the saved results.

Added Nextflow to the `pipeline` feature and ran the full LTEE workflow.
All 32 tasks completed. The final VCF records matched Snakemake exactly:

| Sample | Variants |
|---|---:|
| SRR2584863 | 25 |
| SRR2584866 | 775 |
| SRR2589044 | 10 |

## Build it in two steps

Replaced the full workflow with the QC-only version. Three FastQC tasks
processed the three pairs of FASTQs, followed by one MultiQC task. Checked
all six FastQC ZIP files: each input contained 175,000 sequences.

Inspected a real task folder, its input links, `.command.sh`, `.command.err`,
`.command.log` and exit code. Its command ran FastQC on both mates. These
files explain what actually ran and are the first place to look on failure.

Put the full workflow back and ran `nextflow lint`, then resumed it.
The trace files recorded:

| Run | Completed | Cached |
|---|---:|---:|
| First full LTEE workflow | 32 | 0 |
| QC-only workflow | 4 | 0 |
| Full workflow resumed after QC | 28 | 4 |
| Minimum depth 10, resumed | 6 | 26 |
| Default depth, execution report run | 0 | 32 |

Before changing the filter, predicted that only `FILTER_VARIANTS` and
`VARIANT_STATS` would rerun, three tasks each. The trace confirmed it.
Depth-10 counts were 16, 415 and 5 for the samples listed above, and their
records matched the Snakemake sensitivity VCFs exactly. The YAML kept depth
2 throughout; the stricter threshold was a command-line override.

## Run and compare

From the project root:

```bash
pixi install --locked --all
pixi run run-nextflow
pixi run compare-workflows
```

The two workflow managers use `config/config.yaml`, the same sample sheet,
locked tools and BWA batch size. `compare-workflows` checks the VCF records,
excluding run-specific headers. `reproduce` continues to use Snakemake.

To resume and generate the execution report:

```bash
pixi run -e pipeline nextflow run workflow/nextflow/main.nf -params-file config/config.yaml -resume -with-report results/nextflow/execution-report.html
```

`workflow.output.mode = 'copy'` keeps published files independent of the
task-cache folders. Confirmed the outputs were real files, then previewed
and removed runs older than the last run with `nextflow clean -n/-f -before`.
Removed the temporary QC-only and depth-10 published folders after their
checks; the main outputs and execution report remain. macOS native tasks
do not provide the CPU/memory metrics that container runs can collect, so
the execution report should not be read as a complete resource benchmark.

## nf-core demo

Ran `nf-core/demo -r 1.2.0 -profile test,docker` in a separate practice folder.
All eight tasks completed: COWPY, three FastQC, three SEQTK_TRIM and MultiQC.
Saved the published demo outputs under `results/nf-core-demo/`. The release
was pinned; the pipeline supplied its own test inputs and containers.

To rerun from this project with Docker running:

```bash
pixi run -e pipeline nextflow run nf-core/demo -r 1.2.0 -profile test,docker --outdir results/nf-core-demo
```

## Break it: launch directory

Launched from `workflow/nextflow/` using `../../config/config.yaml`. The run
failed with `Input file 'metadata/samples.tsv' does not exist`, as predicted:
relative paths are resolved from the launch directory. Removed only the
failed run's generated files inside that folder, then verified the main
published VCFs still matched Snakemake. Launch the real run from the root.

## macOS path fix

The Bioconda launcher did not quote its distribution directory or preserve
Java arguments when the environment path contained spaces. This affected
the `Hanzhe Liang` home path before any task could run.

`scripts/activate-nextflow.sh` generates a compatibility launcher within the
Pixi environment using `scripts/prepare_nextflow_launcher.py`. It quotes the
distribution path and preserves Java argument boundaries. The installed
package files are unchanged. The helper checks the expected launcher
structure and fails explicitly if it changes. The toy used the same fix.

## Which tool?

Snakemake fits a file-based Python analysis well. Nextflow is useful when
channels, shared process modules or an existing nf-core pipeline fit the
work. For a short linear analysis, a few Pixi tasks may be sufficient.
