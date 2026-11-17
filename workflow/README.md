# workflow

`Snakefile` currently covers the reference and alignment steps from
Lesson 09, sections 1–5. From the project root, run:

```bash
pixi run -e pipeline snakemake -c 4 results/bam/SRR2584863.aligned.sorted.bam.bai
```

Add `-n` to preview the work. Settings are in `config/config.yaml` and sample
paths come from `metadata/samples.tsv`. Use an explicit target at this stage;
the full target rule is added later in Lesson 09.

The Nextflow workflow is introduced in Lesson 10.
