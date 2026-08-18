.PHONY: run mcp cli test verify build up down lint

mcp:
	PYTHONPATH=src python -m superagenticmcp.server

cli:
	PYTHONPATH=src python -m superagenticmcp.cli status

run: mcp

lint:
	ruff check src && ruff format --check src

test:
	PYTHONPATH=src pytest -q

verify:
	bash scripts/verify.sh

build:
	docker compose build

up:
	docker compose up --build -d

down:
	docker compose down
