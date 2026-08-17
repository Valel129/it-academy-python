# Задание 2
# Создайте декоратор ignore_duplicates, который не позволяет выполнить функцию два раза подряд с одинаковыми аргументами.
# Пример:
# @ignore_duplicates
# def send_message(text):
# print(f"Отправлено: {text}")
# Вызовы
# send_message("Привет")
# send_message("Привет")
# send_message("Как дела?")
# send_message("Как дела?")
# send_message("Привет")
# должны вывести
# Отправлено: Привет
# Повторный вызов проигнорирован.
# Отправлено: Как дела?
# Повторный вызов проигнорирован.
# Отправлено: Привет

from functools import wraps

def ignore_duplicates(func):
    previous_message_args = None
    previous_message_kwargs = None
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal previous_message_args
        nonlocal previous_message_kwargs
        if args == previous_message_args and kwargs == previous_message_kwargs:
            print("Повторный вызов проигнорирован")
            return None
        else:
            previous_message_args = args
            previous_message_kwargs = kwargs
            return func(*args, **kwargs)
    return wrapper
#
#
# @ignore_duplicates
# def send_message(text: str) -> str | None:
#     print(f"Отправлено: {text}")
#
# send_message("Привет")
# send_message({"Hello": "World"})
# send_message("Привет")
# send_message("Привет")
# send_message("Как дела?")
# send_message("Как дела?")
# send_message("Привет")
# send_message("Нормально, как всегда")
# send_message("Нормально, как всегда")

from functools import wraps

def ignore_duplicates(func):
    previous_message_args = None
    previous_message_kwargs = None
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal previous_message_args
        nonlocal previous_message_kwargs
        if args == previous_message_args and kwargs == previous_message_kwargs:
            print("Повторный вызов проигнорирован")
            return None
        else:
            previous_message_args = args
            previous_message_kwargs = kwargs
            return func(*args, **kwargs)
    return wrapper


@ignore_duplicates
def send_message(*args, **kwargs) -> str | None:
    print(f"Отправлено: {args}, {kwargs}")

send_message("Привет", {"Alex": "Employee"})
send_message("Привет", {"Alex": "Employee"})
send_message("Пока", {"Alex": "Employee"})
send_message("Пока", {"Alex": "Unemployed"})

