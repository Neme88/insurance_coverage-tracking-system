import pandas as pd
from payment_type_report_generator import generate_payment_type_report

def test_payment_type_report_output(tmp_path):
    """
    Test that the payment type report:
    - Groups by payment_type
    - Aggregates payment_amount as total_amount

    Asserts:
        - Output CSV contains the correct columns.
        - Total amount is correctly summed.
    """
    df = pd.DataFrame({
        'payment_type': ['CASH', 'CARD'],
        'payment_amount': [100, 200],
        'status': ['SUCCESSFUL', 'SUCCESSFUL'],
        'created': pd.to_datetime(['2024-01-01', '2024-01-01']),
        'agent_user_id': [1, 1]
    })
    generate_payment_type_report(df, tmp_path)
    result = pd.read_csv(tmp_path / "payment_type_report.csv")

    assert result['total_amount'].sum() == 300
    assert 'payment_type' in result.columns
    assert 'total_amount' in result.columns


