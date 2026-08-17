# Задание 4
# Отсортируйте список
# cities = [
# "Москва",
# "Париж",
# "Берлин",
# "Рим",
# "Токио"
# ]
# по последней букве каждого слова.
# Используйте lambda.

cities = ["Москва", "Париж", "Берлин", "Рим", "Токио"]

sorted_cities = sorted(cities, key = lambda city: city[-1])

print(sorted_cities)