# задача 1

with open("recipes.txt", encoding = 'utf-8') as file:
    lines = file.readlines()
   
cookbook = {}
        
index = 0
while index < len(lines):
    dish_name = lines[index].strip()
    index += 1
    num_ingredients = int(lines[index].strip())
    index += 1
    
    ingredients = []
    
    for ingredient in range(num_ingredients):
        split_ingregients = lines[index].strip().split(' | ')
        ingredient_dict = {
            'ingredient_name' : split_ingregients[0],
            'quantity' : split_ingregients[1],
            'measure' : split_ingregients[2]
        }
        
        ingredients.append(ingredient_dict)
        index += 1
        
    cookbook[dish_name] = ingredients
    
    if index < len(lines) and lines[index].strip() == '':
        index += 1
    
#print(cookbook)

# задача 2

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish_name in cookbook:
        if dish_name in dishes:
            for ingredient in cookbook[dish_name]:
                ingredient_name = ingredient['ingredient_name']
                quantity = int(ingredient['quantity']) * person_count
                measure = ingredient['measure']
                
                if ingredient_name in result:
                    result[ingredient_name]['quantity'] += quantity
                else:
                    result[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return result

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))