import pandas as pd

def load_payments(file_path):
    """
    Load and clean payment data from a CSV file.

    Steps:
    - Normalize column names
    - Filter for successful payments
    - Convert 'created' to datetime
    - Convert 'payment_amount' to numeric
    - Drop rows with invalid or missing values

    Args:
        file_path (str): Path to the CSV input file.

    Returns:
        pd.DataFrame: Cleaned and structured payment data.
    """
    df = pd.read_csv(file_path)
    df.columns = [col.strip().lower() for col in df.columns]
    df = df[df['status'].str.upper() == 'SUCCESSFUL']
    df['created'] = pd.to_datetime(df['created'], errors='coerce')
    df = df.dropna(subset=['created'])
    df['payment_amount'] = pd.to_numeric(df['payment_amount'], errors='coerce')
    df = df.dropna(subset=['payment_amount'])
    return df
