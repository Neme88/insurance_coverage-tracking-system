import pandas as pd
from src.payment_type_report_generator import calculate_total_per_payment_type

def test_calculate_total_per_payment_type():
    """
    Test that payment amounts are correctly summed by payment type.
    """
    df = pd.DataFrame({
        'payment_type': ['CASH', 'CARD'],
        'payment_amount': [100, 200],
        'status': ['SUCCESSFUL', 'SUCCESSFUL']
    })
    result = calculate_total_per_payment_type(df)
    assert result['payment_amount'].sum() == 300

def test_payment_type_summary_filters_unsuccessful():
    """
    Test that payment type report excludes non-successful payments.
    """
    df = pd.DataFrame({
        'payment_type': ['CASH', 'CARD', 'BANK'],
        'payment_amount': [100, 200, 300],
        'status': ['SUCCESSFUL', 'FAILED', 'SUCCESSFUL']
    })
    result = calculate_total_per_payment_type(df)
    assert 'CARD' not in result['payment_type'].values
    assert result['payment_amount'].sum() == 400

