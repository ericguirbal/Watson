# Watson

PYTHON ?= python
VENV_WATSON_DIR = $(CURDIR)/data
VENV_DIR = $$(poetry env info -p)

all: docs

.PHONY: venv
.ONESHELL:
env:
	@if [ -z "${VENV_DIR}" ]; then
		poetry env use python3;
		echo "export WATSON_DIR=\"$(VENV_WATSON_DIR)\"" >> $(VENV_DIR)/bin/activate;
		echo "set -x WATSON_DIR \"$(VENV_WATSON_DIR)\"" >> $(VENV_DIR)/bin/activate.fish;
	fi

.PHONY: install
install: venv
	poetry install

.PHONY: build
build: install
	poetry build

.PHONY: check
check: clean
	poetry run pytest

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr

.PHONY: distclean
distclean: clean
	rm -fr *.egg *.egg-info/ .eggs/

.PHONY: mostlyclean
mostlyclean: clean distclean
	rm -rf "$(VENV_DIR)"

.PHONY: docs
docs: install
	poetry run scripts/gen-cli-docs.py
	poetry run mkdocs build

.PHONY: completion-scripts
completion-scripts:
	scripts/create-completion-script.sh bash
	scripts/create-completion-script.sh zsh
