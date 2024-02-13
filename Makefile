# Disable echoing executed statements for specific commands
.SILENT: install
# .DEFAULT_GOAL := help

# Assumes that pdm is installed (difficult to check using Makefile conditional variables)
install:
	python -m venv .venv

	pdm use -f .venv
	pdm install --production

	cp .env.example .env
	echo "Please fill in .env file"

install-dev: install
	pdm install --group dev
