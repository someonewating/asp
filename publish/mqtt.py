from paho.mqtt import client as mqtt_client
import json
import random
import time
import ssl

broker = "srv-iot.diatel.upm.es"
port = 8883

topic="v1/devices/me/telemetry"
client_id = f'python-mqtt-2'

username="JCGf3ApcTWWLqul1Btxo"
password=""

class MQTT:
    def __init__(self, broker, port, topic, client_id, username):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client_id = client_id
        self.username = username
        self.client = None

    def connect(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print(f"Client {self.client_id}: connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        # Set Connecting Client ID
        client = mqtt_client.Client(self.client_id)
        client.username_pw_set(self.username, "")
        client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)
        # client.on_connect = on_connect
        client.connect(self.broker, self.port)
        self.client =  client

    def start(self):
        self.client.loop_start()

    def publish(self, msg):
        result = self.client.publish(self.topic, msg)
        status = result[0]
        if status == 0:
            print(f"Client {self.client_id}: send `{msg}` to topic `{topic}`")
        else:
            print(f"Client {self.client_id}: failed to send message to topic {topic}")
        return result

if __name__ == '__main__':
    sensor = MQTT(broker, port, topic, "sensor1", username)
    sensor.connect()
    sensor.start()
    msg_count = 0

    while True:
        time.sleep(1)
        msg = json.dumps({
            "temperature": msg_count,
            "humidity": msg_count
        })
        result = sensor.publish(msg)

        msg_count += 1