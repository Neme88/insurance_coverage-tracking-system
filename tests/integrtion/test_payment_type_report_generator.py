import pandas as pd
import tempfile
import os
from src.payment_type_report_generator import generate_payment_type_report

def test_generate_payment_type_report():
    df = pd.DataFrame({
        'device_id': [1, 2],
        'created': pd.to_datetime(['2024-01-01', '2024-01-01']),
        'payment_amount': [60, 40],
        'status': ['SUCCESSFUL', 'SUCCESSFUL'],
        'agent_user_id': [10, 10],
        'payment_type': ['CASH', 'CARD']
    })

    with tempfile.TemporaryDirectory() as tmpdirname:
        generate_payment_type_report(df, tmpdirname)
        result = pd.read_csv(os.path.join(tmpdirname, "payment_type_report.csv"))
        assert 'payment_type' in result.columns
        assert 'total_amount' in result.columns
