from decimal import Decimal

math = 4  # Целое деление (int)
code = 5
eng = 4
arithmetic_average = (math + code + eng) // 3
print (arithmetic_average)

math = 4  # Дробное (float)
code = 5
eng = 4
arithmetic_average = (math + code + eng) / 3
print (arithmetic_average)

math = 4  # Decimal (Я все тут правильно сделал или есть какие-то нюансы?)
code = 5
eng = 4
arithmetic_average = (math + code + eng) /Decimal('3')
print (arithmetic_average)