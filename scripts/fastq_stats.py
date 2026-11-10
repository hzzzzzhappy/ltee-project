"""Summaries for the trimmed, four-line FASTQ files in the LTEE teaching data.

Adapted from CBIO7501 Lesson 07 (Aziz Khan and course contributors, MIT).
https://khanlab.bio/cbio7501-f26/pages/07-quarto.html
"""
from itertools import islice
from pathlib import Path

import pandas as pd


def read_fastq(path, max_reads=None):
    """Yield the sequence and Phred+33 quality string for each sampled read."""
    with open(path, encoding="ascii") as stream:
        records = iter(lambda: list(islice(stream, 4)), [])
        for number, record in enumerate(islice(records, max_reads), start=1):
            if len(record) != 4 or not record[0].startswith("@") or not record[2].startswith("+"):
                raise ValueError(f"Invalid FASTQ record {number} in {path}")
            sequence = record[1].rstrip("\r\n")
            quality = record[3].rstrip("\r\n")
            if not sequence or len(sequence) != len(quality):
                raise ValueError(f"Sequence and quality lengths differ or are empty at record {number} in {path}")
            yield sequence, quality


def count_reads(path):
    """Count every read in one four-line FASTQ file."""
    with open(path, encoding="ascii") as stream:
        count, remainder = divmod(sum(1 for _ in stream), 4)
    if remainder:
        raise ValueError(f"Incomplete four-line record in {path}")
    return count


def summarize(path, max_reads=20000):
    """Count the full file and summarize bases in its first max_reads records."""
    sampled = bases = gc = quality_sum = 0
    for sequence, quality in read_fastq(path, max_reads):
        sampled += 1
        bases += len(sequence)
        sequence = sequence.upper()
        gc += sequence.count("G") + sequence.count("C")
        quality_sum += sum(quality.encode("ascii")) - 33 * len(quality)
    if sampled == 0:
        raise ValueError(f"No reads sampled from {path}")
    return {"file": Path(path).name, "reads": count_reads(path),
            "mean_length": bases / sampled, "gc_percent": 100 * gc / bases,
            "mean_quality": quality_sum / bases}


def quality_by_position(path, max_reads=20000):
    """Average Phred+33 scores among reads reaching each 1-based position."""
    totals, counts = [], []
    for _, quality in read_fastq(path, max_reads):
        for i, value in enumerate(quality.encode("ascii")):
            if i == len(totals):
                totals.append(0)
                counts.append(0)
            totals[i] += value - 33
            counts[i] += 1
    return pd.Series([total / n for total, n in zip(totals, counts)],
                     index=range(1, len(totals) + 1), name=Path(path).name, dtype=float)
