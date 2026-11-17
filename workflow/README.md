# workflow

`Snakefile` covers Lesson 09, sections 1–9: reference preparation, alignment,
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
`pixi run reproduce` still runs the original shell pipeline and the Quarto
report; switching it to Snakemake comes in section 11.

The Nextflow workflow is introduced in Lesson 10.
