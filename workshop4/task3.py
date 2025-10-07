#1
words = ["cat", "banana", "dog", "elephant", "bat"]
display = list(map(str.upper, filter(lambda word: len(word) <= 3, words)))
print("Short words in uppercase:", display)

#2
temps = [10, 25, -10, 13, 5, -5, 18]
fahrenheit = list(map(lambda i: (i * 9/5) + 32, filter(lambda i: i >= 0, temps)))
print("Temperature in Fahrenheit:", fahrenheit)
