# Задание 3
# Дана строка
# text = "functional programming"
# Создайте словарь, где ключ — символ, значение — количество его появлений.
# Пробелы учитывать не нужно.

text = "functional programming"

char_count = {char: text.count(char) for char in text if char != " "}

print(char_count)