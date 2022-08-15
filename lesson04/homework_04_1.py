# 1. Створити універсальну функцію для підрахунку чисел кратних будь-якому числу
# в діапазоні від 0 до 100. Тобто функція має приймати один параметр - число
# кратність якому ми будемо перевіряти. І повертати кількість чисел кратних цьому
# числу в заданому діапазоні.
# Викликати функцію декілька разів з різними значеннями.
print("=" * 30)


def red_text(text):  # red text
    print("\033[1;31m{}\33[0m".format(text))


def input_value():  # input
    while True:
        try:
            number = int(input("Вкажіть число: ", ))
            return number
        except ValueError:
            red_text("Ви ввели не ціле число")


def try_exit():  # exit
    while True:
        exit_check = (input("Перевіряємо ще? Введіть Y або N ", ))
        if exit_check == "N":
            print("       _")
            print("    ._(.)< (THE END)")
            print("     \__)")
            exit(0)
        if exit_check == "Y":
            multiples_counting(input_value())
        else:
            red_text("Введіть Y або N! ")


def multiples_counting(checked_value):  # main function
    count = 0
    for diapason in range(101):
        if checked_value == 0:
            continue
        else:
            if diapason % checked_value == 0:
                count = count + 1
    print("Кількість чисел що діляться на " + str(checked_value) + ": " + str(count))
    print("=" * 30)
    try_exit()


multiples_counting(input_value())
print("=" * 30)
