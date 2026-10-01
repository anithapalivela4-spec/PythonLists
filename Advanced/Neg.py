numbers = [10, -5, 20, -3, 8, -1]

result = []

for n in numbers:
    if n < 0:
        result.append(n)

for n in numbers:
    if n >= 0:
        result.append(n)

print(result)