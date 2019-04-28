DOCKER_ID_USER=eltonlaw

.PHONY: all build test upload install docs

all: test

rebuild-pybase:
	docker rmi $(DOCKER_ID_USER)/pybase
	docker build -f Dockerfile.pybase -t $(DOCKER_ID_USER)/pybase .

build:
	docker pull $(DOCKER_ID_USER)/pybase
	docker build -t impyute .

test: build
	docker run impyute python2.7 -m pytest
	docker run impyute python3.5 -m pytest
	docker run impyute python3.6 -m pytest
	docker run impyute python3.7 -m pytest

# Need to pip install `wheel` and `twine`
upload: build test docs
	python3 setup.py bdist_wheel --universal
	python3 setup.py sdist
	twine upload dist/*

install:
	python3 setup.py install

docs:
	cd docs && $(MAKE) html

# Remember to call `docker login` first
push-pybase:
	docker build -t $(DOCKER_ID_USER)/pybase -f Dockerfile.pybase .
	docker push $(DOCKER_ID_USER)/pybase
