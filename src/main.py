import pandas as pd
from pathlib import Path

def validate_dataset(df):
    """Return basic validation results."""
    return {
        "row_count": len(df),
        "column_count": df.shape[1],
        "total_missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }

def create_column_report(df):
    """Create column-level validation report."""
    return pd.DataFrame({
        "column": df.columns,
        "data_type": df.dtypes.astype(str).values,
        "missing_values": df.isna().sum().values,
        "missing_percentage": (df.isna().mean() * 100).round(2).values,
        "unique_values": df.nunique().values
    })

def load_and_process_data(filepath="data/dataset.csv", output_path="data/processed_dataset.csv"):
    """Load data, validate, remove duplicates, validate again, and save output."""
    filepath = Path(filepath)
    output_path = Path(output_path)

    df = pd.read_csv(filepath)

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    raw_validation = validate_dataset(df)
    raw_report = create_column_report(df)
    raw_report.to_csv(reports_dir / "raw_validation_report.csv", index=False)

    cleaned_df = df.drop_duplicates().reset_index(drop=True)

    cleaned_validation = validate_dataset(cleaned_df)
    cleaned_report = create_column_report(cleaned_df)
    cleaned_report.to_csv(reports_dir / "cleaned_validation_report.csv", index=False)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(output_path, index=False)

    print("Raw validation:", raw_validation)
    print("Cleaned validation:", cleaned_validation)
    print(f"Processed dataset saved to: {output_path}")

    return cleaned_df

if __name__ == "__main__":
    load_and_process_data()
