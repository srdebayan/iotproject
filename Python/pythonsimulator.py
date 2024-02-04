#final_combined_sensor
import paho.mqtt.client as paho
import time
import random
import json

# Hostname and port
#broker="localhost"
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
    temp2 = random.randint(20, 40)
    hum2 = random.randint(75, 100)
    sunlight2 = random.randint(150, 200)
    moisture2 = random.randint(50,100)
    temp3 = random.randint(20, 40)
    hum3 = random.randint(75, 100)
    sunlight3 = random.randint(150, 200)
    moisture3 = random.randint(50,100)

    # Telemetry to send
    message_temp = json.dumps({"temperature": temp})
    message_hum = json.dumps({"humidity": hum})
    message_sun = json.dumps({"sunlight": sunlight})
    message_moisture = json.dumps({"moisture": moisture})
    message_temp2 = json.dumps({"temperature": temp2})
    message_hum2= json.dumps({"humidity": hum2})
    message_sun2 = json.dumps({"sunlight": sunlight2})
    message_moisture2 = json.dumps({"moisture": moisture2})
    message_temp3 = json.dumps({"temperature": temp3})
    message_hum3 = json.dumps({"humidity": hum3})
    message_sun3 = json.dumps({"sunlight": sunlight3})
    message_moisture3 = json.dumps({"moisture": moisture3})

    # Publish message
    ret = client.publish("/temperature/farm1", message_temp)
    ret2 = client.publish("/humidity/farm1", message_hum)
    ret3 = client.publish("/sunlight/farm1", message_sun)
    ret4 = client.publish("/moisture/farm1", message_moisture)
    ret21 = client.publish("/temperature/farm2", message_temp2)
    ret22 = client.publish("/humidity/farm2", message_hum2)
    ret23 = client.publish("/sunlight/farm2", message_sun2)
    ret24 = client.publish("/moisture/farm2", message_moisture2)
    ret31 = client.publish("/temperature/farm3", message_temp3)
    ret32 = client.publish("/humidity/farm3", message_hum3)
    ret33 = client.publish("/sunlight/farm3", message_sun3)
    ret34 = client.publish("/moisture/farm3", message_moisture3)
    time.sleep(d)

print("Stopped...")
