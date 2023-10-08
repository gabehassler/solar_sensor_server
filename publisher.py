import paho.mqtt.client as paho
from dotenv import load_dotenv
import os
import time


load_dotenv()

broker="localhost"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


client= paho.Client("control1")
client.username_pw_set(username=os.getenv('MOSQUITTO_USERNAME'),
                       password=os.getenv("MOSQUITTO_PASSWORD"))

client.on_publish = on_publish
client.on_connect = on_connect
client.connect(broker, port, 60)
ret= client.publish("test","on")

iter = 0
topic = "test"
while True:
        # Get the current time

        # Publish the current time to the MQTT topic
        client.publish(topic, iter)

        # Print the published message
        print(f"Published: {iter} to topic: {topic}")
        iter += 1

        # Sleep for 10 seconds
        time.sleep(10)
