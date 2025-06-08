# Contributing Guide

This project welcomes contributions. The following conventions help maintain consistency across the repository.

## Folder Structure

- `src/` – Python packages and modules.
- `tests/` – Unit tests mirroring the structure under `src/`.
- `docs/` – Project documentation.
- `scripts/` – Utility scripts for development and automation.

## Coding Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for general style conventions.
- Format code with [Black](https://black.readthedocs.io/en/stable/).
- Lint with [Flake8](https://flake8.pycqa.org/en/latest/).
- Include type hints where practical and document functions with docstrings.

## Automated Checks

Install development dependencies and run automated checks before committing:

```bash
python -m pip install -r requirements-dev.txt
pre-commit install
pre-commit run --all-files
pytest
```

`pre-commit` runs Black and Flake8, ensuring consistent formatting and linting. `pytest` executes all tests in the `tests/` folder.

