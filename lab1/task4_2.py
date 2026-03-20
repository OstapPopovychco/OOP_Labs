class Callable:
    def make_call(self):
        pass

class Messagable:
    def send_sms(self):
        pass

class NetworkConnectable:
    def connect_to_network(self):
        pass

class Smartphone(Callable, Messagable, NetworkConnectable):
    def make_call(self):
        print("Смартфон: Виконую дзвінок...")

    def send_sms(self):
        print("Смартфон: Надсилаю SMS...")

    def connect_to_network(self):
        print("Смартфон: Підключено до 4G/5G.")

class IoTDevice(NetworkConnectable):
    def connect_to_network(self):
        print("IoT-датчик: Підключено до мережі для передачі даних.")

print("Робота зі Смартфоном")
phone = Smartphone()
phone.make_call()
phone.send_sms()
phone.connect_to_network()

print("\nРобота з IoT-пристроєм")
sensor = IoTDevice()
sensor.connect_to_network()
