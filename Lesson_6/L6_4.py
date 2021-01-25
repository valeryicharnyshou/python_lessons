class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость {self.name} : {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского авто {self.name} : {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} превышает допустимую!'
        else:
            return f'Скорость {self.name} в норме.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего авто {self.name} : {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышает допустимую!'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейский авто.'
        else:
            return f'{self.name} это авто не из полиции.'


ferrari = SportCar(300, 'Красный', 'Ferrari', False)
vw = TownCar(60, 'Чёрный', 'VW', True)
mercedes = WorkCar(180, 'Белого', 'Mercedes', False)
audi = PoliceCar(110, 'Серый', 'Audi', True)
print(mercedes.turn_left())
print(f'{vw.turn_right()}, {ferrari.turn_left()}')
# print(f'{mercedes.go()} текущая скорость {mercedes.show_speed()}')
# print(f'{mercedes.name} {mercedes.color} цвета.')
print(f'{ferrari.name} полицейский автомобиль? {ferrari.is_police}')
print(f'{vw.name}  полицейский автомобиль? {vw.is_police}')
print(ferrari.show_speed())
print(vw.show_speed())
print(audi.police())
print(audi.show_speed())
