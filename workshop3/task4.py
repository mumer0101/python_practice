class Card:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Description: {self.__description}")


class Monster(Card):
    def __init__(self, name, description, lives, attack):
        super().__init__(name, description)
        self.__lives = lives
        self.__attack = attack

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, value):
        self.__lives = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack = value

    def display(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Lives: {self.__lives}")
        print(f"Attack: {self.__attack}")


class Item(Card):
    def __init__(self, name, description, factor):
        super().__init__(name, description)
        self.__factor = factor

    @property
    def factor(self):
        return self.__factor

    @factor.setter
    def factor(self, value):
        self.__factor = value

    def display(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Factor: {self.__factor}")


# Testing
kirby = Monster("Kirby", "Kirby is a little monster that attacks by chewing his enemies.", 5, "Chomp!")
kirby.display()

kirby.lives -= 1
print(kirby.name)
kirby.display()

kirby.attack = "Chomp Chomp!"
kirby.display()

threeup = Item("3X Power Up", "This card increases by three the power of an attack.", 3)
print(threeup.description)
threeup.display()
