class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_calc(self):
        return (self._length * self._width * 25 * 5) / 1000


example_1 = Road(5000, 20)
print("Понадобится", int(example_1.asphalt_calc()), "Тонн асфальта.")
