# simple_grpc

- Simple gRPC based microservice

# Requirements
- Kindly install `docker-compose` in your system
- Use python 3+
- Preferrably Node v14+

# Setup
- Run `make setup_install`
- Run the postgres docker instance `make run_db`
- Once the DB is up run `make seed_data` to seed the data in DB
- Run the grpc server via `make run_grpc`
- Run the flask proxy server via `make run_flask` 
- Change directory to the `frontend` folder
- Run `npx webpack serve` 
- Then go to [http://localhost:8080/](http://localhost:8080/)


# Points for improvement
- Dockerize app
- Use [gRPC Gateway](https://github.com/grpc-ecosystem/grpc-gateway) for proxying requests
- Add tests to grpc server