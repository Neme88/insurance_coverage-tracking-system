"""
Main entrypoint for the Lumkani Payment Report Generator.

Parses command-line arguments, loads payment data, and generates:
- Days from suspension report
- Agent collection report
- Payment type report
"""

import argparse
import os
import sys
from datetime import datetime

from src.data_loader import load_payments
from src.suspension_calculator import generate_days_from_suspension_report
from src.agent_report_generator import generate_agent_collection_report
from src.payment_type_report_generator import generate_payment_type_report

def main():
    """
    CLI handler for the report generation pipeline.
    Accepts input file and output folder paths, and an optional date override.
    """
    parser = argparse.ArgumentParser(description="Lumkani Payment Report Generator")

    parser.add_argument("input_file", help="Path to the input CSV file (e.g. 2024_09_10_payments.csv)")
    parser.add_argument("output_folder", help="Path to the output folder (must not exist)")

    parser.add_argument(
        "--date",
        help="Optional override for today's date in YYYY-MM-DD format (default: system date)",
        required=False
    )

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.")
        sys.exit(1)

    if os.path.exists(args.output_folder):
        print(f"Error: Output folder '{args.output_folder}' already exists.")
        sys.exit(1)

    os.makedirs(args.output_folder)

    try:
        today = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else datetime.today().date()
    except ValueError:
        print("Error: --date must be in format YYYY-MM-DD (e.g., 2024-10-01)")
        sys.exit(1)

    payments_df = load_payments(args.input_file)

    generate_days_from_suspension_report(payments_df, args.output_folder, today)
    generate_agent_collection_report(payments_df, args.output_folder)
    generate_payment_type_report(payments_df, args.output_folder)

    print(f"Reports generated successfully in folder: {args.output_folder}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
