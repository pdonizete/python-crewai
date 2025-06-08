"""Minimal Flask API exposing the analysis service."""

from flask import Flask, jsonify, request

from agentes_crewai import Orquestrador

app = Flask(__name__)


@app.route("/analyze", methods=["POST"])
def analyze():
    base_path = request.json.get("path", ".")
    orq = Orquestrador(base_path)
    report = orq.run()
    return jsonify({"report": report})


if __name__ == "__main__":
    app.run(debug=True)
