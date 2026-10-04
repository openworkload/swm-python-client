PYTHON=python3.12
VENV_BIN=.venv/bin

update-api-local:
	. .venv/bin/activate
	./update-openapi.sh -l

.PHONY: prepare-venv
.ONESHELL:
prepare-venv: .SHELLFLAGS := -euo pipefail -c
prepare-venv: SHELL := bash
prepare-venv:
	# Isolated venv (no --system-site-packages): system packages can register
	# broken pytest entry points (e.g. platformdirs) under act/GHA.
	$(PYTHON) -m venv --clear .venv
	$(VENV_BIN)/python -m pip install --upgrade pip
	$(VENV_BIN)/pip install --ignore-installed --no-deps -r requirements.txt
	$(VENV_BIN)/pip install -e ".[test]"

.PHONY: format
format:
	. .venv/bin/activate
	$(VENV_BIN)/autoflake -i -r --ignore-init-module-imports swmclient scripts
	$(VENV_BIN)/black swmclient scripts
	$(VENV_BIN)/isort swmclient scripts

.PHONY: check
check:
	. .venv/bin/activate
	$(VENV_BIN)/ruff check swmclient
	$(VENV_BIN)/mypy swmclient
	$(VENV_BIN)/bandit -r swmclient -c "pyproject.toml" --silent

.PHONY: test
test:
	. .venv/bin/activate
	$(VENV_BIN)/python -m pytest -q tests

.PHONY: act
act:
	scripts/run-act.sh $(ARGS)


.PHONY: package
package:
	. .venv/bin/activate
	$(PYTHON) -m build

.PHONY: clean
clean:
	rm -fr ./dist
	rm -fr swmclient.egg-info
	rm -fr build

.PHONY: upload
upload:
	. .venv/bin/activate
	$(PYTHON) -m twine upload --verbose --config-file .pypirc dist/*

.PHONY: requirements
requirements: requirements.txt
	make prepare-venv || true

requirements.txt: requirements.in
	@pip-compile $<
