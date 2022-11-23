SHELL = /bin/bash
PYTHON := python3
PIP := pip3
FILES_PATH := src/*/*.py

.PHONY: help
help:
	@echo "~~~~~~~~~~~~~~~~~HELP~~~~~~~~~~~~~~~~~~"
	@echo "lint : lint the code."
	@echo "setup : prepares the enviornment."
	@echo "clean : cleans the environment."
	@echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

.PHONY: lint
lint:
	${PYTHON} -m isort ${FILES_PATH}
	${PYTHON} -m black ${FILES_PATH}
	${PYTHON} -m flake8 ${FILES_PATH}
	${PYTHON} -m autoflake ${FILES_PATH}

.ONESHELL:
.PHONY: setup
setup:
	${PYTHON} -m venv .venv
	source .venv/bin/activate
	${PIP} install --no-cache-dir --upgrade -r requirements.txt
	pre-commit install
	docker-compose up -d

.ONESHELL:
.PHONY: clean
clean: setup
	docker-compose down
	pre-commit clean
	pre-commit uninstall
	deactivate
	rm -rf .venv/