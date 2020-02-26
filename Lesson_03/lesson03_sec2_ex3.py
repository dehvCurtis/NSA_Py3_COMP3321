g_list = ['milk','juice','pencils']

def in_grocery_list(grocery_item):
    if type(grocery_item) == str:
        print(f'It\'s a string! {type(grocery_item)}')
    elif type(grocery_item) != str:
        print(f'Nah, not a string {type(grocery_item)}')
        pass

user_item = input('Pick an item: ')
in_grocery_list(user_item)