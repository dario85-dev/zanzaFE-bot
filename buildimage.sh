#!/bin/sh
git pull
docker build --pull --rm -f "Dockerfile" -t zanzabot:latest "." 