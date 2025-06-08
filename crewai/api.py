from __future__ import annotations

from pathlib import Path

from flask import Flask, jsonify, request

from .file_utils import discover_files
from .validation import validate_tests

app = Flask(__name__)


@app.route("/files")
def list_files():
    directory = request.args.get("directory", ".")
    pattern = request.args.get("pattern", "*.py")
    files = [str(p) for p in discover_files(directory, pattern)]
    return jsonify(files)


@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json(force=True) or {}
    files = [Path(f) for f in data.get("files", [])]
    valid = [str(p) for p in validate_tests(files)]
    return jsonify(valid)
