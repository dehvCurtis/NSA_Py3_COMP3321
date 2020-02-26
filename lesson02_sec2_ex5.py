import random

my_list = {"apples":9.42,"oranges":5.67,"dog food":3.25,"milk":13.40,"bread":7.5}

food, price = random.choice(list(my_list.items()))

print('Item:', food, '\nPrice:', round(price))

if price <= 10:
    difference = 10 - price
    print('You get back the difference:', difference)
elif price >= 10:
    difference = 10 + price
    print('You made some money, collect', difference)