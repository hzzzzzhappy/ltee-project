# Contributing

This is the CBIO7501 LTEE classroom example. Corrections and suggestions
are welcome.

1. Open an issue before making a larger change.
2. Make a branch (or fork the repository) and update the code or notes.
3. Run `pixi run reproduce` and validate `CITATION.cff` with
   `pixi exec --spec cffconvert=2.0.0 cffconvert --validate -i CITATION.cff`.
4. Open a pull request and wait for the Reproduce check to pass before merging.

Keep raw data and generated results out of Git. Commit `pixi.toml` and
`pixi.lock` together when dependencies change, retain source credits, and
record analysis decisions in `docs/decisions.md`.

Please follow [the code of conduct](CODE_OF_CONDUCT.md).
