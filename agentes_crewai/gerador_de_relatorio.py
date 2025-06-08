"""Agent responsible for generating text reports."""

from typing import Dict


class GeradorDeRelatorio:
    """Return a simple formatted report from metrics."""

    def run(self, metrics: Dict[str, int]) -> str:
        lines = ["Relatório de Análise:"]
        for k, v in metrics.items():
            lines.append(f"- {k}: {v}")
        return "\n".join(lines)
