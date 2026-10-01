a = [1,2,3,4,5,6]
target = 7
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print(a[i], a[j])