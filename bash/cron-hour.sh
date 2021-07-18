#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

printf -v TIMESLUG '%(%Y-%m-%d-%H)T' -1

/home/pi/.pyenv/shims/python3 $DIR/../python/ndviMain.py \
  && gsutil cp -a public-read $DIR/../data/images/*-$TIMESLUG.jpg gs://growimages/images
