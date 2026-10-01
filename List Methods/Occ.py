numbers = [10, 20, 10, 30, 10]

result = []

for n in numbers:
    result.append(n)
    if n == 10:
        result.append(99)

print(result)