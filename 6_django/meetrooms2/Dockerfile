FROM python:3.12.0-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /django-app

COPY requirements.txt /django-app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /django-app/

EXPOSE 8000

