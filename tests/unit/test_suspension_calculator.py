import pandas as pd
from datetime import datetime
from src.suspension_calculator import calculate_days_from_suspension

def test_calculate_days_from_suspension():
    df = pd.DataFrame({
        'device_id': [1],
        'created': pd.to_datetime(['2024-01-01']),
        'status': ['SUCCESSFUL']
    })
    today = datetime(2024, 03, 01).date()
    result = calculate_days_from_suspension(df, today)
    assert result.iloc[0]['days_from_suspension'] == 30
