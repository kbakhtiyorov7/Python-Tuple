numbers = (3, 6, 7, 8, 10, 11)
numbers_list = list()
for i in numbers:
    if i % 2 == 0:
        numbers_list.append(i)
numbers_list = tuple(numbers_list)
print(numbers_list)