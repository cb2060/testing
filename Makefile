index.html: talk.md
	python refreeze/freeze.py
	vim -s script index.html

test:
	python -m doctest talk.md
pytest:
	python -m pytest -vx --doctest-glob '*.md'

RANDOM_PORT=`python -c 'import random; print(int(5000+ 5000*random.random()))'`

slideshow:
	PORT=$(RANDOM_PORT) python refreeze/flask_app.py
