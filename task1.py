people = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

oldest_person = people[0]
for i in people:
    if i[1] > oldest_person[1]:
        oldest_person = i
print(oldest_person)