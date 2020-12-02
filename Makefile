# Makefile for configuring and setting up the application

setup_install:
	# Setting up backend
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

	# Setting up frontend
	npm --prefix ./frontend install ./frontend

run_db:
	docker-compose up db &

seed_data:
	# Make sure the DB is UP
	.venv/bin/python scripts/seeder.py

run_flask:
	.venv/bin/flask run &

run_grpc:
	.venv/bin/python -m server.grpc_server &

run_backend:run_db run_flask run_grpc

kill_backend:
	kill -9 $(ps aux | grep "flask run" | awk '{print $2}')

clean:
	rm -rf .venv
	rm -rf frontend/node_modules