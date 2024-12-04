count = 1
while count <= 10:
    print("NO", count, "Time")
    count += 1
print("\n--------------------")
while count >= 1:
    print("NO", count, "Time")
    count -= 1
print("\n--------------------")
for i in range(10):
    print(i)
print("\n--------------------")
for i in range(1, 10):
    print(i)
print("\n--------------------")
for i in range(0, 10, 3):
    print(i)
print("\n--------------------")
for i in range(0, 10, 3):
    print(i)
else:
    print("finish")
print("\n--------------------")

k = 0
for i in range(1, 10):
    for j in range(1, 10):
        k = i * j
        print("%d X %d = %2d" % (i, j, k), end="   ")
    print()
print("\n--------------------")
