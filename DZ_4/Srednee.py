# python3.6

import random

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "test"
client_id = f'python-mqtt-{random.randint(0, 100)}'
i = 0
counter = 0
count = [0]*3

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)

    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global i
        global counter
        print(f"Received {msg.payload.decode()} from {msg.topic} topic")
        count[i] = msg.payload.decode()
        if i == 2: 
            i = 0
        else: 
            i+=1
        func = (float(count[0])*0.6 + float(count[1])*0.3+float(count[2])*0.1)
        print ("Скользящее среднее = ", func)
       
    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
