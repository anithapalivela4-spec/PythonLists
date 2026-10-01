a = [1,2,3,5,6]
n = 6
total = n * (n + 1) // 2
actual = 0
for x in a:
    actual += x
print("Missing number is:", total - actual)