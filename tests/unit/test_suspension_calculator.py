import pandas as pd
from datetime import datetime
from src.suspension_calculator import calculate_days_from_suspension

def test_calculate_days_from_suspension():
    """
    Test correct calculation of days from suspension based on the most recent payment date.
    """
    df = pd.DataFrame({
        'device_id': [1],
        'created': pd.to_datetime(['2024-01-01']),
        'status': ['SUCCESSFUL']
    })
    today = datetime(2024, 3, 1).date()
    result = calculate_days_from_suspension(df, today)
    assert result.iloc[0]['days_from_suspension'] == 30

def test_suspension_ignores_failed_payments():
    """
    Test that failed payments are excluded from the suspension calculation.
    """
    df = pd.DataFrame({
        'device_id': [1, 1, 2],
        'created': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-03-01']),
        'status': ['SUCCESSFUL', 'FAILED', 'SUCCESSFUL']
    })
    today = datetime(2024, 3, 15).date()
    result = calculate_days_from_suspension(df, today)
    assert 1 in result['device_id'].values
    assert result.shape[0] == 2

