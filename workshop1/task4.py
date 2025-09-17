fruits = {"apple", "banana"}

while True:
    user_input = input("The set of fruits have been created now what would you like to do: add / remove / check / quit: ")
    
    if user_input == "add":
        fruit = input("Fruit to add: ")
        fruits.add(fruit)

    elif user_input == "remove":
        fruit = input("Fruit to remove: ")
        fruits.remove(fruit)  

    elif user_input == "check":
        fruit = input("Fruit to check: ")
        print(fruit in fruits)

    elif user_input == "quit":
        print("Set of Fruits:", fruits)
        break
    print("Set of Fruits:", fruits)
