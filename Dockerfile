FROM python:3.7

WORKDIR /app

COPY requirements.txt /app
COPY main.py /app
# COPY . /app

RUN pip install -r requirements.txt
