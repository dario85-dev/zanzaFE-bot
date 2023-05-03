#!/bin/sh


sh buildimage.sh

docker run -d --rm --name zanzabot zanzabot:latest
