import pytest
from validators import ResponseValidator

class TestPetsAPI:
    validator = ResponseValidator()

    def test_post_new_pets(self, api_client, pet_data):
        """Тест на добавление нового питомца методом POST"""
        response = api_client.post(f"/pet", pet_data)
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "id", pet_data["id"])
        self.validator.validate_json_value(response, "name", pet_data["name"])
        self.validator.validate_dict_field(response, "category", ["id", "name"])
        self.validator.validate_list_field(response, "tags", ["id", "name"])

    def test_get_pets_by_status(self, api_client, pet_status):
        """Тест на GET-запрос поиска питомцев по статусу"""
        response = api_client.get("/pet/findByStatus", params=pet_status)
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_status(response, "status", pet_status["status"])

    def test_put_update_pets(self, api_client, pet_data):
        """Тест на изменение питомца методом PUT"""
        response = api_client.put("/pet", pet_data)
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "id", pet_data["id"])
        self.validator.validate_json_value(response, "name", pet_data["name"])
        self.validator.validate_json_value(response, "tags", pet_data["tags"])

    def test_post_update_pet_with_form_data(self, api_client, get_id_from_pet_data, pet_update_data):
        """Тест на изменение питомца методом POST используя данные name, status"""
        pet_id = get_id_from_pet_data
        response = api_client.post(f"/pet/{pet_id}", data=pet_update_data)
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "message", str(pet_id))

    def test_get_find_pets_by_id(self, api_client, get_id_from_pet_data):
        """Тест на поиск питомца по ID методом GET"""
        pet_id = get_id_from_pet_data
        response = api_client.get(f"/pet/{pet_id}")
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "id", pet_id)
        self.validator.validate_dict_field(response, "category", ["id", "name"])
        self.validator.validate_list_field(response, "tags", ["id", "name"])

    def test_delete_pet_by_id(self, api_client, get_id_from_pet_data):
        """Тест на удаление питомца по ID методом DELETE"""
        pet_id = get_id_from_pet_data
        response = api_client.delete(f"/pet/{pet_id}")
        json_data = response.json()
        print("JSON-ответ от API:", json_data)
        self.validator.validate_status_code(response, 200)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "message", str(pet_id))