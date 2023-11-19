FROM ubuntu:20.04

ARG PYTHON=python3.8

RUN apt-get update
RUN apt-get install -y python3.8 python3-venv python3-pip

COPY ./requirements.txt ./
RUN $PYTHON -m pip install -r requirements.txt

WORKDIR /app 
CMD python3 main.py