"""Quote paths in the Bioconda launcher on macOS.

Writes a local compatibility copy; the installed package is left unchanged.
"""
from pathlib import Path
import re
import shlex
import sys

source, target = map(Path, sys.argv[1:])
text = source.read_text()
dist = source.parent.parent / "share/nextflow/dist"
text, count = re.subn(r"^NXF_DIST=.*$", lambda _: "NXF_DIST=" + shlex.quote(str(dist)),
                      text, flags=re.MULTILINE)
if count != 1:
    raise RuntimeError("Expected one NXF_DIST assignment in the installed launcher")
old = r'cli=("\"$JAVA_CMD\"" "${JAVA_OPTS[@]}" -jar "$NXF_BIN")'
new = r'''cli=("\"$JAVA_CMD\"")
      for argument in "${JAVA_OPTS[@]}" -jar "$NXF_BIN"; do
          cli+=("$(printf '%q' "$argument")")
      done'''
if old not in text:
    raise RuntimeError("Unrecognised Nextflow modern-launcher argument assembly")
text = text.replace(old, new, 1)
old = 'declare -a cmd_base="(${BASH_REMATCH[1]})"'
if old not in text:
    raise RuntimeError("Unrecognised Java command parsing")
text = text.replace(old, 'declare -a cmd_base=("${BASH_REMATCH[1]}")', 1)
target.parent.mkdir(parents=True, exist_ok=True)
if not target.exists() or target.read_text() != text:
    target.write_text(text)
    target.chmod(0o755)
