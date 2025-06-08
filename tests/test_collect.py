from agentes_crewai.coletor_de_codigo import coletar_python_files


def test_collect_tmp(tmp_path):
    (tmp_path / "a.py").write_text("print('hi')")
    (tmp_path / "b.txt").write_text("ignore")
    files = coletar_python_files(tmp_path)
    assert len(files) == 1
    assert files[0].name == "a.py"
