import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload}")
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        collection.insert_one(data)
        print("Data saved to MongoDB")
    except json.JSONDecodeError:
        print("Failed to decode JSON")
    except Exception as e:
        print(f"Failed to save data to MongoDB: {e}")

def main():
    mongo_client = MongoClient('mongodb://localhost:27017/')
    db = mongo_client['sensor_data']
    collection = db['dht11_readings']

    mqtt_broker = 'localhost'
    mqtt_port = 1883
    mqtt_user = 'mqtt_user'
    mqtt_password = '8218'
    mqtt_topic = 'sensor/dht11'

    client = mqtt.Client()
    client.username_pw_set(mqtt_user, mqtt_password)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(mqtt_broker, mqtt_port, 60)

    client.loop_forever()


if __name__ == '__main__':
    main()
