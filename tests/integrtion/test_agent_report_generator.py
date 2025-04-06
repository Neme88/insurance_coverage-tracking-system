import pandas as pd
import os
import tempfile
from src.agent_report_generator import generate_agent_collection_report

def test_generate_agent_collection_report():
    """
    Integration test: validate that agent collection report is generated with expected structure.
    """
    df = pd.DataFrame({
        'device_id': [1, 2],
        'created': pd.to_datetime(['2024-01-01 08:00:00', '2024-01-01 09:00:00']),
        'payment_amount': [60, 40],
        'status': ['SUCCESSFUL', 'SUCCESSFUL'],
        'agent_user_id': [10, 10],
        'payment_type': ['CASH', 'CARD']
    })

    with tempfile.TemporaryDirectory() as tmpdirname:
        generate_agent_collection_report(df, tmpdirname)
        result = pd.read_csv(os.path.join(tmpdirname, "agent_collection_report.csv"))
        assert 'agent_user_id' in result.columns
        assert 'date' in result.columns
        assert 'payment_type' in result.columns
        assert 'payment_amount' in result.columns or 'total_amount' in result.columns

