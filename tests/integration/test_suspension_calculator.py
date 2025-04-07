import pandas as pd
import tempfile
import os
from datetime import datetime

from suspension_calculator import generate_days_from_suspension_report


def test_generate_days_from_suspension_report():
    """
    Integration test: validate that the suspension report CSV is created and contains expected columns.
    """
    df = pd.DataFrame({
        'device_id': [1, 1, 2],
        'created': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-01-15']),
        'payment_amount': [60, 60, 60],
        'status': ['SUCCESSFUL', 'SUCCESSFUL', 'SUCCESSFUL'],
        'agent_user_id': [10, 10, 20],
        'payment_type': ['CASH', 'CASH', 'CASH']
    })

    today = datetime(2024, 3, 1).date()

    with tempfile.TemporaryDirectory() as tmpdirname:
        generate_days_from_suspension_report(df, tmpdirname, today)
        result = pd.read_csv(os.path.join(tmpdirname, "days_from_suspension_report.csv"))

        assert 'device_id' in result.columns
        assert 'days_from_suspension' in result.columns

