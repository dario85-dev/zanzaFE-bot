#!/bin/sh
sh buildimage.sh
docker stop zanzabot
docker run -d --rm --name zanzabot zanzabot:latest
