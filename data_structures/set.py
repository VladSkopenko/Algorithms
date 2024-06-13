some_set = {1, 2, 3, 4, 5}
some_set1 = {1, 7, 8, 9, 10}

print(some_set)
some_set.add(6)
print(some_set)
some_set.remove(6)
print(some_set)
print(some_set.intersection(some_set1)) # пересечение
print(some_set.difference(some_set1))# уникальные с 1 сета
