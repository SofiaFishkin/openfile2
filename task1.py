def readFile(name):
    with open(name, encoding="utf8") as file:
        data = file.read().split("\n\n")
        cook_book = {}
        for line in data:
            lines = line.split("\n")
            dish = lines[0]
            ingredients = lines[1]
            cook_book[dish] = []
            print(dish, ingredients)
            print()
            for recipe in lines[2:]:
                elments = recipe.split("|")
                cook = {'ingredient_name': elments[0], 'quantity': elments[1], 'measure': elments[2]}
                cook_book[dish].append(cook)
        return cook_book

result = readFile('list.txt')
keys = result.keys()
for line in keys:
    print(line)
    for recipe in result[line]:
        print(recipe)
    print()
