#!/bin/sh
docker stop zanzabot
docker rm zanzabot

sh buildimage.sh

docker run -d --rm --name zanzabot zanzabot:latest
