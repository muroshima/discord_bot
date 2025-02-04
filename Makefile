SHELL = /bin/bash
SOURCE_DIR = application
CONTAINER_NAME = python_app
DOCKER = docker exec $(CONTAINER_NAME)
POETRY_RUN = $(DOCKER) poetry run
RUN_FILE = main.py
DOCS = docs
LINT_RESULT = lint_result.txt

run:
	$(POETRY_RUN) python $(RUN_FILE)

test:
	$(POETRY_RUN) pytest -n auto -ra -p no:cacheprovider --strict-config --strict-markers -vv --diff-symbols --cov --cov-report=html
	# xdistと--gherkin-terminal-reporterの相性が悪いみたいなので一時的にコメントアウト
	# versionが修正され次第こちらのコマンドで実施予定
	# $(POETRY_RUN) pytest -n auto -ra -p no:cacheprovider --strict-config --strict-markers -vv --diff-symbols --cov --cov-report=html --gherkin-terminal-reporter

up:
	docker compose up -d

build:
	docker compose build

down:
	docker compose down

check:
	@$(POETRY_RUN) black .
	-@$(POETRY_RUN) ruff --fix --show-source --output-format text -o $(LINT_RESULT) .
	@less $(SOURCE_DIR)/$(LINT_RESULT)

install:
	$(DOCKER) poetry install

update:
	$(DOCKER) poetry update

docs:
	@$(POETRY_RUN) pdoc module -o $(DOCS) -d google

mypy:
	$(POETRY_RUN) mypy --install-types --non-interactive

