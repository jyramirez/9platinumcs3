# PARENT CLASS

class Animal:
    def __init__(self, name: str):
        self._name = name

    def eat(self):
        print(self._name, "eats.")

    def make_sound(self, name):
        print(self._name, "makes sounds.")

# CHILD CLASS 1 - LION

class Lion(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        print(self._name, "roars loudly!")

    def eat(self):
        print(self._name, "eats fresh meat.")

# CHILD CLASS 2 - ELEPHANT

class Elephant(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        print(self._name, "trumpets!")

    def eat(self):
        print(self._name, "eats grass and fruits.")

# CHILD CLASS 3 - MONKEY

class Monkey(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def make_sound(self):
        print(self._name, "chatters!")

    def eat(self):
        print(self._name, "eats bananas.")

def main():

    lion = Lion("Simba")
    elephant = Elephant("Dumbo")
    monkey = Monkey("George")

    lion.make_sound()
    lion.eat()
    print("-----")

    elephant.make_sound()
    elephant.eat()
    print("-----")

    monkey.make_sound()
    monkey.eat()

main()