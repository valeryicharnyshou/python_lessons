with open('2.txt') as f:
    line_counter = 0
    words_counter = 0
    lines = f.readlines()
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        print('В строке номер {}: {} слов.'.format(index + 1, number_of_words))
with open('2.txt') as f:
    for line in f:
        line_counter += 1
        words = line.split()
        words_counter += len(words)
print("Количество строк в файле: ", line_counter)
print("Всего слов в файле: ", words_counter)
