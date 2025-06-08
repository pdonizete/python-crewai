from __future__ import annotations

from pathlib import Path
from typing import Iterable, List


def is_valid_test_file(path: Path) -> bool:
    """Return True if ``path`` represents a valid pytest file."""
    return path.name.startswith("test_") and path.suffix == ".py"


def validate_tests(paths: Iterable[Path]) -> List[Path]:
    """Return only valid test files from ``paths``."""
    return [p for p in paths if is_valid_test_file(p)]
