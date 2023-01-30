import sys
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
topic_led = "v1/devices/me/attributes"

temp_hum_mqtt = MQTT(broker, port, topic, "bodyTem", "JCGf3ApcTWWLqul1Btxo")
temp_hum_mqtt.connect()
temp_hum_mqtt.start()

led = MQTT(broker, port, topic_led, "led", "IvdXagVsS3LtmnqXim0A")

while True:
    try:
        message = led.subscribe(topic_led)

    except KeyboardInterrupt:
        sys.exit()

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(3.0)
        continue
    
    except Exception as error:
        tem_hum_device.exit()
        GPIO.cleanup()
        raise error

    time.sleep(3.0)
