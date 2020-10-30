#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

printf -v TIMESLUG '%(%Y-%m-%d-%H-%M)T' -1

touch $DIR/../data/logs/thermals-$TIMESLUG.csv

# Get Thermals
for value in {1..5}
do
  /home/pi/.pyenv/shims/python3 $DIR/../python/thermals.py >> $DIR/../data/logs/thermals-$TIMESLUG.csv
  if [ $value -lt 5 ]
  then
    sleep 6
  fi
done


# Save Thermals
echo "Saving data for $TIMESLUG"

bq load --source_format=CSV \
    grow-293817:grow.stats \
    $DIR/../data/logs/thermals-$TIMESLUG.csv \
    timestamp:TIMESTAMP,tempcpu:FLOAT,temp1:FLOAT,humid1:FLOAT

