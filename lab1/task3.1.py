class NetworkConnection():
    def connect(self):
        print("Підключення...")

class WiFiConnection(NetworkConnection):
    def connect(self):
        print("WiFi: Підключено до бездротової мережі.")

class LTEConnection(NetworkConnection):
    def connect(self):
        print("LTE: Встановлено з'єднання")

def establish_connection(connection: NetworkConnection):
    connection.connect()

wifi_network = WiFiConnection()
lte_network = LTEConnection()

establish_connection(wifi_network)
establish_connection(lte_network)