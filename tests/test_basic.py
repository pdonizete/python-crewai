import importlib


def test_package_import():
    module = importlib.import_module("crewai")
    assert hasattr(module, "__path__")

