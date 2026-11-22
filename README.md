# LTEE course notes

Hanzhe Liang · CBIO7501

[GitHub](https://github.com/hzzzzzhappy) · hanzhe.liang@mbzuai.ac.ae

Course practice using three *E. coli* samples from the Long-Term Evolution
Experiment. The project runs from data download through variant calling to a Quarto report.

## Run the analysis

With [Pixi](https://pixi.prefix.dev/latest/) installed, run these commands from
the project folder on Linux or macOS:

```bash
pixi install --locked --all
pixi run reproduce
```

This checks the data, runs the Snakemake workflow for QC, alignment, variants
and depth sensitivity, then renders the Quarto report. Package versions are
saved in `pixi.lock`.

- QC report: `results/qc/multiqc/multiqc_report.html`
- Final variants: `results/vcf/`
- Alignment and variant statistics: `results/stats/`
- Main report: `reports/ltee-report.html`
- Depth sensitivity: `results/sensitivity/`

To get the data or check the files separately:

```bash
pixi run download
pixi run python scripts/download_data.py --verify-only
```

## 4 November — Pixi Part B

Adding all the tools to the default environment failed because BWA has no
Windows build. The tools now sit in a separate `pipeline` environment for
Linux and macOS. The default environment still includes Windows.

The full workflow ran successfully on macOS. Final variant counts:

| Sample | Variants |
|--------|---------:|
| SRR2584863 | 25 |
| SRR2584866 | 775 |
| SRR2589044 | 10 |

A second run gave the same variant records. FastQC passed the base-quality
and adapter checks, but some sequence-content, GC and length checks have
warnings or failures. These are kept in the report.

The [Reproduce workflow](https://github.com/hzzzzzhappy/ltee-project/actions/workflows/reproduce.yml)
runs the same command on a fresh Linux runner after each push.

## 11 November — Docker

Ran `hello-world`, used an Ubuntu container and mounted the project folder.
The container read the same sample table as the Mac. Saved the Ubuntu image
digest in the [Docker notes](docs/lesson-08-docker.md). This covers sections 1–4.

## 16 November — Snakemake

Finished sections 1–3: installed the tools, ran the small text workflow and
created the config file. The old shell results are saved in
`results/shell-script/`. Commands and checks are in the
[Snakemake notes](docs/lesson-09-snakemake.md).

## 17 November — Snakemake sections 4–5

Repeated the workflow setup and ran the six alignment rules for `SRR2584863`.
The new sorted BAM and index passed validation, with 350,000 primary records.
A second dry run needed no work. The DAG is in `results/dag.svg`; commands
and checks are in the [Snakemake notes](docs/lesson-09-snakemake.md).

## 17 November — Snakemake sections 6–7

Added variant calling, filtering, statistics and QC rules. The three samples
produced 25, 775 and 10 variants. FastQC ran on all six files and MultiQC
summarised them. Both sets of targets needed no work on a second dry run.
The QC report is `results/qc/multiqc/multiqc_report.html`; commands are in
the [Snakemake notes](docs/lesson-09-snakemake.md).

## 17 November — Snakemake sections 8–9

Added depth sensitivity at 2, 5, 10 and 15 reads, plus the default `all`
target. `pixi run -e pipeline snakemake -c 4` now requests all 22 outputs.
The complete rule graph is in `results/rulegraph.svg`; sensitivity counts
are in the [Snakemake notes](docs/lesson-09-snakemake.md).

## 17 November — Snakemake section 10

Compared the variant records with the shell baseline: all three samples
matched exactly. A temporary depth change to 10 planned only filtering and
variant statistics again. Restored depth 2; the workflow was up to date.

## 18 November — finish Snakemake

`reproduce` now runs download → Snakemake → report. It rebuilt all 49 workflow
jobs after the generated outputs were moved aside. The report includes the
variant counts, depth-sensitivity figure and decision to keep depth 2 with
the full sensitivity analysis. `pixi run compare-to-shell` checks all variant
records against a fresh shell-script run.

The format check passed. Lint kept the course's suggestions about logs for
small rules and per-rule software environments; package versions are locked
for the whole workflow with Pixi. Removing BWA's fixed batch size changed
four records of SRR2584866 even though its count stayed at 775. Restoring
`-K 10000000` restored every record exactly. Details are in the
[Snakemake notes](docs/lesson-09-snakemake.md).

## 22 November — Nextflow homework

Completed sections 1–9 and the launch-directory exercise. Nextflow produced
the same VCF records as Snakemake (25, 775 and 10 variants). With depth 10,
only six tasks reran and the other 26 were cached. The fixed-release
`nf-core/demo` test also ran with Docker.

```bash
pixi run run-nextflow
pixi run compare-workflows
```

`reproduce` continues to use Snakemake. Nextflow outputs are in
`results/nextflow/`, including `execution-report.html`; the Docker demo
outputs are in `results/nf-core-demo/`. The
[Nextflow notes](docs/lesson-10-nextflow.md) record the runs, cache checks,
clean-up and the macOS launcher fix.

The homework was also repeated over a real two-hour schedule; the
[repeat record](docs/lesson-10-repeat-20261122.md) lists actual stage times
and checks.

## Data and files

The reads are the Data Carpentry subset on
[figshare](https://doi.org/10.6084/m9.figshare.7726454): `sub.tar.gz`, CC0,
175,000 read pairs per sample. The original runs are in
[PRJNA295606](https://www.ebi.ac.uk/ena/browser/view/PRJNA295606).
The reference is *E. coli* REL606, GenBank CP000819.1, assembly GCA_000017985.1.

`metadata/sources.tsv` has the download URLs and provider MD5 checksums;
`metadata/checksums.sha256` records the retained files. The seven raw files
are verified and read-only. Raw data, processed data and results are excluded
from Git and can be rebuilt with the commands above.

Scripts are in `scripts/`. Earlier notes cover
[project organization](docs/lesson-02-notes.md),
[data management](docs/data-management-notes.md) and
[Git exercises](docs/lesson-04-terminal.md).

## Sources

Started from the [CBIO7501 project template](https://github.com/khan-lab/cbio7501-f26/tree/main/templates/cookiecutter-repro-project).
Code is MIT-licensed, except for the Data Carpentry variant-calling script
adapted under CC BY 4.0. See [LICENSE](LICENSE) and
[third-party notices](docs/third-party-notices.md) for details.
Citation details are in [CITATION.cff](CITATION.cff). No release published yet.
