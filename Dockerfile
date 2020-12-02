FROM  python:3.8-slim-buster

LABEL maintainer=""

COPY requirements.txt /app/requirements.txt
# RUN  apt-get update -y && apt-get  install -y postgresql-11

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app

COPY ./entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh
WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]
