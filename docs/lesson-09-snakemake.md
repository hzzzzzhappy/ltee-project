# Snakemake notes

Hanzhe Liang · 16 November 2026

[Lesson 09](https://khanlab.bio/cbio7501-f26/pages/09-snakemake.html), sections 1–3.

## Environment

Added Snakemake 9.27.1, Graphviz 14.1.2 and snakefmt 2.1.0 to the pipeline
feature. Ran `dot -c` and checked that Graphviz could create an SVG.
BWA, samtools, bcftools, FastQC and MultiQC kept the same versions and builds.
Snakemake needs pandas below version 3, so the pipeline environment now uses
pandas 2.3.3. The default environment used by Quarto did not change.

## Small workflow first

Used a separate `snakemake-practice` folder with `a.txt` and `b.txt`.
A dry run showed the commands without creating the output. After the first
real run, asking for the same target gave `Nothing to be done`.

Changed the rule to use `{name}` and added a concatenation rule. Editing only
`a.txt` rebuilt `a.upper.txt` and `a_b.txt`; `b.upper.txt` kept its timestamp.
The final output was:

```text
THIS IS A CHANGED A.TXT
THIS IS B.TXT
```

The isolated `pixi exec` environment also used Snakemake 9.27.1. Its first
installation attempt hit the open-file limit. Running `ulimit -n 4096` in
that Terminal session allowed the retry to finish.

## Config and saved results

`config/config.yaml` holds the sample sheet, compressed reference and
`bwa_extra: "-K 10000000"`. The batch-size option makes the alignment
independent of thread count. The depth settings will be used in the later
variant-calling sections.

Moved the previous `sam`, `bam`, `bcf`, `vcf`, `stats` and `qc` folders into
`results/shell-script/` to keep them as a comparison baseline. Kept the old processed
reference there too. File sizes and the three final VCF checksums matched
after the move. Raw data stayed in `data/raw/`.
