"""Agent responsible for collecting basic metrics from analysis results."""

from typing import List
from pathlib import Path


class ColetorDeMetricas:
    """Collect metrics about the code base."""

    def run(self, files: List[Path]) -> dict:
        return {"file_count": len(files)}
