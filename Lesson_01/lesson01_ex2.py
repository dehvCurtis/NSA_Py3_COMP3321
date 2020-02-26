list = {"apples":9.42,"oranges":5.67,"dog food":3.25,"milk":13.40,"bread":7.5}

print('Printing grocery list:')
for item in list:
    print('\t',item)

print('Adding prices. Total:')

print(list["apples"] + list["oranges"] + list["dog food"] + list["milk"] + list["bread"])