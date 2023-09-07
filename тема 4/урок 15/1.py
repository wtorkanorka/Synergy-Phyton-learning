# 1 https://github.com/wtorkanorka/Synergy-Phyton-learning.git
class Transport(object):
    name = ""
    max_speed = 0
    mileage = 0

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):
    def getData(self):
        print(
            f"Название автомобиля:{self.name} Скорость:{self.max_speed} Пробег:{self.mileage}"
        )


a1 = Autobus("Renaul Logan", 180, 12).getData()
