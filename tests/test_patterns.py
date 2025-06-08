from pathlib import Path

from agentes_crewai.analista_de_padroes import AnalistaDePadroes


def test_pattern_metrics(tmp_path: Path):
    test_file = tmp_path / "test_sample.py"
    test_file.write_text(
        "from unittest.mock import Mock\n\n"
        "def test_example():\n"
        "    # TODO: fix later\n"
        "    Mock()\n"
        "    assert True\n"
    )

    helper_file = tmp_path / "helper.py"
    helper_file.write_text("print('hi')\n")

    agent = AnalistaDePadroes()
    metrics = agent.run([test_file, helper_file])

    assert metrics["todo_count"] == 1
    assert metrics["test_file_count"] == 1
    assert metrics["assert_count"] == 1
    assert metrics["mock_usage"] == 1
