# Variables
int_value = 5
print("Value is ", int_value)
print(type(int_value))
type_int_value = type(int_value)
print(type_int_value)

flt_value = float()
print(flt_value)
type_flt_value = type(flt_value)
print(type_flt_value)

bool_value = int_value > flt_value
print(bool_value)
type_bool_value = type(bool_value)
print(type_bool_value)

# None
non = None
print(non)

# Bool
true = True
false = False
x = 1 > 3
print(x)
x = 1 == 2
print(x)
x = 1 != 2
print(x)

# Number
# Int
int_value = 25
print(int_value - 7)
print(int_value + 7)
print(int_value * 7)
print(int_value / 7)
print(int_value ** 2)

# List
lst = [1, 2, 3, 4, False]
print(lst)
print(lst[0])  # 1
print(lst[2])  # 3
# print(lst[8])  # out of range
# Change element
lst[1] = True
print(lst)
# Add element
lst.append(6)
print(lst)

# Tuple
tpl = (1, 2, False, 37)
print(tpl)
print(tpl[0])  # 1
print(tpl[2])  # 3
# print(tpl[8])  # out of range

# String
string = "Hello, my name is "
name = "Luda"
print(string + name)

# Set
st = {2, 2, 2, 4, 5, 6, 6, 6, 7, 7, 4}
print(st)  # {2, 4, 5, 6, 7}
st1 = {9, 9, 2, 2, 2, 4, 5, 6, 6, 6, 7, 7, 4}
print(st1)  # {2, 4, 5, 6, 7, 9}

# Dict
dct = {"name": "Luda", "age": 45, 76: "value"}
print(dct)
# Get element
print(dct["name"])
print(dct["age"])
print(dct[76])
# Set element
dct["age"] = 28
print(dct)
# Add element
dct["age"] = 13
dct["lastname"] = "Afanasenko"
print(dct)
print("="*30)
print("\n"*5)
# Types
num_str = "7"
num_str_2 = "17"
print(num_str + num_str_2)
int_sum = int(num_str) + int(num_str_2)
print(int_sum)
