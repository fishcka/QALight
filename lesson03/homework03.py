print("=" * 30)
# TASK 1
# Створити програму яка виводить всі числа що без остачі діляться на 4,
# від 0 до заданого числа (числа з input)
# * Відлік починається не з нуля, а з іншого заданого числа (додатковий інпут).
# Якщо перше число більше другого, то виводити повідомлення з підказкою
# (типу "Введіть корректні числа, перше менше, друге більше")
print("Завдання 1")
print("   ", "*" * 3)


def red_text(text):
    print("\033[1;31m{}\33[0m".format(text))


while True:
    try:
        start_input = int(input("Вкажіть число початку відліку: ", ))
        break
    except ValueError:
        red_text("Ви ввели не ціле число")
while True:
    try:
        stop_input = int(input("Вкажіть число кінця відліку: ", ))
        break
    except ValueError:
        red_text("Ви ввели не ціле число")
while start_input >= stop_input:
    red_text("Введіть корректні числа: початок відліку має бути менше, кінець відліку має бути більше")
    while True:
        try:
            start_input = int(input("Вкажіть число початку відліку: ", ))
            break
        except ValueError:
            red_text("Ви ввели не ціле число")
    while True:
        try:
            stop_input = int(input("Вкажіть число кінця відліку: ", ))
            break
        except ValueError:
            red_text("Ви ввели не ціле число")
else:
    for number_1 in range(start_input, stop_input):
        if number_1 % 4 == 0:
            print(number_1, end=" ")
print("")
print("=" * 30)
# TASK 2
# Створити програму, яка рахує кількість чисел кратних 5 від 0 до введеного числа (input).
# Вивести це значення.
print("Завдання 2")
print("   ", "*" * 3)
while True:
    try:
        number_input = int(input("Вкажіть число: ", ))
        break
    except ValueError:
        red_text("Ви ввели не ціле число")
count = 0
for number_2 in range(number_input):
    if number_2 % 5 == 0:
        count = count + 1
print("Кількість чисел що діляться на 5: ", count)
print("=" * 30)
# TASK 3
# Створити список з декількох елементів, вивести іх суму (за допомогою циклу for)
print("Завдання 3")
print("   ", "*" * 3)
any_list = [1, 2, 3, 4]
summa_1 = 0
for number_3 in any_list:
    summa_1 = summa_1 + number_3
print("Сума елементів списку: ", summa_1)
print("=" * 30)
# TASK 4
# Створити список з повторюваними елементами, вивести суму всіх унікальних.
print("Завдання 4")
print("   ", "*" * 3)
other_list = [12, 25, 78, 9, 25, 9, 25, 78, 93, 12]
summa_2 = 0
unique_list = set(other_list)
for number_4 in unique_list:
    summa_2 = summa_2 + number_4
print("Сума елементів списку: ", summa_2)
print("=" * 30)
print("       _")
print("    ._(.)< (THE END)")
print("     \__)")
