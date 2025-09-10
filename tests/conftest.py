import pytest
from faker import Faker
from datetime import datetime, timezone
import json
import os
from api.api_client import APIClient, APIStore, BASE_URL
fake = Faker()

@pytest.fixture
def api_client():
    """Фикстура для API"""
    return APIClient()

@pytest.fixture
def api_store():
    """Фикстура для API"""
    return APIStore()

@pytest.fixture(params=["available", "pending", "sold"])
def pet_status(request):
    """Фикстура передает статус питомца"""
    return {"status": request.param}

@pytest.fixture()
def pet_data(request):
    """Фикстура для генерации тестовых данных питомца"""
    filename = os.path.join(os.path.dirname(__file__), "..", "test_data", "pet_data.json")
    data = {
        "id": fake.random_int(min=1, max=100),
        "category": {
            "id": fake.random_int(min=1, max=100),
            "name": fake.word()
        },
        "name": fake.first_name(),
        "photoUrls": [fake.image_url()],
        "tags": [
            {
                "id": fake.random_int(min=1, max=100),
                "name": fake.word()
            }
        ],
        "status": fake.random_element(elements=["available", "pending", "sold"])
    }
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(json.dumps(data, ensure_ascii=False, indent=4))
    return data

@pytest.fixture
def get_id_from_pet_data(filename=os.path.join(os.path.dirname(__file__), "..", "test_data", "pet_data.json")):
    """Фикстура забирает id из сгенерированных тестовых данных птомца"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get('id', 'category')

@pytest.fixture()
def pet_update_data():
    """Фикстура для генерации имени и статуса питомца"""
    filename = os.path.join(os.path.dirname(__file__), "..", "test_data", "pet_update_data.json")
    data = {    # Формирование данных для отправки
        "name": fake.user_name(),
        "status": fake.random_element(elements=("placed", "shipped", "delivered"))
    }
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(json.dumps(data, ensure_ascii=False, indent=4))
    return data

@pytest.fixture()
def order_data():
    """Фикстура для генерации тестовых данных заказа"""
    filename = os.path.join(os.path.dirname(__file__), "..", "test_data", "order_data.json")
    data = {
        "id": fake.random_int(min=1, max=100),
        "petId": fake.random_int(min=100, max=200),
        "quantity": fake.random_int(min=1, max=10),
        "shipDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0000",
        "status": fake.random_element(elements=("placed", "shipped", "delivered")),
        "complete": fake.boolean()
    }
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(json.dumps(data, ensure_ascii=False, indent=4))
    return data

@pytest.fixture
def get_id_from_order_data(filename=os.path.join(os.path.dirname(__file__), "..", "test_data", "order_data.json")):
    """Фикстура забирает id из сгенерированных тестовых данных заказа"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get('id')

@pytest.fixture()
def user_data():
    """Фикстура для генерации тестовых данных пользователя"""
    filename = os.path.join(os.path.dirname(__file__), "..", "test_data", "user_data.json")
    data = {
        "id": fake.random_int(min=1, max=100),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": fake.random_int(min=0, max=10)
    }
    with open(filename, 'w', encoding='utf-8') as file_object:
        file_object.write(json.dumps(data, ensure_ascii=False, indent=4))
    return data

@pytest.fixture
def get_username_from_user_data(filename=os.path.join(os.path.dirname(__file__), "..", "test_data", "user_data.json")):
    """Фикстура забирает username из сгенерированных тестовых данных пользователя"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data.get('username')

@pytest.fixture
def get_mock_inventory(requests_mock):
    """Мок: генерация фальшивого инвентаря"""
    data = {
        "available": fake.random_int(min=1, max=100),
        "pending": fake.random_int(min=100, max=100),
        "sold": fake.random_int(min=1, max=100),
        "result": "Все четко!"
    }
    requests_mock.get(f"{BASE_URL}/store/inventory", json=data, status_code=200)
    return data

@pytest.fixture()
def mock_order_data(requests_mock):
    """Мок: генерация фальшивых тестовых данных заказа"""
    data = {
        "id": "unknown",
        "petId": "unknown",
        "quantity": "unknown",
        "shipDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "+0000",
        "status": fake.random_element(elements=("placed", "shipped", "delivered")),
        "complete": fake.boolean()
    }
    requests_mock.post(f"{BASE_URL}/store/order", json=data, status_code=201)
    return data

@pytest.fixture()
def mock_order_with_wrong_id(requests_mock):
    """Мок: запрашиваем один order_id, а в ответе другой"""
    requested_id = 199   # то, что передадим в метод
    data = {
        "id": 99,       # специально другой ID
        "petId": 555,
        "quantity": 3,
        "status": "placed",
        "complete": True
    }
    requests_mock.get(f"{BASE_URL}/store/order/{requested_id}", json=data, status_code=400)
    return requested_id, data

@pytest.fixture()
def mock_delete_order(requests_mock):
    """Мок: удаляем заказ с одним order_id, а в ответе другой order_id"""
    requested_id = 99   # то, что передадим в метод
    data = {
        "code": 123,
        "type": "deleted",
        "message": "23"
    }
    requests_mock.delete(f"{BASE_URL}/store/order/{requested_id}", json=data, status_code=400)
    return requested_id, data