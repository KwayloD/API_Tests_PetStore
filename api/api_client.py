import requests
import os
from dotenv import load_dotenv
from utilities.logger_utils import setup_logger

# Загружаем переменные окружения из .env
load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"Accept": "application/json",
                        "apy_key": "special-key"}
        self.logger = setup_logger()

    def _log_request(self, method, url, response):
        """Вспомогательный метод для логирования запросов"""
        self.logger.info(f"Отправка {method}-запроса на {url}")
        self.logger.info(f"Ответ: {response.status_code} - {response.text}")

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=self.headers)
        self._log_request("GET", url, response)
        return response

    def post(self, endpoint, json=None, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=json, data=data, headers=self.headers)
        self._log_request("POST", url, response)
        return response

    def put(self, endpoint, json=None, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=json, data=data, headers=self.headers)
        self._log_request("PUT", url, response)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers)
        self._log_request("DELETE", url, response)
        return response


class APIStore:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"Accept": "application/json",
                        "apy_key": "special-key"}
        self.logger = setup_logger()

    def _log_request(self, method, url, response):
        """Вспомогательный метод для логирования запросов"""
        self.logger.info(f"Отправка {method}-запроса на {url}")
        self.logger.info(f"Ответ: {response.status_code} - {response.text}")

    def get_store_inventory(self):
        """Получает список товаров в магазине"""
        url = f"{self.base_url}/store/inventory"
        response = requests.get(url, headers=self.headers)
        self._log_request("GET", url, response)
        return response

    def post_store_order(self, body):
        """Создает заказ в магазине"""
        url = f"{self.base_url}/store/order"
        response = requests.post(url, json=body, headers=self.headers)
        self._log_request("POST", url, response)
        return response

    def get_store_order(self, order_id):
        """Получает информацию о заказе по ID"""
        url = f"{self.base_url}/store/order/{order_id}"
        response = requests.get(url, headers=self.headers)
        self._log_request("GET", url, response)
        return response

    def delete_store_order(self, order_id):
        """Удаляет заказ по ID"""
        url = f"{self.base_url}/store/order/{order_id}"
        response = requests.delete(url, headers=self.headers)
        self._log_request("DELETE", url, response)
        return response