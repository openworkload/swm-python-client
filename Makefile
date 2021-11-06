PYTHON=python3

RUNTEST=$(PYTHON) -m unittest -v -b
ALLMODULES=$(patsubst %.py, %.py, $(wildcard test*.py))

all: $(generate) $(format) $(test) $(package)

generate:
	./update-openapi.sh

format:
	autoflake -i -r --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports .
	black .
	isort .

package:
	$(PYTHON) setup.py bdist_wheel

clean:
	rm -f ./dist/*.whl

upload:
	$(PYTHON) -m twine upload --verbose --config-file .pypirc dist/*

test:
	${RUNTEST} ${ALLMODULES}

% : test%.py
	${RUNTEST} test$@

.PHONY: all package upload test

