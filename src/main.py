import pandas as pd

def load_and_process_data(filepath="data/dataset.csv", output_path="data/processed_dataset.csv"):
    # Load the data
    df = pd.read_csv(filepath)
    print(f"Starting rows: {df.shape[0]}")

    # Remove duplicate rows
    df = df.drop_duplicates()
    print(f"Final rows: {df.shape[0]}")

    # Save the clean data
    df.to_csv(output_path, index=False)
    return df
