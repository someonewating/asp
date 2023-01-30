import paho.mqtt.client as mqtt
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("v1/devices/me/attributes")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("IvdXagVsS3LtmnqXim0A", None)
client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)
client.connect("srv-iot.diatel.upm.es", 8883, 60)

client.loop_forever()