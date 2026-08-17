# Задание 2
# Напишите декоратор limit_calls, который ограничивает количество вызовов функции.
# Декоратор принимает три параметра:
# ● limit — максимальное количество вызовов;
# ● message — сообщение, которое выводится после достижения лимита;
# ● default — значение, которое возвращается вместо результата функции после достижения лимита.
# Пример:
# @limit_calls(
# limit=3,
# message="Лимит вызовов исчерпан!",
# default=None
# )
# def get_data(name, age):
# print(f"Получаем данные: {name}, {age}")
# return f"{name}: {age}"
# print(get_data("Иван", 20))
# print(get_data("Анна", 25))
# print(get_data("Петр", 30))
# print(get_data("Мария", 22))
# Первые три вызова должны выполнить функцию.
# Четвёртый и последующие вызовы должны вывести:
# Лимит вызовов исчерпан!
# и вернуть:
# None
# При этом декоратор должен сохранять количество вызовов отдельно для каждой декорированной функции.
# Например:
# @limit_calls(2, "Лимит!", 0)
# def add(a, b):
# return a + b
# @limit_calls(3, "Больше нельзя!", [])
# def get_items(category):
# return ["item1", "item2"]
# У add и get_items должны быть независимые счётчики.
# Дополнительное условие: декорируемая функция может принимать любое количество *args и **kwargs.


from functools import wraps
from typing import Callable, Any


def limit_calls(limit: int, message: str, default: Any) -> Callable:

    def decorator(func):
        calls_count = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls_count
            calls_count += 1

            if calls_count > limit:
                print(message)
                return default

            return func(*args, **kwargs)

        return wrapper

    return decorator

@limit_calls(limit=3, message="Лимит вызовов исчерпан!", default=None)
def get_data(name: str, age: int) -> str | int:
    print(f"Получаем данные: {name}, {age}")
    return f"{name}: {age}"

print(get_data("Иван", 20))
print(get_data("Анна", 25))
print(get_data("Петр", 30))
print(get_data("Мария", 22))

print("\n" + "="*30 + "\n")

@limit_calls(2, "Лимит!", 0)
def add(a: int, b: int) -> int:
    return a + b

@limit_calls(3, "Больше нельзя!", [])
def get_items(category: str) ->list[str]:
    return ["item1", "item2"]


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

print("\n" + "="*30 + "\n")

print(get_items("гаджеты"))
print(get_items("деньги"))
print(get_items("книги"))
print(get_items("ключи"))
print(get_items("документы"))