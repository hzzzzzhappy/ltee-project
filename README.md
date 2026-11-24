# LTEE variant calling

Hanzhe Liang · CBIO7501 · hanzhe.liang@mbzuai.ac.ae

Course practice using three *E. coli* clones from population Ara-3 of the
Long-Term Evolution Experiment, sampled at 5,000, 15,000 and 50,000 generations.
The question is how variant counts change over time and with the minimum
read depth used to filter calls. This is a classroom example, not a separate
research project.

## Publication

No publication from this project. The biological study is
[Tenaillon et al. (2016), Nature](https://doi.org/10.1038/nature18959).
The analysis follows the Data Carpentry genomics lesson.

## Reproduce

Install [Pixi](https://pixi.prefix.dev/latest/) and use Linux or macOS.
On Windows, use WSL2 for the pipeline tools. Internet access is needed to
download packages and data. Run from the project folder:

```bash
git clone https://github.com/hzzzzzhappy/ltee-project.git
cd ltee-project
pixi install --locked --all
pixi run reproduce
```

This downloads and verifies the raw data, runs Snakemake for QC, alignment,
variant calling and depth sensitivity, then renders the Quarto report.
Exact package versions are recorded in `pixi.lock`.
The [GitHub Action](https://github.com/hzzzzzhappy/ltee-project/actions/workflows/reproduce.yml)
checks reproduction on a fresh Linux runner after pushes.

Other commands:

```bash
pixi run run-nextflow
pixi run compare-workflows
pixi run python scripts/download_data.py --verify-only
pixi task list
```

Nextflow runs the same analysis; `compare-workflows` checks that its variant
records match Snakemake. The nf-core/demo Docker exercise is separate and
is not required by `reproduce`.

## Hardware and disk space

Measured on 23 November 2026 on an Apple M5 Pro MacBook Pro with 24 GB RAM.
The Snakemake command uses up to four cores. Installed environments occupy
1.1 GB (default) and 2.6 GB (pipeline); raw data occupies 332 MB and the
current results directory about 1.0 GB. These are rounded local disk-usage
measurements, not minimum requirements. Results include Snakemake, Nextflow
and the Docker demo; workflow caches and temporary downloads need extra space.
Key package versions are listed in [software-versions.txt](docs/software-versions.txt).
Peak workflow memory and a fresh-run runtime have not been benchmarked here.
See the [measurement notes](docs/lesson-11-documentation.md).

## Outputs

| Path | Content |
|------|---------|
| `reports/ltee-report.html` | Report with read quality, variants and depth sensitivity |
| `results/qc/multiqc/multiqc_report.html` | Read-quality summary |
| `results/vcf/` | Filtered variant calls per sample |
| `results/sensitivity/` | Calls at depths 2, 5, 10 and 15 |
| `results/stats/` | Alignment and variant statistics |
| `results/nextflow/` | Nextflow outputs and execution report |

At minimum depth 2, expected counts are SRR2589044: 10, SRR2584863: 25,
and SRR2584866: 775. Settings are in `config/config.yaml`.

## Data

The reads are the Data Carpentry subset on
[figshare](https://doi.org/10.6084/m9.figshare.7726454): `sub.tar.gz`, CC0,
175,000 read pairs per sample. Original runs are in
[PRJNA295606](https://www.ebi.ac.uk/ena/browser/view/PRJNA295606).
The reference is *E. coli* REL606, GenBank CP000819.1, assembly GCA_000017985.1.

`metadata/sources.tsv` records download URLs and provider MD5 checksums;
`metadata/checksums.sha256` records our retained files. Raw data is read-only.
Raw data, processed data, results and caches are excluded from Git.

## Repository contents

See the [folder guide](docs/structure.md) and
[classroom notes](docs/class-notes.md). Detailed commands and checks are
linked from those notes. The [rule graph](docs/rulegraph.svg) shows the
Snakemake steps and their dependencies.

## Cite

Author and citation details are in [CITATION.cff](CITATION.cff).
No release has been published yet.

## License

Project code is MIT-licensed: see [LICENSE](LICENSE). The Data Carpentry
shell-script adaptation retains its CC BY 4.0 license. Report text, figures
and classroom notes are shared under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), with attribution
to their sources. The raw read subset retains its provider's CC0 dedication;
other external material keeps its original terms. This repository does not
relicense third-party material. See the
[third-party notices](docs/third-party-notices.md).

## Contact

Questions: [open an issue](https://github.com/hzzzzzhappy/ltee-project/issues)
or email hanzhe.liang@mbzuai.ac.ae. See [CONTRIBUTING.md](CONTRIBUTING.md)
for changes and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for participation.
