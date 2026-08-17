# Задание 4
# Напишите функцию longest_word(text), которая:
# ● принимает строку;
# ● находит самое длинное слово;
# ● возвращает его.
# Если слов одинаковой длины несколько — вернуть первое.

"""Первое решение, к которому я пришел (тут я через
"""

def longest_word(text: str) -> str | None:

    words = text.split()

    if not text:
        return None

    longest_word = [text[0]]

    for word in words:
        if len(word) > len(longest_word[0]):
            longest_word[0] = word

    return longest_word[0]

print(longest_word("Яблоко Мандарин Груша Апельсин"))

"""Чуть упростил функцию и сделал как в примере, где мы решали схожую задачу, но с числами
"""

def longest_word(text: str) -> str | None:

    words = text.split()

    if not text:
        return None

    longest = words[0]

    for word in words[1:]:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word("Яблоко Мандарин Груша Апельсин"))

"""Нашел решение через key=len (вроде, ты его показывал)
"""

def longest_word(text: str) -> str | None:
    return max(text.split(), key=len)

print(longest_word("Яблоко Мандарин Груша Апельсин"))

def longest_word(text: str) -> str | None:

    words = text.split()

    if not text:
        return None

    longest_word = [words[0]]
    print(longest_word)
    print(longest_word[0])

    for word in words:
        if len(word) > len(longest_word[0]):
            print(words[0])
            print(words[1])
            print(words)
            print(longest_word)
            print(longest_word[0])
            longest_word[0] = word

    return longest_word[0]

(longest_word("Яблоко Мандарин Груша Апельсин"))

# print(longest_word("Яблоко Мандарин Груша Апельсин"))