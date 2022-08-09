def inp_ut(x):
    while True:
        try:
            # number = int(input('{} {} '.format("Введите, пожалуйста,число", x, )))
            number = input("Введите, пожалуйста,число " + x + " ")
            return number
        except ValueError:
            print("Please reinsert")


a = inp_ut('a')
b = inp_ut('b')
c = inp_ut('c')
print(a)
print(b)
print(c)
