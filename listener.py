import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import time


load_dotenv()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.username_pw_set(username=os.getenv('MOSQUITTO_USERNAME'),
                       password=os.getenv("MOSQUITTO_PASSWORD"))
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()