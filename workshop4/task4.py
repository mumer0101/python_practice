from functools import reduce

cart = {
    "apple": 1.20,
    "banana": 0.50,
    "chocolate": 2.00,
    "steak": 12.50,
    "chips": 3.00,
    "soda": 1.75
}

# 1
expensive_items = dict(filter(lambda item: item[1] > 2.00, cart.items()))
print("Items worth more than $2.00:", expensive_items)

# 2
total = reduce(lambda acc, item: acc + item[1], cart.items(), 0)
print("Total amount spent on shopping: $", round(total, 2))

# 
total_with_tax = round(total * 1.13, 2)
print("Total after taxes: $", total_with_tax)
