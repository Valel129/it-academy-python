days = 45  # Моя первоначальная логика с простой формулой
full_weeks = days // 7
days_in_one_full_week = 7
days_left = days - (days_in_one_full_week * full_weeks)
print (full_weeks)
print (days_left)
print (2 ** 10)

days = 45  # Здесь я уже решил упростить, высчитав остаток, поделив 45 на 7, плюс добавил сепаратор и end, а также сделав одну команду print
full_weeks = days // 7
days_left = days % 7
print (full_weeks, days_left, 2 ** 10, sep=";\n", end="\n")

days, full_weeks, days_left = 45, 45 // 7, 45 % 7  # Здесь упростил еще больше, поместив все в две строки. Однако второй вариант считаю более подходящим, потому что days может в теории меняться, а в 3 варианте у меня зафиксировано 45 // 7. Во втором же варианте формула.
print (full_weeks, days_left, 2 ** 10, sep=";\n", end="\n")

days = 45  # То же, что и второй вариант, только я сделал так, чтобы названия переменных тоже выводились.
full_weeks = days // 7
days_left = days % 7
print ("Full weeks — " + str(full_weeks), "Days left — " + str(days_left), "Two to the tenth — " + str(2 ** 10), sep=", ", end=".")