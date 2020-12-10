from flask import Flask
app = Flask(__name__)

# Requirements:
#   - Set Wifi Details if can not connect
#   - Sensor Data
#   - Power Cycle

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
