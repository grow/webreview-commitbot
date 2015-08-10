FROM gcr.io/google_appengine/python-compat

RUN apt-get update
RUN apt-get install -y --no-install-recommends git python python-pip wget

# RUN pip install -U pip
RUN pip install -r requirements.txt

ADD . /app
