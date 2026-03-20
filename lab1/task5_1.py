class Logger:
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        print(f"Запис у файл: {message}")

class NetworkMonitor:

    def __init__(self, logger: Logger):
        self.logger = logger

    def check(self):
        self.logger.log("Мережа працює стабільно")


file_log = FileLogger()

monitor = NetworkMonitor(file_log)

monitor.check()