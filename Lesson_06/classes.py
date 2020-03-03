
class Person(object):
    species = "Home Sapiens"
    def __init__(self, name="Uknown", age=18):
        self.name = name
        self.age = age
    def talk(self):
        return "Hello there"
    def __str__(self):
        return f"Name: {self.name} Age: {self.age}"
    def __repr__(self):
        return f"Person: {self.name} Age: {self.age}"

class Student(Person):
    bedtime = "Midnight"
    def do_homework(self):
        import time
        print("I need to do homework")
        time.sleep(5)
        print("Did I fall asleep")

class Employee(Person):
    def __init__(self):
        super(Employee, self).__init__(name,age)
        self.employer = employer
    def talk(self):
        talk_str = super(Employee, self).talk()
        return f"{talk_str} I work for {self.employer}"