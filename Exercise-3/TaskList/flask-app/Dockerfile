FROM python:3

LABEL maintainer="Carmelo Sammarco <carmelosammarco.com>"

# copy our application code
ADD  . /opt/flask-app
WORKDIR /opt/flask-app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000