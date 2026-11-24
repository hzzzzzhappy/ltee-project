# workflow

`Snakefile` covers Lesson 09, sections 1–12: reference preparation, alignment,
variant calling, QC and depth sensitivity. From the project root:

```bash
pixi run -e pipeline snakemake -c 4
pixi run -e pipeline snakemake -n
```

The default `all` target requests the MultiQC report, final variants,
alignment and variant statistics, and sensitivity outputs at every configured
depth. Use `-n` for a dry run. The rule graph is `results/rulegraph.svg`.

Settings are in `config/config.yaml`; sample paths come from
`metadata/samples.tsv`. You can also request individual output files.
`pixi run reproduce` now runs download → Snakemake → Quarto report.
`pixi run compare-to-shell` reruns the original shell workflow in
`results/shell-script/`, checks the Snakemake results, then compares the VCF
records exactly. It excludes headers, which contain run-specific metadata.

`bwa_extra: "-K 10000000"` fixes the BWA batch size across thread counts.
Keep it when changing the number of cores. Formatting can be checked with
`pixi run -e pipeline snakefmt --check workflow/Snakefile`; see the lesson
notes for the reviewed lint suggestions.

`nextflow/main.nf` implements the same pipeline for Lesson 10. Its config
publishes copies under `results/nextflow/` and limits CPU requests to the
available cores. Run it with `pixi run run-nextflow`; compare exact VCF
records with `pixi run compare-workflows`. See
[the Nextflow notes](../docs/lesson-10-nextflow.md) for resume examples.
