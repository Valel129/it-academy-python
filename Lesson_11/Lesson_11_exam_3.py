# Задание 3
# Дан список оценок:
# grades = [78, 91, 56, 83, 95, 61, 88]
# Используя map() и filter():
# 1. оставить оценки не ниже 60;
# 2. увеличить каждую оставшуюся оценку на 5 баллов;
# 3. вывести полученный список.
# Использование обычного цикла для обработки списка запрещено.

grades = [78, 91, 56, 83, 95, 61, 88]

passed_grades = filter(lambda g: g >= 60, grades)

updated_grades = map(lambda g: g + 5, passed_grades)

final_grades = list(updated_grades)

print(f"Полученный список оценок: {final_grades}")