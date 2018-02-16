default: 
	$(MAKE) build
	$(MAKE) test

build:
	docker build -t impyute/impyute .

test:
	docker run impyute/impyute

clean:
	docker system prune
