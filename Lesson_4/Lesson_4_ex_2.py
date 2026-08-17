""" Задание 2
Напишите программу, которая рассчитывает финальную стоимость заказа с учетом доставки. Пользователь вводит
сумму покупки (число) и тип клиентской зоны (строка: "RU", "EU" или "US").
Логика расчета:
● Если зона "RU": при сумме покупки от 5000 руб. доставка бесплатная, иначе доставка стоит 500 руб.
● Если зона "EU": фиксированная стоимость доставки 1000 руб. для любых заказов.
● Если зона "US": при сумме покупки более 15000 руб. доставка стоит 800 руб., иначе — 2000 руб.
Программа должна вывести итоговую стоимость (сумма + доставка) с использованием f-строки отладочного
формата вида {total_price=}.
"""

price = float(input("Please enter your price:\n"))  # Вложенные условия
area = input("Please specify your customer area (RU, EU, US):\n").upper()

if area == "RU":
    if price >=5000:
        delivery_price = 0
    else:
        delivery_price = 500
elif area == "EU":
    delivery_price = 1000
elif area == "US":
    if price > 15000:
        delivery_price = 800
    else:
        delivery_price = 2000
total_price = price + float(delivery_price)

print(f"{total_price= } rubles.")


price = float(input("Please enter your price:\n"))  # Вложенные условия и инфа о стоимости доставки
area = input("Please specify your customer area (RU, EU, US):\n").upper()

if area == "RU":
    if price >=5000:
        delivery_price = 0
        msg = f"Your delivery is free."
    else:
        delivery_price = 500
        msg = f"Your delivery will cost 500 rubles (included)."
elif area == "EU":
    delivery_price = 1000
    msg = f"Your delivery cost is 1000 rubles for any order (included)."
elif area == "US":
    if price > 15000:
        delivery_price = 800
        msg = f"Your delivery will cost 800 rubles (included)."
    else:
        delivery_price = 2000
        msg = f"Your delivery will cost 2000 rubles (included)."
total_price = price + float(delivery_price)

print(f"{msg} Your {total_price= } rubles.")


price = float(input("Please enter your price:\n"))  # Сделал через тернарный оператор и тоже с инфой о стоимости доставки.
area = input("Please specify your customer area (RU, EU, US):\n").upper()

if area == "RU":
    delivery_price = 0 if price >= 5000 else 500
    msg = f"Your delivery is free." if price >= 5000 else f"Your delivery will cost 500 rubles (included)"
elif area == "EU":
    delivery_price = 1000
    msg = f"Your delivery cost is 1000 rubles for any order (included)."
elif area == "US":
    delivery_price = 800 if price > 15000 else 2000
    msg = f"Your delivery will cost 800 rubles (included)." if price > 15000 else f"Your delivery will cost 2000 rubles (included)."
total_price = price + float(delivery_price)

print(f"{msg} Your {total_price= } rubles")