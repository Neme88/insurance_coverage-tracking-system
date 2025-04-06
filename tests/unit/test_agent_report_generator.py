import pandas as pd
from src.agent_report_generator import group_by_agent_day_payment

def test_group_by_agent_day_payment():
    """
    Test that agent payments are grouped correctly by date and payment type.
    """
    df = pd.DataFrame({
        'created': pd.to_datetime(['2024-01-01 09:00', '2024-01-01 10:00']),
        'payment_amount': [50, 70],
        'status': ['SUCCESSFUL', 'SUCCESSFUL'],
        'agent_user_id': [1, 1],
        'payment_type': ['CASH', 'CASH']
    })
    result = group_by_agent_day_payment(df)
    assert result['payment_amount'].sum() == 120

def test_agent_report_excludes_failed_status():
    """
    Test that agent collection report excludes failed transactions.
    """
    df = pd.DataFrame({
        'created': pd.to_datetime(['2024-01-01 08:00:00', '2024-01-01 09:00:00']),
        'payment_amount': [100, 50],
        'status': ['SUCCESSFUL', 'FAILED'],
        'agent_user_id': [1, 1],
        'payment_type': ['CASH', 'CASH']
    })
    result = group_by_agent_day_payment(df)
    assert result['payment_amount'].sum() == 100

