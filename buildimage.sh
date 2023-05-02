#!/bin/sh
git pull

docker stop zanzabot
docker rm zanzabot

docker build --pull --rm -f "Dockerfile" -t zanzabot:latest "." 