#!/bin/bash

touch /etc/cron.d/grow-node

echo "* * * * * root bash  /home/pi/grow-node/bash/cron-thermals.sh" >> /etc/cron.d/grow-node

