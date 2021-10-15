FROM python:3.9.7-bullseye
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /usr/src/app/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN set -ex \
    && pip install --upgrade pip \
    && pip install Cmake \
    && pip install gunicorn\
    && pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
# RUN python /app/manage.py migrate 


# WORKING DIRECTORY 
WORKDIR /usr/src/app

ADD . .

# CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT