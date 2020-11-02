#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Save Thermals
bq query --use_legacy_sql=false \
  "INSERT INTO \`grow-293817\`.grow.stats
    (timestamp, tempcpu, temp1, humid1) VALUES (`/home/pi/.pyenv/shims/python3 $DIR/../python/thermals.py`)"
