# Задание 5 Есть файл users.csv:
# name,email,phone
# Alex,alex@example.com,+375291234567
# Maria,maria@test.by,+375441112233
# John,john@example,+375123
# Anna,anna@gmail.com,+375297778899
# Программа должна:
# ● прочитать CSV;
# ● проверить каждый email с помощью регулярного выражения;
# ● проверить телефон;
# ● вывести пользователей с некорректными данными.

import csv
import os
import re

csv_file = os.path.join(os.getcwd(), "users.csv")

correct_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
correct_phone = r"\+\d{12}"

with open(csv_file, "r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row["name"]
        email = row["email"].strip()
        phone = row["phone"].strip()

        is_email_correct = bool(re.fullmatch(correct_email, email))
        is_phone_correct = bool(re.fullmatch(correct_phone, phone))

        if not is_email_correct or not is_phone_correct:

            print(f"Пользователь с некорректными данными: {name}")

            if not is_email_correct:

                print(f"Некорректный email: {email}")

            if not is_phone_correct:
                print(f"Некорректный номер телефона: {phone}")