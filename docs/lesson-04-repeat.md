# Lesson 04 repeat practice

This is a second, terminal-based pass through the conflict, pull-request,
tag and recovery exercises, starting on 2 November 2026. The original
`main` branch and `lesson-04` tag retain the first completed walkthrough.
The branch `lesson-04-repeat-20261102` acts as the integration branch for
this repeat. Terminal operations are assisted by OpenAI Codex and use
actual commit timestamps. Ada and Ben are the simulated roles in the lesson.

This practice does not run a variant-calling analysis. The Reproduce check
still runs the course's placeholder task.

## Outcomes

- Produced a new depth-5 versus depth-10 conflict, then resolved it in
  merge commit `729e711`, which has two parents. Read the previous version
  of the decision log and removed the merged exercise branches.
- Opened and reviewed [PR #2](https://github.com/hzzzzzhappy/ltee-project/pull/2).
  Both automatic checks passed; the Actions log confirmed the placeholder
  task ran. Merged the PR into the practice branch as `1f1e995`.
- Created the annotated tag `lesson-04-repeat-20261102-checkpoint` at the
  merged-PR checkpoint. The original `lesson-04` tag was not moved.
- Cloned the practice branch from GitHub. Initially, all seven raw data
  files were missing, as expected. Downloaded them and verified all seven
  checksums; downloading left the tracked tree clean.
- Committed deletion of the download script and sample sheet. Restored
  them from the preceding commit and compared their Git blob hashes with
  their originals. Both matched, and the restored script verified the
  seven existing raw files successfully.

The original `main` remains at `4ce01c0`. This repeat is recorded separately
on `lesson-04-repeat-20261102`.
