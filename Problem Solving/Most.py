a = [10,20,10,30,40,50,10]
most = a[0]
for x in a:
    if a.count(x) > a.count(most):
        most = x
print(most)