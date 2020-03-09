
class Awesome(object):
    def __init__(self, awesome_thing):
        self.thing = awesome_thing
    def __str__(self):
        return f'{self.thing}'

def cool(group):
    return f'Everything cool when you a part of {group}'

if __name__ == '__main__':
     a = Awesome("EVERYTHING")
     print(a)
