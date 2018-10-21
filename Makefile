DOCKER_ID_USER=eltonlaw

.PHONY: all build test upload install docs

all: test

build:
	docker pull eltonlaw/pybase
	docker build -t impyute .

test: build
	docker run impyute python2.7 -m pytest
	docker run impyute python3.4 -m pytest
	docker run impyute python3.5 -m pytest
	docker run impyute python3.6 -m pytest
	docker run impyute python3.7 -m pytest

upload: build test docs
	python3 setup.py bdist_wheel --universal
	python3 setup.py sdist
	twine upload dist/*

install:
	python3 setup.py install

docs:
	cd docs && $(MAKE) html

# Remember to call `docker login` first
push_pybase:
	docker build -t $(DOCKER_ID_USER)/pybase -f Dockerfile.pybase .
	docker push $(DOCKER_ID_USER)/pybase
