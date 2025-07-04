students = [("Ali", ["Fizika", "Matematika"]), ("Laylo", ["Ingliz tili"]), ("Jasur", ["Matematika", "Informatika"])]

soni = 0
for i in students:
    if "Matematika" in i[1]:
        soni += 1
print(soni)