import pandas as pd
from src.payment_type_report_generator import calculate_total_per_payment_type

def test_calculate_total_per_payment_type():
    df = pd.DataFrame({
        'payment_type': ['CASH', 'CARD'],
        'payment_amount': [100, 200],
        'status': ['SUCCESSFUL', 'SUCCESSFUL']
    })
    result = calculate_total_per_payment_type(df)
    assert 'payment_type' in result.columns
    assert result['payment_amount'].sum() == 300
