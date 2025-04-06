import pandas as pd
import os

def generate_agent_collection_report(df, output_folder):
    df['date'] = df['created'].dt.date
    grouped = (
        df.groupby(['agent_user_id', 'date', 'payment_type'])['payment_amount']
        .sum()
        .reset_index()
    )
    grouped = grouped.sort_values(by=['agent_user_id', 'date'])
    grouped.to_csv(os.path.join(output_folder, "agent_collection_report.csv"), index=False)
