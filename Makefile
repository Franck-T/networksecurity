build:
	docker compose build --no-cache app


up:
	docker compose up -d

down:
	docker compose down

check-main-file:
	docker compose exec app cat /app/app/main.py

restart:
	docker compose down
	docker compose up -d

freeze:
	docker compose run --rm app pip freeze > requirements.txt

run-shell:
	docker compose exec app /bin/bash