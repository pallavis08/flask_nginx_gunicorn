FROM python:3.7.15

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN pip install -r $CONTAINER_HOME/requirement.txt
