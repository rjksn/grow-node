from gpiozero import CPUTemperature
import board
import adafruit_dht
import time
import datetime
now = datetime.datetime.utcnow()

try:
    dhtDevice = adafruit_dht.DHT11(board.D4)
    sensor1_temp = dhtDevice.temperature
    sensor1_humidity = dhtDevice.humidity
except RuntimeError as e:
    # RuntimeError: DHT sensor not found, check wiring
    sensor1_temp = "null"
    sensor1_humidity = "null"

values = [now.strftime('%Y-%m-%d %H:%M:%S'), CPUTemperature().temperature,
                    sensor1_temp, sensor1_humidity]

print("'{}',{},{},{}".format(*values))
