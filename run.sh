#!/bin/sh
docker stop zanzabot

sh buildimage.sh

docker run -d --rm --name zanzabot zanzabot:latest
