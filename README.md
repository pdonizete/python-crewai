# Projeto de Demonstração CrewAI

## Visão Geral
Este repositório fornece um exemplo mínimo de como organizar um projeto Python que cria "crews" de IA compostas de agentes, tarefas e ferramentas. O objetivo é oferecer um ponto de partida para experimentar os conceitos do CrewAI e estendê-los para suas próprias aplicações.

## Estrutura de Pastas
- `crewai/` – Pacote fonte de todo o código
  - `agents/` – definições de agentes
  - `tasks/` – implementações de tarefas
  - `tools/` – ferramentas reutilizáveis
- `tests/` – testes unitários
- `requirements.txt` – dependências de execução
- `requirements-dev.txt` – ferramentas de desenvolvimento e testes
- `CONTRIBUTING.md` – diretrizes de contribuição
- `LICENSE` – licença do projeto (Apache 2.0)

## Instalação
1. Crie e ative um ambiente virtual Python.
2. Instale as dependências de execução:
   ```bash
   pip install -r requirements.txt
   ```
3. Para desenvolvimento ou para executar a suíte de testes, instale as ferramentas adicionais:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Uso
Os módulos em `crewai/` atualmente contêm placeholders. Expanda esses módulos com suas próprias classes de agentes, tarefas e ferramentas e então importe-os em seus projetos.

### Executando os Testes
Execute a suíte de testes com:
```bash
pytest
```

## Contribuindo
Pull requests são bem-vindos! Leia o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para informações sobre estilo de código e verificações automáticas antes de abrir um PR.

## Licença
Este projeto está licenciado sob a Licença Apache 2.0. Veja o arquivo `LICENSE` para detalhes.
