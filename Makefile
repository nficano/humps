deploy-patch: clean version-patch git-push-on-deploy upload clean

deploy-minor: clean version-minor git-push-on-deploy upload clean

deploy-major: clean version-major git-push-on-deploy upload clean

# Version prior to update
VERSION := ${shell poetry version -s}

version-patch:
	poetry version patch

version-minor:
	poetry version minor

version-major:
	poetry version major

git-push-on-deploy:
	git commit -m 'Bump version: $(VERSION) → $(shell poetry version -s)' pyproject.toml
	git push
	git tag v${shell poetry version -s}
	git push --tags

upload:
	poetry build
	poetry publish

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "install - install the package to the active Python's site-packages"

ci:
	pip install poetry
	poetry install
	poetry run flake8 humps
	poetry run pylint humps
	# poetry run pytest --cov-report term-missing # --cov=humps
	poetry run coverage run -m pytest

lint:
	poetry run flake8 humps
	poetry run pylint humps

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.DS_Store' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

install: clean
	poetry install
