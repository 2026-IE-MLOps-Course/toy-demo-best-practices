import pytest

from src.load_data import load_data


def test_load_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError, match="Check paths.raw_data"):
        load_data(tmp_path / "nope.csv")


def test_load_reads_rows(tmp_path):
    csv = tmp_path / "x.csv"
    csv.write_text("a,b\n1,2\n", encoding="utf-8")
    assert len(load_data(csv)) == 1
