dict1 = {1: 'abc', 2: 'bcd'}
dict2 = {2: 'cde', 4: 'def'}
dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)
