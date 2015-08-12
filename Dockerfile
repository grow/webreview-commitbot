FROM grow/baseimage-managed-vms:0.0.53
MAINTAINER Grow SDK Authors <hello@grow.io>

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app
WORKDIR /app
