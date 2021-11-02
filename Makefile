build:
	poetry build

publish:
	poetry publish --dry-run	

install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	@poetry run brain-games
