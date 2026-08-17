square_side = 8  # Вариант с умножением
square_area = square_side * square_side
square_perimeter = 4 * square_side
print(square_perimeter, square_area, sep=", ", end="\n")


square_side = 8  # Вариант с возведением во вторую степень
square_area = square_side ** 2
square_perimeter = 4 * square_side
print(square_perimeter, square_area, sep=", ", end="\n")

square_side = 8  # Вариант, где дополнительно выводится текст
square_area = square_side ** 2
square_perimeter = 4 * square_side
print("Square perimeter = " + str(square_perimeter), "Square area = " + str(square_area), sep=", ", end="\n")

square_side = 8  # Упрощенный вариант, где мы перечисляем через запятую просто, а оно и так подставится. То есть, убираем лишний пробел и тип данных str. Однако, так как мы убрали сепаратор, потому что он ставил запятые перед каждым блоком, нам нужно заменить запятую между периметром и площадью на and. Потому что даже если во втором блоке написать ", Square area =", то запятая не сидит вплотную к 32, а именно: Square perimeter = 32 , Square area = 64
square_area = square_side ** 2
square_perimeter = 4 * square_side
print("Square perimeter =", square_perimeter, "and Square area =", square_area, end=" ")
