.PHONY: lint
lint:
	black --check .
	flake8 .
	mypy .
	isort --diff .

.PHONY: format
format:
	black .
	isort .

.PHONY: test
test:
	pytest .
