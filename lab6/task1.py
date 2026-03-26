import requests

class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return f"Помилка {response.status_code}: {response.text}"
        except Exception as e:
            return f"Виникла помилка при GET-запиті: {e}"

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:
                return response.json()
            else:
                return f"Помилка {response.status_code}: {response.text}"
        except Exception as e:
            return f"Виникла помилка при POST-запиті: {e}"

# --- Демонстрація роботи ---

if __name__ == "__main__":
    client = RestClient("https://jsonplaceholder.typicode.com/")

    print("--- Тестування GET-запиту (отримання списку постів) ---")
    posts = client.get("posts")
    if isinstance(posts, list):
        print(f"Отримано {len(posts)} постів. Перші два:")
        print(posts[:2])

    print("\n--- Тестування POST-запиту (створення нового посту) ---")
    new_post_data = {
        "title": "Гугу гага",
        "body": "бубу бебе",
        "userId": 1
    }
created_post = client.post("posts", new_post_data)
print("Сервер повернув створений об'єкт:")
print(created_post)