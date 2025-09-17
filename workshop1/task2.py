phone_book = {
    "Alice": "416-555-1234",
    "Bob": "647-555-5678",
    "Charlie": "905-555-2468",
    "Diana": "289-555-1357",
    "Ethan": "613-555-9876"
}

user_input = input("Enter the name of a person: ")

if user_input in phone_book:
    print("Phone number of", user_input,"is:", phone_book[user_input])
else:
    print("Error:", user_input,"is not in the dictionary")
