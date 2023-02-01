import time
import board
import adafruit_dht
from mqtt import MQTT
import json
import RPi.GPIO as GPIO
import numpy as np

#DHT11 sensor
tem_hum_device = adafruit_dht.DHT11(board.D4)

#GPS
LATITUDE = 40.388
LONGITUDE = -3.62834

# MQTT
broker = "srv-iot.diatel.upm.es"
port = 8883
topic = "v1/devices/me/telemetry"

gateway = MQTT(broker, port, topic, "sheep001", "7kDEhwF0RUtckoILFPeR")
gateway.connect()
gateway.start()

while True:
    try:
        heartbeat = np.random.normal(70, 5)
        temperature = tem_hum_device.temperature

        temp_hum_msg = json.dumps({
            "sheepid": 1,
            "temperature": temperature,
            "latitude": LATITUDE,
            "longitude": LONGITUDE,
            "heartbeat": heartbeat
        })
        gateway.publish(temp_hum_msg)

    except KeyboardInterrupt:
        tem_hum_device.exit()
        GPIO.cleanup()

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(3.0)
        continue
    
    except Exception as error:
        tem_hum_device.exit()
        GPIO.cleanup()
        raise error

    time.sleep(3.0)
