import pandas as pd
import os

def generate_payment_type_report(df, output_folder):
    """
    Generate a report of total payment amounts grouped by payment type.

    Args:
        df (pd.DataFrame): Preprocessed payment data.
        output_folder (str): Directory to write the output CSV.
    """
    grouped = (
        df.groupby('payment_type')['payment_amount']
        .sum()
        .reset_index()
    )
    grouped.columns = ['payment_type', 'total_amount']
    grouped = grouped.sort_values(by='payment_type')
    grouped.to_csv(os.path.join(output_folder, "payment_type_report.csv"), index=False)
