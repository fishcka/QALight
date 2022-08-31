#  Ludmila Afanasenko

# 1. *В якості тестового файла використовуйте python_zen.txt або будь-який інший файл з текстом англійскою
# Потрібно:
#   - Вивести найпопулярніший символ цього файлу
#   - Вивести речення з найбільшою кількістю пробілів
#   - Записати весь текст в новий файл задом наперед
print("=" * 30)
print("Завдання 1")
print("   ", "*" * 3)
file_name = "python_zen.txt"
with open(file_name) as file:
    text = file.read()

text_uniq = set(text)
# text_uniq.remove(" ")  # можна видалити пробіл
max_count = 0
letter = ""
for symbol in text_uniq:
    count = text.count(symbol)
    if count > max_count:
        letter = symbol
        max_count = count
print(f"Символ \"{letter}\" зустрічається {max_count} раз")

sentences = text.split("\n")
space_count = 0
max_sentence = ""
for sentence in sentences:
    count = sentence.count(" ")
    if count > space_count:
        space_count = count
        max_sentence = sentence
print(f"Речення \"{max_sentence}\" має найбільше пробілів - {space_count}")

backwards_text = "".join(reversed(text))
new_file_name = "zen_backwards.txt"
with open(new_file_name, "w") as file:
    file.write(backwards_text)

# 2. * В якості JSON файла викоритовуйте currency.json.
# Потрібно:
#   - Вивести повідомлення про кожну валюту в форматі "Курс ʼХʼ сьогодні - ʼХʼ на купівлю та ʼХʼ на продаж"
#   - Зберегти значення євро та доллара в новий файл
#   - В оригінальний файл додати ще одну валюту (будь-яку на ваш розсуд та фантазію)
print("=" * 30)
print("Завдання 2")
print("   ", "*" * 3)
import json
currency = "currency.json"
with open(currency) as file:
    json_data = json.load(file)

for curr in json_data:
    ccy = curr["ccy"]
    base_ccy = curr["base_ccy"]
    buy = curr["buy"]
    sale = curr["sale"]
    print(f"Курс {ccy} сьогодні - {buy} {base_ccy} на купівлю та {sale} {base_ccy} на продаж")

some_currencies = []
for curr in json_data:
    if curr["ccy"] == "USD":
        some_currencies.append(curr)
    if curr["ccy"] == "EUR":
        some_currencies.append(curr)
with open("some_currencies.json", "w") as file:
    json.dump(some_currencies, file, indent=2)

new_currency = {"ccy": "PLN", "base_ccy": "UAH", "buy": 8.615, "sale": 8.645}
json_data.append(new_currency)
with open("currency.json", "w") as file:
    json.dump(json_data, file, indent=2)

# 3(Додаткове). Створити (програмно) XML файл.
# Після чого вивести повідомлення про кожного студента в форматі "Студент studentX(тег) навчається в закладі X(name)"
# Будьте уважні, є певна відповідність між курсами студентів та курсами які наявні в закладах )
# *(зробити це програмно, а не просто "руками" заповнити)
print("=" * 30)
print("Завдання 3")
print("   ", "*" * 3)
from lxml import etree

root = etree.Element("root")
students = etree.SubElement(root, "students")
student1 = etree.SubElement(students, "student1", attrib={"age": "23", "course": "5"})
student2 = etree.SubElement(students, "student2", attrib={"age": "20", "course": "3"})
student3 = etree.SubElement(students, "student3", attrib={"age": "19", "course": "2"})
universities = etree.SubElement(root, "universities")
university1 = etree.SubElement(universities, "university1", attrib={"existingCourses": "1, 2", "name": "Brooksberry"})
university2 = etree.SubElement(universities, "university2", attrib={"existingCourses": "3, 4", "name": "Serbuten"})
university3 = etree.SubElement(universities, "university3", attrib={"existingCourses": "5, 6", "name": "Finestrally"})

xml_str = etree.tostring(root, pretty_print=True).decode("utf-8")

with open("xml_hw", "w") as file:
    file.write(xml_str)

et = etree.parse("xml_hw")
root = et.getroot()
name = ""
for stud in range(len(root[0])):
    student = root[0][stud].tag
    course0 = root[0][stud].get("course")
    for univ in range(len(root[1])):
        course1 = root[1][univ].get("existingCourses").split(", ")
        for i in range(len(course1)):
            if course0 == course1[i]:
                name = root[1][univ].get("name")
    print(f"Студент {student} навчається на {course0} курсі в закладі {name}")

print("=" * 30)
