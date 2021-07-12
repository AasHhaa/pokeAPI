build:
	@docker-compose build

down:
	@docker-compose down

test:
	@docker-compose -f docker-compose.yaml run django_pokemon_api python manage.py test corn

stop:
	@docker-compose stop

clean: stop # add '--rmi all' for remove containers
	@docker-compose  down --remove-orphans -v

up:
	@docker-compose up

reboot:
	@docker-compose stop && docker-compose up

quick-start:
	@docker-compose build && docker-compose up

migrate:
	@docker-compose run django_pokemon_api python manage.py migrate

makemigrate:
	@docker-compose run django_pokemon_api python manage.py makemigrations

bash-api:
	@docker exec -it django_pokemon_api bash

bash-db:
	@docker exec -it postgres_db_pokemon bash

test:
	@docker-compose run django_pokemon_api python manage.py test
