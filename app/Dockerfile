FROM ubuntu:16.04

RUN apt-get update \
    && apt-get -y install python3 python-pip gcc g++ \
    && pip install --upgrade pip \
    && pip install flask uwsgi

COPY ./ /simple_flask
WORKDIR /simple_flask

CMD ["uwsgi", "--ini", "wsgi.ini"]

