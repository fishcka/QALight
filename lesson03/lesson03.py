# IF
x = 5
if x > 5:
    print("True")
elif x > 0:
    print(">0")
else:
    print("False")

# TASK1
age = int(input("Вкажіть свій вік: ", ))
if age >= 18:
    print("Добре, можна купувати алкоголь")
elif age >= 16:
    print("Почекай трошки")
else:
    print("Тобі ще зарано")

# WHILE
x = 0
while x < 10:
    if x > 5:
        break
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1

# TASK2
even_input = int(input("Вкажіть число: ", ))
while even_input < 10:
    if even_input < 0:
        print("break here")
        break
    if even_input % 2 == 0:
        print(even_input)
    even_input = even_input + 1
else:
    print("break wasn't here")

# FOR
for a in range(0, 10, 3):  # range(start, stop, step)
    print(a)

for b in [3, 6, 473]:
    print(b)

for c in range(10):
    if c > 5:
        break
    if c == 3:
        continue
    print(c)

# TASK3
number_input = int(input("Вкажіть число: ", ))
count = 0
for number in range(number_input):
    if count > 10:
        break
    if number % 2 != 0:
        continue
    print(number)
    count = count + 1

#
d = 3
if d:  # if d != 0
    print(d)
