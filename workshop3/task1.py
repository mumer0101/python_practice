class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")


# Testing
power = Card("3X Power Up", "This card increases by three the power of an attack.")
power.display()
print(power.name) # this should work
print(power.description) # this should work
kirby = Card("Kirby", "Kirby is a little monster that attacks by chewing his enemies.")
kirby.display()
print(kirby.name) # this should work
print(kirby.description) # this should work
