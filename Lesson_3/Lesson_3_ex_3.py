hero = {
    "name": "Gandalf",
    "level": 80,
    "inventory": ["staff", "robe", "potion"]
}
hero["inventory"].append("sword")
hero["level"] = hero["level"] + 1
hero["guild"] = "Wizards"
print(f"{hero}")

hero = {
    "name": "Gandalf",
    "level": 80,
    "inventory": ["staff", "robe", "potion"]
}
hero["inventory"].append("sword")
hero["level"] = hero["level"] + 1
hero["guild"] = "Wizards"
print(f"Name: {hero['name']}", f"Level: {hero['level']}", f"Inventory: {hero['inventory']}", f"Guild: {hero['guild']}", sep="\n")

hero = {
    "name": "Gandalf",
    "level": 80,
    "inventory": ["staff", "robe", "potion"]
}
hero["inventory"].append("sword")
hero["level"] = hero["level"] + 1
hero["guild"] = "Wizards"
print(f"Name: {hero['name']}\nLevel: {hero['level']}\nInventory: {hero['inventory']}\nGuild: {hero['guild']}")