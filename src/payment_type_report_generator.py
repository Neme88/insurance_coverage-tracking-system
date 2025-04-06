import pandas as pd

def generate_payment_type_report(df, output_folder):
    grouped = (
        df.groupby('payment_type')['payment_amount']
          .sum()
          .reset_index()
    )
    grouped = grouped.sort_values(by='payment_type')
    grouped.to_csv(f"{output_folder}/payment_type_report.csv", index=False)