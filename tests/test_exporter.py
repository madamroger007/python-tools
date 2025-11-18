import pytest
from tools_managed_file.exporter import export_dataset

def test_export_dataset(tmp_path):
    data = [{"name": "Adam", "age": 20}]
    output = tmp_path / "data.csv"

    export_dataset(data, output)

    assert output.exists()
    content = output.read_text()

    assert "Adam" in content
    assert "20" in content

def test_export_empty_dataset(tmp_path):
    output = tmp_path / "empty.csv"

    with pytest.raises(ValueError):
        export_dataset([], output)
