city = input("Please enter your favorite city (for example, Novosibirsk): \n")
first_part_of_city = city[:3]
second_part_of_city = city[-3:]
combo = first_part_of_city + second_part_of_city

print(f"{(combo + "-") * 2}{combo}")

city = input("Please enter your favorite city (for example, Novosibirsk): \n")
first_part_of_city = city[:3]
second_part_of_city = city[-3:]
combo = first_part_of_city + second_part_of_city

print(f"{combo}-{combo}-{combo}")