# tests/integration/test_main_pipeline.py

import os
import tempfile
import pandas as pd
from main import main

def test_run_pipeline_creates_expected_csv_outputs():
    """
    Integration test that checks main pipeline:
    - Loads data
    - Runs all generators
    - Writes expected CSV output files
    """
    csv_content = "created,payment_amount,status,agent_user_id,payment_type,device_id\n" \
                  "2024-01-01,100,SUCCESSFUL,1,CASH,dev001"

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(csv_content)
        input_path = f.name

    with tempfile.TemporaryDirectory() as output_dir:
        main(input_csv=input_path, output_folder=output_dir)

        output_files = os.listdir(output_dir)
        assert "agent_collection_report.csv" in output_files
        assert "payment_type_report.csv" in output_files
        assert "days_from_suspension_report.csv" in output_files

        # Spot check one file
        agent_df = pd.read_csv(os.path.join(output_dir, "agent_collection_report.csv"))
        assert not agent_df.empty
