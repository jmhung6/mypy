coffee = {"arabica": 500, "robusta": 450, "liberia": 470}
print(coffee)
print(type(coffee))
print("coffee所有鍵:", coffee.keys())
print("robusta價格:", coffee.get("robusta"), "元")

for e in coffee:
    print("%10s\t-->\t%3d元" % (e, coffee.get(e)))
