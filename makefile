default:
	@cat makefile

env:
	@echo "Setting up virtual environment called env"
	@python3 -m venv env
	@echo "Installing required packages"
	@. env/bin/activate && pip install -r requirements.txt

run:
	@echo "Running clockdeco_param.py"
	@. env/bin/activate && python bin/clockdeco_param.py

lint:
	@echo "Running lint"
	@. env/bin/activate && pylint --disable=R1728 --disable=C0103 bin/perceptron.py

tests:
	@echo "Running tests"
	@source env/bin/activate && pytest -vv tests/test_perceptron.py
