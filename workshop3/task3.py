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


# Testing
power = Card("3X Power Up", "This card increases by three the power of an attack.")
power.display()

power.name = "Three Times Power Up"
power.description = "This card triples the power of an attack."
print(power.name)
print(power.description)
