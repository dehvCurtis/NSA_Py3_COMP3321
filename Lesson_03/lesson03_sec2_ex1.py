favorite_snack = "butterfinger"

def snack_check(snack):
    if snack == favorite_snack:
        print(f'{snack} is your favorite snack!')
    elif snack != favorite_snack:
        print(f'{snack} is NOT your favorite snack!')

which = input("Snack? ")
snack_check(which)