#!/bin/bash

# pulls recent code
git pull

# if running, kills current bot version
docker rm --force helixbot

# builds new bot with applied code changes
docker build -t "bot" .

# runs new bot with applied code changes
docker run --detach --name helixbot bot
