# Задание 1
# Напишите декоратор repeat, который позволяет автоматически повторять вызов функции несколько раз.
# Декоратор принимает два параметра:
# times — количество повторений;
# separator — строка, которая выводится между результатами.
# Пример:
# @repeat(times=3, separator="---")
# def greet(name):
# return f"Привет, {name}!"
# print(greet("Иван"))
# Ожидаемый результат:
# Привет, Иван!
# ---
# Привет, Иван!
# ---
# Привет, Иван!
# При этом декоратор должен корректно работать с функциями, которые принимают несколько параметров:
# @repeat(times=2, separator="=")
# def add(a, b):
# return a + b
# print(add(5, 3))
# Результат:
# 8
# =
# 8
# Условия:
# ● Использовать декоратор с параметрами.
# ● Использовать *args и **kwargs.
# ● Не изменять код декорируемой функции.
# ● Сохранить результаты всех выполнений функции и объединить их в одну строку, используя separator в качестве разделителя.
# Декоратор должен вернуть полученную объединённую строку.

from functools import wraps
from typing import Callable

def repeat(times: int, separator: str) ->Callable:

    def repeat_decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            resulting_list = []

            for _ in range(times):
                res = func(*args, **kwargs)
                resulting_list.append(str(res))

            full_separator = f"\n{separator}\n"
            final_result = full_separator.join(resulting_list)

            return final_result

        return wrapper

    return repeat_decorator

@repeat(times=3, separator="---")
def greet(name: str) -> str:
    return f"Привет, {name}!"

print(greet("Иван"), end="\n\n")

@repeat(times=2, separator="=")
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 3))

