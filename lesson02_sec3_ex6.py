import random
my_list = {"apples":9.42,"oranges":5.67,"dog food":3.25,"milk":13.40,"bread":7.5,"juice":3.95}

food, price = random.choice(list(my_list.items()))

def price_matcher():
    # print('Item:', food, '\nPrice:', abs(price))
    return food, abs(price)

def free_change():
    result = price_matcher()
    print('Cost: ', result)
    if price <= 10:
        print('Change: ', 10 - price)
    elif price >= 10:
        pass

free_change()