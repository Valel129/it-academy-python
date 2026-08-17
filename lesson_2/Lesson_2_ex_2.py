# name = "Hero"  # Первый шаг, просто смотрю, как будет выглядеть и что нужно сделать, чтобы соответствовало условиям задания.
# level = 1
# hp = 40
# print (name, level, hp, sep=" | ", end=".\n")
name = "Nameless Hero"  # Под условие задания подходит, но на практике это либо не будет работать, либо придется через костыли выводить "x" в число через int, а потом обратно. Это в случаях, когда уровень героя и количество хп будет меняться.
level = "1"
hp = "40"
print ("Name: " + name, "Level: " + level, "HP: " + hp, sep=" | ", end="\nWelcome to the Colony!")

name = "Name: Nameless Hero"  # Аналогично с предыдущим, только я зашил названия переменных в сами значения.
level = "Level: 1"
hp = "HP: 40"
print (name, level, hp, sep=" | ", end="\nWelcome to the Colony!")

name = "Nameless Hero"  # Здесь уже значения в int, поэтому формулы повышения опыта и очков здоровья должны работать как надо. Превратил изначальное значение int в текст с помощью str, чтобы прошла склейка.
level = 1
hp = 40
print ("Name = " + str(name), "Level = " + str(level), "HP = " + str(hp), sep=" | ", end="\nWelcome to the Colony!")

name = "Nameless Hero"  # Здесь я убрал str перед name, потому что в переменной name и так уже тип данных str.
level = 1
hp = 40
print ("Name: " + name, "Level: " + str(level), "HP: " + str(hp), sep=" | ", end="\nWelcome to the Colony!\n")

name = "Nameless Hero"  # Здесь я убрал str вообще и перечислил через запятую, ведь должны и так вставиться. Однако, как я полагаю, такое сработает только для print. В значениях уже нужно будет использовать str, если нужно будет склеить int и строку, я правильно понимаю? Но даже тут пришлось sep убрать и прописать "|" вручную в каждом блоке, потому что с сепаратором выглядело бы так: Name= | Nameless Hero | Level= | 1 | HP= | 40
level = 1
hp = 40
print ("Name:", name, "| Level:", level, "| HP:", hp, end="\nWelcome to the Colony!")