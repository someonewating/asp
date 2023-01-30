import paho.mqtt.client as mqtt
import ssl
import json
import sheep_led as led

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("v1/devices/me/attributes")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    value = msg.payload
    changeled(value)

def changeled(value):
    data = json.loads(value)

    if (data.get('sick') == True and data['sick'] == True):
        print("sick light")
        led.sick()
    elif(data.get('sick') == False and data['sick'] == False):
        print("sick off")
        led.sick_off()
    elif(data.get('track') == True and data['track'] == True):
        print("track light")
        led.track()
    elif(data.get('track') == False and data['track'] == False):
        print("track off")
        led.track_off()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set("eUBoJH5pKozXzf3KbTVg", None)
client.tls_set(certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED)
client.connect("srv-iot.diatel.upm.es", 8883, 60)

client.loop_forever()