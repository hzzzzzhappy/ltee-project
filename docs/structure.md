# Project structure

| Folder | Contents | Tracking |
|--------|----------|----------|
| `data/raw/` | Downloaded reference and reads | Read-only; not committed |
| `data/processed/` | Decompressed reference and indexes | Rebuilt; not committed |
| `metadata/` | Samples, sources, checksums and data dictionary | Committed |
| `scripts/` | Download, comparison and analysis helpers | Committed |
| `config/` | Shared workflow settings | Committed |
| `workflow/` | Snakemake and Nextflow workflows | Committed |
| `notebooks/` | Read exploration | Source committed; outputs cleared |
| `reports/` | Quarto source and references | Source committed; generated report excluded |
| `results/` | Workflow outputs | Rebuilt; not committed |
| `docs/` | Classroom notes, decisions and attribution | Committed |
| `envs/` | Environment documentation and exports | See folder README |
| `containers/` | Container recipes and instructions | Committed |
| `.github/workflows/` | Reproduction check | Committed |

`pixi.toml` describes software requirements and tasks; `pixi.lock` fixes the
resolved versions. The Snakemake rules are in `workflow/Snakefile`.
