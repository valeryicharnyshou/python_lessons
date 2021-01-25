from time import sleep


class TrafficLight:
    __light_color = [
        "\033[31m Красный".format(), "\033[33m Жёлтый".format(), "\033[32m Зелёный".format()]

    def running(self):
        while True:
            print(TrafficLight.__light_color[0])
            sleep(7)
            print(TrafficLight.__light_color[1])
            sleep(2)
            print(TrafficLight.__light_color[2])
            sleep(7)
            print(TrafficLight.__light_color[1])
            sleep(2)


my_traffic_light = TrafficLight()
my_traffic_light.running()
