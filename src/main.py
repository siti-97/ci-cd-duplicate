import pandas as pd

# This function loads data, removes duplicate rows, and saves the clean version
def load_and_process_data(filepath="data/dataset.csv", output_path="data/processed_dataset.csv"):
    df = pd.read_csv(filepath)
    print(f"Original dataset shape: {df.shape}")
    
    # Remove exact duplicate rows
    df = df.drop_duplicates()
    
    print(f"Dataset shape after removing duplicates: {df.shape}")
    
    # Save the cleaned data without row numbers (index=False)
    df.to_csv(output_path, index=False)
    return df
