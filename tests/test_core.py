from pathlib import Path

import json

from crewai import app, discover_files, generate_report, validate_tests


def test_discover_files(tmp_path: Path):
    (tmp_path / "a.py").write_text("print('a')")
    (tmp_path / "b.txt").write_text("text")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "c.py").write_text("print('c')")

    files = discover_files(tmp_path, pattern="*.py")
    names = sorted(f.name for f in files)
    assert names == ["a.py", "c.py"]

    files = discover_files(tmp_path, pattern="*.py", exclude=["c.py"])
    names = sorted(f.name for f in files)
    assert names == ["a.py"]


def test_validate_tests(tmp_path: Path):
    paths = [
        tmp_path / "test_example.py",
        tmp_path / "example_test.py",
        tmp_path / "test_bad.txt",
    ]
    for p in paths:
        p.write_text("")

    valid = validate_tests(paths)
    assert valid == [paths[0]]


def test_generate_report():
    results = {"test_a": True, "test_b": False}
    report = generate_report(results)
    assert "test_a: PASSED" in report
    assert "test_b: FAILED" in report
    assert "1/2 tests passed" in report


def test_flask_endpoints(tmp_path: Path):
    (tmp_path / "test_api.py").write_text("print('hello')")
    client = app.test_client()

    res = client.get(
        "/files", query_string={"directory": str(tmp_path), "pattern": "*.py"}
    )
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data == [str(tmp_path / "test_api.py")]

    res = client.post(
        "/validate",
        json={
            "files": [
                str(tmp_path / "test_api.py"),
                str(tmp_path / "notest.txt"),
            ],
        },
    )
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data == [str(tmp_path / "test_api.py")]
