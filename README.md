<!--
README.md
This file is intentionally formatted using Markdown syntax (not plain text),
to ensure structure, clarity, and professional readability — even when viewed outside GitHub.
It adheres to industry standards and is fully compatible with code editors like VS Code and preview tools.
-->

# Lumkani Payment Reporting Tool

A Python-based command-line tool for generating actionable reports from raw payment data. This solution addresses Lumkani’s technical assessment requirements with a focus on **clarity**, **clean architecture**, and **testability**.

---

## 🚀 What It Does

Given a CSV of successful and failed payment transactions, this tool produces:

1. **Suspension report**: Shows how many days remain before each client is suspended.
2. **Agent collection report**: Aggregates collections by agent per day.
3. **Payment type summary**: Shows total amount collected by payment method.

---

## 📁 Project Structure

```
lumkani_payment_report/
├── src/
│   ├── main.py                             # CLI entry point
│   ├── data_loader.py                      # Preprocess input CSV
│   ├── suspension_calculator.py            # Report logic
│   ├── agent_report_generator.py           # Report logic
│   └── payment_type_report_generator.py    # Report logic
├── tests/
│   ├── unit/                               # Unit tests (logic only)
│   └── integration/                        # Full pipeline + file output
├── 2024_09_10_payments.csv                 # Sample CSV provided by Lumkani
├── requirements.txt                        # Project dependencies
├── Makefile                                # For `make run` and `make test`
├── setup.py                                # Editable install support
├── .gitignore
└── README.md
```

---

## ⚙️ Environment Setup (1-Minute Guide)

### ✅ 1.unzip locally

```bash
cd ~/Desktop
cd lumkani_payment_report
```

### ✅ 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows
```

### ✅ 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Run the Tool

### ✅ CLI usage:

```bash
python src/main.py <input_csv> <output_folder> [--date YYYY-MM-DD]
```

### Example:

```bash
python src/main.py 2024_09_10_payments.csv output_reports
```

> The tool creates the output folder and generates 3 CSV files.

---

## 📂 Output Reports

| File                                | Columns                                         |
|-------------------------------------|-------------------------------------------------|
| `days_from_suspension_report.csv`  | `device_id`, `days_from_suspension`            |
| `agent_collection_report.csv`      | `agent_user_id`, `date`, `payment_type`, `payment_amount` |
| `payment_type_report.csv`          | `payment_type`, `total_amount`                 |

All reports are sorted and validated according to the expected business logic.

---

## ✅ Data Rules (As Interpreted from the Spec)

- Only `SUCCESSFUL` payments are valid.
- Each successful payment provides **30 days** of coverage.
- A client is suspended on **day 91** (if no payment extends coverage).
- Payments with `NaN`/invalid values are dropped silently (gracefully).
- Reports exclude all failed, malformed, or corrupted data.

---

## 📊 Running Tests

The tool is fully covered by **unit** and **integration** tests.

### ✅ Run all tests with coverage:

```bash
make test
```

### ✅ Or manually:

```bash
pytest --cov=src --cov-report=term-missing
```

> Coverage ≥ 80% (all core logic tested)

---

## 🛠️ Makefile Commands

```makefile
run:
	python src/main.py $(INPUT) $(OUTPUT)

test:
	pytest --cov=src --cov-report=term-missing

lint:
	flake8 src tests
```

### ✅ Usage:

```bash
make run INPUT=2024_09_10_payments.csv OUTPUT=output_reports
make test
make lint
```

---

## 📦 Requirements

```txt
pandas==2.2.3
python-dateutil==2.9.0.post0
pytest==8.3.5
pytest-cov==6.1.1
numpy==2.2.4
```

> These are the runtime + testing libraries used. Tools like `black`, `flake8` were used during dev but not pinned for the submission.

---

## 💡 Notes on Submission

- All CLI args, naming, and validations align with Lumkani's PDF spec.
- Input sample file was used in both test coverage and real execution.
- The pipeline is modular, easily testable, and extensible for future use.

---

## 👨🏾‍💻 Author

**Chinemerem Nwaka**  
Intermediate Full-Stack Python Developer Candidate  
Submission Date: **April 2025**

> “Built with clarity, modularity, and correctness in mind.”
