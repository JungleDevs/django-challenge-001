# Jungle Devs - Django Challenge #001

## [Documentation](https://github.com/rgzfx/django-challenge-001/wiki) 

## To install Git
``` shell
sudo apt install git
git clone https://github.com/rgzfx/django-challenge-001.git
```

## Setting up Postgres db
```shell
sudo apt-get install postgresql postgresql-contrib postgis postgresql-12-postgis-scripts

sudo su - postgres
psql

CREATE DATABASE jungledevs;
CREATE USER test_user WITH PASSWORD 'qwer1234';
ALTER ROLE test_user SUPERUSER;
GRANT ALL PRIVILEGES ON DATABASE jungledevs TO test_user;
create extension postgis;

```

## Running dev server
```shell
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

## To install Docker

```shell
sudo apt install docker-ce
```

## Running prod server
```shell
sh deploy.sh
```
