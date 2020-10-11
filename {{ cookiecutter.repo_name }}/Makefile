.PHONY: test coverage lint install_deps reqs install_reqs


###########################################################
### GLOBALS

# Dependencies for tests, linting, requirements
META_DEPENDENCIES=coverage flake8 pipreqs pytest
# File for runtime dependencies only
REQUIREMENTS_FILE=requirements.txt

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif


###########################################################
### COMMANDS

default: test

test:
	PYTHONPATH=. pytest

coverage:
	PYTHONPATH=. coverage run -m pytest
	PYTHONPATH=. coverage report -m

lint:
	flake8 src

# Install meta dependencies (for running tests, etc.)
install_deps:
ifeq (True,$(HAS_CONDA))
	conda install --yes $(META_DEPENDENCIES)
else
	pip install $(META_DEPENDENCIES)
endif

reqs:
	pipreqs --savepath ${REQUIREMENTS_FILE}

install_reqs:
ifeq (True,$(HAS_CONDA))
	conda install --yes --file ${REQUIREMENTS_FILE}
else
	pip install -r ${REQUIREMENTS_FILE}
endif
