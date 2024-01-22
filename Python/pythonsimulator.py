#final_combined_sensor
import paho.mqtt.client as paho
import time
import random
import json

# Hostname and port
broker = "172.30.0.101"
port = 1883

def on_publish(client, userdata, result):
    print("Data published.")

# MQTT client setup
client = paho.Client("admin")
client.on_publish = on_publish
client.connect(broker, port)

for i in range(300):
    d = random.randint(1, 8)
    temp = random.randint(20, 40)
    hum = random.randint(75, 100)
    sunlight = random.randint(150, 200)
    moisture = random.randint(50,100)

    # Telemetry to send
    message_temp = json.dumps({"temperature": temp})
    message_hum = json.dumps({"humidity": hum})
    message_sun = json.dumps({"sunlight": sunlight})
    message_moisture = json.dumps({"moisture": moisture})

    # Publish message
    ret = client.publish("/temperature", message_temp)
    ret2 = client.publish("/humidity", message_hum)
    ret3 = client.publish("/sunlight", message_sun)
    ret4 = client.publish("/moisture", message_moisture)
    time.sleep(d)

print("Stopped...")