# Задание 1
# Дан список попыток входа:
# logs = [
# ("alice", True),
# ("bob", False),
# ("alice", True),
# ("alice", False),
# ("bob", True),
# ("charlie", False),
# ]
# Напишите функцию
# analyze_logins(logs)
# которая возвращает словарь вида
# {
# "alice": {"success": 2, "failed": 1},
# "bob": {"success": 1, "failed": 1},
# "charlie": {"success": 0, "failed": 1},
# }

"""Первый вариант, к которому я пришел, но он ведь не совсем верный, потому что в словаре может быть
больше пользователей."""

def analyze_logins(logs: list | bool | tuple | int) -> dict:

    resulting_dict = {

        "alice":
            {"success": 0, "failed": 0},

        "bob":
            {"success": 0, "failed": 0},

        "charlie":
            {"success": 0, "failed": 0}
    }

    for name, status in logs:

        if status == True:
            resulting_dict[name]["success"] += 1

        else:
            resulting_dict[name]["failed"] += 1

    return resulting_dict

print(*analyze_logins([
    ("alice", True),
    ("bob", False),
    ("alice", True),
    ("alice", False),
    ("bob", True),
    ("charlie", False)
]).items(), sep="\n", end="\n" * 2)

"""Второй вариант уже более оптимальный, плюс в конце я попробовал разные способы print."""

def analyze_logins(logs):

    resulting_dict = {}

    for item in logs:

        name = item[0]
        status = item[1]

        if name not in resulting_dict:
            resulting_dict[name] = {"success": 0, "failed": 0}

        if status == True:
            resulting_dict[name]["success"] += 1
        else:
            resulting_dict[name]["failed"] += 1

    return resulting_dict

logs = [
    ("alice", True),
    ("bob", False),
    ("alice", True),
    ("alice", False),
    ("bob", True),
    ("charlie", False),
]

lines = [f"'{name}': {stats}" for name, stats in analyze_logins(logs).items()]

print("\n".join(lines), end="\n" * 2)

print(*analyze_logins(logs).items(), sep="\n", end="\n" * 2)

print(*analyze_logins([

    ("alice", True),
    ("bob", False),
    ("alice", True),
    ("alice", False),
    ("bob", True),
    ("charlie", False)]).items(), sep="\n")