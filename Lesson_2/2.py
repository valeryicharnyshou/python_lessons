user_list = input("Введите элементы списка для обработки: ")
i = list(user_list)
t = list()
if len(i) % 2 == 0:
    i[::2], i[1::2] = i[1::2], i[::2]
    print(i)
else:
    t = i.pop(len(i) - 1)
    i[::2], i[1::2] = i[1::2], i[::2]
    i.append(t)
    print(i)
