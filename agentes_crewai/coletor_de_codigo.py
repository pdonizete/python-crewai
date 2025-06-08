"""Agent responsible for collecting source files from a directory."""

from pathlib import Path
from typing import List


def coletar_python_files(path: str) -> List[Path]:
    """Collect python files recursively under *path*."""
    base = Path(path)
    return list(base.rglob("*.py"))


class ColetorDeCodigo:
    """Simple code collector agent."""

    def __init__(self, base_path: str) -> None:
        self.base_path = base_path

    def run(self) -> List[Path]:
        return coletar_python_files(self.base_path)
