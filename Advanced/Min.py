numbers = [10, 20, 30, 40]

minimum = numbers[0] + numbers[1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        total = numbers[i] + numbers[j]

        if total < minimum:
            minimum = total

print("Minimum sum:", minimum)