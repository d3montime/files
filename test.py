x = {'funny': 2, 'troll': 5, 'almen': 10, 'david' : 11}
print(x)
print(sorted([(k,v) for v, k in x.items()]))