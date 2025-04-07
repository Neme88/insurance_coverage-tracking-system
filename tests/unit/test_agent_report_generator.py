import pandas as pd
from datetime import datetime
from agent_report_generator import generate_agent_collection_report

def test_agent_report_groups_by_agent_and_date(tmp_path):
    """
    Test that the agent collection report is grouped correctly by:
    - agent_user_id
    - date (from the 'created' column)
    - payment_type

    Asserts:
        - Sum of payment amounts is accurate.
        - Expected columns exist in the output.
    """
    df = pd.DataFrame({
        'created': pd.to_datetime(['2024-01-01 09:00', '2024-01-01 10:00']),
        'payment_amount': [50, 70],
        'status': ['SUCCESSFUL', 'SUCCESSFUL'],
        'agent_user_id': [1, 1],
        'payment_type': ['CASH', 'CASH']
    })
    df['date'] = df['created'].dt.date
    output = tmp_path
    generate_agent_collection_report(df, output)
    result = pd.read_csv(output / "agent_collection_report.csv")

    assert result['payment_amount'].sum() == 120
    assert set(result.columns) == {'agent_user_id', 'date', 'payment_type', 'payment_amount'}


