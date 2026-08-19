# Задание 4 Напишите консольную программу, которая работает в цикле:
# while True:
# command = input("Введите команду: ")
# Поддерживаются команды:
# ●
# ● add
# ● remove
# ● show
# ● exit
# В программе хранится список:
# items = []
# Поведение:
# ● add — запросить число и добавить его в список;
# ● remove — запросить индекс элемента и удалить его;
# ● show — вывести все элементы;
# ● exit — завершить программу.
# Необходимо обработать ошибки:
# ● пользователь ввёл не число при добавлении → ValueError;
# ● пользователь ввёл некорректный индекс → IndexError;
# ● пользователь ввёл неизвестную команду → вывести сообщение об ошибке.
# После обработки ошибки программа должна продолжить работу, а не завершаться.
# Дополнительное условие: для команды remove нельзя проверять индекс через if. Необходимо продемонстрировать обработку IndexError.

items = []

while True:

    try:
        approved_commands = ["add", "remove", "show", "exit"]
        command = input("Введите команду: ").strip().replace(" ", "")  # Добавил дополнительные страховки на случай ввода с пробелами лишними

        if command not in approved_commands:
            print("Вы ввели неизвестную команду, попробуйте снова")
            continue

        if command == "add":
            add_number = int(input(f"Введите число, чтобы добавить его в список: "))
            items.append(add_number)

        if command == "remove":  # Или как вариант вместо items.remove(items[remove_number]) написать del items[remove_number]
            remove_number = int(input(f"Введите индекс элемента, чтобы удалить его: "))
            items.remove(items[remove_number])

        if command == "show":
            print(items)

        if command == "exit":
            print(f"Завершение работы")
            break

    except ValueError:
        print(f"Ошибка: нужно ввести число")

    except IndexError:
        print(f"Ошибка: введен некорректный индекс")



