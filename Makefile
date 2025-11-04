.PHONY: help install install-dev test test-cov lint format type-check clean build docs

help:
	@echo "Available commands:"
	@echo "  install       - Install package"
	@echo "  install-dev   - Install package with dev dependencies"
	@echo "  test          - Run tests"
	@echo "  test-cov      - Run tests with coverage"
	@echo "  lint          - Run linter"
	@echo "  format        - Format code with black"
	@echo "  type-check    - Run type checking"
	@echo "  clean         - Clean build artifacts"
	@echo "  build         - Build distribution packages"
	@echo "  docs          - Build documentation"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

test-cov:
	pytest --cov=langgraph_crosschain --cov-report=html --cov-report=term-missing

lint:
	ruff check langgraph_crosschain tests examples

format:
	black langgraph_crosschain tests examples

type-check:
	mypy langgraph_crosschain

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

docs:
	cd docs && make html

all: format lint type-check test
