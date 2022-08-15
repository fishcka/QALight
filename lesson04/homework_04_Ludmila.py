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
    return count


print(multiples_counting(8))
print(multiples_counting(0))
print(multiples_counting(99))
print(multiples_counting(13))

print("=" * 30)
print("Завдання 2")
print("   ", "*" * 3)


def calculator(param1, param2, action="+"):
    if action == "+":
        result = param1 + param2
        return result
    elif action == "-":
        result = param1 - param2
        return result
    elif action == "*":
        result = param1 * param2
        return result
    elif action == "/":
        result = param1 / param2
        return result
    else:
        print("Введіть +, -, * або /")


print(calculator(14, 28))
print(calculator(63, 7, "/"))
print(calculator(89, 13, "-"))
print(calculator(5, 45, "*"))
print(calculator(10, 12, "%"))

print("=" * 30)
print("Завдання 3")
print("   ", "*" * 3)


class MathAction:

    def square(self, param):
        result1 = param ** 2
        return result1

    def square_root(self, param):
        result2 = param ** 0.5
        return result2


math_action1 = MathAction()
print(math_action1.square(8))
print(math_action1.square(51))
print(math_action1.square_root(11))
print(math_action1.square_root(125))
print("=" * 30)
