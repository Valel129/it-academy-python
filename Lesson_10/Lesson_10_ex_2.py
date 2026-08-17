# Задание 2
# words = [
# "Python",
# "java",
# "C++",
# "Rust",
# "Go",
# "Swift",
# "PHP"
# ]
# Получите новый список, содержащий слова длиной не менее пяти символов в нижнем регистре.

words = ["Python", "java", "C++", "Rust", "Go", "Swift", "PHP"]

new_words = [word.lower() for word in words if len(word) >= 5]

print(new_words)