# Lesson 03: FAIR, CARE and data-sharing notes

These are sample discussion responses prepared alongside the terminal exercises,
not a record of classroom participation. The questions come from
[CBIO7501 Lesson 03](https://khanlab.bio/cbio7501-f26/pages/03-data-management.html).
The repository records cited below were checked through their APIs with `curl`
on 2026-10-28. No personal capstone topic has been assumed.

## A1. Scotland wastewater data: FAIR assessment

The [Zenodo concept record](https://doi.org/10.5281/zenodo.6339631) resolved to
[version V1.2](https://doi.org/10.5281/zenodo.6349579). Its API reports open
access, CC BY 4.0, authors, keywords and links to the associated paper and a
specific GitHub code version. The downloadable ZIP was retrieved without an
account and inspected in memory; it contains CSV data, a column-level README
and analysis scripts.

| Principle | Evidence of meeting it | Practical improvement |
|---|---|---|
| Findable | Concept and version DOIs, title, named creators, keywords and a description identify the dataset. | Add more specific, standardized subject terms alongside the broad wastewater/COVID keywords to improve machine discovery. |
| Accessible | An HTTPS endpoint supplied the archive without authentication; the API exposes the file size and checksum. | Offer the principal CSV and data dictionary as separate downloads, so reuse does not require extracting the full code-and-data ZIP. |
| Interoperable | Data are CSV; the README defines columns, units, date formats and missing-value meanings. | Add a machine-readable schema and stable site identifiers. The README currently describes `Site` as a treatment-centre name, which makes linking across datasets harder than a persistent identifier would. |
| Reusable | The record specifies CC BY 4.0, versions the archive and links to a code revision and publication; the README explains transformations and fields. | Replace the archived README's `XXX` paper-link placeholder with the published article DOI already present in the record metadata. |

These suggestions concern documentation and access; they are not a claim that
the dataset is unusable. For an analysis, cite the version DOI as well as the
concept DOI so the exact archived input can be identified.

## A2. LTEE example data: strengths and missing context

The [figshare API record](https://api.figshare.com/v2/articles/7726454) identifies
version 3, DOI `10.6084/m9.figshare.7726454.v3`, with a CC0 license. Its
`sub.tar.gz` entry has an HTTPS download URL, size 115,114,554 bytes, and MD5
`e1294a9201359d4341856bcc735929d3`, matching the course's source manifest.
Persistent identifiers support findability; an open download supports access;
FASTQ is a standard sequencing format; the license and links to the original
study support reuse.

The record alone does not fully map the six subset files to clone, population
and generation, or document the exact trimming and subsampling procedure. Reuse
therefore also needs the course sample sheet, Data Carpentry provenance, pairing
information and a description of how the subset was produced. Recording sources,
provider MD5 values, retained-file SHA-256 values and column definitions in
`metadata/` preserves that information with the download script.

One provenance detail needs care: the figshare description names BioProject
`PRJNA294072`, whereas the course names `PRJNA295606` for the selected runs.
The individual ENA run records resolve this: all three selected runs belong to
`PRJNA295606` / `SRP064605`. The course identifier is retained.

| Run | ENA sample accession |
|---|---|
| [SRR2589044](https://www.ebi.ac.uk/ena/portal/api/filereport?accession=SRR2589044&result=read_run&fields=run_accession,study_accession,secondary_study_accession,sample_accession&format=tsv) | SAMN04096081 |
| [SRR2584863](https://www.ebi.ac.uk/ena/portal/api/filereport?accession=SRR2584863&result=read_run&fields=run_accession,study_accession,secondary_study_accession,sample_accession&format=tsv) | SAMN04096083 |
| [SRR2584866](https://www.ebi.ac.uk/ena/portal/api/filereport?accession=SRR2584866&result=read_run&fields=run_accession,study_accession,secondary_study_accession,sample_accession&format=tsv) | SAMN04096085 |

## A3. Indigenous-community microbiome scenario

The proposed SRA deposition supports several FAIR properties: accessions,
standard formats, discoverable metadata and a retrieval route. Individual written
consent does not by itself settle the community-governance questions raised by
CARE. A suitable discussion response addresses all four principles:

- **Collective benefit:** agree with the community what useful results, training
  or other benefits the project should return.
- **Authority to control:** involve the community in decisions about access,
  future reuse and the conditions attached to sharing.
- **Responsibility:** define who maintains the data and communicates findings
  back in an accessible language and format.
- **Ethics:** consider harms to the community as well as individuals. Publicly
  naming the village can expose a group; microbiome reads may also include human
  DNA. Address these issues before deposition.

Agree governance and permitted uses before collection, minimize unnecessary
identifying metadata, and choose open or controlled access consistent with those
agreements. Document the access conditions and how applications are decided.
FAIR allows a clear, controlled-access procedure; it does not require every file
to be public. These points apply to the course's hypothetical scenario, not to
the laboratory *E. coli* data in this project.

## Discussion: a 200-person rare-disease sequencing study

Analysis code, environment specifications and an empty metadata schema can
usually be shared openly after checking that they contain no participant data.
Individual FASTQ files, variant calls and a participant-level sheet linking age,
sex and hospital need an appropriate controlled-access route under the study's
consent and governance arrangements. Removing names alone does not establish
that these records are safe to publish. Cohort allele frequencies also need
review: a small rare-disease cohort or very rare variants can reveal information
about individuals, so aggregation is not automatically sufficient.

An example data-availability statement should identify the actual repository and
accession, the access committee or application process, and the consent-related
conditions. It should separately link public code, the environment, a metadata
schema and any reviewed aggregate results. Those fields would be filled with
verified details from the hypothetical study; no accession or approval is invented
here.

For this LTEE project, the README's data-availability statement instead points to
the public runs, the CC0 teaching subset, the reference genome and the download
script. Derived results should be claimed reproducible only when the later
analysis workflow has been implemented and checked.
