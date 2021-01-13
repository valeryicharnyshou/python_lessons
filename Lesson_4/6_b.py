from itertools import cycle
counter = 0
some_list = ['AbCdEfZ', 123456]
for i in cycle(some_list):
    if counter > 17:
        break
    print(i)
    counter += 1
