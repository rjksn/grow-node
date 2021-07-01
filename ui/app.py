import os

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


@app.route('/track')
@CloudIot(CONFIG_LOCATION)
def track():
    if request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        print(f"{name} : {value}")

if __name__ == '__main__':
    app.run()