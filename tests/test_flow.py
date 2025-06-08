from agentes_crewai import Orquestrador


def test_basic_flow(tmp_path):
    (tmp_path / "code.py").write_text("# TODO: fix\nprint('hi')")
    orq = Orquestrador(str(tmp_path))
    report = orq.run()
    assert "todo_count" in report
    assert "file_count" in report
