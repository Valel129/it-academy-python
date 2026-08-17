# name = input("Please enter your name: \n")
# weight = input("Please provide your weight in kg (for example, 120.50): \n")
# height = input("Please provide your height in meters (for example, 1.93): \n")
# BMI = float(weight) / (float(height) ** 2)

# print (f"Your BMI = {int(BMI)}")

name = input("Please enter your name: \n")  # Подвинул float выше, в input
weight = float(input("Please provide your weight in kg (for example, 120.50): \n"))
height = float(input("Please provide your height in meters (for example, 1.93): \n"))
BMI = weight / (height ** 2)

print (f"Hey, {name}, your BMI = {int(BMI)}")

name = input("Please enter your name: \n")  # Формула в print
weight = float(input("Please provide your weight in kg (for example, 120.50): \n"))
height = float(input("Please provide your height in meters (for example, 1.93): \n"))

print (f"Hey, {name}, your BMI = {int(weight / height ** 2)}")