#!/bin/bash

printf -v timeslug '%(%Y-%m-%d-%H-%M)T' -1

# Get Image
python3 ../python/ndvi.py $timeslug

