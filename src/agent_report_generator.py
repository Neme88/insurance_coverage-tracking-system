import pandas as pd
import os

def generate_agent_collection_report(df, output_folder):
    """
    Generate a report of total collections grouped by agent, date, and payment type.

    Args:
        df (pd.DataFrame): Preprocessed payment data.
        output_folder (str): Directory to write the output CSV.
    """
    df['date'] = df['created'].dt.date
    grouped = (
        df.groupby(['agent_user_id', 'date', 'payment_type'])['payment_amount']
        .sum()
        .reset_index()
    )
    grouped = grouped.sort_values(by=['agent_user_id', 'date'])
    grouped.to_csv(os.path.join(output_folder, "agent_collection_report.csv"), index=False)

