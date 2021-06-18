my_list = [8, 7, 5, 5, 4, 2]
new_number = int(input("Введите новый элемент рейтинга:"))
m = max(set(my_list), key=my_list.count)
i = my_list.index(m)
c = my_list.count(m)
if int(new_number) < int(my_list[5]):
    my_list.append(new_number)
elif int(new_number) > int(my_list[0]):
    my_list.insert(0, new_number)
else:
    my_list.insert((int(i) + c), new_number)
my_list.sort(reverse=True)
for s in my_list:
    print(s, '', end='')
