class Subscriber:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class SmsService:
    def send_sms(self, phone, message):
        print(f"Надсилаємо СМС на {phone}: {message}")

class BalanceManager:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def calculate_balance(self, spent_amount):
        self.balance += spent_amount
        return self.balance

sub = Subscriber(name="Ostap", phone="+380934894943")
sms = SmsService()
calc = BalanceManager()

print(sub.name, sub.phone)

sms.send_sms(sub.phone, message="Ваш баланс оновлено")
current_balance = calc.calculate_balance(154)

print(f"Баланс: {sub.name}, {current_balance} грн")