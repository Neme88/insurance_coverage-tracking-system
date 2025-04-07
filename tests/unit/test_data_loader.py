# tests/unit/test_data_loader.py

import os
import tempfile
import pandas as pd
from data_loader import load_payments

def test_load_payments_csv_reads_valid_csv():
    """
    Ensure that the loader correctly reads a CSV file and parses dates.
    """
    csv_content = "created,payment_amount,status,agent_user_id,payment_type,device_id\n" \
                  "2024-01-01,100,SUCCESSFUL,1,CASH,dev001"

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(csv_content)
        temp_path = f.name

    df = load_payments(temp_path)
    os.remove(temp_path)

    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 6)
    assert pd.api.types.is_datetime64_any_dtype(df['created'])
    assert df.iloc[0]['payment_amount'] == 100
