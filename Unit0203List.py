coffee = ["美式", "義式", "拿鐵", "卡布"]
print(coffee)
print()
print(coffee[0])
print(coffee[1])
print(coffee[2])
print(coffee[3])
print()
for e in coffee:
    print(e)

coffee2 = [10, 20, 30, 35]
for e in coffee2:
    print(e)
    e += e
print()
print("總數量:%d" % (e))
