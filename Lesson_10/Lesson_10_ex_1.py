# Задание 1 *
# Напишите рекурсивную функцию find_file(folder, target_filename), которая ищет полный путь к
# целевому файлу в словаре-дереве и возвращает строку с путем или None.
#
# file_system = {
# "documents": {
# "work": {
# "project_notes.txt": "content",
# "budget.xlsx": "content"
# },
# "personal": {
# "passport.pdf": "content"
# }
# },
# "photos": {
# "vacation.jpg": "content"
# }
# }

def find_file(folder: dict, target_filename: str) ->str | None:

    for name, contents in folder.items():

        if isinstance(contents, str) and name == target_filename:
            return name

        elif isinstance(contents, dict):
            result = find_file(contents, target_filename)

            if result is not None:
                return f"{name}/{result}"
    else:
        return None

file_system = {
"documents": {
"work": {
"project_notes.txt": "content",
"budget.xlsx": "content"
},
"personal": {
"passport.pdf": "content"
}
},
"photos": {
"vacation.jpg": "content"
}
}

print(find_file(file_system, "passport.pdf"))
print(find_file(file_system, "vacation.jpg"))
print(find_file(file_system, "project_notes.txt"))
print(find_file(file_system, "budget.xlsx"))