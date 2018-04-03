import operator

# How to sort a dict by value
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
# Return a list of dict's tuple pairs
print(sorted(xs.items(), key=lambda x: x[1]))

print(sorted(xs.items(), key=operator.itemgetter(1)))

