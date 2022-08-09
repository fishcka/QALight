# завдання 1 вибираєм довільне значення
randomList1 = ["My", "beautiful", "new", "watch", "had", "run", 18, "months", "without", "losing"]
randomDict1 = {"thing": "watch", "period": "month", "q-ty": 18}
listElement = input("Вкажіть число від 0 до 9: ", )
dictElement = input("Вкажіть число від 0 до 2: ", )
term1 = (randomList1[int(listElement)])
term2 = (list(randomDict1.keys())[int(dictElement)])
print((format(term1)) + format(term2))
