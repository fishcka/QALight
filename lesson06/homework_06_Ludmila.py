#  Ludmila Afanasenko

# Дано текст (нижче), який треба зберегти в строку.
verse = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print("=" * 30)
# - Підрахувати кількість літер "с"

print(verse.count("c"))

print("=" * 30)
# - Знайти "найнепопулярнійший" символ (з тих що є в тексті, той що зустрічається найменшу кількість разів)

verse_uniq = set(verse)
min_count = 1
min_list = {}
for symbol in verse_uniq:
    count = verse.count(symbol)
    if count <= min_count:
        letter = symbol
        min_count = count
        min_list[letter] = min_count

for key, value in sorted(min_list.items()):
    print("Символ", key, "зустрічається", value, "раз")

print("=" * 30)
# - Знайти найдовше речення (по кількості символів). Тут бажано створити алгоритм пошуку найбільшого,
# за допомогою циклу.

sentence = verse.split("\n")
max_symbol_count = 0
max_sentence = ()
for i in range(len(sentence) - 1):
    count = len(sentence[i])
    if count >= max_symbol_count:
        max_symbol_count = count
        max_sentence = sentence[i]

print("В реченні \"" + max_sentence + "\" " + str(max_symbol_count) + " символів")

print("=" * 30)
# - Знайти найдовше речення (по кількості слів)

max_word_count = 0
for y in range(len(sentence) - 1):
    count = len(sentence[y].split())
    if count >= max_word_count:
        max_word_count = count
        max_sentence = sentence[y]
print("В реченні \"" + max_sentence + "\" " + str(max_word_count) + " слів")
print("=" * 30)
