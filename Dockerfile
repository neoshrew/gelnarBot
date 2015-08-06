FROM ubuntu:14.04

RUN apt-get update
RUN locale-gen en_GB.UTF-8
ENV LANG=en_GB.UTF-8

RUN apt-get install -y python python-dev gcc python-pip
RUN pip install --upgrade pip

RUN pip install irc

ADD . /vol/app
RUN cd /vol/app && easy_install .
