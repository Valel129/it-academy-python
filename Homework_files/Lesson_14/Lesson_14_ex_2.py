# Задание 2
# Есть файл data.txt
# Напишите программу, которая:
# ● проверяет существование файла с помощью os.path.exists();
# ● если файла нет — выводит сообщение;
# ● если файл существует — читает его;
# ● создаёт директорию backup если её ещё нет;
# ● создаёт backup/data.txt
# записывает туда содержимое исходного файла.

import os

source_file = os.path.join(os.getcwd(), "data.txt")
backup_dir = os.path.join(os.getcwd(), "backup")
backup_file = os.path.join(backup_dir, "data.txt")

if not os.path.exists(source_file):

    print("Ошибка: файл не найден")

else:

    with open(source_file, "r", encoding="utf-8") as file:
        text = file.read()

    if not os.path.exists(backup_dir):
        os.mkdir(backup_dir)
        print("Создание backup папки")

    with open(backup_file, "w", encoding="utf-8") as file:
        file.write(text)

    print("Копирование данных успешно завершено! Файл скопирован в папку backup.")
