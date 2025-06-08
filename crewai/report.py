from __future__ import annotations

from typing import Mapping


def generate_report(results: Mapping[str, bool]) -> str:
    """Generate a simple textual report from test ``results``."""
    lines = ["Test Report"]
    for name, passed in results.items():
        status = "PASSED" if passed else "FAILED"
        lines.append(f"{name}: {status}")
    passed_count = sum(1 for p in results.values() if p)
    summary = f"{passed_count}/{len(results)} tests passed."
    lines.append(summary)
    return "\n".join(lines)
