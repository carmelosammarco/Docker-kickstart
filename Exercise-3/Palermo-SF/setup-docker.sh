#!/bin/bash

# build the flask container
docker build -t sicilian4ever/palermosf-web .

# create the network
docker network create palermo-net

# start the ES container
docker run -d --name es --net palermo-net -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2

# start the flask app container
docker run -d --net palermo-net -p 5000:5000 --name palermosf-web sicilian4ever/palermosf-web
