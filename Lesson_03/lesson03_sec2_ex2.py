g_list = ['milk','juice','pencils']

def in_grocery_list(grocery_item):
    if grocery_item in g_list:
        print(f'Yes, {grocery_item} is in the list')
    elif grocery_item not in g_list:
        print(f'No, {grocery_item} is NOT in the list')

user_item = input('Pick an item: ')
in_grocery_list(user_item)