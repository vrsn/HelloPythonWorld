shopping_list = ["milk", "sugar", "eggs", "bread"]

for item in shopping_list:
    if "sugar" in item:
        continue
    if "egg" in item:
        break
    print(item)