"""Orchestrator that glues all agents together."""

from pathlib import Path

from .coletor_de_codigo import ColetorDeCodigo
from .analista_de_padroes import AnalistaDePadroes
from .gerador_de_relatorio import GeradorDeRelatorio
from .coletor_de_metricas import ColetorDeMetricas


class Orquestrador:
    """Execute the basic analysis pipeline."""

    def __init__(self, base_path: str) -> None:
        self.coletor = ColetorDeCodigo(base_path)
        self.analista = AnalistaDePadroes()
        self.metricas = ColetorDeMetricas()
        self.relatorio = GeradorDeRelatorio()

    def run(self) -> str:
        arquivos = self.coletor.run()
        dados = self.analista.run(arquivos)
        dados.update(self.metricas.run(arquivos))
        return self.relatorio.run(dados)
