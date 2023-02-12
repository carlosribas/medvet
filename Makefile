INITIAL_JSON_FILE=load_initial_data

install:
	pip install -r requirements.txt

test:
	python manage.py test

load-initial-data:
 docker-compose run web python manage.py loaddata ${INITIAL_JSON_FILE}