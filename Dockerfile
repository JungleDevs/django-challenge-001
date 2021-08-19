FROM python:3.8.0-slim-buster

RUN mkdir /app
COPY requirements.txt /app

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y \
    python3 \
    python3-pip \
    gettext \
    gdal-bin \
    geoip-bin \
    rpl
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt


ENV PYTHONUNBUFFERED 1
COPY . /app/

WORKDIR /app

EXPOSE 8000
CMD ["./start.sh"]
