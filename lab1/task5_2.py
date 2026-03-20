class Logger:
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        print(f"[FILE]: {message}")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[CONSOLE]: {message}")

class ServerLogger(Logger):
    def log(self, message):
        print(f"[SERVER]: Надсилання логу на віддалений сервер: {message}")

class NetworkMonitor:
    def __init__(self, logger: Logger):
        self.logger = logger

    def check(self):
        self.logger.log("Мережа працює")


monitor_file = NetworkMonitor(FileLogger())
monitor_file.check()

monitor_console = NetworkMonitor(ConsoleLogger())
monitor_console.check()

monitor_server = NetworkMonitor(ServerLogger())
monitor_server.check()