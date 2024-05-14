FILES_TO_CHECK ?= calc_world calculators

.PHONY: lint
lint:
	@echo "Running linting..."
	pylint $(FILES_TO_CHECK)
	mypy --strict $(FILES_TO_CHECK)
	flake8 $(FILES_TO_CHECK)

.PHONY: test
test:
	@echo "Running tests..."
	pytest

.PHONY: coverage
coverage:
	@echo "Running coverage tests..."
	pytest --cov

.PHONY: runserver
runserver:
	@echo "Running Django development server..."
	python manage.py runserver

.PHONY: all
all: lint test coverage runserver