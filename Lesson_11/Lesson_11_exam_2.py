# Задание 2
# Пользователь вводит предложение.
# Необходимо написать функцию
# analyze_text(text)
# которая возвращает словарь следующего вида:
# {
# "words": ...,
# "letters": ...,
# "longest_word": …,
# "shortest_word": ...,
# "unique_words": ...
# }
# где:
# ● words — количество слов;
# ● letters — количество букв (без учета пробелов);
# ● longest_word — самое длинное слово.
# ● shortest_word — самое короткое слово;
# ● unique_words — количество различных слов без учета регистра.
# Запрещается использовать регулярные выражения и сторонние библиотеки. Нельзя использовать функцию max()

def analyze_text(text: str) -> dict | None:

    words = text.split()

    letters_count = len(text.replace(" ", ""))

    if not words:
        return None

    unique_words_set = set()

    for word in words:
        unique_words_set.add(word.lower())

    unique_words_count = len(unique_words_set)

    longest = words[0]
    shortest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word

    resulting_dict = {
    "words": len(words),
    "letters": letters_count,
    "longest_word": longest,
    "shortest_word": shortest,
    "unique_words": unique_words_count
}
    return resulting_dict

print(*analyze_text("Hello there! How is it going?").items(), sep="\n")

"""ИЛИ"""

result = analyze_text("Hello there! How is it going?")

# 2. Печатаем заголовок
print("Результат анализа:")

# 3. Достаем данные из словаря по ключам и выводим столбиком
print(f"words: {result['words']}")
print(f"letters: {result['letters']}")
print(f"longest_word: {result['longest_word']}")
print(f"shortest_word: {result['shortest_word']}")
print(f"unique_words: {result['unique_words']}")