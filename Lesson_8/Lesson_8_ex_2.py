# Задание 2
# Создайте функцию
# business_card(name, surname, **kwargs)
# Обязательные параметры:
# ● имя;
# ● фамилия.
# Остальная информация передается через **kwargs.
# Пример вызова
# business_card(
# "Иван",
# "Иванов",
# age=30,
# city="Минск",
# company="Google",
# email="ivan@gmail.com"
# )
# Результат
# =====================
# Иван Иванов
# Age: 30
# City: Минск
# Company: Google
# Email: ivan@gmail.com
# =====================
# Не обязательно:
# ● вывести дополнительные поля в алфавитном порядке.

"""Сначала сделал через print
"""

def business_card(name: str, surname: str, **adinfo: int | str | float | bool | None) -> dict | int | str | float | bool | None:

    print(f"{name} {surname}")

    for key, value in sorted(adinfo.items()):
        print(f"{key}: {value}")

business_card("Иван", "Иванов", Company="Google", Age=34, City="Moscow", Email="1234567@gmail.com")

"""Пришлось повозиться и покопаться, чтобы вывести функцию через return
"""

def business_card(name: str, surname: str, **adinfo: str | dict | list | int) -> dict | int | str | float | bool | None | list:

    collection = []

    for key, value in sorted(adinfo.items()):
        collection.append(f"{key}: {value}")

    resulting_kwargs = "\n".join(collection)

    border = "=" * 24

    return f"{border}\n{name} {surname}\n{resulting_kwargs}\n{border}"

print(f"Характеристика:\n{business_card('Иван', 'Иванов', Company='Google', Age=34, City='Moscow', Email='1234567@gmail.com')}")