FROM python:latest

RUN apt-get -y update
RUN apt-get -y install ffmpeg

WORKDIR /app        
COPY . /app
RUN pip install -r requirements.txt

ENV DATA=/data

ENTRYPOINT [ "python", "/app/convert.py" ]

