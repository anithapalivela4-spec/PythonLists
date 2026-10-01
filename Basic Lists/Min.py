numbers = [10, 50, 20, 80, 30]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print(smallest)