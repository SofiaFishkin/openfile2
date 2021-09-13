def readFile(name):
    with open(name, encoding="utf8") as file:
        data = file.read().split("\n\n")
        cook_book = {}
        for line in data:
            lines = line.split("\n")
            dish = lines[0]
            ingredients = lines[1]
            cook_book[dish] =
            print(dish, ingredients)
            print()
            for recipe in lines[2:]:
                elments = recipe.split("|")
                cook = {'ingredient_name': elments[0], 'quantity': elments[1], 'measure': elments[2]}
                cook_book[dish].append(cook)

        return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    result = readFile('list.txt')
    res = {}
    for line in dishes:
        for recipe in result[line]:
            res[recipe['ingredient_name']] = {'measure': recipe['measure'],'quantity': int(recipe['quantity'])*2}
    return res

result = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)
for line in result:
    print(line + ": " + result[line].__str__())



