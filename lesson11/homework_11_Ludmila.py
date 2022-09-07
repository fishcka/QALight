#  Ludmila Afanasenko

# 1.  Дано список з 5 словників
# Написати тест, що перевіряє чи всім є 18 років, при падінні теста помилка має містити імена всіх неповнолітніх
import pytest

users = [{"name": "John", "age": 4},
         {"name": "James", "age": 65},
         {"name": "Aaron", "age": 56},
         {"name": "Alice", "age": 24},
         {"name": "Jen", "age": 15}]

output_l = []
u1 = ''
for user in users:
    for key, value in user.items():
        u1 = (user["name"], user["age"])
    output_l.append(u1)


@pytest.mark.parametrize(["name", "age"], output_l)
def test_adult_user(name, age):
    assert age >= 18, f"{name} is {age}"


# 2. Створити класс з властивостями, що задаються при ініцілізації:
# - Параметр login(str). Значення за замовчування - порожня строка.
# - Параметр password(str). Значення за замовчуванням - порожня строка.
# - Метод sign_in_enabled.  Який повертає True, якщо логін і пароль заповнені і False, якщо хоча б одне з полів пусте
# Написати тести:
# - 2 поля пусті, тож sign_in_enabled -> False
# - 1 поле заповнене, тож sign_in_enabled -> False
# - 2 поля заповнені, тож sign_in_enabled ->True.
# А якщо замінити одне зі значень на None або порожню строку, то sign_in_enabled -> False.

class LoginChecker:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def sign_in_enabled(self):
        if self.login != "" and self.password != "":
            return True
        else:
            return False

