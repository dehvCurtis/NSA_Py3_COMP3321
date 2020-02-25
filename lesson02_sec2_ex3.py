import random

list = ["apples","oranges","dog food","milk","bread"]

rand_int = len(list)
number = random.randint(1, rand_int)
print(f'Finding number between 0 and {rand_int}')
print(list[number])