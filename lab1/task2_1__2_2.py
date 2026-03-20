class BasicTariff:
    def calculate(self, units):
        return 0


class VoiceTariff(BasicTariff):
    def calculate(self, units):
        return units * 0.9


class DataTariff(BasicTariff):
    def calculate(self, units):
        return units * 0.4


class RoamingTariff(BasicTariff):
    def calculate(self, units):
        return units * 50.0


def calc_billing(tariff: BasicTariff, amount):
    print(f"Тариф {tariff.__class__.__name__}: до сплати {tariff.calculate(amount)} грн")

voice = VoiceTariff()
internet = DataTariff()
roaming = RoamingTariff()

calc_billing(voice, 60)
calc_billing(internet, 5634)
calc_billing(roaming, 23)