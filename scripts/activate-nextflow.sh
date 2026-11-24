# Quote Bioconda's embedded path in a generated launcher, outside its package files.
if [ -f "$CONDA_PREFIX/bin/nextflow" ]; then
    python "$PIXI_PROJECT_ROOT/scripts/prepare_nextflow_launcher.py" \
        "$CONDA_PREFIX/bin/nextflow" "$CONDA_PREFIX/.nextflow-compat/nextflow"
    export PATH="$CONDA_PREFIX/.nextflow-compat:$PATH"
fi
