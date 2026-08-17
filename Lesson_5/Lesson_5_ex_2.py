"""Задание 2
Пользователь вводит: имя файла; размер файла в мегабайтах; является ли пользователь администратором (yes/no).
Правила:
1. Если файл имеет расширение .exe или .bat и пользователь не является администратором, вывести: Доступ запрещен: опасный файл
2. Если файл имеет расширение .zip или .rar, его размер меньше 100 МБ и пользователь является
администратором, вывести: Архив администратора принят
3. Во всех остальных случаях вывести: Файл отправлен на проверку"""

"""Первое решение, к которому я пришел."""

file_name = input("Введите имя файла (с расширением самого файла, например, .rar): ")
file_size = int(input("Введите размер файла в мегабайтах: "))
user_status = input("Является ли пользователь администратором (Yes/No): ").capitalize()

if (".exe" in file_name or ".bat" in file_name) and user_status == "No":
    print("Доступ запрещен: опасный файл")
elif (".zip" in file_name or ".rar" in file_name) and file_size < 100 and user_status == "Yes":
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")

"""Здесь я решил сделать множественное присваивание в одну строку"""

file_name, file_size, user_status = input("Введите имя файла (с расширением самого файла, например, .rar): "), int(input("Введите размер файла в мегабайтах: ")), input("Является ли пользователь администратором (Yes/No): ").capitalize()

if (".exe" in file_name or ".bat" in file_name) and user_status == "No":
    print("Доступ запрещен: опасный файл")
elif (".zip" in file_name or ".rar" in file_name) and file_size < 100 and user_status == "Yes":
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")

"""Ну а здесь просто поэкспериментировал с методом split, вышло как костыль, конечно))"""

user_input = input("Вводите через один пробел: Имя файла, Размер в мб, Является ли пользователь администратором (Yes/No): ")

file_name, file_size, user_status = user_input.split()

file_size = int(file_size)
user_status = user_status.capitalize()

if (".exe" in file_name or ".bat" in file_name) and user_status == "No":
    print("Доступ запрещен: опасный файл")
elif (".zip" in file_name or ".rar" in file_name) and file_size < 100 and user_status == "Yes":
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")

"""Здесь я сделал уже по твоей подсказке, которую просмотрел только в пятницу уже))"""

file_name = input("Введите имя файла (с расширением самого файла, например, .rar): ")
file_size = int(input("Введите размер файла в мегабайтах: "))
is_admin = input("Являетесь ли вы админом?(Yes/No): ").capitalize()

if (file_name.endswith(".exe") or file_name.endswith(".bat")) and is_admin == "No":
    print("Доступ запрещен: опасный файл")
elif (file_name.endswith(".zip") or file_name.endswith(".rar")) and file_size < 100 and is_admin == "Yes":
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")

"""А в этом варианте я решил упростить сами условия, добавив две переменные is_dangerous, is_archive. 
Плюс сделал is_admin bool через сравнение ==.
Подскажи, пожалуйста, какой из вариантов наиболее практичный?"""

file_name = input("Введите имя файла (с расширением самого файла, например, .rar): ")
file_size = int(input("Введите размер файла в мегабайтах: "))
is_admin = input("Являетесь ли вы админом?(Yes/No): ").capitalize() == "Yes"

is_dangerous = file_name.endswith(".exe") or file_name.endswith(".bat")
is_archive = file_name.endswith(".zip") or file_name.endswith(".rar")

if is_dangerous and not is_admin:
    print("Доступ запрещен: опасный файл")
elif is_archive and file_size < 100 and is_admin:
    print("Архив администратора принят")
else:
    print("Файл отправлен на проверку")