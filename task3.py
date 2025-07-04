words = ("apple", "banana", "strawberry", "kiwi",'qovuntarvuz')
long_word = words[0]
for fruits in words:
    if len(fruits) > len(long_word):
        long_word = fruits
print(long_word)