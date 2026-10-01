a = [10,20,30]
b = [20,30,40]
c = [20,30,50]
result = []
for x in a:
    if x in b and x in c:
        result.append(x)
print(result)