a = [10,20,30,40]
b = [20,40]
result =[]
for x in a:
    if x not in b:
        result.append(x)
print(result)