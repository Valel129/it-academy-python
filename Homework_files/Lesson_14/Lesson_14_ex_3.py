# Задание 3
# Дана директория:
# project/
# data.txt
# confi g.json
# image.png
# users.txt
# README.md
# Напишите программу, которая с помощью os.listdir():
# ● получает список содержимого директории;
# ● находит только файлы с расширением .txt;
# ● выводит их имена;
# ● считает их количество.
#

import os

project_dir = os.path.join(os.getcwd(), "project")

txt_file_count = 0

all_files = os.listdir(project_dir)

for item in all_files:

    if item.endswith(".txt"):
        txt_file_count += 1
        print(f"Файл txt найден: {item}")

print("=" * 30)

print(f"Всего txt файлов найдено: {txt_file_count}")
