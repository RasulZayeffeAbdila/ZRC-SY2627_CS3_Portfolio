class Animal:
    def __init__(self, name):
        self.__name = name

    def eat(self):
        print(f"{self.__name} is eating.")

    def make_sound(self):
        print(f"{self.__name} makes a sound.")

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__name = name

    def make_sound(self):
        print(f"{self.__name} roars loudly!")

    def eat(self):
        print(f"{self.__name} eats fresh meat.")

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__name = name

    def make_sound(self):
        print(f"{self.__name} trumpets!")

    def eat(self):   
        print(f"{self.__name} eats grass and fruits.")

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.__name = name

    def make_sound(self):
        print(self.__name," chatters!")

    def eat(self):
        print(self.__name," eats bananas.")

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
print("-----")