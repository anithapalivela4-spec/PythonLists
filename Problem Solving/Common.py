a = [10,20,30,40]
b = [20,30,50]
common = []
for x in a:
    if x in b:
        common.append(x)
print(common)