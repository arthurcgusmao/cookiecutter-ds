.PHONY: test coverage lint init install_deps install_deps_dev

default: test

########################################
# GLOBALS

DOCKER_REPO = your.registry.url/image-name

GIT_COMMIT = $$(git log -1 --format=%h)
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


docker-build:
	docker build -t $(DOCKER_REPO):latest\
                     -t $(DOCKER_REPO):$(GIT_COMMIT)\
		     .

docker-run:
	docker run -p 5000:5000 -it --rm $(DOCKER_REPO):$(GIT_COMMIT)
