a = [10,20,10,10,30,20,40]
duplicates = []
for x in a:
    if a.count(x) > 1 and x not in duplicates:
        duplicates.append(x)
print(duplicates)