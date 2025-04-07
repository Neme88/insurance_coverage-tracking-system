import argparse
import os
import sys
from datetime import datetime

from data_loader import load_payments_csv
from suspension_calculator import generate_days_from_suspension_report
from agent_report_generator import generate_agent_collection_report
from payment_type_report_generator import generate_payment_type_report


def run_pipeline(input_csv: str, output_folder: str, date: str = None):
    """
    Run the full payment report generation pipeline.

    This function:
    - Validates input and output paths
    - Loads and preprocesses payment data
    - Executes the agent collection, payment type, and suspension report generators
    - Writes reports as CSV files to the specified output folder

    Args:
        input_csv (str): Path to the input CSV file containing payment data.
        output_folder (str): Directory where output reports will be saved.
        date (str, optional): Override today's date (format: YYYY-MM-DD). Defaults to system date.

    Raises:
        SystemExit: If input file is missing, output folder exists, or date format is invalid.
    """
    if not os.path.exists(input_csv):
        print(f"Error: Input file '{input_csv}' does not exist.")
        sys.exit(1)

    if os.path.exists(output_folder):
        print(f"Error: Output folder '{output_folder}' already exists.")
        sys.exit(1)

    os.makedirs(output_folder)

    try:
        today = datetime.strptime(date, "%Y-%m-%d").date() if date else datetime.today().date()
    except ValueError:
        print("Error: --date must be in format YYYY-MM-DD (e.g., 2024-10-01)")
        sys.exit(1)

    payments_df = load_payments_csv(input_csv)

    generate_days_from_suspension_report(payments_df, output_folder, today)
    generate_agent_collection_report(payments_df, output_folder)
    generate_payment_type_report(payments_df, output_folder)

    print(f"Reports generated successfully in folder: {output_folder}")


def main():
    """
    Command-line interface for generating Lumkani payment reports.

    Parses CLI arguments for:
    - Input CSV path
    - Output folder
    - Optional date override

    Then calls the `run_pipeline()` function with parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Lumkani Payment Report Generator")

    parser.add_argument("input_file", help="Path to the input CSV file (e.g., 2024_09_10_payments.csv)")
    parser.add_argument("output_folder", help="Path to the output folder (must not exist)")
    parser.add_argument(
        "--date",
        help="Optional override for today’s date in YYYY-MM-DD format (default: system date)",
        required=False
    )

    args = parser.parse_args()
    run_pipeline(args.input_file, args.output_folder, args.date)


if __name__ == "__main__":
    main()
