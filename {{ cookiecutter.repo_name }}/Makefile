.PHONY: test coverage lint init install_deps install_deps_dev

default: test

########################################
# GLOBALS

NAME 	:= your.registry.url/image-name
TAG 	:= $$(git log -1 --format=%h)
IMG 	:= ${NAME}:${TAG}
LATEST	:= ${NAME}:latest

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


# Install dependencies

install_deps:
	pipenv install

install_deps_dev:
	pipenv install --dev


# Docker commands

build:
	docker build -t ${IMG} .
	docker tag ${IMG} ${LATEST}

run:
	docker run -p 5000:5000 -it --rm ${IMG}

login:
	docker log -u ${DOCKER_USER} -p ${DOCKER_PASS}

push:
	docker push ${NAME}
