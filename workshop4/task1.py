odds = [num for num in range(21) if num % 2 != 0]
print(odds)

words = {"cat", "dog", "elephant", "bat", "ant", "horse"}
small_words = {word for word in words if len(word) <= 3}
print(small_words)

grades = {
        "Alice": 85, 
        "Bob": 62, 
        "Charlie": 90}

grade_list = [(name, grade) for name, grade in grades.items()]
print(grade_list)
