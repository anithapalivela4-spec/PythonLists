numbers = [10, 50, 20, 80, 30]

difference = 0

for i in range(len(numbers)):
    for j in range(len(numbers)):
        diff = abs(numbers[i] - numbers[j])

        if diff > difference:
            difference = diff

print("Maximum difference:", difference)