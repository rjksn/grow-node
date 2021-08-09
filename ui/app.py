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
                    "device_timestamp": now.isoformat(),
                    "name": f"sensor_{name}",
                    "value": float(value)
                    })
            except ValueError:
                pass
        cloud.publish_messages(messages)

        return f"Connection: {enabled}\n" + "\n".join([
                    "{} : {:.2f}".format(message["name"], message["value"]) for message in messages])

    return "POST data as name=value= or name[]=value[]="

if __name__ == '__main__':
    app.run()
