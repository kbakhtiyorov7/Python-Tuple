orders = [(102, "Ali"), (99, "Vali"), (150, "Sami")]
new_orders = list()
for i in orders:
    if i[0] % 2 == 0:
        new_orders.append(i)
print(new_orders)