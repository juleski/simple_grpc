FROM python:3.9.0

WORKDIR /app
COPY requirements.txt /app/
COPY .env /app/

RUN pip install -r requirements.txt
COPY /server/ /app/server/

RUN python --version
EXPOSE 50051

CMD ["python", "-m", "server.grpc_server"]