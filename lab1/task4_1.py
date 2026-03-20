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
        print("Смартфон: Здійснюю виклик через мобільну мережу...")

    def send_sms(self):
        print("Смартфон: Надсилаю текстове повідомлення...")

    def connect_to_network(self):
        print("Смартфон: Підключено до 4G/5G мережі.")

class USBModem(NetworkConnectable):
    def connect_to_network(self):
        print("4G-Модем: Встановлено зв'язок з вишкою. Інтернет доступний.")


print("Перевірка Смартфона")
iphone = Smartphone()
iphone.make_call()
iphone.connect_to_network()

print("\nПеревірка Модема")
modem = USBModem()
modem.connect_to_network()
