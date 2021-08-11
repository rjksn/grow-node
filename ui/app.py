import os
import logging
from datetime import datetime as dt

from flask import Flask, request
app = Flask(__name__)

from iot.core import CloudIot

CONFIG_LOCATION = os.path.join(os.path.dirname(__file__), 'cloud_config.ini')

# Requirements:
#   - Set Wifi Details if cannot connect
#   - Sensor Data
#   - Power Cycle

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/track', methods = ['POST', 'GET'])
@CloudIot(CONFIG_LOCATION)
def track(cloud=None):
    '''
    An endpoint for tracking statistics put out by the grow bot, and related wifi services.
    '''
    if request.method == 'POST':
        print('Received request')
        app.logger.debug('this is a DEBUG message')
        app.logger.info('this is an INFO message')
        app.logger.warning('this is a WARNING message')
        app.logger.error('this is an ERROR message')
        app.logger.critical('this is a CRITICAL message')
        try:
            names = [request.form['name']]
            values = [request.form['value']]
        except:
            names = request.form.getlist('name[]')
            values = request.form.getlist('value[]')
        enabled = 'enabled' if cloud.enabled() else 'disabled'

        messages = []
        now = dt.now()
        for name, value in zip(names, values):
            try:
                messages.append({
                    "timestamp": now.isoformat(),
                    "device_id": cloud._device_id,
                    "name": f"sensor_{name}",
                    "value": float(value)
                    })
            except ValueError:
                pass

        cloud.publish_messages(messages)

        message = f"Connection: {enabled}\n" + "\n".join(["{} : {:.2f}"
                    .format(message.get('name', '(not-set)'), message.get("value", '(not-set)')) for message in messages])
        app.logger.debug('message')
        return message

    return "POST data as name=value= or name[]=value[]="

if __name__ == '__main__':
    app.run()
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)