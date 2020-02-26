import random
num_list = [9.42,5.67,3.25,13.41,17.50]

def you_won():
    choice = random.choice(num_list)
    if choice < 10:
        print('Choice less than 10')
        print(f'Choice: {choice}')
    elif choice > 10:
        print('Choice greater than 10')
        print(f'Choice: {choice}')

you_won()