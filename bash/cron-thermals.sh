#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# BigQuery Direct Call

bq query --use_legacy_sql=false \
  "INSERT INTO \`grow-293817\`.grow.stats
   (timestamp, tempcpu, temp1, humid1) VALUES (`/home/pi/.pyenv/shims/python3 $DIR/../python/thermals.py`)"

# Google IOT Core

LABELS=("cpu_temp_1" "temp_1" "humid_1")
THERMALS=(`/home/pi/.pyenv/shims/python3 $DIR/../python/thermals.py | sed 's/^[^,]*,//' | tr "\," "\n"`)

for i in "${!THERMALS[@]}"; do
	curl --data "name=${LABELS[i]}&value=${THERMALS[i]}" http://localhost:8000/track
done

