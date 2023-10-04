# ? Windows does not support Makefile?
# https://makefiletutorial.com/

# Disable echoing executed statements for specific commands
.SILENT: init
.DEFAULT_GOAL := help

init:  ## Create required files and configs
ifneq ("$(wildcard .env)","")
	echo ".env file exists, skipping"
else
	cp .env.example .env
	sed -i 's/ENVIRONMENT=development/ENVIRONMENT=production/g' .env
endif

init-dev:  # Create required files and configs
	make init

install:  ## Production installation
	make init
	docker compose build
	python -m poetry install

install-dev:  ## Development installation
	make init-dev
	python -m poetry install --group dev
	pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push

export-dependencies:  ## Export prod dependencies
	poetry export --no-interaction --without-hashes --without=dev --output requirements.txt

export-dev-dependencies:  ## Export all dependencies
	poetry export --no-interaction --without-hashes --output requirements-dev.txt

activate-venv:  ## Activate virtual environment using Poetry
	poetry shell

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
