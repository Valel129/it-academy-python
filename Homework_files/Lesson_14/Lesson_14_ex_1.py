# Задание 1
# Создайте программу, которая имитирует журнал событий.
# Пользователь вводит сообщения:
# Введите сообщение:
# Сервер запущен
# Каждое сообщение должно добавляться в log.txt
# Формат:
# Сервер запущен
# Пользователь вошёл в систему
# Получен запрос
# Условие: старые записи нельзя удалять.

import os

file_path = os.path.join(os.getcwd(), "log.txt")

while True:

    message = input("Введите сообщение (для выхода, нажмите exit): ")

    if message == "exit".lower():
        break

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(message + "\n")

