.PHONY: install test lint build clean

install:
	pip install -r requirements.txt

test:
	pytest

lint:
	flake8 src/

build:
	docker-compose build

clean:
	rm -rf __pycache__
