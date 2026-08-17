# Задание 6
# Дан список студентов:
# students = [
# {"name": "Иван", "score": 82},
# {"name": "Анна", "score": 95},
# {"name": "Петр", "score": 67},
# {"name": "Мария", "score": 91},
# {"name": "Олег", "score": 73},
# {"name": "Елена", "score": 88},
# ]
# Используя функциональный стиль программирования:
# 1. оставить студентов, набравших не менее 80 баллов;
# 2. отсортировать их по убыванию результата;
# 3. получить список строк вида:
# Анна (95)
# Мария (91)
# Елена (88)
# Иван (82)

students = [
{"name": "Иван", "score": 82},
{"name": "Анна", "score": 95},
{"name": "Петр", "score": 67},
{"name": "Мария", "score": 91},
{"name": "Олег", "score": 73},
{"name": "Елена", "score": 88},
]

passed_grades = filter(lambda s: s["score"] >= 80, students)
sorted_passed_grades = sorted(passed_grades, key=lambda s: s["score"], reverse=True)
final_student_list = [f'{s["name"]} ({s["score"]})' for s in sorted_passed_grades]

print(*final_student_list, sep="\n")