import random
num_list = [9.42,5.67,3.23,13.43,17.49]

def you_won():
    choice = random.choice(num_list)
    difference = choice - 10
    if choice < 10:
        print(f'Number: {choice} You LOSE')
    elif choice > 10:
        print(f'Number: {choice} You WIN {difference}')

you_won()