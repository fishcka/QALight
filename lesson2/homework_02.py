# завдання 1
randomList = ["My", "beautiful", "new", "watch", "had", "run", 18, "months", "without", "losing"]
randomDict = {"thing": "watch", "period": "month", "q-ty": 18}
print(str(randomList[6]) + randomDict["period"])
print("="*30)

# завдання 2
divisionList = ["21", 3]
divisionResult = int(divisionList[0]) / divisionList[1]
print(int(divisionResult))
print("="*30)

# завдання 3
nonUniqueList = [100, 75, 100, 20, 75, 12, 75, 25]
uniqueList = set(nonUniqueList)
print(uniqueList)
sortedUniqueList = sorted(set(nonUniqueList))
print(sortedUniqueList)
print("="*30)

# завдання 4
salary = {"name": "Ludmila", "sal": 2500}
print(salary)
salary["sal"] = int(salary["sal"] * 1.5)
print(salary)
