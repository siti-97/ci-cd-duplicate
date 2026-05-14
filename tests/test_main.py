import sys
import os

# Help Python find the main.py file in the folder next door
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

# This test checks if the duplicate removal actually worked
def test_no_duplicates():
    # Run the function and save a temporary test file
    df = load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")
    
    # Assert demands that the total number of duplicate rows is exactly 0
    assert df.duplicated().sum() == 0, "Error: Duplicates were not removed!"
