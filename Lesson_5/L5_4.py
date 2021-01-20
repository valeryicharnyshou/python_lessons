new_file = []
rus_list = ['Один', 'Два', 'Три', 'Четыре']
counter = 0
with open('4.txt') as f:
    for line in f:
        i = line.split(' ', 1)
        new_file.append(rus_list[counter] + ' ' + i[1])
        counter += 1
with open('4_new.txt', 'w') as new_f:
    new_f.writelines(new_file)
