emails = (("Ali", "ali@gmail.com"), ("Vali", "vali@yandex.ru"), ("Sami", "sami@mail.ru"))
domens = list()
for email in emails:
    dot_index = email[1].index("@")
    domen = email[1][dot_index::]
    domens.append(domen)
domens = tuple(domens)
print(domens)