FROM python:3

LABEL maintainer="Carmelo Sammarco <carmelosammarco.com>"

# copy our application code
ADD  /todo
WORKDIR /opt/flask-app


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# expose port
EXPOSE 5000