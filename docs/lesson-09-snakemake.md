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

## 17 November — sections 4–5

Rebuilt the Snakefile setup from the config file and sample sheet. Restricted
the sample wildcard to the three run IDs and checked every mate path.

The alignment target for section 5 is:

```bash
pixi run -e pipeline snakemake -c 4 results/bam/SRR2584863.aligned.sorted.bam.bai
```

The rules follow the course sequence: decompress the reference, index it,
align one sample, convert SAM to BAM, sort and index. The old generated
alignment files are kept outside the repository so this run can start
without those outputs. The shell-script comparison baseline stays in
`results/shell-script/`.

All six jobs ran successfully on 17 November. The sorted BAM passed
`samtools quickcheck`, the index was readable, and there were 350,000 primary
records. Snakemake removed the temporary SAM and unsorted BAM; a second dry
run reported `Nothing to be done`. The job graph is in `results/dag.svg`.
All seven raw-file checksums and the archived VCF checksums still match.

## 17 November — sections 6–7

Added `flagstat`, `mpileup`, `call`, `filter` and `variant_stats` rules.
The filter reads `min_depth` from the config. With depth 2, the three samples
produced 25, 775 and 10 variants for SRR2584863, SRR2584866 and SRR2589044.
The VCFs were readable, the statistics were present and the temporary raw
BCFs were removed. Repeating the requested targets needed no work.

To request variant and alignment statistics for one sample:

```bash
pixi run -e pipeline snakemake -c 4 results/stats/SRR2584863.flagstat.txt results/stats/SRR2584863.bcftools-stats.txt
```

Added one FastQC job per sample and mate, then used `expand()` to pass all
six ZIP files to MultiQC. To build the QC report:

```bash
pixi run -e pipeline snakemake -c 4 results/qc/multiqc/multiqc_report.html
```

All seven QC jobs completed. Each FASTQ contained 175,000 sequences and
MultiQC included the six correct input files. Base-quality and adapter
checks passed in all six. Sequence content had warnings or failures; GC
content and length distribution had warnings. These remain in the reports.
The second dry run needed no work. All seven raw-file checksums still match.

The rules now cover sections 1–7. Use explicit output targets for now;
the full target rule and the switch of `reproduce` to Snakemake are later
lesson steps.
