FROM python:3.8.0-slim-buster

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev --no-install-recommends

RUN mkdir /fourpartsweb
WORKDIR /fourpartsweb

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install packages/fourparts-0.0.1-py3-none-any.whl

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "fourpartsweb.app:create_app()"
