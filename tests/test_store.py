import pytest
from validators import ResponseValidator

class TestStoreAPI:
    validator = ResponseValidator()

    def test_get_pet_inventory(self, api_store):
        """Тест на получения инвентаря питомцев методом GET"""
        response = api_store.get_store_inventory()
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)

    def test_post_place_an_order(self, api_store, order_data):
        """Тест на создание заказа методом POST в магазине"""
        response = api_store.post_store_order(order_data)
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "id", order_data["id"])
        self.validator.validate_json_value(response, "petId", order_data["petId"])
        self.validator.validate_json_value(response, "quantity", order_data["quantity"])

    def test_get_find_purchase_by_id(self, api_store, get_id_from_order_data):
        """Тест на поиск заказа на покупку методом GET по ID"""
        order_id = get_id_from_order_data
        response = api_store.get_store_order(order_id)
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "id", order_id)

    def test_delete_purchase_by_id(self, api_store, get_id_from_order_data):
        """Тест на удаление заказа на покупку методом DELETE по ID"""
        order_id = get_id_from_order_data
        response = api_store.delete_store_order(order_id)
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "message", str(order_id))