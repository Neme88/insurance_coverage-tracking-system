import pandas as pd
from src.suspension_calculator import generate_days_from_suspension_report
from src.agent_report_generator import generate_agent_collection_report
from src.payment_type_report_generator import generate_payment_type_report
import os
import tempfile
from datetime import datetime

def test_generate_days_from_suspension_report():
    df = pd.DataFrame({
        'device_id': [1, 1, 2],
        'created': pd.to_datetime(['2024-01-01', '2024-02-01', '2024-01-15']),
        'payment_amount': [60, 60, 60],
        'status': ['SUCCESSFUL', 'SUCCESSFUL', 'SUCCESSFUL'],
        'agent_user_id': [10, 10, 20],
        'payment_type': ['CASH', 'CASH', 'CASH']
    })

    with tempfile.TemporaryDirectory() as tmpdirname:
        today = datetime(2024, 3, 1).date()
        generate_days_from_suspension_report(df, tmpdirname, today)
        result = pd.read_csv(os.path.join(tmpdirname, "days_from_suspension_report.csv"))
        assert 'device_id' in result.columns

def test_generate_agent_collection_report():
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