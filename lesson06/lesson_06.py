"""Lesson 6"""

# Літерали
str_1 = "isn't"
str_2 = 'I am running "Coca-Cola"'
str_x3 = """Hello!
    My name is John.
    I'm running "Cola-Cola" """
print(str_x3)

# Екрановані послідовності
str_3 = "Hello!\vMy name is John."
print(str_3)
str_4 = "Hello!\n\tMy name is John."
print(str_4)
str_5 = "To \\name\\ "
print(str_5)
str_6 = 'I\'m running "Coca-Cola"'
print(str_6)
str_7 = "I'm running \"Coca-Cola\""
print(str_7)


# Операції
str_8 = "Hello! My name is John."
print(len(str_8))
print(str_8[1])
print(str_8[-3])
# - Зріз
print(str_8[0: 6])
print(str_8[7:])
print(str_8[:4])


# Find
print(str_8.find("o"))  # 4
print(str_8.find("u"))  # -1 (non-existing)

print(str_8.rfind("o"))  # 19

# Index
print(str_8.index("o"))  # 4
# print(str_8.index("u"))  # ValueError: substring not found

print(str_8.rindex("o"))  # 19

# Replace
str_9 = str_8.replace("Hello", "Hi")
print(str_9)
print("aaaaaa".replace("a", "b", 3))

# Split
print(str_9.split())
print("ababababa".split("b"))

# IS..
print("777".isdigit())
print("777a".isdigit())

# Upper/lower
print(str_9.upper().isupper())
print(str_9.lower())
print("hElLo, My NaMe iS JoHN".capitalize())

# ..with
print(str_9.startswith("Hi!"))
print(str_9.endswith("John."))

# Join
str_9_5 = "My name is John."
splited = str_9_5.split()
print(splited)
str_10 = "-".join(splited)
print(str_10)

# Count
str_11 = "My name My Name My name - John"
print(str_11.lower().count("name"))
print(str_11.count("My"))
print(str_11.count("John"))

# Зі строки “Hello! My name John. Nice to meet you!”
# зробити список ['H*llo!', 'My', 'nam*', 'John.', 'Nic*', 'to', 'm**t', 'you!'].
str_12 = "Hello! My name John. Nice to meet you!"
replaced_string = str_12.replace("e", "*")
splited_str = replaced_string.split()
print(splited_str)
print(['H*llo!', 'My', 'nam*', 'John.', 'Nic*', 'to', 'm**t', 'you!'] == splited_str)

print("Hello! My name John. Nice to meet you!".replace("e", "*").split())


# Форматування строк
hello_str = "Hello, {} {}"
name = input("What is your name?: ")
print(hello_str.format(name, name))
print(f"Hello, {name}")
print("Hello, %s %s" % (name, name))

# Import
# import importing.test_import_1 as test
#
# new_obj = test.RandomClass()
# print(test.rand_func())
# print(test.rand_val)
#
# from importing.test_import_1 import RandomClass
# new_obj_2 = RandomClass()
#
# from importing.test_import_1 import *
# print(rand_func())
# print(rand_val)
