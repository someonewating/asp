import time
import board
import adafruit_dht
from mqtt import MQTT
import json
import RPi.GPIO as GPIO

tem_hum_device = adafruit_dht.DHT11(board.D4)

# MQTT
broker = "srv-iot.diatel.upm.es"
port = 8883
topic = "v1/devices/me/telemetry"

temp_hum_mqtt = MQTT(broker, port, topic, "bodyTem", "JCGf3ApcTWWLqul1Btxo")
temp_hum_mqtt.connect()
temp_hum_mqtt.start()

while True:
    try:
        temperature = tem_hum_device.temperature

        temp_hum_msg = json.dumps({
            "temperature": temperature
        })
        result = temp_hum_mqtt.publish(temp_hum_msg)

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
