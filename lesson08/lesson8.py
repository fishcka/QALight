"""Lesson 8"""

# Exception
def make_error():
    100 / 0

print("Before")
make_error()
print("After")

# AssertError
# assert 1 == 1

# AttributeError
# class NewClass:
#     pass
#
#
# new_class = NewClass()
# print(new_class.value())

# LookupError
# lst = [1, 2, 3]
# dct = {"name": "John"}
#
# # lst[77]
# dct["surname"]

# NameError
# print(new_name)

# TypeError
# print("name" + 11.0)

# Try/Except
# lst_1 = [1, 2, 3, 4]
# indx = int(input("Enter any index:"))
# try:
#     print(f"Ur value is: {lst_1[indx]}")
# except IndexError as exp:
#     print(exp)
#     print(f"List doesn't have such index '{indx}'. List len: '{len(lst_1)}' (use index from 0 to {len(lst_1) - 1})")
# print("After")


# Створити універсальний функцію для роботи з словниками і списками.
# Приймає 2 параметри - обʼєкт і індекс/ключ. У разі якщо таке значення є - повертати його,
# якщо ж виникає помилка, то повертати None і виводити інформативне повідомлення ("Такого ключа\індексу не існує")
# def safe_get(iter_obj, key):
#     try:
#         return iter_obj[key]
#     except LookupError:
#         print(f"Index/Key '{key}' was not found")
#         return None
#
#
# print(safe_get((1, 2, 3), 0))  # [0]
# print(safe_get([1, 2, 3], 7))
# print(safe_get({"name": "John"}, "name"))  # ["name"]
# print(safe_get({"name": "John"}, "age"))
#
# raise ZeroDivisionError("Ha-ha, it's prank")


# Try/Except/Else/Finally
# try:
#     100 / 0
#     print("try")
# except IndexError:
#     print("except")
# else:
#     # raise AssertionError("Should be an error")
#     print("else")
# finally:
#     print("finally")
