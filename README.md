# Lumkani Payment Reporting Tool

A Python-based CLI tool for generating operational reports from insurance payment data, including:

- Days remaining until client suspension
- Agent payment collections
- Payment type summaries

This solution is built for Lumkani's technical assessment and adheres to clean code, testability, and architectural best practices.

---

## 📁 Project Structure

```
lumkani_payment_reporting/
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── suspension_calculator.py
│   ├── agent_report_generator.py
│   └── payment_type_report_generator.py
├── tests/
│   ├── unit/
│   │   ├── test_suspension_calculator.py
│   │   ├── test_agent_report_generator.py
│   │   └── test_payment_type_report_generator.py
│   └── integration/
│       ├── test_suspension_calculator.py
│       ├── test_agent_report_generator.py
│       └── test_payment_type_report_generator.py
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Tool

### ✅ Basic Command:

```bash
python src/main.py <input_csv_file> <output_directory>
```

### ✅ Optional Date Override:

```bash
python src/main.py data/2024_09_10_payments.csv output/ --date 2024-10-01
```

- `input_csv_file`: Path to the provided payment CSV.
- `output_directory`: A non-existing folder where reports will be written.
- `--date`: (Optional) Date to simulate "today" in `YYYY-MM-DD` format.

---

## 📝 Output Reports

1. **days_from_suspension_report.csv**  
   Columns: `device_id`, `days_from_suspension`

2. **agent_collection_report.csv**  
   Columns: `agent_user_id`, `date`, `payment_type`, `payment_amount`

3. **payment_type_report.csv**  
   Columns: `payment_type`, `total_amount`

---

## ✅ Data Assumptions & Rules

- Only `SUCCESSFUL` payments are considered.
- Each payment grants 30 days of coverage.
- Suspension occurs **on the 91st day** after the last covered date.
- Failed or malformed rows are ignored with validation.
- Aggregations are case-insensitive and time-zone agnostic.

---

## 🧪 Running Tests

This project uses **pytest** for unit and integration testing.

### ✅ To run all tests:

```bash
pytest
```

### ✅ To run tests by module:

```bash
pytest tests/unit/
pytest tests/integration/
```

---

## 🧱 Architecture & Code Design

- **Modular**: Each report has a dedicated logic module
- **Testable**: Pure logic is separated from file I/O
- **Extendable**: Adding new reports is straightforward
- **Clean structure**:
  - `src/` contains all core logic
  - `tests/unit/` and `tests/integration/` provide full test coverage

---

## ✅ Code Quality Standards

This solution follows Python best practices:

- **PEP8 formatting** using `black`
- **Static analysis** with `flake8` and `mypy`
- **Clean architecture** principles
- **Readable, concise docstrings** and minimal inline comments
- **Tests as documentation**: test names and docstrings clarify behavior

---

## 📦 Dependencies

Listed in `requirements.txt`:

```
pandas==2.2.1
python-dateutil==2.9.0
pytest==8.1.1
```

> Developer tools like `black`, `flake8`, and `mypy` were used but are not included in `requirements.txt` per submission guidelines.

---

## 🔐 Binary Artifact Policy

- No `.pyc`, `.pyo`, or `__pycache__` files included
- Virtual environment (`venv/`) is excluded
- Output CSVs are generated dynamically, not stored

---

## 👨🏾‍💻 Author

**Chinemerem [Your Last Name]**  
Lumkani Technical Assessment Submission  
April 2025
