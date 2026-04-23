import asyncio
import requests
import websockets
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Підключено до MQTT брокера broker.hivemq.com")
        else:
            print(f"Помилка підключення: {rc}")

    def on_disconnect(self, client, userdata, rc):
        print("Відключено від брокера")

    def connect(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def publish(self, topic, message):
        result = self.client.publish(topic, message)
        result.wait_for_publish()
        print(f"MQTT Повідомлення відправлено")

    def disconnect(self):
        self.client.disconnect()
        self.client.loop_stop()

def get_data_from_api():
    try:
        url = "https://meowfacts.herokuapp.com/"
        response = requests.get(url, timeout=5)
        data = response.json()

        fact = data["data"][0]
        return fact

    except Exception as e:
        print("Помилка API:", e)
        return "API не відповідає"


clients = set()

async def websocket_handler(websocket):
    print("Підключився до WS")
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"WS отримано: {message}")
    finally:
        clients.remove(websocket)
        print("Клієнт відключився від WS")

async def send_to_clients(message):
    if clients:
        await asyncio.gather(*[client.send(message) for client in clients])

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "lpnu/ostap/lab8"

mqtt_client = MQTTClient(BROKER, PORT)

async def main():
    print("Запуск інтеграції (REST + WS + MQTT)...")
    server = await websockets.serve(websocket_handler, "localhost", 8765)
    mqtt_client.connect()

    while True:
        fact = get_data_from_api()
        print(f"\n🌐 REST API → {fact}")
        await send_to_clients(fact)
        mqtt_client.publish(TOPIC, fact)
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())