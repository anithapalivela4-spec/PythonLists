numbers = [0, 1, 0, 3, 12, 0, 5]

result = []

for n in numbers:
    if n != 0:
        result.append(n)

zero_count = numbers.count(0)

result.extend([0] * zero_count)

print(result)