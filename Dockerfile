FROM python:2.7-alpine

MAINTAINER  Yu Jiang

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

CMD ./manage.py runserver -h 0.0.0.0


