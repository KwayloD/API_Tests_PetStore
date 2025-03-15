import pytest
from validators import ResponseValidator

class TestUserAPI:
    validator = ResponseValidator()

    def test_post_create_user(self, api_client, user_data):
        """Создание пользователя методом POST"""
        response = api_client.post(f"/user", user_data)
        print("JSON-ответ от API:", response.json())
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "message", str(user_data["id"]))

    def test_put_update_user(self, api_client, get_username_from_user_data, user_data):
        """Изменение пользователя методом PUT по usermane"""
        username = get_username_from_user_data
        response = api_client.put(f"/user/{username}", user_data)
        print("JSON-ответ от API:", response.json())
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "message", str(user_data["id"]))

    def test_get_user_name(self, api_client, get_username_from_user_data):
        """Получение информавции пользователя методом GET по username"""
        username = get_username_from_user_data
        response = api_client.get(f"/user/{username}")
        print("JSON-ответ от API:", response.json())
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "username", username)

    def test_delete_user(self, api_client, get_username_from_user_data):
        """Удаление пользователя методом DELETE по username"""
        username = get_username_from_user_data
        response = api_client.delete(f"/user/{username}")
        print("JSON-ответ от API:", response.json())
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "message", username)