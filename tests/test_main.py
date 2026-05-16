import sys
import os
# Help the computer find the code in the 'src' folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

def test_data_quality():
    # 1. Run the cleaning function
    df = load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")

    # 2. Check for Duplicates (Post-cleaning check)
    assert df.duplicated().sum() == 0, "Error: Duplicates were not removed!"

    # 3. Check for Data Loss (Integrity check)
    # If the original file had 1000 rows and 50 were duplicates,
    # we expect exactly 950 rows.
    assert len(df) > 0, "Error: The cleaned file is empty!"

    print("Post-cleaning validation successful!")
