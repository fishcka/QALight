#  Ludmila Afanasenko

# Створити функцію is_superset(), яка приймає 2 сети. Результат має виводитись в консоль,
# одним з повідомлень в залежності від ситуації:
#   1 - «Суперсет не знайдено»
#   2 – «Обʼєкт {X} є чистим суперсетом»
#   3 – «Сети рівні»
print("=" * 30)
print("Завдання 1")
print("   ", "*" * 3)
set_1 = {"Old", "cherry", "garden", "near", "the", "house"}
set_2 = {"And", "beetles", "buzzing", "in", "green", "leaves"}
set_3 = {"beetles", "buzzing"}
set_4 = {"And", "beetles", "buzzing", "in", "green", "leaves"}


def is_superset(set_a, set_b):
    if set_a.issuperset(set_b):
        if set_a != set_b:
            print(f"Обʼєкт {set_a} є чистим суперсетом")
        else:
            print("Сети рівні")
    else:
        print("Суперсет не знайдено")


is_superset(set_1, set_2)
is_superset(set_2, set_4)
is_superset(set_3, set_4)
is_superset(set_4, set_3)

# Створити словник що містить в собі 5 страв (ключі) та їх калорійність (значення).
# Додати в цей словник ще одну страву та її калорійність. Після чого кожне значення
# калорійності замінити на кортеж (калорійність, температура подачі). Вивести всі температури подачі.
# *Значення калорійності та температури обирайте на власний розсуд та в зручному форматі,
# це можуть бути як числові значення, так і строки (по типу "холодний", "важкий" і т.д)
print("=" * 30)
print("Завдання 2")
print("   ", "*" * 3)
menu = {"сирники": 202, "голубці": 93, "пельмені": 146, "суші": 127, "відбивна": 305}
menu["омлет"] = 131
menu["сирники"] = (menu["сирники"], "тепла")
menu["голубці"] = (menu["голубці"], "тепла")
menu["пельмені"] = (menu["пельмені"], "гаряча")
menu["суші"] = (menu["суші"], "холодна")
menu["відбивна"] = (menu["відбивна"], "тепла")
menu["омлет"] = (menu["омлет"], "гаряча")
for key, value in menu.items():
    print(f"Страва '{key}' має подаватись {value[1]}")

# Створити 3-4 словники з полями імʼя, вік та місто. Ці словники зібрати в список.
# Програма має виводити 3 повідомлення про кожний словник (тобто 9-12 повідомлень)
# наступного формату:
# “My … is ...”
print("=" * 30)
print("Завдання 3")
print("   ", "*" * 3)
student_1 = {"name": "Світлана", "age": 25, "city": "Черкаси"}
student_2 = {"name": "Олексій", "age": 18, "city": "Харків"}
student_3 = {"name": "Каріна", "age": 20, "city": "Житомир"}
student_4 = {"name": "Олег", "age": 30, "city": "Полтава"}

students = [student_1, student_2, student_3, student_4]
print(students)
print()

for student in students:
    for k, v in student.items():
        print(f"My {k} is {v}")

print("=" * 30)
