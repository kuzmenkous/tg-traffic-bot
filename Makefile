dc = docker compose
dc_exec = $(dc) exec ${OPTIONS}

.SILENT:

CONTAINER ?= app
SHELL_CMD ?= bash
OPTIONS ?= -u root

# Docker
build:
	$(dc) build --no-cache

run:
	$(dc) up -d --build

stop:
	$(dc) stop

down:
	$(dc) down

restart:
	$(dc) restart $(CONTAINER)

logs:
	$(dc) logs -f $(CONTAINER)

shell:
	$(dc_exec) $(CONTAINER) $(SHELL_CMD)

shell-root:
	$(dc_exec) -u root $(CONTAINER) $(SHELL_CMD)

ps:
	$(dc) ps


# Migrations
migration:
	${dc_exec} $(CONTAINER) alembic revision --autogenerate -m "$(message)"

migration-upgrade:
	${dc_exec} $(CONTAINER) alembic upgrade head

migration-downgrade:
	${dc_exec} $(CONTAINER) alembic downgrade -1

migration-current:
	${dc_exec} $(CONTAINER) alembic current

migration-history:
	${dc_exec} $(CONTAINER) alembic history

# Requirements
pip-list:
	${dc_exec} $(CONTAINER) pip list
