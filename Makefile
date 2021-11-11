push:
	git add .
	git commit -m 'autocommit'
	git push

check:
	poetry check

build:
	poetry build

publish:
	poetry publish --dry-run -u '\n' -p '\n'	

install:
	poetry install

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

brain-games:
	@poetry run brain-games

brain-even:
	@poetry run brain-even

update-p:
	poetry build
	make install
	make publish
	make package-install	
