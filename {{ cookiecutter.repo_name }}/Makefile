.PHONY: test coverage lint init install_deps install_deps_dev

default: test

########################################
# GLOBALS

export PYTHONPATH = .


########################################
# COMMANDS

test:
	@pytest

coverage:
	@coverage run --source . -m pytest
	@coverage report -m

lint:
	@flake8 src


init:
	git init
	pipenv install --dev flake8 coverage pytest


install_deps:
	pipenv install

install_deps_dev:
	pipenv install --dev
