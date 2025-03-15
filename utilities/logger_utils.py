import logging
import sys
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
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Консольный вывод только для уровня ERROR
    console_handler = logging.StreamHandler(sys.stdout)  # Cоздаёт обработчик для вывода в консоль
    console_handler.setLevel(logging.ERROR)  # Устанавливаем уровень ERROR для консоли
    console_handler.setFormatter(formatter)  # Формат 'formatter' используется для файлового и консольного обработчика
    logger.addHandler(console_handler)

    return logger