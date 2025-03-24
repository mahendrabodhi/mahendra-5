"""set methods"""

"""add method"""
# s = {1, 2, 3}
# s.add(5)
# print(s)

"""update method"""
# s = {1, 2, 3}
# s.update([4, 5, 6])
# print(s)

"""remove method"""
# s = {1, 2, 3}
# s.remove(2)
# print(s)

"""discard method"""

# s = {1, 2, 3}
# s.discard(2)
# print(s)
# s.discard(5)

"""pop() method"""

# s = {1, 2, 3, 4}
# print(s.pop())
# print(s)

"""clear method"""
# s = {1, 2, 3}
# s.clear()
# print(s)

"""creating empty set"""
# s=set()
# print(s)

"""set operations"""

"""union(|)"""

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1.union(s2))
# print(s1|s2)

"""intersection() (&)"""

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# print(s1.intersection(s2))
# print(s1&s2)

"""difference -"""

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# print(s1.difference(s2))
# print(s1-s2)

"""symmetric_difference() (^)"""

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# print(s1.symmetric_difference(s2))

"""isdisjoint()"""

# s1 = {1, 2, 3}
# s2 = {4, 5, 6}
# print(s1.isdisjoint(s2))

"""copy"""
# s1 = {1, 2, 3}
# s2 = s1.copy()
# print(s2)
#
# s1 = {1, 2, 3}
# print(s1.copy())


"""dictionary methods"""

"""dict[key] = value"""
# d = {"name": "Mahendra", "age": 25}
# d["city"] = "Rajahmundry"  #adding new key-value pair
# d["age"] = 26    #updating existing key
# print(d)

"""update"""
# d = {'name': 'Yaswanth', 'age': 25}
# d.update({'city': 'Hyderabad', 'age': 26})
# print(d)


"""get method"""

# d = {'name': 'Yaswanth', 'age': 25}
# print(d.get('name'))
# print(d.get('city', 'not found'))

"""pop()"""

# d = {'name': 'Yaswanth', 'age': 25}
# age = d.pop('age')
# print(age)
# print(d)

"""popitem()"""

# d = {'name': 'Yaswanth', 'age': 25, 'city': 'Rajahmundry'}
# item = d.popitem()
# print(item)
# print(d)

"""del method"""

# d = {'name': 'Yaswanth', 'age': 25}
# del d['age']
# print(d)

"""clear()"""

# d = {'name': 'Yaswanth','age': 25}
# d.clear()
# print(d)

"""key()"""
# d = {'name': 'yaswanth','age': 25,'city':'Rajahmundry'}
# print(d.keys())

"""values()"""

# d = {'name': 'Yaswanth','age': 25, 'city': 'Hyderabad'}
# print(d.values())

"""items()"""

# d = {'name':'Yaswanth', 'age': 25, 'city': 'Rajahmundry'}
# print(d.items())

# d = {'name': 'Yaswanth', 'age': 25}
# print(d.copy())

# d2 = d.copy()
# print(d2)

""" in -method"""

# d = {'name': 'Yaswanth', 'age': 25}
# print('name' in d)
# print('age' in d)
# print('salary' in d)

"""checking if a value exists (use values())"""

# d = {'name': 'Yaswanth','age': 25}
# print('Yaswanth' in d.values())
# print(26 in d.values())

