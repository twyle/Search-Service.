update:
	@pip install --upgrade pip

install:
	@pip install -r services/blog/requirements.txt

install-dev:
	@pip install -r services/blog/requirements-dev.txt

run-blog:
	@docker-compose -f services/blog/docker-compose-dev.yml up --build

create-db:
	@docker-compose -f services/blog/docker-compose-dev.yml exec blog python manage.py create_db

seed-db:
	@docker-compose -f services/blog/docker-compose-dev.yml exec blog python manage.py seed_db

test:
	@python -m pytest

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

init-cz:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog

start-db-containers:
	@sudo docker-compose -f database/docker-compose.yml up --build -d

stop-db-containers:
	@sudo docker-compose -f sdatabase/docker-compose.yml down -v

create-db:
	@python manage.py create_db

seed-db:
	@python manage.py seed_db

test-local:
	@curl localhost

build:
	@docker build -t blog-service:latest .

run-dev:
	@docker run -p5000:5000 --env-file=./.env blog-service:latest

stop-dev:
	@docker-compose -f docker-compose-dev.yml down

coverage:
	@coverage run -m pytest 
	@coverage report -m

lint:
	@isort .
	@black .
	@flake8
	@pylint --rcfile=.pylintrc ./api