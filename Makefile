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

## Build Docker container
# build-docker:
# Check if docker and docker-compose exists
# Check both docker compose and docker-compose
# Export envs


test:  ## Run tests
	# TODO: Set non-prod envs
	python -m poetry run pytest

## Export prod dependencies
export-dependencies:
	poetry export --no-interaction --without-hashes --without=dev --output requirements.txt

## Export prod dependencies
export-dev-dependencies:
	poetry export --no-interaction --without-hashes --output requirements-dev.txt

activate-venv:
	poetry shell

## Check dependencies for update

## Format using black
# format:

## Run ruff, pre-commit and tests
# check:

# coverage:  ## Run tests with coverage
# 	coverage erase
# 	coverage run --include=podsearch/* -m pytest -ra
# 	coverage report -m

# Better to be like create-pr
# branch ?= master
# skip-checks ?= no
# push:
# 	git push
# check-flag:
# # Search for the "-i" flag. MAKEFLAGS is just a list of single characters, one per flag. So look for "i" in this case.
# 	# should-skip-checks = ""
# 	# ifneq (,$(findstring i, $(MAKEFLAGS)))
# ifneq (,$(findstring i, $(MAKEFLAGS)))
# 	# should-skip-checks = "--smth-cmd"
# 	# echo $(should-skip-checks)
# 	echo "True"
# endif

help:
	# TODO: Make fancy colored output
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

run:
# docker run
#? Not sure if env variables will work
# docker run -v ./:/weather-bot/ --name weather-bot -p 8000:8000  python src/main.py