a = [10,20,30]
b = [20,40,50]
c = a+b
result = []
for x in c:
    if x not in result:
        result.append(x)
print(result)