# Terminal walkthrough through Lesson 04

Completed on 2026-10-28 using terminal commands. This records the LTEE
course exercises; it does not represent participation in the paper-sketch
or peer-discussion activities, or completion of an independent capstone.

Sources: [Lesson 02](https://khanlab.bio/cbio7501-f26/pages/02-project-organization.html),
[Lesson 03](https://khanlab.bio/cbio7501-f26/pages/03-data-management.html),
[Lesson 04](https://khanlab.bio/cbio7501-f26/pages/04-git.html).
The Lesson 03 and 04 instructions were retrieved with `curl` on 2026-10-28.
The existing repository and its initial scaffold commit were retained.

## Lesson 03: verified data management

- Recorded the source URLs and provider MD5 values in `metadata/sources.tsv`.
- Downloaded `sub.tar.gz` and the compressed REL606 reference with `curl`.
  Their MD5 values matched `e1294a9201359d4341856bcc735929d3` and
  `84ac547b7fa22c6291aa519f2d1ce444`, respectively.
- Extracted the six FASTQ files and removed the temporary archive.
- Checked all seven retained files against `metadata/checksums.sha256` with
  `shasum -a 256 -c`, the course's macOS alternative to `sha256sum`.
- Removed write permissions with `chmod a-w` and verified the sample sheet's
  six FASTQ paths exist. Added the sample dictionary and data availability
  statement.
- Ran the course download script both normally and with `--verify-only`.
- Attempted to append to the read-only reference: permission was denied.
  After deliberately allowing a write and appending one byte, SHA-256
  verification failed. Re-downloading the reference restored its checksum;
  write protection was reapplied and all seven files passed again.

The FAIR/CARE discussion responses and source checks are in
[data-management-notes.md](data-management-notes.md).

## Lesson 04: Git and GitHub

| Section | Actual operation and evidence |
|---|---|
| 1–3. Setup, tracking and commit | Confirmed the repository author; checked `.gitignore`; ran `pixi lock` (already up to date); committed the download script and metadata in `8264035`. Raw files remained untracked. |
| 4. Change and inspect | Used `git status`, `git diff` and `git diff --staged`; committed the README purpose sentence in `d23fe6b`. Staged the metadata note and analysis-notes file separately, creating `29bd77f` and `5d2c70e`. |
| 5–6. History and remote | Inspected `git log`, `git show --stat` and per-file history; checked the HTTPS remote and pushed `main` to the public repository. |
| 7. Branches | Created `add-decision-log`, committed `73a7a4e`, fast-forward merged it into `main`, and deleted the branch. |
| 8. Merge conflict | Created `depth-5` and `depth-10` from the same base. Merging the second produced exit code 1 and `UU docs/decisions.md`. Inspected the conflict markers and index stages; resolved to comparing depth 2 and 10. Commit `830a162` has two parents and no unresolved paths. Deleted the exercise branches and pushed. |
| 9. Pull request | Pushed `lesson-04-readme`, opened [PR #1](https://github.com/hzzzzzhappy/ltee-project/pull/1) with `gh pr create`, inspected `gh pr diff`, `gh pr checks` and the Actions log. Both checks passed before `gh pr merge --merge`. Pulled merge commit `d7b95e0`, removed the remote/local branch and pruned remote references. |
| 10. Tag | Created and pushed the annotated [`lesson-04` tag](https://github.com/hzzzzzhappy/ltee-project/tree/lesson-04) on `d7b95e0`, after merging the PR. |
| Try it yourself | Used per-file history and `git show 830a162~1:docs/decisions.md` to read the previous depth-5 version. Cloned the real GitHub repository into a temporary directory: only `data/raw/README.md` was present. Verification failed on all seven missing raw files, as expected. Then the download script fetched and verified all seven files, left the tracked tree clean, and the temporary clone was removed. |
| Break it | Deleted `scripts/download_data.py` and `metadata/samples.tsv` and committed `45fa26b`. Restored them from `HEAD~1`, inspected their untracked status, and committed `f7cb745`. Both restored Git blob IDs exactly matched their pre-deletion values; the restored script verified all seven raw files successfully. |

Ada and Ben in the decision-log conflict are simulated roles from the course,
not other collaborators. The deletion/restoration exercise follows the tag
in the current lesson; the tag is therefore retained at the merged-PR checkpoint.

## Checks and scope

The PR checks succeeded:
[push check](https://github.com/hzzzzzhappy/ltee-project/actions/runs/40700634712)
and [pull-request check](https://github.com/hzzzzzhappy/ltee-project/actions/runs/40700645194).
The log shows Pixi using the locked environment and running the placeholder
`reproduce` task. Full variant calling belongs to later lessons and has not
been run. The fresh-clone exercise separately verified data retrieval.

The repository has an annotated course tag, not a published release.
The independent capstone still requires the owner's research question and
specific data source, size, license and intended output.
