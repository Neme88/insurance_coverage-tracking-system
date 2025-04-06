import pandas as pd
from datetime import datetime
from src.agent_report_generator import group_by_agent_day_payment

def test_group_by_agent_day_payment():
    df = pd.DataFrame({
        'created': pd.to_datetime(['2024-01-01 09:00', '2024-01-01 10:00']),
        'status': ['SUCCESSFUL', 'SUCCESSFUL'],
        'agent_user_id': [1, 1],
        'payment_type': ['CASH', 'CASH'],
        'payment_amount': [50, 70]
    })
    result = group_by_agent_day_payment(df)
    assert result.loc[0, 'total_amount'] == 120 or result['payment_amount'].sum() == 120
