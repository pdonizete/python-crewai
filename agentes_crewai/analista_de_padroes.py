"""Agent responsible for analysing code patterns."""

from typing import List
from pathlib import Path


class AnalistaDePadroes:
    """Naive pattern analyser that counts TODO comments."""

    def run(self, files: List[Path]) -> dict:
        todos = 0
        for file in files:
            try:
                for line in Path(file).read_text().splitlines():
                    if "TODO" in line:
                        todos += 1
            except Exception:
                continue
        return {"todo_count": todos}
