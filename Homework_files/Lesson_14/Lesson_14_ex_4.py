# Задание 4 Содержимое:
# name,price,category
# Laptop,1200,Electronics
# Phone,800,Electronics
# Book,25,Books
# Table,300,Furniture
# Напишите программу, которая:
# ● читает CSV;
# ● выводит названия всех товаров;
# ● находит товары дороже 500;
# ● считает их количество;
# ● выводит самый дорогой товар.

import os
import csv

csv_file = os.path.join(os.getcwd(), "products.csv")

expensive_count = 0
max_price = 0
most_expensive_product = ""

with open(csv_file,"r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print("Названия всех товаров:")
    n = 1

    for row in reader:

        name = row["name"]
        price = int(row["price"])

        print(f"{n}: {name}")

        n += 1

        if price > max_price:
            max_price = price
            most_expensive_product = name

        if price > 500:
            expensive_count += 1

print("=" * 30)

print(f"Количество товаров дороже 500: {expensive_count}")
print(f"Самый дорогой товар: {most_expensive_product}")