# workflow

`Snakefile` covers the reference, alignment, variant calling and QC steps
from Lesson 09, sections 1–7. Run from the project root.

For variant and alignment statistics for one sample:

```bash
pixi run -e pipeline snakemake -c 4 results/stats/SRR2584863.flagstat.txt results/stats/SRR2584863.bcftools-stats.txt
```

For FastQC on all six FASTQs and their MultiQC summary:

```bash
pixi run -e pipeline snakemake -c 4 results/qc/multiqc/multiqc_report.html
```

Add `-n` to preview the work. Settings are in `config/config.yaml`; sample
paths come from `metadata/samples.tsv`. Until the full target rule is added
in section 9, request explicit output files. `pixi run reproduce` still
runs the original shell pipeline and the Quarto report.

The Nextflow workflow is introduced in Lesson 10.
