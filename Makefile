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
	$(PYTHON) -m pip install 'virtualenv>=16.4.3' 'pip-tools'
	virtualenv --system-site-packages .venv
	$(VENV_BIN)/pip install --ignore-installed --no-deps -r requirements.txt

.PHONY: format
format:
	$(VENV_BIN)/autoflake -i -r --ignore-init-module-imports swmclient scripts
	$(VENV_BIN)/black swmclient scripts
	$(VENV_BIN)/isort swmclient scripts

.PHONY: check
check:
	$(VENV_BIN)/flake8 swmclient
	$(VENV_BIN)/mypy swmclient

.PHONY: package
package:
	$(PYTHON) setup.py bdist_wheel

.PHONY: clean
clean:
	rm -f ./dist/*.whl

.PHONY: upload
upload:
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
