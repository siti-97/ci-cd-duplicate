import sys
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from main import load_and_process_data, validate_dataset

def test_duplicate_removal(tmp_path):
    """Check that duplicate rows are removed correctly."""
    raw_path = Path("data/dataset.csv")
    output_path = tmp_path / "processed_dataset.csv"

    raw_df = pd.read_csv(raw_path)
    cleaned_df = load_and_process_data(raw_path, output_path)

    expected_df = raw_df.drop_duplicates().reset_index(drop=True)

    assert output_path.exists(), "Processed dataset file was not created."
    assert cleaned_df.duplicated().sum() == 0, "Duplicate rows still exist."
    assert len(cleaned_df) == len(expected_df), "Cleaned row count is incorrect."

    pd.testing.assert_frame_equal(
        cleaned_df.reset_index(drop=True),
        expected_df
    )

def test_validation_summary():
    """Check that validation returns basic metrics."""
    raw_df = pd.read_csv("data/dataset.csv")
    validation = validate_dataset(raw_df)

    assert validation["row_count"] > 0
    assert validation["column_count"] == 12
    assert "duplicate_rows" in validation
    assert "total_missing_values" in validation
