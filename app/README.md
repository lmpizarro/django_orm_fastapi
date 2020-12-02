docker pull timescale/timescaledb:latest-pg12
 
docker run -d --name timescaledb-server -p 5432:5432 -e "POSTGRES_PASSWORD=2001lmp" timescale/timescaledb:latest-pg12

docker volume create timescaledb-data

docker volume inspect timescaledb-data

[
    {
        "CreatedAt": "2020-10-18T23:06:07-03:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/timescaledb-data/_data",
        "Name": "timescaledb-data",
        "Options": {},
        "Scope": "local"
    }
]


docker run -d --name timescaledb-server -p 5434:5432 -v timescaledb-data:/var/lib/postgresql/data -e "POSTGRES_PASSWORD=2001lmp" timescale/timescaledb:latest-pg12

psql -h 127.0.0.1 -p 5434 -U postgresql

CREATE DATABASE dbmanagement;
CREATE USER dbmanagement WITH PASSWORD 'dbmanagement';
ALTER ROLE dbmanagement SET client_encoding TO 'utf8';
ALTER ROLE dbmanagement SET default_transaction_isolation TO 'read committed';
ALTER ROLE dbmanagement SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE dbmanagement TO dbmanagement;


https://docs.djangoproject.com/en/3.1/ref/settings/

https://techexpert.tips/timescaledb/timescaledb-docker-installation/

https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

pip install psycopg2-binary
