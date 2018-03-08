all: test
test:
	docker pull eltonlaw/pybase
	docker build -t impyute .
	docker run impyute python2.7 -m pytest
	docker run impyute python3.4 -m pytest
	docker run impyute python3.5 -m pytest
	docker run impyute python3.6 -m pytest
