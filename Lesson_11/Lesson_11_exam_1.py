# Задание 1
# Пользователь вводит последовательность целых чисел через пробел.
# Например:
# 5 8 -2 10 3 8 10
# Необходимо:
# 1. получить список чисел;
# 2. вывести:
# ○ максимальное число;
# ○ минимальное число;
# ○ сумму всех положительных чисел;
# 3. вывести список уникальных чисел в порядке возрастания.
# Нельзя использовать max(), min() и sum().

user_input = input("Пожалуйста, введите целые числа через пробел: ")
raws = user_input.split()

if not raws:
    print("Вы ничего не ввели.")
else:
    numbers = [int(n) for n in raws]

max_num = numbers[0]
min_num = numbers[0]
positive_summ = 0

for n in numbers:
    if n > max_num:
        max_num = n

    if n < min_num:
        min_num = n

    if n > 0:
        positive_summ += n

unique_sorted_numbers = sorted(set(numbers))

print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
print(f"Сумма всех положительных чисел: {positive_summ}")
print(f"Список уникальных чисел по возрастания: {unique_sorted_numbers}")