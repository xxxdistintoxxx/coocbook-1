

with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    keys = ['ingredient_name', 'quantity', 'measure']
    read = file.read()
    read = read.split('\n\n')
    for dish in read:
        dish = dish.split('\n')
        cook_book[dish[0]] = [dict(zip(keys, dish.split(' | '))) for dish in dish[2:]]

def cook_book_title():
    title=[]
    for k in cook_book.keys():
        title.append(k)
    print(f'Блюда из книги рецептов:\n{",".join(title)}\n')

def get_shop_list_by_dishes(dishes, person_count=1):
    ingredient_list = {}
    for menu in dishes:
        for cook in cook_book[menu]:
            quantity = float(cook['quantity']) * person_count
            measure = cook['measure']
            if cook['ingredient_name'] in ingredient_list.keys():
                quantity += ingredient_list[cook['ingredient_name']]['quantity']
            compound = {
                'quantity': quantity,
                'measure': measure
            }
            ingredient_list[cook['ingredient_name']] = compound
    print(f'Список ингридиентов для блюд:{dishes} на {person_count} человек:')
    return ingredient_list


cook_book_title()
shop = get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2)
print(shop)



