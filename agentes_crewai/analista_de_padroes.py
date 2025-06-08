"""Agent responsible for analysing code patterns."""

from typing import Dict, List
from pathlib import Path

from crewai.validation import is_valid_test_file


class AnalistaDePadroes:
    """Analyse test files and collect simple quality metrics."""

    def run(self, files: List[Path]) -> Dict[str, int]:
        """Return a dictionary with metrics extracted from ``files``.

        Parameters
        ----------
        files:
            List of paths to analyse.
        """

        metrics = {
            "todo_count": 0,
            "test_file_count": 0,
            "assert_count": 0,
            "mock_usage": 0,
        }

        for file in files:
            path = Path(file)
            try:
                text = path.read_text()
            except Exception:
                continue

            metrics["todo_count"] += text.count("TODO")

            if is_valid_test_file(path):
                metrics["test_file_count"] += 1

            metrics["assert_count"] += text.count("assert")

            if any(keyword in text for keyword in ["Mock", "mock", "patch"]):
                metrics["mock_usage"] += 1

        return metrics
