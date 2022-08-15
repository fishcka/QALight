# FUNC


def two_params(param1=9, param2=2):
    return param1 + param2


int_sum = two_params(12, 8)
print(int_sum)
print(two_params(int_sum, 7))
int_sum = two_params(3)
print(int_sum)
print(two_params())


# Class
class MyClass:
    name = "Luda"
    surname = "Afanasenko"

    def print_name(self):
        print(self.name)


my_class = MyClass()
my_class.name = "Julia"
print(my_class.name)
print(my_class.surname)
my_class.print_name()

my_class1 = MyClass()
print(my_class1.name)
