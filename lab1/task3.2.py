class NetworkConnection:
    def connect(self):
        print("Підключення...")


class WiFiConnection(NetworkConnection):
    def connect(self):
        print("Wi-Fi підключено")


class LTEConnection(NetworkConnection):
    def connect(self):
        print("LTE підключено")


class SatelliteConnection(NetworkConnection):
    def __init__(self, has_signal=True):
        self.has_signal = has_signal

    def connect(self):
        if self._check_signal():
            print("Satellite connection established")
        else:
            print("ERROR, Satellite not found")

    def _check_signal(self):
        return self.has_signal



print("Wifi тест:")
wifi = WiFiConnection()
wifi.connect()

print("\nLTE тест:")
lte = LTEConnection()
lte.connect()

print("\nСупутник тест  (сигнал Є):")
satellite_good = SatelliteConnection(has_signal=True)
satellite_good.connect()

print("\nСупутник тест (сигналу НЕМАЄ):")
satellite_bad = SatelliteConnection(has_signal=False)
satellite_bad.connect()