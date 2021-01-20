subjects = {}
try:
    with open('6.txt', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        data = line.replace('(', " ").split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
finally:
    print(subjects)
