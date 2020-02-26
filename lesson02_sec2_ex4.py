import random

my_list = {"apples":9.42,"oranges":5.67,"dog food":3.25,"milk":13.40,"bread":7.5}

food, price = random.choice(list(my_list.items()))

print(food, round(price))