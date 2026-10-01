a = [1,2,3,4,5,6]
target = 9
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if a[i] + a[j] + a[k] == target:
                print(a[i], a[j], a[k])