"""Lesson 5"""


# Object, Class and Static Methods
def func(new_number):
    print("Going to change number to: " + str(new_number))


class RandomClass:
    number = 5

    def obj_method(self, new_number):
        func(new_number)
        self.stat_method(new_number)
        self.number = new_number

    @classmethod
    def class_method(cls, new_number):
        func(new_number)
        cls.stat_method(new_number)
        cls.number = new_number

    @staticmethod
    def stat_method(new_number):
        print("Going to change number to: " + str(new_number))


rand_class = RandomClass()
rand_class_1 = RandomClass()
print(rand_class.number)
print(rand_class_1.number)
rand_class.class_method(10)
print(rand_class.number)
print(rand_class_1.number)
rand_class_2 = RandomClass()
print(rand_class_2.number)


# Наслідування
class Human:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("Om-om-om")

    def say_name(self):
        print("My name is " + self.name)


class Monkey:

    def climb(self):
        pass


class Baby(Human, Monkey):

    def cry(self):
        print("AAAAAA")


class Child(Baby):

    def __init__(self, name, klass):
        super().__init__(name)  # Alt + Enter -> Add super class call
        self.klass = klass


human = Human("John")
human.eat()
human.say_name()
print("=" * 60)
baby = Baby("Aaron")
baby.eat()
baby.cry()
baby.say_name()
baby.climb()

# Поліморфізм, Абстракція
from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def click(self):
        pass


class ChromeBrowser(Browser):

    def click(self):
        print("Click in Chrome")


class FFBrowser(Browser):

    def click(self):
        print("Click in FireFox")


class SafariBrowser(Browser):
    pass


# browser = Browser()
# browser.click()

chrome = ChromeBrowser()
chrome.click()

firefox = FFBrowser()
firefox.click()

# safari = SafariBrowser()
# safari.click()


# Інкапсуляція
class IncapClass:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age / 2


john = IncapClass("John", 45)
print(john.name)
print(john.get_age())


# Property


class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age / 2

    @age.setter
    def age(self, new_age):
        if new_age - self.__age > 1:
            print("Nope, too many years")
        else:
            self.__age = new_age


james = Human("James", 784)
print(james.name)
james.name = "James II"
print(james.name)
print(james.age)
james.age = 789
print(james.age)
james.age = 785
print(james.age)
