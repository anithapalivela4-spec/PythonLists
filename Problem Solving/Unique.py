a = [10,20,10,30,40,50,10]
unique = []
for x in a:
    if a.count(x) == 1:
        unique.append(x)
print(unique)