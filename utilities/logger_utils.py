import logging

def setup_logger(name="api_tests", log_file="test_logs.log", level=logging.INFO):
    """Настройка логирования"""
    logger = logging.getLogger(name)

    # Если у логгера уже есть обработчики, просто возвращаем его
    if logger.handlers:
        return logger

    # Устанавливаем уровень логирования
    logger.setLevel(level)

    # Создаём формат логов
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Файл для логирования (все уровни)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")  # Создаёт обработчик, который записывает логи в файл
    file_handler.setFormatter(formatter)  # Применяет формат к логам
    logger.addHandler(file_handler)  # Добавляет этот обработчик к логгеру

    return logger