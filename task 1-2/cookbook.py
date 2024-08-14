# задача 1
def open_cookbook(filename):
    with open(filename, encoding = 'utf-8') as file:
        lines = file.readlines()
        
    return lines
      

def parse_cookbook(lines):
    cookbook = {}
    
    index = 0
    while index < len(lines):
        dish_name = lines[index].strip()
        index += 1
        num_ingredients = int(lines[index].strip())
        index += 1
        
        ingredients = []
        
        for row in range(num_ingredients):
            split_ingregients = lines[index].strip().split(' | ')
            ingredient_dict = {
                'ingredient_name' : split_ingregients[0],
                'quantity' : int(split_ingregients[1]),
                'measure' : split_ingregients[2]
                }
            
            ingredients.append(ingredient_dict)
            index += 1
            
        cookbook[dish_name] = ingredients
        
        if index < len(lines) and lines[index].strip() == '':
            index += 1
            
    return cookbook

    
#print(parse_cookbook(open_cookbook("recipes.txt")))

# задача 2

def get_shop_list_by_dishes(dishes: list, person_count: int):
    
    recipes = parse_cookbook(open_cookbook("recipes.txt"))
    result = {}
    for dish_name in dishes:
        if dish_name in recipes:
            for ingredient in recipes[dish_name]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                
                if ingredient_name in result:
                    result[ingredient_name]['quantity'] += quantity
                else:
                    result[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return result

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))