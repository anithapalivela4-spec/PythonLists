a = [10,20,10,30,20,10]
least = a[0]
for x in a:
    if a.count(x) < a.count(least):
        least = x
print(least)