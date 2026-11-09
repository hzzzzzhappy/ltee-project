# LTEE course notes

Hanzhe Liang · CBIO7501

[GitHub](https://github.com/hzzzzzhappy) · hanzhe.liang@mbzuai.ac.ae

Course practice using three *E. coli* samples from the Long-Term Evolution
Experiment. The project now runs from data download to variant calling.

## Run the analysis

With [Pixi](https://pixi.prefix.dev/latest/) installed, run these commands from
the project folder on Linux or macOS:

```bash
pixi install --locked --all
pixi run reproduce
```

This checks the data, runs FastQC and MultiQC, then aligns the reads and calls
variants. Package versions are saved in `pixi.lock`.

- QC report: `results/qc/multiqc/multiqc_report.html`
- Final variants: `results/vcf/`
- Alignment and variant statistics: `results/stats/`

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
