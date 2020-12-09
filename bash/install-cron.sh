#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Install Start Up Script
touch /etc/init.d/grow-node-startup
echo "bash ${DIR}/bash/startup.sh" >> /etc/init.d/grow-node-startup
chmod +x /etc/init.d/grow-node-startup

# Install Cron Jobs
touch /etc/cron.d/grow-node
echo "0 * * * * root bash /home/pi/grow-node/bash/cron-hour.sh" >> /etc/cron.d/grow-node
echo "* * * * * root bash ${DIR}/bash/cron-thermals.sh"         >> /etc/cron.d/grow-node
chmod +x /etc/init.d/grow-node
