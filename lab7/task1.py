import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WebSocketClient")


class WebSocketClient:
    def __init__(self):
        self.connection = None

    async def connect(self, url):
        try:
            self.connection = await websockets.connect(url)
            logger.info(f"Підключено до {url}")
        except Exception as e:
            logger.error(f"Помилка підключення: {e}")
            self.connection = None

    async def send_message(self, message):
        if self.connection:
            try:
                await self.connection.send(message)
                logger.info(f"Надіслано: {message}")
            except websockets.exceptions.ConnectionClosed:
                logger.error("Помилка: З'єднання розірвано сервером.")
        else:
            logger.warning("Помилка: З'єднання не встановлено.")

    async def receive_message(self):
        if self.connection:
            try:
                response = await self.connection.recv()
                logger.info(f"Отримано: {response}")
                return response
            except websockets.exceptions.ConnectionClosed:
                logger.error("Помилка: З'єднання закрито.")
                return None
        return None

    async def close_connection(self):
        if self.connection:
            await self.connection.close()
            logger.info("З'єднання закрито.")


async def main():
    client = WebSocketClient()
    uri = "wss://ws.postman-echo.com/raw"

    await client.connect(uri)

    if client.connection:
        await client.send_message("Привіт! Це Епштейн тестує сервер.")
        response = await client.receive_message()
        print(f"\n--- Фінальна відповідь сервера: {response} ---\n")

        await client.close_connection()


asyncio.run(main())