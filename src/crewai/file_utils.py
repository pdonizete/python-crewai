from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Optional


def discover_files(
    directory: str | Path,
    pattern: str = "*.py",
    *,
    exclude: Optional[Iterable[str]] = None,
) -> List[Path]:
    """Return a list of files matching ``pattern`` under ``directory``.

    Parameters
    ----------
    directory:
        Base directory to search.
    pattern:
        Glob pattern to match files. Defaults to ``"*.py"``.
    exclude:
        Optional iterable of file names to exclude from results.
    """
    base = Path(directory)
    files = list(base.rglob(pattern))
    if exclude:
        exclude_set = set(exclude)
        files = [f for f in files if f.name not in exclude_set]
    return [f for f in files if f.is_file()]
