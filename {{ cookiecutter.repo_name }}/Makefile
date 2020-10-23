.PHONY: test coverage lint install_deps install_deps_dev

default: test

########################################
# GLOBALS

export PYTHONPATH = .


########################################
# COMMANDS

test:
	@pytest

coverage:
	@coverage run -m pytest
	@coverage report -m

lint:
	@flake8 src


install_deps:
	pipenv install

install_deps_dev:
	pipenv install --dev
