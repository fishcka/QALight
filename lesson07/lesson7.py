"""Lesson 7"""

# LIST
lst_1 = []
lst_2 = list()
print(lst_1)
print(lst_2)

l = "abba"
lst_3 = list(l)
print(lst_3)

# List comprehension
lst_4 = [1, 3, 5, 7]
lst_5 = [x ** 3 for x in lst_4 if x != 3]
# lst_5 = []
# for x in lst_4:
#     if x != 3:
#         lst_5.append(x ** 3)
print(lst_5)

# METHODS
# - Append
lst_6 = [1, 2, 3]
lst_6.append(4)
print(lst_6)
lst_6.append(77)
print(lst_6)

# - Extend
lst_7 = [1, 2, 3]
lst_8 = [3, 2, 1]
lst_7.extend(lst_8)
print(lst_7)
print(lst_8)

# - Insert
lst_9 = [1, 3, 4, 5]
print(lst_9[1])  # 3
lst_9.insert(1, [21, 2, 12])
print(lst_9[2])  # 3
print(lst_9)

# - Remove
lst_10 = [1, 2, 1, 3]
lst_10.remove(1)
print(lst_10)
# - Pop
print(lst_10.pop(2))
print(lst_10)

# - Index
lst_11 = ["namename", "name", "lastname", "name5", "name"]
print(lst_11.index("name"))
print(lst_11[lst_11.index("name")])
print(lst_11.index("name", 2, 5))

# - Sort
lst_12 = ["a", "g", "y", "x", "A", "f", "#", "X", "1", "2"]
lst_12.sort(reverse=True)
print(lst_12)
# - Reverse
lst_12.reverse()
print(lst_12)

# - Copy
lst_13 = [1, 2, 4, 5]
lst_14 = lst_13
lst_13.insert(2, 3)
print(lst_13)
lst_14.append(6)
print(lst_13)
print(lst_14)

lst_15 = lst_14.copy()  # lst_14[:]
lst_15.append(777)
lst_14.insert(1, 123)
print(lst_14)
print(lst_15)

# # - Clear
lst_15.clear()
print(lst_15)

# TUPLE
tpl_1 = (1, 2, 3)
tpl_2 = tpl_1 + tpl_1
print(tpl_2)
tpl_3 = tpl_1 * 5
print(tpl_3)

# SET
lst_16 = [1, 2, 3, "a", (3, 4), (3, 4)]
st_1 = set(lst_16)
print(st_1)

# - Disjoint
st_2 = {1, 2, 3}
st_3 = {2, 3, 4, 5, 6}
print(st_2.isdisjoint(st_3))
print(st_3.intersection(st_2))
print(st_3.difference(st_2))
print(st_2.difference(st_3))

# DICT
dct_1 = dict(name="John", last_name="Doe", age=23)
print(dct_1)

lst_17 = [1, 3, 5]
dct_2 = {x: x ** 3 for x in lst_17 if x > 1}
print(dct_2)

dct_1["city"] = "Kyiv"
print(dct_1)
dct_1["city"] = "Lviv"
print(dct_1["city"])
print(dct_1.get("country", "Ukraine"))
print(dct_1.items())

# FOR with collection
lst_77 = [77, 44, 55, 123]
dct_3 = {}
for index, value in enumerate(lst_77):
    dct_3[index] = value
print(dct_3)

lst_79 = [11, 22, 33, 256, 678]
dct_4 = {}
for value_1, value_2 in zip(lst_77, lst_79):
    dct_4[value_1] = value_2
print(dct_4)

# Keys
for key in dct_1.keys():
    print(key)

for key, value in dct_1.items():
    print(f"Key: {key} - Value: {value}")
