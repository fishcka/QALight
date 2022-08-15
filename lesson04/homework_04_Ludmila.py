# Ludmila Afanasenko

print("=" * 30)
print("Завдання 1")
print("   ", "*" * 3)


def multiples_counting(checked_value):
    count = 0
    for diapason in range(101):
        if checked_value == 0:
            continue
        else:
            if diapason % checked_value == 0:
                count = count + 1
    print("Кількість чисел що діляться на " + str(checked_value) + ": " + str(count))


multiples_counting(8)
multiples_counting(0)
multiples_counting(99)
multiples_counting(13)

print("=" * 30)
print("Завдання 2")
print("   ", "*" * 3)


def calculator(param1, param2, action="+"):
    if action == "+":
        result = param1 + param2
        print("Сума чисел", param1, "і", param2, "дорівнює:", int(result))
    elif action == "-":
        result = param1 - param2
        print("Різниця чисел", param1, "і", param2, "дорівнює:", int(result))
    elif action == "*":
        result = param1 * param2
        print("Добуток чисел", param1, "і", param2, "дорівнює:", int(result))
    elif action == "/":
        result = param1 / param2
        print("Частка чисел", param1, "і", param2, "дорівнює:", int(result))


calculator(14, 28)
calculator(63, 7, "/")
calculator(89, 13, "-")
calculator(5, 45, "*")

print("=" * 30)
print("Завдання 3")
print("   ", "*" * 3)


class MathAction:
    def square(self, param):
        result1 = param ** 2
        print("Квадрат числа", param, "дорівнює:", result1)
        return result1

    def square_root(self, param):
        result2 = param ** 0.5
        print("Корінь числа", param, "дорівнює:", result2)
        return result2


math_action1 = MathAction()
math_action1.square(8)
math_action1.square(51)
math_action1.square_root(11)
math_action1.square_root(125)
print("=" * 30)
