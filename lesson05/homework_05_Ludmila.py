#  Ludmila Afanasenko
from abc import ABC, abstractmethod

# 1. Створити клас який при ініціалізації приймає число, а також, має методи для розрахунку кореню та квадрату
# цього числа. Створити декілька обʼєктів, викликати методи.
print("=" * 30)
print("Завдання 1")
print("   ", "*" * 3)


class MathAction:

    def __init__(self, number):
        self.number = number

    def square(self):
        result1 = self.number ** 2
        return result1

    def square_root(self):
        result2 = self.number ** 0.5
        return result2


math_action_1 = MathAction(13)
print(math_action_1.square())
print(math_action_1.square_root())
print()
math_action_2 = MathAction(59)
print(math_action_2.square())
print(math_action_2.square_root())

# 2. Створити клас BaseMath, який містить методи, що вміють додавати і віднімати числа (методи приймають 2 числа).
# Від нього наслідувати клас Math, який вміє множити і ділити числа.  Створити обʼєкт, викликати методи.
print("=" * 30)
print("Завдання 2")
print("   ", "*" * 3)


class BaseMath:

    def addition(self, number_1, number_2):
        sum = number_1 + number_2
        return sum

    def substraction(self, number_1, number_2):
        diff = number_1 - number_2
        return diff


class Math(BaseMath):

    def multiplication(self, number_1, number_2):
        prod = number_1 * number_2
        return prod

    def division(self, number_1, number_2):
        quot = number_1 / number_2
        return quot


math = Math()
print(math.addition(19, 23))
print(math.substraction(48, 99))
print(math.multiplication(15, 5))
print(math.division(18, 26))

# 3. Створити абстрактний клас Людина, з одним абстрактним методjм do(). Реалізувати 2 класи базуючись на
# абстрактному - Учень і Робітник. Учень в do має виводити "Я ще вчусь", а робітник "Ех, робота-робота".
print("=" * 30)
print("Завдання 3")
print("   ", "*" * 3)


class Human(ABC):  # імпорт класу АВС на початку файла

    @abstractmethod
    def do(self):
        pass


class Student(Human):

    def do(self):
        print("Я ще вчусь")


class Worker(Human):

    def do(self):
        print("Ех, робота-робота")


student = Student()
student.do()
worker = Worker()
worker.do()

# 4*. Створити клас QualityAssuranceEngineer. При ініціалізації приймає досвід (в роках) і заплатню.
# Клас має метод do_testing, що виводить "Починаю тестування...". Від нього спадкується клас
# ManualQualityAssuranceEngineer. В ньому, перевизначений метод  do_testing має виводити "Ех, знову регресія...".
# Також від основного класу віднаслідувати клас AutomationQualityAssuranceEngineer. Він при інінціалізації має
# приймати додатковий параметр code_lang. Метод do_testing первизначити щоб він виводив "Ха, зараз
# поставлю ранитись тести на <code_lang> і го пити каву )".
print("=" * 30)
print("Завдання 4")
print("   ", "*" * 3)


class QualityAssuranceEngineer:

    def __init__(self, experience, salary):
        self.experience = experience
        self.salary = salary

    def do_testing(self):
        print("Починаю тестування...")


class ManualQualityAssuranceEngineer(QualityAssuranceEngineer):

    def do_testing(self):
        print("Ех, знову регресія...")


class AutomationQualityAssuranceEngineer(QualityAssuranceEngineer):

    def __init__(self, code_lang, experience, salary):
        super().__init__(experience, salary)
        self.code_lang = code_lang

    def do_testing(self):
        print("Ха, зараз поставлю ранитись тести на", self.code_lang, "і го пити каву")


quality = QualityAssuranceEngineer(10, 1500)
quality.do_testing()
manual = ManualQualityAssuranceEngineer(3, 1000)
manual.do_testing()
automation = AutomationQualityAssuranceEngineer("Python", 19, 2000)
automation.do_testing()

print("=" * 30)
