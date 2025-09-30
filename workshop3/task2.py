class Card:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Description: {self.__description}")


# Testing
power = Card("3X Power Up", "This card increases by three the power of an attack.")
power.display()

# These line of code cause errors
# print(power.name)
# print(power.description)

kirby = Card("Kirby", "Kirby is a little monster that attacks by chewing his enemies.")
kirby.display()
# These line of code cause errors
# print(kirby.name)
# print(kirby.description)
