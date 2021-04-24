tup = (2, 4, 5, 6, 2, 3, 4, 4, 7, 8, 4, 3, 2)
rep = []
for t in tup:
    found = 0
    for r in rep:
        if (r[0] == t):
            r[1] += 1
            found = 1
            break

    if (not found):
        rep.append([t, 1])

num = 0
count = 0
for r in rep:
    if (r[1] > count):
        count = r[1]
        num = r[0]

if (count > 1):
    print("Repeated number :" + str(num) + "\n Repeat times : " + str(count))
else:
    print("No number repeated!")