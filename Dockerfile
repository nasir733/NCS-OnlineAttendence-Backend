FROM python:3.9.7-bullseye
COPY requirements.txt /app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install Cmake \
    && pip install gunicorn\
    && pip install --no-cache-dir -r /app/requirements.txt 
RUN apt-get update && apt-get install -y python3-opencv

# WORKING DIRECTORY 
WORKDIR /app

ADD . .

EXPOSE 8000
CMD ["gunicorn","--bind",":8000","--workers","3","core.wsgi:application"]