#!/bin/sh


sh buildimage.sh

docker run -d --restart --rm --name zanzabot zanzabot:latest
