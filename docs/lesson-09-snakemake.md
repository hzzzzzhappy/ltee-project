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

## 17 November — sections 8–9

Added `depth_sensitivity` to filter each sample at the thresholds in
`sensitivity_depths`. The 12 output VCFs were readable; each retained record
met its depth threshold. Higher-depth outputs were subsets of lower-depth
outputs, and depth 2 matched the existing final VCF records.

| Sample | Depth 2 | Depth 5 | Depth 10 | Depth 15 |
|---|---:|---:|---:|---:|
| SRR2584863 | 25 | 22 | 16 | 4 |
| SRR2584866 | 775 | 723 | 415 | 123 |
| SRR2589044 | 10 | 8 | 5 | 1 |

Added `rule all` with `default_target: True`. It requests the MultiQC report,
three final VCFs, six statistics files and 12 sensitivity VCFs: 22 outputs.
All exist, and running the workflow with no named target found everything
up to date. The rule graph is in `results/rulegraph.svg`.

```bash
pixi run -e pipeline snakemake -c 4
pixi run -e pipeline snakemake -n
```

These commands now use the complete default target. `pixi run reproduce`
still uses the shell workflow; switching it to Snakemake is section 11.
All seven raw-file SHA-256 checks still pass.

## 17 November — section 10

Added `scripts/compare_vcfs.py` and compared the variant records with the
archived shell outputs. All records matched exactly for the three samples
(25, 775 and 10 variants). Headers are excluded because they include run dates
and commands. The script also checks for file names missing from either side.

```bash
pixi run python scripts/compare_vcfs.py results/shell-script/vcf results/vcf
```

Before changing the depth to 10, predicted three `filter` jobs, three
`variant_stats` jobs and `all`. The dry run matched that prediction; alignment,
calling, QC and the sensitivity outputs did not need to rerun. Restored the
original config bytes (minimum depth 2), then checked that the default target
was up to date. The depth-10 change was a dry run only.

## 18 November — sections 11–12

Added Pixi tasks for Snakemake and comparison with the shell workflow.
`reproduce` now follows download → Snakemake → report. The shell task writes
to `results/shell-script/`. PyYAML is an explicit dependency of the report.

```bash
pixi run reproduce
pixi run compare-to-shell
```

The comparison task reran both versions as needed and matched every VCF
record (25, 775 and 10). Moved generated outputs aside, then ran `reproduce`
with no generated reference, workflow state or result files in place. All
49 jobs completed, followed by the report. Its variant table, sensitivity
table, figure alt text and decision were checked against the output files.
The earlier outputs remain in a local backup outside the repository.

The report keeps minimum depth 2 for comparison with Data Carpentry and
shows depths 2, 5, 10 and 15. Absolute counts depend on the cutoff. At each
cutoff, the last clone has more calls than the 15,000-generation clone.
This describes the teaching subset rather than a complete mutation rate.

After a real four-minute interval, ran the section 12 checks. `snakefmt
--check` passed. `snakemake --lint` returned 1 with two types of suggestions:
small rules without their own log directive, and rules without separate
Conda/container environments. The course uses one Pixi-locked environment
for all rules; larger workflows may need separate environments. Tool logs
are already recorded for alignment, pileup, FastQC and MultiQC.

### Break it: threads and batch size

Saved trusted VCFs, ran with four cores and an empty `bwa_extra`, and compared
records. SRR2584863 and SRR2589044 were identical. SRR2584866 still had 775
variants, but four trusted records were replaced by four different records.
The count alone would have missed the difference. Restored the configured
`-K 10000000` and rebuilt the downstream results; every VCF record matched
the trusted set again. Re-rendered the report and verified the raw checksums.

### Optional cluster exercise

Section 13 requires a Slurm cluster, project account and partition. This Mac
has no `sbatch` or `srun`, so no cluster execution was performed. The local
workflow and required LTEE exercises through section 12 are complete.
