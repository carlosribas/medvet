install:
	pip install -r requirements.txt
	pip install --user codecov
test:
	python manage.py test