import paho.mqtt.client as mqtt
import random
import time
import json

mqtt_broker = 'localhost'
mqtt_port = 1883
mqtt_user = 'mqtt_user'
mqtt_password = '8218'
mqtt_topic = 'sensor/dht11'

def generate_data():
    temperature = round(random.uniform(15.0, 35.0), 2)
    humidity = round(random.uniform(30.0, 85.0), 2)

    data = {"temperature": temperature, "humidity": humidity}
    return data



def publish_data(client):
    data = generate_data()
    payload = json.dumps(data)
    client.publish(mqtt_topic, payload)
    print(f"Published: {payload}")


def main():
    client = mqtt.Client()
    client.username_pw_set(mqtt_user, mqtt_password)

    client.connect(mqtt_broker, mqtt_port, 60)
    client.loop_start()

    try:
        while True:
            publish_data(client)
            time.sleep(60)
    except KeyboardInterrupt:
        client.loop_stop()
        print("Simulation stopped")

if __name__ == '__main__':
    main()
