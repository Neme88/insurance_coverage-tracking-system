import pandas as pd

def load_payments(file_path):
    df = pd.read_csv(file_path)
    df.columns = [col.strip().lower() for col in df.columns]
    df = df[df['status'].str.upper() == 'SUCCESSFUL']
    df['created'] = pd.to_datetime(df['created'], errors='coerce')
    df = df.dropna(subset=['created'])
    df['payment_amount'] = pd.to_numeric(df['payment_amount'], errors='coerce')
    df = df.dropna(subset=['payment_amount'])
    return df