.PHONY: virtualenv requirements requirements_dev test coverage coverage_html format lint activate clean_cache

PYTHON ?= python3.8
VENV ?= ./venv
ENV_PYTHON ?= $(VENV)/bin/python
MANAGE ?= $(ENV_PYTHON) manage.py


virtualenv:
	@if [ ! -d "$(VENV)" ]; then \
		$(PYTHON) -m venv $(VENV); \
		$(VENV)/bin/pip install pip; \
	fi

requirements: virtualenv
	$(VENV)/bin/pip install -r requirements.txt

requirements_dev: virtualenv requirements
	$(VENV)/bin/pip install -r requirements_dev.txt

migrate:
	$(MANAGE) migrate

collectstatic:
	$(MANAGE) collectstatic --noinput

loaddata:
	$(MANAGE) loaddata dhost/demo/fixture.json

api-develop: requirements_dev collectstatic migrate

demo: develop loaddata

clean_db:
	if [ -f "db.sqlite3" ]; then \
		rm db.sqlite3; \
	fi

clean: clean_db

test:
	$(MANAGE) makemigrations --dry-run
	$(MANAGE) test --settings dhost.settings.tests

coverage:
	$(ENV_PYTHON) -m coverage run manage.py test --settings dhost.settings.tests
	$(ENV_PYTHON) -m coverage report -m

coverage_html:
	$(ENV_PYTHON) -m coverage html

runserver:
	$(MANAGE) runserver

black:
	$(ENV_PYTHON) -m black .

black-check:
	$(ENV_PYTHON) -m black --check .

isort:
	$(ENV_PYTHON) -m isort .

isort-check:
	$(ENV_PYTHON) -m isort --check .

format: black isort

flake8:
	$(ENV_PYTHON) -m flake8 .

lint: flake8 black-check isort-check

prepare-dashboard:
	@if [ ! -d "dhost/frontend/node_modules" ]; then \
		cd dhost/frontend; \
		yarn install; \
	fi

build-dashboard: prepare-dashboard
	cd dhost/frontend
	yarn build

start-dashboard: prepare-dashboard
	cd dhost/frontend
	yarn start

test-dashboard: prepare-dashboard
	cd dhost/frontend
	yarn test

dashboard-develop: build-dashboard start-dashboard

develop: api-develop build-dashboard

# after pulling a new version
refresh: clean develop
