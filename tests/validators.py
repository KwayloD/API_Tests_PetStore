import json
from utilities.logger_utils import setup_logger
logger = setup_logger()


class ResponseValidator:
    """Класс для проверки различных аспектов HTTP-ответа"""

    @staticmethod
    def validate_status_code(response, expected_status):
        """Проверяет, что стутус-код ответа соответствует ожидаемому"""
        assert response.status_code == expected_status, (f"Ошибка {response.status_code}: {response.text}")

    @staticmethod
    def validate_json_response(response):
        """Проверяет, что тело ответа валидный JSON"""
        try:
            response.json()
        except json.JSONDecodeError:
            assert False, "Ответ не является валидным JSON"

    @staticmethod
    def validate_json_value(response, value, excepted_value):
        """Проверяет, что в JSON-ответе есть нужное значение и оно соответствует ожидаемому"""
        json_data = response.json()
        assert value in json_data, f"Ответ не содержит {value}"
        assert json_data[value] == excepted_value, (f"Ожидали {excepted_value}, а получили {json_data[value]}")

    @staticmethod
    def validate_status(response, value, excepted_value):
        """Проверяет статусы JSON-объектов, которые приходыт в списке"""
        for obj in response.json():
            assert obj[value] == excepted_value, (f"Ожидали {excepted_value}, а получили {obj[value]}")

    @staticmethod
    def validate_dict_field(response, field_name, required_keys):
        """Проверяет, что указанное поле является словарем и содержит нужные ключи"""
        json_data = response.json()
        assert field_name in json_data, f"Ответ не содержит поле '{field_name}'"
        assert isinstance(json_data[field_name], dict), f"'{field_name}' должно быть словарем"
        missing_keys = [key for key in required_keys if key not in json_data[field_name]]
        assert not missing_keys, f"'{field_name}' не содержит ключи: {missing_keys}"

    @staticmethod
    def validate_list_field(response, field_name, required_keys):
        """Проверяет, что указанное поле является списком словарей и содержит нужные ключи"""
        json_data = response.json()
        assert field_name in json_data, f"Ответ не содержит поле '{field_name}'"
        assert isinstance(json_data[field_name], list), f"'{field_name}' должно быть списком"
        for index, item in enumerate(json_data[field_name]):
            assert isinstance(item, dict), f"Элемент {index} в '{field_name}' должен быть словарем"
            missing_keys = [key for key in required_keys if key not in item]
            assert not missing_keys, f"Элемент {index} в '{field_name}' не содержит ключи: {missing_keys}"

    @staticmethod
    def validate_invalid_json_value(response, value, excepted_value):
        """Проверяет, что в JSON-ответе есть нужное значение и оно не соответствует ожидаемому"""
        json_data = response.json()
        assert value in json_data, f"Ответ не содержит {value}"
        assert json_data[value] != excepted_value, (f"Ожидали {excepted_value}, а получили {json_data[value]}")