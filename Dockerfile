FROM python:3
ENV PYTHONBUFFERED 1
RUN apt-get update
RUN apt-get -y install binutils libproj-dev gdal-bin
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/