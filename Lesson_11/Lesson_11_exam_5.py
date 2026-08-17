# Задание 5
# products = [
# {"name": "Хлеб", "price": 70, "count": 2},
# {"name": "Молоко", "price": 120, "count": 1},
# {"name": "Сыр", "price": 350, "count": 3},
# ]
# Написать функцию, которая возвращает
# {
# "total": ...,
# "most_expensive": ...,
# "items": ...
# }
# где
# ● total — общая стоимость покупки;
# ● most_expensive — название самого дорогого товара;
# ● items — общее количество товаров.

products = [
    {"name": "Хлеб", "price": 70, "count": 2},
    {"name": "Молоко", "price": 120, "count": 1},
    {"name": "Сыр", "price": 350, "count": 3},
]

def calculate_order(catalog: list) -> dict:
    if not catalog:
        return {"total": 0, "most_expensive": "", "items": 0}

    total_cost = 0
    total_items = 0

    max_price = catalog[0]["price"]
    expensive_name = catalog[0]["name"]

    for prod in catalog:

        total_cost += prod["price"] * prod["count"]
        total_items += prod["count"]

        if prod["price"] > max_price:
            max_price = prod["price"]
            expensive_name = prod["name"]

    return {
        "total": total_cost,
        "most_expensive": expensive_name,
        "items": total_items
    }

res = calculate_order(products)

print("Результат подсчета:")
print(f"total: {res['total']}")
print(f"most_expensive: {res['most_expensive']}")
print(f"items: {res['items']}")

