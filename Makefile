# Disable echoing executed statements for specific commands
.SILENT: install
# .DEFAULT_GOAL := help

# Assumes that pdm is installed (difficult to check using Makefile conditional variables)
install:
	python -m venv .venv

	pdm use -f .venv
	pdm install --production
	make init-pre-commit

	cp .env.example .env
	echo "Please fill in .env file"

install-dev: install
	pdm install --group dev

init-pre-commit:
	# --hook-type commit-msg is required for gitlint hook to work. commit-msg hook is not installed by default
	pdm run pre-commit install --install-hooks --hook-type commit-msg --hook-type pre-push

build:
	docker compose build

run-docker:
	docker compose up
