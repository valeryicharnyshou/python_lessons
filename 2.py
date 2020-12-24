seconds = int(input("Введите время в секундах:"))
minutes = 0
hours = 0
if seconds >= 60:
    while seconds >= 60:
        minutes += 1
        seconds -= 60
    if minutes >= 60:
        while minutes >= 60:
            hours += 1
            minutes -= 60
    print(f"Время в формате ЧЧ:ММ:СС - {hours:1}:{minutes:1}:{seconds:1}")
else:
    print(f"Время в формате ЧЧ:ММ:СС - {hours:1}:{minutes:1}:{seconds:1}")
