# Задание 2
# Создайте файл math_utils.py.
# Реализуйте функции:
# square(number)
# cube(number)
# is_even(number)
# factorial(number)
# max_of_two(a, b)
# Запрещается использовать встроенные функции max() и math.factorial().
# После создания файла импортируйте функции в другой программе и продемонстрируйте их работу.

from math_utils import square, cube, is_even, factorial, max_of_two

print(square(5))

print(cube(5))

print(max_of_two(5, 25))

print(is_even(6))

print(factorial(5))