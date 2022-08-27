#  Ludmila Afanasenko
# Створити функцію, що приймає число строкою. І повертає його int значення.
# Якщо строку не вдається конвертувати в int, то виводити повідомлення
# "Щось не так з інпутом, передайте коректне число" і повертати None.
print("=" * 30)
print("Завдання 1")
print("   ", "*" * 3)


def red_text(text):
    print(f"\033[1;31m{text}\33[0m")


def input_value(number):
    try:
        return int(number)
    except ValueError:
        red_text("Введіть число!")
        return None


print(input_value(19))
print(input_value(59.68))
print(input_value("i'm not number"))

# Створити метод, що приймає 2 числа. Якщо хоча б один з параметрів не є числом,
# то має виконуватися конкантенація (додавання строк). В інших випадках введені числа сумуються.
print("=" * 30)
print("Завдання 2")
print("   ", "*" * 3)


class TwoNum:

    def two_num(self, number_one, number_two):
        try:
            if isinstance(number_one, int) and isinstance(number_two, int):
                result = number_one + number_two
                return result
            else:
                result = round(number_one + number_two, 2)
                return result
        except TypeError:
            result = str(number_one) + str(number_two)
            return result


my_num = TwoNum()
print(my_num.two_num(9, "cat"))
print(my_num.two_num("caterpillar", 40.5))
print(my_num.two_num(56, 98))
print(my_num.two_num(4.7, 8.9))
print(my_num.two_num(4, 8.9))
print(my_num.two_num(4.731, 8))
# Створити метод, що приймає значення з input(). Якщо значення не може бути конвертовано в int,
# то перезапитувати його до моменту поки не прийде валідне значення (згадуємо цикл while)
# Якщо значення валідне, то виводити повідомлення "Х може бути інт".
print("=" * 30)
print("Завдання 3")
print("   ", "*" * 3)


class IntValue:

    def input_v(self):
        while True:
            try:
                number = int(input("Вкажіть число: ", ))
                return number
            except ValueError:
                red_text("Ви ввели не ціле число")


input_num = IntValue()
print(f"\033[1;33m{input_num.input_v()} може бути int\33[0m")

print("=" * 30)
