l3 = list(range(100))
ex7 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex8 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex8)

