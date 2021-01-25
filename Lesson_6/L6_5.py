class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки. {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        Stationary.__init__(self, title)

    def draw(self):
        return f'У вас в руках {self.title}. Запуск отрисовки. {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        Stationary.__init__(self, title)

    def draw(self):
        return f'Это {self.title}. Запуск отрисовки. {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        Stationary.__init__(self, title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки. {self.title}'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
