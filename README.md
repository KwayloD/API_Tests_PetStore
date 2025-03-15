## Практикуюсь писать автотесты на Python для API: https://petstore.swagger.io/
Для работы данного кода понадобятся следующие библиотеки **Python**:
+ `pytest`
+ `rquests`
+ `dotenv`
+ `os`
+ `faker`
+ `datetime`
+ `json`
+ `logging`
+ `sys`

## Структура проекта:
+ `api` содержит файл *api_client.py* с описанием методов
+ `test_data` сюда сохраняются json-файлы с тестовыми данными
+ `tests` содержит файлы API-тестов. В *conftest.py* содержатся фикстуры, в *validators.py* - валидаторы
+ `utilities` содержит файл *logger_utils.py*, который оформляет логги и записывает их в папку `tests` в файл *test_logs.log*
+ `.env` содержит информацию для тестов