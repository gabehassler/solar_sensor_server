import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os
import time
# import pandas as pd
from datetime import date
from datetime import datetime as dt

CSV_DIR = "results"

load_dotenv()

def get_today_file():
    nw = date.today()
    fn = "results/power_temp_" + str(nw) + ".csv"
    return fn

def process_temp_power(data, topic):
    data = data.strip('b')
    data = data.strip('\'')
    path = get_today_file()
    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.write('datetime,sensor,temp,current,voltage,power\n')
    s = data.split(',')
    keysvals = [x.split(':') for x in s]
    results_final = [dt.now(), topic]
    for kv in keysvals:
        results_final.append(kv[1])
    
    s_final = ','.join(str(x) for x in results_final)
    with open(path, 'a') as file:
        file.write(s_final)
        file.write('\n')


        
    

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("solar/+/temppower")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    process_temp_power(str(msg.payload), msg.topic)

client = mqtt.Client()
client.username_pw_set(username=os.getenv('MOSQUITTO_USERNAME'),
                       password=os.getenv("MOSQUITTO_PASSWORD"))
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()