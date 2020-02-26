
grocery_list = ['apples','bread','milk','juice']

def in_grocery_list():
    item_check = input('Which item would you like to check for? ')
    if item_check in grocery_list:
        print('ok')
    elif item_check not in grocery_list:
        print(f'{item_check} Not Found!')

in_grocery_list()