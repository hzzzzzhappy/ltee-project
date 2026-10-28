# Lesson 02: project organization notes

Course: <https://khanlab.bio/cbio7501-f26/pages/02-project-organization.html>

## How files move through the project

```text
metadata/       describes the samples, sources and checksums
     |
data/raw/  -->  data/processed/  -->  results/  -->  reports/
           scripts/ and workflow/ use parameters in config/
           pixi.toml and, later, pixi.lock describe the software
```

This diagram documents the generated layout. The course's initial paper sketch
and discussion are personal learning activities to complete separately.

| Material | Location | Treatment |
|---|---|---|
| Six downloaded FASTQ files | `data/raw/fastq/` (Lesson 03) | Preserve the downloaded files; never edit them by hand. |
| Downloaded reference genome | `data/raw/` | Preserve the original. |
| Sample descriptions, source URLs, checksums | `metadata/` | Small text records, kept with the code. |
| Analysis and download code | `scripts/` | Human-written source, tracked by Git in Lesson 04. |
| Snakemake and Nextflow pipelines | `workflow/` | Track the workflow source. |
| Analysis parameters | `config/` | Track the settings needed to reproduce results. |
| Environment specification and lock | Project root | Track `pixi.toml` and the lock file once generated. |
| Cleaned or intermediate data | `data/processed/` | Rebuild from raw data and code. |
| QC reports, alignments, variants, plots | `results/` | Rebuild from the workflow; do not edit manually. |
| Written report source | `reports/` | Track the source; regenerate rendered reports. |
| README, license and citation metadata | Project root | Keep the project description and attribution current. |

The template separates small, curated `metadata/` records from downloaded data.
Results need no `final/` folder: the code will regenerate them, and Git will
record the history of the code and parameters.

## File-naming exercise

Use sample identifiers first when looking files up by sample, consistent
separators, ISO dates (`YYYY-MM-DD`) and zero-padded sequence numbers.

| Example from the exercise | Problem / revision |
|---|---|
| `12-10-2026 alignment SRR2589044.bam` | Date is ambiguous and the name has spaces. Confirm whether it means 12 October or 10 December before renaming. |
| `2026-10-13_SRR2584866_aligned.bam` | Valid ISO date, but put the sample first if using the sample-first convention: `SRR2584866_2026-10-13_aligned.bam`. |
| `2026-10-9_SRR2584863_aligned.bam` | Pad the day: `SRR2584863_2026-10-09_aligned.bam`. |
| `Final results (use this).xlsx` | Does not identify the content or analysis; replace with a descriptive name once the contents are known. |
| `SRR2584863_aligned_v2.bam` | Use Git for code/parameter history and regenerate the output; reserve version numbers for releases. |
| `sample1.bam`, `sample10.bam`, `sample2.bam` | Lexicographic order is misleading; use `sample01.bam`, `sample02.bam`, …, `sample10.bam`. |

The best of the three CSV choices is `variant-counts_2026-08-05.csv`:
it describes the content, has an ISO date, and contains no spaces.

## Absolute and relative paths: verified exercise

The exercise was run on a temporary copy of this scaffold:

1. An absolute-path script read the first line of `metadata/README.md` successfully.
2. Renaming the project directory caused the unchanged script to raise
   `FileNotFoundError`, because it still pointed to the old directory.
3. A script using `metadata/README.md` as a relative path succeeded from the
   renamed project root.
4. The temporary copy and exercise scripts were removed.

Run future commands from the project root. A path relative to the working
directory remains valid after moving the whole project, provided the internal
layout stays the same.

## Lesson 02 checkpoint

- Generated with the official Cookiecutter template, keeping the default MIT
  license and workflow/container stubs.
- Template source commit: `d62674d4daf195feec6d6043bfeefd661d2f32a4`.
- Main README includes the raw-read DOI, CC0 license and reference accession.
- Author: Hanzhe Liang (`hanzhe.liang@mbzuai.ac.ae`); GitHub: `hzzzzzhappy`.
- At the Lesson 02 checkpoint, data downloading and sample-sheet creation
  were pending Lesson 03; they have since been completed.
- The lock file has been generated in preparation for the first Git commit,
  following Lesson 04.
- Installing the project environment and implementing reproduction belong to
  Lesson 05 and subsequent lessons.
- The independent capstone project still needs a research question, data source,
  data size, data license and expected output supplied by the project owner.

This scaffold does not contain an executed variant-calling analysis or a
published GitHub release.
