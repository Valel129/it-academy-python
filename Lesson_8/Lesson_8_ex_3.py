# Задание 3
# Напишите функцию is_palindrome(text), которая:
# ● принимает строку;
# ● игнорирует регистр букв и пробелы;
# ● возвращает True, если строка является палиндромом, иначе False.

"""Игнорирует пробелы через .replace()
"""

def is_palindrome(text: str) -> bool:

    text = text.replace(" ", "").lower()

    if text == text[::-1]:
        return True
    else:
        return False

print(is_palindrome("А роза упала на лапу Азора"))

"""Игнорирует пробелы через "".join(...split())
"""

def is_palindrome(text: str) -> bool:

    text = "".join(text.split()).lower()

    if text == text[::-1]:
        return True
    else:
        return False

print(is_palindrome("А роза упала на лапу Азора"))