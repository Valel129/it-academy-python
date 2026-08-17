# Задание 5
# Дан список
# files = [
# "main.py",
# "test.py",
# "README.md",
# "data.csv",
# "notes.txt"
# ]
# Оставьте только Python-файлы.
# Используйте filter.

files = ["main.py", "test.py", "README.md", "data.csv", "notes.txt"]

python_files = list(filter(lambda file: file.endswith(".py"), files))

print(python_files)