with open("1.txt", "w") as f:
    while True:
        content = input("Введите данные: ")
        if content == "":
            break
        else:
            f.write(content + '\n')
