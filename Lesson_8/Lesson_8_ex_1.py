# Задание 1
# Напишите функцию
# analyze_grades(*grades)
# которая возвращает словарь
# {
# "count": ...,
# "average": ...,
# "highest": ...,
# "lowest": ...,
# "passed": ...
# }
# где
# ● passed — количество оценок больше либо равно 60.
# Если оценки отсутствуют — вернуть None.

def analyze_grades(*grades: int) -> dict | int| float | None:

    if not grades:
        return None

    passed_count = 0

    for grade in grades:
        if grade >= 60:
            passed_count += 1

    resulting_dict = {
    "count": len(grades),
    "average": sum(grades) / len(grades),
    "highest": max(grades),
    "lowest": min(grades),
    "passed": passed_count,
    }

    return resulting_dict

print(analyze_grades(67, 78, 54, 59, 38, 91, 87, 88, 82, 51, 34, 99, 52, 77, 85))