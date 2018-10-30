from time import sleep
import paho.mqtt.client as mqtt
import random
import json

def on_connect(client, userdata, flags, rc):
    print(rc)
    print('connected with result {0}'.format(rc))
    client.subscribe('soil_moisture')
def on_message(client, userdata, msg):
    print("the data recieved")
    t,h= msg.payload.decode("utf-8").split(",")
    print("the "+str(t)+": "+str(h))

def main():
    # Create a new client for receiving messages
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.subscribe('soil_moisture')
    client.connect('127.0.0.1',1883,60)
    client.loop_start()
    
    while True:
        try:
            p=random.randint(1,101)
            if isinstance(p,int):
                
                msg=json.loads(str(p))
                client.publish('soil_moisture',msg)
                print(msg)
            else:
                print('Invalid sensor readings')
        except OSError:
            print('Failed to read sensor')
        sleep(4)
main()
