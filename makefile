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

tests:
	@echo "Running tests"
	@. env/bin/activate && pytest -vv tests
lint:

	@echo "Linting"
	@. env/bin/activate && pylint bin/perceptron.py
