glist = ['bread','detergent','donut','juice','cookie']
snack = glist[2]

# ex 1
# for num in range(len(glist)):
#     print(f'{num} ' + glist[num])

# ex 2
# for num in enumerate(glist):
#     print(num)

# ex 3
# for i in range(10):
#     print(snack)

# ex 4 - Guess My Number game
import random

ran_num = random.randint(1,10)
print(ran_num)
guesses = 0

def guess_num():

    guess = input('Please guess a number between 1 and 10 > ')
    guess = int(guess)
    global guesses

    if guess == ran_num:
        print('You got it right!')
        exit()
    elif guess != ran_num:
        print('Nope, sorry!')
        while guesses < 3:
            guesses += 1
            guess_num()

guess_num()