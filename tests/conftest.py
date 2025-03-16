import pytest
from faker import Faker
from datetime import datetime, timezone
import json
import os
from api.api_client import APIClient, APIStore
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
        return data.get('id')

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