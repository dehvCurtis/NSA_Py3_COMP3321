import random

list = {"apples":9.42,"oranges":5.67,"dog food":3.25,"milk":13.40,"bread":7.5}

rand_int = len(list)
number = random.randint(0, rand_int)
print(number)
# print(f'Finding number between 0 and {rand_int}')
print(list[number])