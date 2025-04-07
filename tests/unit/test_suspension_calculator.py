import pandas as pd
from datetime import datetime
from suspension_calculator import generate_days_from_suspension_report

def test_suspension_days_calculation(tmp_path):
    """
    Test that suspension days are correctly calculated based on:
    - last payment coverage ending
    - system rule: suspension = 91st day after last covered date

    Asserts:
        - Output CSV has correct device ID and suspension days.
        - Calculated suspension days match expectation.
    """
    df = pd.DataFrame({
        'device_id': [1],
        'created': pd.to_datetime(['2024-01-01']),
        'payment_amount': [100],
        'status': ['SUCCESSFUL'],
        'agent_user_id': [1],
        'payment_type': ['CASH']
    })
    today = datetime(2024, 3, 1).date()
    generate_days_from_suspension_report(df, tmp_path, today)
    result = pd.read_csv(tmp_path / "days_from_suspension_report.csv")

    assert 'device_id' in result.columns
    assert 'days_from_suspension' in result.columns
    assert result.iloc[0]['days_from_suspension'] == 30


