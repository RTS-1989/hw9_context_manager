from time import time, sleep

def file_to_cb(file_input):
    with open(file_input, encoding='utf8') as f:
        cook_book = {}
        for line in f:
            dish = line[:-1]
            sleep(1)
            ing_counter = f.readline().strip()
            list_of_ingridient = []
            for i in range(int(ing_counter)):
                dish_ing = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # - временный словарь с ингридиетом
                ingridient = f.readline().strip().split(' | ') # - вот так перемещаемся по файлу
                for item in ingridient:
                    dish_ing['ingredient_name'] = ingridient[0]
                    dish_ing['quantity'] = ingridient[1]
                    dish_ing['measure'] = ingridient[2]
                list_of_ingridient.append(dish_ing)
                dish_dict = {dish: list_of_ingridient}
                cook_book.update(dish_dict)
            f.readline()

    return(cook_book)


def get_shop_list_by_dishes(dishes, person_counter: int):
    cook_book = file_to_cb('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_dict = {ingredient['ingredient_name']: {'quantity': int(ingredient['quantity']), 'measure': ingredient['measure']}}
            sleep(1)
            for nd_key, nd_value in new_dict.items():
                if nd_key not in shop_list:
                    shop_list.update(new_dict)
                else:
                    for key, value in shop_list.items():
                        if key == nd_key:
                            value['quantity'] += nd_value['quantity']

    for value in shop_list.values():
        value['quantity'] = value['quantity'] * person_counter
                                
    return shop_list

if __name__ == '__main__':
    print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))