import os
import logging

from flask import Flask
from flask import request
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
        for name, value in zip(names, values):
            messages.append((f"sensor_{name}", float(value)))

        cloud.publish_message(messages)

        return f"Connection: {enabled}\n" + "\n".join(["{} : {:.2f}".format(*param) for param in messages])
    return "POST data as name=value= or name[]=value[]="

if __name__ == '__main__':
    app.run()
