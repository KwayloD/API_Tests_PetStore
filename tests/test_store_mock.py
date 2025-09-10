from validators import ResponseValidator

class TestStoreWithMockAPI:
    validator = ResponseValidator()

    def test_get_pet_inventory_with_mock(self, api_store, get_mock_inventory):
        """Тест на получения фальшивого инвентаря питомцев методом GET"""
        response = api_store.get_store_inventory()
        print("MOCK-ответ от API:", f"Code: {response.status_code}", response.json())
        self.validator.validate_status_code(response, 200)

    def test_post_place_an_order_with_mock(self, api_store, mock_order_data):
        """Тест на создание фальшивого заказа методом POST в магазине"""
        response = api_store.post_store_order(mock_order_data)
        print("MOCK-ответ от API:", f"Code: {response.status_code}", response.json())
        self.validator.validate_status_code(response, 201)
        self.validator.validate_json_response(response)
        self.validator.validate_json_value(response, "id", mock_order_data["id"])
        self.validator.validate_json_value(response, "petId", mock_order_data["petId"])
        self.validator.validate_json_value(response, "quantity", mock_order_data["quantity"])

    def test_get_order_with_wrong_id(self, api_store, mock_order_with_wrong_id):
        """Негативный тест: в ответе приходит другой ID"""
        requested_id, data = mock_order_with_wrong_id
        response = api_store.get_store_order(requested_id)
        print("MOCK-ответ от API:", f"Code: {response.status_code}", response.json())
        self.validator.validate_status_code(response, 400)
        self.validator.validate_json_response(response)
        self.validator.validate_invalid_json_value(response, "id", requested_id)

    def test_delete_purchase_by_wrong_id(self, api_store, mock_delete_order):
        """Негативный тест: удаление заказа на покупку, в ответе приходит другой ID"""
        requested_id, data = mock_delete_order
        response = api_store.delete_store_order(requested_id)
        print("JSON-ответ от API:", f"Code: {response.status_code}", response.json())
        self.validator.validate_status_code(response, 400)
        self.validator.validate_json_response(response)
        self.validator.validate_invalid_json_value(response, "message", str(requested_id))