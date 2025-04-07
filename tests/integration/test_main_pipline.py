import os
import tempfile
import pandas as pd
from main import run_pipeline

def test_run_pipeline_creates_expected_csv_outputs():
    """
    Integration test that validates the entire pipeline works:
    - Loads sample CSV data
    - Runs all 3 report generators
    - Confirms output files exist and contain content
    """
    csv_content = (
        "created,payment_amount,status,agent_user_id,payment_type,device_id\n"
        "2024-01-01,100,SUCCESSFUL,1,CASH,dev001"
    )

    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(csv_content)
        input_path = f.name

    with tempfile.TemporaryDirectory() as output_dir:
        run_pipeline(input_csv=input_path, output_folder=output_dir, strict_folder=False)

        files = os.listdir(output_dir)
        assert "agent_collection_report.csv" in files
        assert "payment_type_report.csv" in files
        assert "days_from_suspension_report.csv" in files

        # Validate one file has expected structure
        df = pd.read_csv(os.path.join(output_dir, "agent_collection_report.csv"))
        assert not df.empty

