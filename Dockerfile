FROM python:2.7-stretch

RUN pip install requests

ADD . /es-gdelt

WORKDIR /es-gdelt

VOLUME /es-gdelt/data

CMD ./realtime_download.sh
