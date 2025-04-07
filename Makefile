run:
	python src/main.py $(INPUT) $(OUTPUT)

test:
	pytest --cov=src --cov-report=term-missing

lint:
	flake8 src tests
