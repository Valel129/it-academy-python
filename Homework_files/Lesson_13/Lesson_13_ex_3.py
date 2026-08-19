# Задание 3
# Напишите декоратор handle_errors, который автоматически перехватывает ошибки, возникающие внутри функции.
# Например, есть функция:
# @handle_errors
# def divide(a, b):
# return a / b
# Декоратор должен:
# ● выполнить функцию;
# ● если функция завершилась успешно — вернуть её результат;
# ● если возник ZeroDivisionError — вывести: Ошибка: деление на ноль.
# ● если возник ValueError — вывести: Ошибка: некорректное значение.
# ● в любом случае программа не должна завершаться с traceback.
# Проверьте работу декоратора:
# print(divide(10, 2))
# print(divide(10, 0))
# Ожидаемое поведение:
# 5.0
# Ошибка: деление на ноль.
# Дополнительное усложнение
# Сделайте так, чтобы декоратор работал не только с divide(), но и с другими функциями:
# @handle_errors
# def convert_to_int(value):
# return int(value)
# Например:
# convert_to_int("100")
# convert_to_int("hello")

from functools import wraps
from typing import Callable, Any

def handle_errors(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        try:
            return func(*args, **kwargs)

        except ZeroDivisionError:
            print(f"Ошибка: деление на ноль", end="")
            return ""  # Если не ставить end="" в print, то можно было бы в return print(end="") добавить везде

        except ValueError:
            print(f"Ошибка: некорректное значение", end="")
            return ""

        except TypeError:  # Добавил еще проверку на TypeError, чтобы могло поймать ошибку в делении на строку
            print(f"Ошибка: нужно ввести число", end="")
            return ""

    return wrapper

@handle_errors
def divide(a: int | float, b: int | float) -> float:
    return a / b

print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "Два"))

@handle_errors
def convert_to_int(value: Any) -> int:
    return int(value)

print("=" * 30)

print(convert_to_int("100"))
print(convert_to_int("hello"))