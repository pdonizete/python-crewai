# Agent Development Guide

This repository follows the coding standards described in `CONTRIBUTING.md`.
Key points:

- Use PEP 8 style with formatting enforced by **Black**.
- Lint code with **Flake8**.
- Add type hints and docstrings where practical.

## Running Checks

Install development dependencies and run automated checks before committing:

```bash
python -m pip install -r requirements-dev.txt
pre-commit run --all-files
pytest
```

Both `pre-commit` and `pytest` must succeed prior to every commit.

## Developing Locally

The project includes example Flask and Streamlit apps. To run them during
development:

```bash
# Flask app
export FLASK_APP=crewai.flask_app
flask run

# Streamlit app
streamlit run crewai/streamlit_app.py
```

These commands allow you to iterate quickly while building new features.
