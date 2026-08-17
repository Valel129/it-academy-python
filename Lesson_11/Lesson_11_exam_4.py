# Напишите функцию
# process_numbers(numbers, operation)
# которая принимает:
# ● список чисел;
# ● функцию, выполняющую преобразование одного числа.
# Функция должна вернуть новый список, содержащий результат применения operation к каждому элементу.
# Например:
# numbers = [1, 2, 3, 4]
# result = process_numbers(numbers, lambda x: x ** 2)
# print(result)
# Результат:
# [1, 4, 9, 16]
# Продемонстрируйте работу функции, передав ей три разные операции:
# ● квадрат;
# ● куб;
# ● модуль числа.
# 3 вызова с lambda и три функции написать самостоятельно. Итого 6 вызовов.

def process_numbers(numbers: list, operation) -> list:

    output = []

    for x in numbers:
        output.append(operation(x))
    return output

def get_square(x):
    return x ** 2

def get_cube(x):
    return x ** 3

def get_abs(x):
    return abs(x)

numbers_list = [1, 2, -3, 4]
print(f"Исходный список: {numbers_list}\n")

res_func_sq = process_numbers(numbers_list, get_square)
res_func_cb = process_numbers(numbers_list, get_cube)
res_func_ab = process_numbers(numbers_list, get_abs)

print("=== Вызовы через обычные функции ===")
print(f"Квадрат: {res_func_sq}")
print(f"Куб:     {res_func_cb}")
print(f"Модуль:  {res_func_ab}\n")

res_lam_sq = process_numbers(numbers_list, lambda x: x ** 2)
res_lam_cb = process_numbers(numbers_list, lambda x: x ** 3)
res_lam_ab = process_numbers(numbers_list, lambda x: abs(x))

print("=== Вызовы через Лямбда функции ===")
print(f"Квадрат: {res_lam_sq}")
print(f"Куб:     {res_lam_cb}")
print(f"Модуль:  {res_lam_ab}")