import unittest
from unittest.mock import Mock
from parameterized import parameterized

class MathTool:
    def add(self, a, b): return a + b

    def subtract(self, a, b): return a - b

    def multiply(self, a, b): return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Ділення на 0")
        return a / b


class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def details(self):
        return f"{self.title} by {self.author} ({self.year})"


class NotificationService:
    def send(self, message):
        pass


class UserManager:
    def __init__(self, service):
        self.service = service

    def notify_user(self, message):
        self.service.send(message)


def check_even(number):
    return number % 2 == 0


class TestWork(unittest.TestCase):

    def setUp(self):
        self.math = MathTool()

    def test_math_tool(self):
        self.assertEqual(self.math.add(24, 16), 40)
        self.assertEqual(self.math.subtract(100, 37), 63)
        self.assertEqual(self.math.multiply(12, 4), 48)
        self.assertEqual(self.math.divide(81, 9), 9)
        with self.assertRaises(ValueError):
            self.math.divide(5, 0)

    def test_library_item_details(self):
        item = LibraryItem("Call of Cthulhu", "Hovard Philips Lovecraft", 1928)
        self.assertEqual(item.details(), "Call of Cthulhu by Hovard Philips Lovecraft (1928)")

    def test_user_manager_mock(self):
        mock_service = Mock(spec=NotificationService)
        manager = UserManager(mock_service)
        manager.notify_user("Привіт!")
        mock_service.send.assert_called_once_with("Привіт!")

    @parameterized.expand([
        ("even_pos", 2, True),
        ("odd_pos", 3, False),
        ("zero", 0, True),
        ("even_neg", -4, True),
    ])
    def test_check_even_parameterized(self, name, val, expected):
        self.assertEqual(check_even(val), expected)


if __name__ == "__main__":
    unittest.main()