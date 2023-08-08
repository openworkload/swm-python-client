PYTHON=python3
VENV_BIN=.venv/bin

RUNTEST=$(PYTHON) -m unittest -v -b
ALLMODULES=$(patsubst %.py, %.py, $(wildcard test*.py))

generate:
	./update-openapi.sh

.PHONY: prepare-venv
.ONESHELL:
prepare-venv: .SHELLFLAGS := -euo pipefail -c
prepare-venv: SHELL := bash
prepare-venv:
	virtualenv --system-site-packages .venv
	$(VENV_BIN)/pip install --ignore-installed --no-deps -r requirements.txt

.PHONY: format
format:
	. .venv/bin/activate
	$(VENV_BIN)/autoflake -i -r --ignore-init-module-imports swmclient scripts
	$(VENV_BIN)/black swmclient scripts
	$(VENV_BIN)/isort swmclient scripts

.PHONY: check
check:
	. .venv/bin/activate
	$(VENV_BIN)/ruff swmclient
	$(VENV_BIN)/mypy swmclient
	$(VENV_BIN)/bandit -r swmclient -c "pyproject.toml" --silent

.PHONY: package
package:
	. .venv/bin/activate
	$(PYTHON) setup.py bdist_wheel

.PHONY: clean
clean:
	rm -f ./dist/*.whl

.PHONY: upload
upload:
	. .venv/bin/activate
	$(PYTHON) -m twine upload --verbose --config-file .pypirc dist/*

.PHONY: test
test:
	${RUNTEST} ${ALLMODULES}

% : test%.py
	${RUNTEST} test$@

.PHONY: requirements
requirements: requirements.txt
	make prepare-venv || true

requirements.txt: requirements.in
	@pip-compile $<
