import pandas as pd
import os
from datetime import timedelta

def generate_days_from_suspension_report(df, output_folder, today):
    device_days = []

    for device_id, group in df.groupby('device_id'):
        group_sorted = group.sort_values(by='created')
        coverage_end = None

        for _, row in group_sorted.iterrows():
            payment_date = row['created'].date()
            if coverage_end is None or payment_date > coverage_end:
                coverage_start = payment_date
            else:
                coverage_start = coverage_end + timedelta(days=1)
            coverage_end = coverage_start + timedelta(days=29)

        if coverage_end is None:
            days_from_suspension = 0
        else:
            suspension_date = coverage_end + timedelta(days=61)
            days_from_suspension = max((suspension_date - today).days, 0)

        device_days.append((device_id, days_from_suspension))

    result_df = pd.DataFrame(device_days, columns=['device_id', 'days_from_suspension'])
    result_df = result_df.sort_values(by='days_from_suspension', ascending=False)
    result_df.to_csv(os.path.join(output_folder, "days_from_suspension_report.csv"), index=False)
