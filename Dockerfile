FROM gcr.io/google_appengine/python-compat

RUN apt-get update && apt-get install -y \
  git \
  python \
  python-pip \
  wget

RUN pip install -U pip
RUN pip install \
  GitPython

#RUN mkdir -p /root/.ssh/
#ADD ./ssh /root/.ssh
#RUN chmod 600 /root/.ssh/id_rsa.pub
#RUN mkdir -p /etc/ssh/
#RUN echo "    IdentityFile /root/.ssh/id_rsa.pub" >> /etc/ssh/ssh_config

ADD . /app
