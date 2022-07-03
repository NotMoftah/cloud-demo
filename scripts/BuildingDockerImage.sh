#!/bin/bash
set -e

# build the docker image
docker build -t notmoftah/tibcogram .

# push image to registery
docker push notmoftah/tibcogram:latest