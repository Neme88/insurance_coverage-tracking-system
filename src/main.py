import argparse
import os
import sys
from datetime import datetime

from src.data_loader import load_payments
from src.suspension_calculator import generate_days_from_suspension_report
from src.agent_report_generator import generate_agent_collection_report
from src.payment_type_report_generator import generate_payment_type_report

def main():
    parser = argparse.ArgumentParser(description="Lumkani Payment Report Generator")
    parser.add_argument("input_file", help="Path to the input CSV file (e.g. 2024_09_10_payments.csv)")
    parser.add_argument("output_folder", help="Path to the output folder (must not exist)")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        sys.exit(1)

    if os.path.exists(args.output_folder):
        print(f"Error: Output folder '{args.output_folder}' already exists.")
        sys.exit(1)

    os.makedirs(args.output_folder)

    payments_df = load_payments(args.input_file)
    today = datetime.today().date()

    generate_days_from_suspension_report(payments_df, args.output_folder, today)
    generate_agent_collection_report(payments_df, args.output_folder)
    generate_payment_type_report(payments_df, args.output_folder)

    print(f"Reports generated successfully in folder: {args.output_folder}")

if __name__ == "__main__":
    main()