from functools import reduce
with open('3.txt') as f:
    salary = []
    for line in f:
        line = line.split()
        salary.append(line[1])
        salary = list(salary)
        if int(line[1]) < 20000:
            print(line[0], "имеет оклад менее 20000.")
average_salary = int((reduce(lambda x, y: int(x) + int(y), salary)) / (len(salary)))
print("Средняя величина дохода сотрудников: ", average_salary)
