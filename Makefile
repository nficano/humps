deploy-patch: clean bumpversion-patch upload clean

deploy-minor: clean bumpversion-minor upload clean

deploy-major: clean bumpversion-major upload clean

bumpversion-patch:
	bumpversion patch
	git push
	git push --tags

bumpversion-minor:
	bumpversion minor
	git push
	git push --tags

bumpversion-major:
	bumpversion major
	git push
	git push --tags

upload:
	python setup.py sdist bdist_wheel
	twine upload dist/*

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
