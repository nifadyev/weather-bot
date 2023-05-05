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


install:  ## Production installation
	make init
	docker compose build

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
