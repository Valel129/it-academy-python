# Задание 3
# Создайте функцию:
# convert(value, from_unit, to_unit)
# Поддерживаемые единицы:
# km
# m
# cm
# Примеры:
# convert(5, "km", "m")
# Результат:
# 5000
# convert(350, "cm", "m")

"""Первый вариант, к которому я пришел сам."""

def convert(value: int | float | None, from_unit: str, to_unit: str) -> int | float | None:

    km_to_m = value * 1000
    km_to_cm = value * 100000
    m_to_cm = value * 100
    m_to_km = value / 1000
    cm_to_m = value / 100
    cm_to_km = value / 100000

    if from_unit == "km" and to_unit == "m":
        value = km_to_m
    elif from_unit == "km" and to_unit == "cm":
        value = km_to_cm
    elif from_unit == "m" and to_unit == "cm":
        value = m_to_cm
    elif from_unit == "m" and to_unit == "km":
        value = m_to_km
    elif from_unit == "cm" and to_unit == "m":
        value = cm_to_m
    elif from_unit == "cm" and to_unit == "km":
        value = cm_to_km
    else:
        return value
    return value

print(convert(5, "km", "m"))
print(convert(350, "cm", "m"))
print(convert(1, "km", "cm"))
print(convert(3000, "m", "km"))
print(convert(700, "m", "cm"))
print(convert(200000, "cm", "m"))
print(convert(400000, "cm", "km"))
print(convert(12, "cm", "cm"))
print("=" * 24)

"""Вариант, который я нашел уже через поиск в гугле и разобрал, что к чему.
Он, конечно, куда более компактный, но самому до него изначально трудно дойти пока))"""


def convert(value: int | float, from_unit: str, to_unit: str) -> float | None:

    to_meters = {
        "km": 1000,
        "m": 1,
        "cm": 0.01
    }

    if from_unit not in to_meters or to_unit not in to_meters:
        return None

    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]

    return result

print(convert(5, "km", "m"))
print(convert(350, "cm", "m"))
print(convert(1, "km", "cm"))
print(convert(3000, "m", "km"))
print(convert(700, "m", "cm"))
print(convert(200000, "cm", "m"))
print(convert(400000, "cm", "km"))
print(convert(12, "cm", "cm"))